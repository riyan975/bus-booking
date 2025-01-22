from passinfo import*
from showticket import*
from admin import*
global ch 

print("---------------------------------------------------")
print("           Welcome To Royal Bus Travel        ")
print("---------------------------------------------------")
print()

def start(): #called function
    print()
    print("1. Passenger Registration :")
    print("2. Show Ticket            :")
    print()
    ch = int(input("Choose Any One Option :"))
    if ch == 1:
        pd_obj = PassengerDataCsv()
        pd_obj.getPassengerInfo()
        pd_obj.saveInfo()
    elif ch ==2:
        obj = TicketShow()
        obj.ticketShow()

start()

    
