from ticket import Ticket
from classifier import TicketClassifier
from priority import PriorityEngine
from queue_manager import TicketQueue

classifier = TicketClassifier()
priority_engine = PriorityEngine()
ticket_queue = TicketQueue()
from database import Database
db = Database()
db.clear_tickets()

tickets = [
    Ticket(1, "Internet Issue", "Office internet is down"),
    Ticket(2, "Salary Issue", "Salary not credited this month"),
    Ticket(3, "SAP Error", "ABAP dump in production system")
]
print(tickets[0])
print(tickets[1])
for ticket in tickets:
    ticket.category = classifier.classify(ticket.description)
    ticket.priority = priority_engine.assign_priority(ticket.category)
    ticket_queue.add_ticket(ticket)
    db.insert_ticket(ticket)

processed = ticket_queue.process_ticket()

print(processed)
print("\nAll Tickets in Database:")
for row in db.get_all_tickets():
    print(row)