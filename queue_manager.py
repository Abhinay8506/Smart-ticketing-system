import heapq

class TicketQueue:
    def __init__(self):
        self.queue = []

    def add_ticket(self, ticket):
        # push ticket with priority
        heapq.heappush(self.queue, (ticket.priority,ticket.ticket_id, ticket))

    def process_ticket(self):
        if not self.queue:
            return None
        _, _, ticket = heapq.heappop(self.queue)
        return ticket
    def get_position(self, ticket_id):
        """
        Returns number of tickets ahead of given ticket.
        0 means ticket is currently in progress.
        """
        for index, (_, tid, _) in enumerate(self.queue):
            if tid == ticket_id:
                return index
        return -1