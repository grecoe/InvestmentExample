
class RetirementFund:

    def __init__(self, name, retirementData):
        if isinstance(retirementData, dict) == False:
            raise Exception("Holding expected to be dictionary")
        
        self.Name = name
        # Now ensure the keys
        holdingKeys = retirementData.keys()
        if "CurrentValue"  not in holdingKeys:
            raise Exception("Current Value expected in Holding")
        self.CurrentValue = retirementData["CurrentValue"]

        if "AnnualGrowth"  not in holdingKeys:
            raise Exception("AnnualGrowth as decimal of percentage expected.")
        self.AnnualGrowth = retirementData["AnnualGrowth"]

        if "AnnualAdditionFromIncome"  not in holdingKeys:
            raise Exception("AnnualAdditionFromIncome as decimal of percentage expected.")
        self.AnnualAdditionFromIncome = retirementData["AnnualAdditionFromIncome"]

    def MoveForward(self, income):
        ret_retirement = self.Copy()
        ret_retirement.CurrentValue = self.CurrentValue + (self.CurrentValue * self.AnnualGrowth) + (income.Base * self.AnnualAdditionFromIncome)
        return ret_retirement

    def Copy(self):
        return RetirementFund(self.Name, self.__dict__)
