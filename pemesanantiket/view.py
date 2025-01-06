class TicketView:
    def display_tickets(self, tickets):
        if not tickets:
            print("Tidak ada tiket yang dipesan.")
            return

        print(f"{'No':<4} {'Nama':<20} {'Tujuan':<20} {'Jumlah':<10}")
        print("-" * 60)
        for i, ticket in enumerate(tickets, start=1):
            print(f"{i:<4} {ticket['name']:<20} {ticket['destination']:<20} {ticket['quantity']:<10}")