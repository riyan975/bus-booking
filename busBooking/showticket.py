#Data Importing section
from passinfo import*

class TicketShow:

    def ticketShow(self):
        bln = [] # list for storing data and retrieving from passengerData.csv file
        with open("passengerData.csv",'r+',newline="") as f:
            r =  csv.reader(f)
            data = list(r)
            id = int(input("Enter Your Booking Id  :"))
            for i in data:
                if id == int(i[0]):
                    for j in i:
                        bln.append(j)
                    break
        #print(bln)  
        print("------------------------------------------------------------------------------")
        print("                          Ankush Nag Bus Travel                               ")
        print("------------------------------------------------------------------------------")
        print()
        print(" e_Ticket :", "NUZVID Address              : RGUKT IIIT collage")
        print("           ", "Phone No\Mob No             :",bln[3])
        print()
        print("",bln[5],"------------->",bln[6],"            ","        Passenger Id:",bln[0])
        print()
        print(" Passenger Name :", bln[1],"              ","Number of Passenger :",bln[4])
        
        print("______________________________________________________________________________")
        print()
        print("Seat No :",bln[8],"              "," Date of Booking :",bln[7],"              ")
        print(" Passenger gender with respective to seat No:",bln[2])
        print()
        print(" Bus Type :       ",bln[9],"                                                           ")
        print(" Bus Fare :       ",bln[10],"                                                           ")
        print()
        print("------------------------------------------------------------------------------")
                



