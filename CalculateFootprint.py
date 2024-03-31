from tabulate import tabulate
class CalculateFootprint:
    __Data:tuple
    __TotalFootprint:float
    def __init__(self, Data=''):
        self.__Data = Data
        self.__Result = []
        self.__TotalFootprint = 0
        self.__Values = (2  # Poultry (g)
                        ,2  # Beef/lamb (g)
                        ,2  # Pork (g)
                        ,2  # Seafood (g)
                        ,2  # Egg, dairy (g)
                        ,2  # Rice (g)
                        ,2  # Brea (g)
                        ,2  # Vegan dairy (g)
                        ,2  # Fresh local (g)
                        ,2  # Non-fresh local (g)
                        ,2  # Canned (g)
                        ,2  # Car (km)
                        ,2  # Motorbike (km)
                        ,2  # Plane (km)
                        ,2  # Bus (km)
                        ,2  # Train (km)
                        ,2) # Boat (km)
    
        
    def CalcTable(self, Data):
        BiggerData = []
        
        self.__Data = Data
        for x in range(len(self.__Data)):
            self.__Result.append(self.__Data[x] * self.__Values[x])
        BiggerData.append(self.__Result)
        Headers = ['Poultry', 'Beef_lamb', 'Pork', 'Seafood', 'Egg_dairy', 'Rice', 'Bread', 'Vegan_dairy', 'Fresh_local', 'Non_fresh_local', 'Canned', 'Car', 'Motorbike', 'Plane', 'Bus', 'Train', 'Boat']
        return tabulate(BiggerData, Headers, tablefmt="grid")
    
    def CalcMain(self):
        for x in self.__Result:
            self.__TotalFootprint += x
        return self.__TotalFootprint