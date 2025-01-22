class SeatBooking:
    def __init__(self):
        # Initial list of available seats
        self.seatNoList = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36
        ]
        # Initialize the seating arrangement with None (no gender assigned yet)
        self.bookingList = [None] * 36  # None means unbooked, 'M' for Male, 'F' for Female
    
    def display_seating_chart(self):
        """Display current seat availability"""
        for i in range(36):
            seat = self.bookingList[i]
            if seat == 'M':
                print("[M]", end=" ")
            elif seat == 'F':
                print("[F]", end=" ")
            else:
                print("[ ]", end=" ")
            if (i + 1) % 6 == 0:
                print()  # New line after every 6 seats
        print()  # Extra new line after chart
    
    def is_adjacent_restricted(self, seatNo, gender):
        """Check if any adjacent seat is already booked by the opposite gender"""
        adjacent_seats = []
        row_start = (seatNo - 1) // 6 * 6  # Row start index (0, 6, 12, 18, 24, 30)
        
        # Get the indexes of adjacent seats
        if seatNo - 2 >= row_start:  # Left seat
            adjacent_seats.append(seatNo - 2)
        if seatNo < 36 and seatNo % 6 != 0:  # Right seat
            adjacent_seats.append(seatNo)
        if seatNo - 6 >= 0:  # Top seat (previous row)
            adjacent_seats.append(seatNo - 6)
        if seatNo + 6 < 36:  # Bottom seat (next row)
            adjacent_seats.append(seatNo + 6)
        
        # Check if any adjacent seat is taken by the opposite gender
        for seat in adjacent_seats:
            if self.bookingList[seat] and self.bookingList[seat] != gender:
                return True  # If an opposite gender occupies adjacent seat
        return False

    def book_seat(self):
        """Booking process for passengers"""
        self.noOfPassenger = int(input("Enter number of passengers: "))
        
        for i in range(self.noOfPassenger):
            self.display_seating_chart()  # Show seating chart for every passenger

            while True:  # Repeatedly ask for a seat until valid
                try:
                    # Input seat number
                    seatNo = int(input(f"Passenger {i + 1}, Choose a Seat Number: "))

                    # Validate the seat number
                    if seatNo > 36 or seatNo <= 0:
                        print("Don't Choose a Seat Number which is not available.")
                    elif self.bookingList[seatNo - 1] is not None:
                        print("Ticket Already Booked, enter another seat.")
                    else:
                        # Ask for gender
                        gender = input("Enter your gender (M for Male, F for Female): ").strip().lower()
                        if gender not in ['m', 'f']:
                            print("Invalid gender input. Please enter 'M' for Male or 'F' for Female.")
                            continue  # Prompt the user again for gender if invalid
                        
                        # Check if adjacent seats are restricted
                        if self.is_adjacent_restricted(seatNo - 1, gender):
                            print("This seat cannot be booked due to adjacent seating restrictions.")
                            continue  # Prompt again for a different seat

                        # Book the seat
                        self.bookingList[seatNo - 1] = gender

                        # Print booking success and available seats
                        print(f"Seat {seatNo} booked successfully for {'Male' if gender == 'm' else 'Female'}.")
                        break  # Exit the loop once a valid seat is booked

                except ValueError:
                    print("Please enter a valid seat number.")

# Example of usage:
booking_system = SeatBooking()
booking_system.book_seat()
