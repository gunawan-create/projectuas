class TicketData:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, name, destination, quantity):
        ticket = {
            'name': name,
            'destination': destination,
            'quantity': quantity
        }
        self.tickets.append(ticket)

    def get_tickets(self):
        return self.tickets