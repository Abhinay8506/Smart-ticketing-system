import sqlite3

class Database:
    def __init__(self, db_name="tickets.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            priority INTEGER NOT NULL,
            status TEXT CHECK(status IN ('OPEN','CLOSED')) NOT NULL 
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_ticket(self, ticket):
        query = """
        INSERT INTO tickets (title, description, category, priority, status)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor = self.conn.execute(query, (
            ticket.title,
            ticket.description,
            ticket.category,
            ticket.priority,
            ticket.status
        ))
        self.conn.commit()

        # Assign DB-generated ID back to ticket object
        ticket.ticket_id = cursor.lastrowid

    def get_all_tickets(self):
        cursor = self.conn.execute("SELECT * FROM tickets")
        return cursor.fetchall()
    
    def get_next_open_ticket(self):
        query = """
        SELECT ticket_id, title, description, category, priority, status
        FROM tickets
        WHERE status = 'OPEN'
        ORDER BY priority ASC, ticket_id ASC
        LIMIT 1
        """
        cursor = self.conn.execute(query)
        row = cursor.fetchone()
        return row

    def get_stats(self):
        total = self.conn.execute(
            "SELECT COUNT(*) FROM tickets"
        ).fetchone()[0]

        open_count = self.conn.execute(
            "SELECT COUNT(*) FROM tickets WHERE status='OPEN'"
        ).fetchone()[0]

        closed_count = self.conn.execute(
            "SELECT COUNT(*) FROM tickets WHERE status='CLOSED'"
        ).fetchone()[0]

        return {
            "total": total,
            "open": open_count,
            "closed": closed_count
        }
    

    def close_ticket(self, ticket_id):
        query = "UPDATE tickets SET status = 'CLOSED' WHERE ticket_id = ?"
        self.conn.execute(query, (ticket_id,))
        self.conn.commit()

    def clear_tickets(self):
        self.conn.execute("DELETE FROM tickets")
        self.conn.commit()

    def get_open_tickets(self):
        query = """
          SELECT ticket_id, title, description, category, priority
          FROM tickets WHERE status = 'OPEN' ORDER BY priority ASC, ticket_id ASC
        """
        cursor = self.conn.execute(query)
        return cursor.fetchall()

