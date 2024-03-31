class FoodDetails:
    __Poultry:int
    __Beef_lamb:int
    __Pork:int
    __Seafood:int
    __Egg_dairy:int
    __Rice:int
    __Bread:int
    __Vegan_dairy:int
    __Fresh_local:int
    __Non_fresh_local:int
    __Canned:int
    
    
    def __init__(self, Poultry='', Beef_lamb='', Pork='', Seafood='', Egg_dairy='', Rice='', Bread='', Vegan_dairy='', Fresh_local='', Non_fresh_local='', Canned=''):
        self.__Poultry = Poultry
        self.__Beef_lamb = Beef_lamb
        self.__Pork = Pork
        self.__Seafood = Seafood
        self.__Egg_dairy = Egg_dairy
        self.__Rice = Rice
        self.__Bread = Bread
        self.__Vegan_dairy = Vegan_dairy
        self.__Fresh_local = Fresh_local
        self.__Non_fresh_local = Non_fresh_local
        self.__Canned = Canned
        
        
    def getPoultry(self):
        return self.__Poultry
    def setPoultry(self,Poultry):
        self.__Poultry=Poultry
        
    def getBeef_lamb(self):
        return self.__Beef_lamb
    def setBeef_lamb(self,Beef_lamb):
        self.__Beef_lamb=Beef_lamb
        
    def getPork(self):
        return self.__Pork
    def setPork(self,Pork):
        self.__Pork=Pork
        
    def getSeafood(self):
        return self.__Seafood
    def setSeafood(self,Seafood):
        self.__Seafood=Seafood
        
    def getEgg_dairy(self):
        return self.__Egg_dairy
    def setEgg_dairy(self,Egg_dairy):
        self.__Egg_dairy=Egg_dairy
        
    def getRice(self):
        return self.__Rice
    def setRice(self,Rice):
        self.__Rice=Rice
        
    def getBread(self):
        return self.__Bread
    def setBread(self,Bread):
        self.__Bread=Bread
        
    def getVegan_dairy(self):
        return self.__Vegan_dairy
    def setVegan_dairy(self,Vegan_dairy):
        self.__Vegan_dairy=Vegan_dairy
        
    def getFresh_local(self):
        return self.__Fresh_local
    def setFresh_local(self,Fresh_local):
        self.__Fresh_local=Fresh_local
        
    def getNon_fresh_local(self):
        return self.__Non_fresh_local
    def setNon_fresh_local(self,Non_fresh_local):
        self.__Non_fresh_local=Non_fresh_local
        
    def getCanned(self):
        return self.__Canned
    def setCanned(self,Canned):
        self.__Canned=Canned
        
    def SetInfo(self):
        self.setPoultry(0)
        self.setBeef_lamb(0)
        self.setPork(0)
        self.setSeafood(0)
        self.setEgg_dairy(0)
        self.setRice(0)
        self.setBread(0)
        self.setVegan_dairy(0)
        self.setFresh_local(0)
        self.setNon_fresh_local(0)
        self.setCanned(0)
    
        if (input("Animal based food? (y/n): ") == "y"):
            self.setPoultry(input("Enter Poultry weight in grams: "))
            self.setBeef_lamb(input("Enter Beef/lamb weight in grams: "))
            self.setPork(input("Enter Pork weight in grams: "))
            self.setSeafood(input("Enter Seafood weight in grams: "))
            self.setEgg_dairy(input("Enter Egg, dairy weight in grams: "))
            print("\n")
            
        if (input("Non-animal based food? (y/n): ") == "y"):
            self.setRice(input("Enter Rice weight in grams: "))
            self.setBread(input("Enter Bread weight in grams: "))
            self.setVegan_dairy(input("Enter Vegan dairy-like products weight in grams: "))
            print("\n")
        
        print("The total should be 100")
        F = int(input("Enter percentage of fresh locally sourced food (local market): "))
        N = int(input("Enter percentage of bulk locally sourced food (produce isle in supermarket): "))
        C = int(input("Enter percentage of Canned food: "))
        print("\n")
        
        while(F+N+C != 100):
            print("The total should be 100")
            F = int(input("Enter percentage of fresh locally sourced food (local market): "))
            N = int(input("Enter percentage of bulk locally sourced food (produce isle in supermarket): "))
            C = int(input("Enter percentage of Canned food: "))
            print("\n")
        self.setFresh_local(F)
        self.setNon_fresh_local(N)
        self.setCanned(C)
    