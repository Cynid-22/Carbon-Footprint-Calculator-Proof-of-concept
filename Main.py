from DBconnection import DBconnection
from FoodDetails import FoodDetails
from TransportationDetails import TransportationDetails
from mgr import mgr

tmp =-1
while tmp != 0:
    print("1. Add")
    print("2. View")
    print("3. Calculate Carbon Footprint")
    print("0. Exit")
    tmp = int(input("chon: "))
    if tmp == 1:
        k = mgr()
        newF = FoodDetails()
        newF.SetInfo()
        newT = TransportationDetails()
        newT.SetInfo()
        k.create_user(newF, newT)
    elif tmp == 2:
        k = mgr()
        k.view_all()
    elif tmp == 3:
        k = mgr()
        k.calculate(int(input('Enter ID: ')))