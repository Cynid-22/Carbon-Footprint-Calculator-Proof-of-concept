from DBconnection import DBconnection
from FoodDetails import FoodDetails
from TransportationDetails import TransportationDetails
from CalculateFootprint import CalculateFootprint
from tabulate import tabulate
import datetime

class mgr:        
    def create_user(self, userF:FoodDetails, userT:TransportationDetails):
        db = DBconnection()
        x = datetime.datetime.now()
        strqueryF = f"insert into FoodDetails (Date, Poultry, Beef_lamb, Pork, Seafood, Egg_dairy, Rice, Bread, Vegan_dairy, Fresh_local, Non_fresh_local, Canned) values('{x}','{userF.getPoultry()}','{userF.getBeef_lamb()}','{userF.getPork()}','{userF.getSeafood()}','{userF.getEgg_dairy()}','{userF.getRice()}','{userF.getBread()}','{userF.getVegan_dairy()}','{userF.getFresh_local()}','{userF.getNon_fresh_local()}','{userF.getCanned()}')"
        strqueryT = f"insert into TransportationDetails (Date, Car, Motorbike, Plane, Bus, Train, Boat) values('{x}','{userT.getCar()}','{userT.getMotorbike()}','{userT.getPlane()}','{userT.getBus()}','{userT.getTrain()}','{userT.getBoat()}')"
        kqF = db.Execute(strqueryF)
        kqT = db.Execute(strqueryT)
        if kqF == True & kqT == True:
            print("them thanh cong")
        else:
            print("them khong thanh cong")
        
    def view_all(self):
        db = DBconnection()
        strquery = f"SELECT MAX(ID) FROM FoodDetails"
        Max = db.Return(strquery)
        Data = []
        for i in range(Max[0]):
            strqueryF = f"SELECT * FROM FoodDetails WHERE ID={i+1}"
            strqueryT = f"SELECT Car, Motorbike, Plane, Bus, Train, Boat FROM TransportationDetails WHERE ID={i+1}"
            DataFood = db.Return(strqueryF)
            DataTrans = db.Return(strqueryT)
            Data.append(DataFood + DataTrans)
        Headers = ["ID", "Date", 'Poultry', 'Beef_lamb', 'Pork', 'Seafood', 'Egg_dairy', 'Rice', 'Bread', 'Vegan_dairy', 'Fresh_local', 'Non_fresh_local', 'Canned', 'Car', 'Motorbike', 'Plane', 'Bus', 'Train', 'Boat']
        sourceFile = open('.VIEW DETAILS OUTPUT.txt', 'w')
        print(tabulate(Data, Headers, tablefmt="grid"), file = sourceFile)
        sourceFile.close()
        
    def calculate(self, i):
        db = DBconnection()
        strqueryF = f"SELECT Poultry, Beef_lamb, Pork, Seafood, Egg_dairy, Rice, Bread, Vegan_dairy, Fresh_local, Non_fresh_local, Canned FROM FoodDetails WHERE ID={i}"
        strqueryT = f"SELECT Car, Motorbike, Plane, Bus, Train, Boat FROM TransportationDetails WHERE ID={i}"
        DataFood = db.Return(strqueryF)
        DataTrans = db.Return(strqueryT)
        sourceFile = open('.CALCULATED OUTPUT.txt', 'w')
        CF = CalculateFootprint()
        print(CF.CalcTable(DataFood + DataTrans), "\n\nTotal carbon footprint for ID", i, ": ", CF.CalcMain(), file = sourceFile)
        sourceFile.close()
            
    
            