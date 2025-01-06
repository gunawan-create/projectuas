class TicketProcess:
    def __init__(self, data):
        self.data = data

    def add_ticket(self):
        try:
            name = input("Masukkan nama pemesan: ")
            destination = input("Masukkan tujuan: ")
            quantity = int(input("Masukkan jumlah tiket: "))

            if quantity < 1:
                raise ValueError("Jumlah tiket harus lebih dari 0.")

            self.data.add_ticket(name, destination, quantity)
            print("Tiket berhasil dipesan!")

        except ValueError as e:
            print(f"Error: {e}")