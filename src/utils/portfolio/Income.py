
class Income :

    def __init__(self, incomeData):
        if isinstance(incomeData, dict) == False:
            raise Exception("Income expected to be dictionary")
        
        # Now ensure the keys
        holdingKeys = incomeData.keys()
        if "Base"  not in holdingKeys:
            raise Exception("Base salary Value expected in Holding")
        self.Base = incomeData["Base"]

        if "AnnualGrowth"  not in holdingKeys:
            raise Exception("AnnualGrowth of held shares expected")
        self.AnnualGrowth = incomeData["AnnualGrowth"]

        if "Bonus"  not in holdingKeys:
            raise Exception("Bonus of held shares expected")
        self.Bonus = incomeData["Bonus"]

    def MoveForward(self):
        ret_value = self.Copy()
        ret_value.Base = self.Base + (self.Base * self.AnnualGrowth)
        return ret_value
    
    def Copy(self):
        return Income(self.__dict__)
