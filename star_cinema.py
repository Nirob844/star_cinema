class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls._hall_list.append(hall)

    @classmethod
    def get_halls(cls):
        return cls._hall_list


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}  
        self.__show_list = []  
        self.__rows = rows  
        self.__cols = cols  
        self.__hall_no = hall_no  

        Star_Cinema.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.__show_list.append(show_info)
        self.__seats[show_id] = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            print("Error: Show ID not found!")
            return

        for (row, col) in seat_list:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                print(f"Error: Seat ({row}, {col}) is out of range!")
                continue
            if self.__seats[show_id][row][col] == 1:
                print(f"Error: Seat ({row}, {col}) is already booked!")
            else:
                self.__seats[show_id][row][col] = 1  
                print(f"Seat ({row}, {col}) booked successfully.")

    def view_show_list(self):
        if not self.__show_list:
            print("No shows are currently running.")
            return
        print("Current shows running:")
        for show in self.__show_list:
            print(f"Show ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("Error: Show ID not found!")
            return
        print(f"Available seats for Show ID: {show_id}")
        for row in range(self.__rows):
            for col in range(self.__cols):
                if self.__seats[show_id][row][col] == 0:
                    print(f"({row}, {col})", end=' ')
            print()

    def get_hall_no(self):
        return self.__hall_no

    def get_show_ids(self):
        return [show[0] for show in self.__show_list]



def main():
    # Create hall objects
    hall1 = Hall(10, 15, 1)
    hall2 = Hall(8, 12, 2)
    
    # Add shows to the halls
    hall1.entry_show(101, "Movie A", "10:00 AM")
    hall1.entry_show(102, "Movie B", "02:00 PM")
    hall2.entry_show(201, "Movie C", "04:00 PM")
    
    while True:
        print("\n--- Star Cinema System ---")
        print("1. View all shows")
        print("2. View available seats for a show")
        print("3. Book seats for a show")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            for hall in Star_Cinema.get_halls():
                print(f"\nHall No: {hall.get_hall_no()}")
                hall.view_show_list()

        elif choice == '2':
            try:
                show_id = int(input("Enter Show ID to view available seats: "))
            except ValueError:
                print("Error: Invalid Show ID format.")
                continue
            for hall in Star_Cinema.get_halls():
                if show_id in hall.get_show_ids():
                    hall.view_available_seats(show_id)
                    break
            else:
                print("Error: Show ID not found!")

        elif choice == '3':
            try:
                show_id = int(input("Enter Show ID to book seats: "))
            except ValueError:
                print("Error: Invalid Show ID format.")
                continue
            seat_list = input("Enter seats to book (format: row,col row,col ...): ")
            try:
                seats_to_book = [(int(seat.split(',')[0]), int(seat.split(',')[1])) for seat in seat_list.split()]
            except ValueError:
                print("Error: Invalid seat format.")
                continue
            for hall in Star_Cinema.get_halls():
                if show_id in hall.get_show_ids():
                    hall.book_seats(show_id, seats_to_book)
                    break
            else:
                print("Error: Show ID not found!")

        elif choice == '4':
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
