
class Holding :

    def __init__(self, name, holdingData):
        if isinstance(holdingData, dict) == False:
            raise Exception("Holding expected to be dictionary")
        
        self.Name = name
        # Now ensure the keys
        holdingKeys = holdingData.keys()
        if "CurrentValue"  not in holdingKeys:
            raise Exception("Current Value expected in Holding")
        self.CurrentValue = holdingData["CurrentValue"]

        if "SharesHeld"  not in holdingKeys:
            raise Exception("Number of held shares expected")
        self.SharesHeld = holdingData["SharesHeld"]

        if "DividendPayout"  not in holdingKeys:
            raise Exception("Dividend Value expected, 0 accepted")
        self.DividendPayout = holdingData["DividendPayout"]

        if "AnnualGrowth"  not in holdingKeys:
            raise Exception("AnnualGrowth as decimal of percentage expected.")
        self.AnnualGrowth = holdingData["AnnualGrowth"]

        if "AnnualGrant" not in holdingKeys:
            raise Exception("AnnualGrant as decimal of percentage expected.")
        self.AnnualGrant = holdingData["AnnualGrant"]

    def MoveForward(self, income):
        ret_holding = self.Copy()
        currentTotalValue = self.CurrentValue * self.SharesHeld
        dividendIncome = currentTotalValue * self.DividendPayout
        newSharePrice = self.CurrentValue + (self.CurrentValue * self.AnnualGrowth)
        newShareCount = self.SharesHeld + (dividendIncome/newSharePrice)

        # if annual grant figure it out
        if self.AnnualGrant > 0:
            additionalShares = (income.Base * self.AnnualGrant)/newSharePrice
            newShareCount += additionalShares

        ret_holding.CurrentValue = newSharePrice
        ret_holding.SharesHeld = newShareCount

        return ret_holding


    def Copy(self):
        return Holding(self.Name, self.__dict__)
