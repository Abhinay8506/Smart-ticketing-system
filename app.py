from flask import Flask, render_template, request, jsonify
from ticket import Ticket
from classifier import TicketClassifier
from priority import PriorityEngine
from queue_manager import TicketQueue
from database import Database

app = Flask(__name__)
classifier = TicketClassifier()
queue = TicketQueue()
db = Database()
priority_engine = PriorityEngine()

open_tickets = db.get_open_tickets()

for row in open_tickets:
    ticket = Ticket(
        title=row[1],
        description=row[2],
        category=row[3],
        priority=row[4]
    )
    ticket.ticket_id = row[0]
    queue.add_ticket(ticket)

@app.route("/")
def home():
    stats = db.get_stats()
    return render_template("index.html", stats=stats)


@app.route("/raise_ticket", methods=["POST"])
def raise_ticket():
    description = request.form.get("description", "").strip()

    category = classifier.classify(description)
    priority = priority_engine.assign_priority(category)
    title = f"{category} Issue"

    ticket = Ticket(
        title=title,
        description=description,
        category=category,
        priority=priority
    )
    db.insert_ticket(ticket)
    queue.add_ticket(ticket)

    position = queue.get_position(ticket.ticket_id)
   

    return jsonify({
        "ticket_id": ticket.ticket_id,
        "position": position
    })

@app.route("/process_next", methods=["POST"])
def process_next():
   ticket = queue.process_ticket()

   if not ticket:
        return jsonify({
            "message": "No open tickets"
        })

   
   db.close_ticket(ticket.ticket_id)

   return jsonify({
        "message": "Ticket processed successfully",
        "ticket_id": ticket.ticket_id
    })




if __name__ == "__main__":
    app.run(debug=True)
