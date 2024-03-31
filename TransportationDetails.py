class TransportationDetails:
    __Car:float
    __Motorbike:float
    __Plane:float
    __Bus:float
    __Train:float
    __Boat:float
    
    
    def __init__(self, Car='', Motorbike='', Plane='', Bus='', Train='', Boat=''):
        self.__Car = Car
        self.__Motorbike = Motorbike
        self.__Plane = Plane
        self.__Bus = Bus
        self.__Train = Train
        self.__Boat = Boat
        
        
    def getCar(self):
        return self.__Car
    def setCar(self,Car):
        self.__Car=Car
        
    def getMotorbike(self):
        return self.__Motorbike
    def setMotorbike(self,Motorbike):
        self.__Motorbike=Motorbike
        
    def getPlane(self):
        return self.__Plane
    def setPlane(self,Plane):
        self.__Plane=Plane
        
    def getBus(self):
        return self.__Bus
    def setBus(self,Bus):
        self.__Bus=Bus
        
    def getTrain(self):
        return self.__Train
    def setTrain(self,Train):
        self.__Train=Train
        
    def getBoat(self):
        return self.__Boat
    def setBoat(self,Boat):
        self.__Boat=Boat
        
    def SetInfo(self):
        self.setCar(0)
        self.setMotorbike(0)
        self.setPlane(0)
        self.setBus(0)
        self.setTrain(0)
        self.setBoat(0)
        
        if (input('Personal Transporation (y/n): ') == 'y'):
            self.setCar(float(input('How much did you travel with your Car (km): ')))
            self.setMotorbike(float(input('How much did you travel with your Motorbike (km): ')))
            print("\n")
        
        if (input('Public Transporation (y/n): ') == 'y'):
            self.setPlane(float(input('How much did you travel with a Plane (km): ')))
            self.setBus(float(input('How much did you travel with a Bus (km): ')))
            self.setTrain(float(input('How much did you travel with a Train (km): ')))
            self.setBoat(float(input('How much did you travel with a Bus (km): ')))
            print("\n") 