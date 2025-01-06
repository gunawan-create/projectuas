from data import TicketData
from view import TicketView
from process import TicketProcess

def main():
    ticket_data = TicketData()
    ticket_view = TicketView()
    ticket_process = TicketProcess(ticket_data)

    while True:
        print("\nMenu Pemesanan Tiket")
        print("1. Pesan Tiket")
        print("2. Tampilkan Tiket")
        print("3. Keluar")
        choice = input("Pilih opsi (1/2/3): ")

        if choice == '1':
            ticket_process.add_ticket()
        elif choice == '2':
            tickets = ticket_data.get_tickets()
            ticket_view.display_tickets(tickets)
        elif choice == '3':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()