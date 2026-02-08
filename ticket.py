class Ticket:
    def __init__(self, title,description, category, priority):
        self.ticket_id = None          
        self.title = title  
        self.description = description
        self.category = category
        self.priority = priority
        self.status = "OPEN"

    def __repr__(self):
        return f"Ticket({self.ticket_id}, {self.title}, {self.category}, P{self.priority}, {self.status})"
