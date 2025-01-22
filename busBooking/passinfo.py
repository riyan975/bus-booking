import csv
class PassengerRegistration():
    def __init__(self):
        self.passengerName = None
        self.noOfPassenger = None
        self.departureLocation = None
        self.destinationLocation = None
        self.ddmmyyyy = None
        self.seatNo = None
        self.selectBusType = None
        self.busFare = None
        self.gender = []
        self.autoInc = 1
        self.countcol= 0
        self.number=0
    def getPassengerInfo(self):
        self.passengerName     = input("Enter Passenger Name          :")
        print("1: Kurnool")
        print("2: Vijayawada")
        print("3: Hyderabad")
        self.dl = int(input("Enter Departure Location"))
        if self.dl == 1:
            self.departureLocation = "Kurnool"
        elif self.dl == 2:
            self.departureLocation = "Vijayawada"
        elif self.dl == 3:
            self.departureLocation = "Hyderabad"
        else:
            print("Please Enter correct choice  :")
        print("1: Kurnool")
        print("2: Vijayawada")
        print("3: Hyderabad")
        self.dpl = int(input("Enter Destination Location  :"))
        if self.dpl == 1:
            self.destinationLocation = "Kurnool"
        elif self.dpl == 2:
            self.destinationLocation = "Vijayawada"
        elif self.dpl == 3:
            self.destinationLocation = "Hyderabad"
        else:
            print("Please Enter correct choice  :")
        self.ddmmyyyy = input("Enter Date of Joiurney Like 07-05-1992   :")
        self.number = int(input("enter mobile number"))
        self.noOfPassenger = int(input("Enter Number Of Passenger :"))
        if self.dl != self.dpl:
            if ((self.dl == 1 and self.dpl == 2) or (self.dl== 2 and self.dpl== 1 )):
                print(" 1. AC BUS = 950 fare with all GST")
                print(" 2. NON AC BUS = 620 fare with all GST")
                self.busType = int(input("Select Bus Type  :"))
                if  self.busType == 1 :
                    self.busFare = self.noOfPassenger*950
                else :
                    self.busFare = self.noOfPassenger*620

            elif ((self.dl == 1 and self.dpl == 3 ) or (self.dl == 3 and self.dpl == 1 )):
                print(" 1. AC BUS = 700 fare with all GST")
                print(" 2. NON AC BUS = 450 fare with all GST")
                self.busType = int(input("Select Bus Type  :")) 
                if  self.busType == 1 :
                    self.busFare = self.noOfPassenger*700
                else :
                    self.busFare = self.noOfPassenger*450
            elif ((self.dl == 2 and self.dpl == 3 ) or (self.dl == 3 and self.dpl == 2 )):
                print(" 1. AC BUS = 750 fare with all GST")
                print(" 2. NON AC BUS = 450 fare with all GST")
                self.busType = int(input("Select Bus Type  :"))
                if  self.busType == 1 :
                    self.busFare = self.noOfPassenger*750
                else :
                    self.busFare = self.noOfPassenger*450
            if  self.busType == 1 :
                self.type = "AC"
            else :
                self.type = "non AC"
            print("[1]__[7]__[8]_[15]_[16]_[23]_[24]_[31]_[32]")
            print("[2]__[6]__[9]_[14]_[17]_[22]_[25]_[30]_[33]")
            print("                                       [34]")
            print("   __[5]_[10]_[13]_[18]_[21]_[26]_[29]_[35]")
            print("[3]__[4]_[11]_[12]_[19]_[20]_[27]_[28]_[36]")
            self.bookingList = []
            self.seatNoList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
            for i in range(self.noOfPassenger):
                seatbooking(self.noOfPassenger,self.bookingList,self.seatNoList,i)
                gender = input("Enter passenger gender(M for Male, F for Female) : ")
                self.gender.append(gender)
        else :
            print("you selected the same location")

class PassengerDataCsv(PassengerRegistration):
    def saveInfo(self):
        try:
            with open("passengerData.csv",'r+',newline="") as f:
                r =  csv.reader(f)
                data = list(r)
                for  i in data:
                    self.autoInc += 1
                    for j in i:
                        self.countcol +=1
                    print()
                print("your booking id is :",self.autoInc)   
            
        except:
            print("File has not available")
        finally:     
            with open("passengerData.csv",'a+',newline="") as f:
                w =  csv.writer(f)
                w.writerow([self.autoInc,self.passengerName,self.gender,self.number,self.noOfPassenger,self.departureLocation,self.destinationLocation,self.ddmmyyyy,self.bookingList,self.type,self.busFare])
                print("Data Save successfully")
                print()
def seatbooking(noOfPassenger,bookingList,seatNoList,i):
         
                    try:
                        seatNo = int(input(f"Passenger {i + 1}, Choose a Seat Number: "))
                        if seatNo > 36 or seatNo <= 0:
                            print("Don't Choose a Seat Number which is not available.")
                        elif seatNo not in seatNoList:
                            print("Ticket Already Booked")
                            print("enter another seat")
                            seatbooking(noOfPassenger,bookingList,seatNoList,i) 

                        else:
                            bookingList.append(seatNo)
                            seatNoList.remove(seatNo)
                            print(f"Seat {seatNo} booked successfully.")
                            print(f"{len(seatNoList)} seats remaining.")
                            print("Available seats:",seatNoList)

                    except ValueError:
                        print("Please enter a valid seat number.")