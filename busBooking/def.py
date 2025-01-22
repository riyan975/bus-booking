import csv
seatNoList=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
with open("passengerData.csv",'r+',newline="") as f:
    r =  csv.reader(f)
    data = list(r)
    for i in data:
        if i[0]!='1':
            seatNoList = list(set(seatNoList) - set(i[8]))
            print(seatNoList)
