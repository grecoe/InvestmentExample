import json
import os
from utils.portfolio.Holding import Holding
from utils.portfolio.Retirement import RetirementFund
from utils.portfolio.Income import Income

class Portfolio:

    def __init__(self, porfolioFile):
        self.PortfolioFile = porfolioFile
        self.Holdings = []
        self.RetirementFunds = []
        self.Income = None

        # If none we want a blank slate
        if porfolioFile != None:

            if os.path.exists(self.PortfolioFile) == False:
                raise Exception("Must provide valid portfolio file")

            with open(self.PortfolioFile, "r") as input_config:
                config_settings = json.loads("\n".join(input_config.readlines()))

                self.Income = Income(config_settings["Income"])

                for holding in config_settings["Investments"].keys():
                    self.Holdings.append(Holding(holding, config_settings["Investments"][holding]))

                for retirement in config_settings["Retirement"].keys():
                    self.RetirementFunds.append(RetirementFund(retirement, config_settings["Retirement"][retirement]))

    def MoveForward(self):
        newPortfolio = Portfolio(None)
        newPortfolio.Income = self.Income.MoveForward()

        for holding in self.Holdings:
            newPortfolio.Holdings.append(holding.MoveForward(self.Income))

        for retirement in self.RetirementFunds:
            newPortfolio.RetirementFunds.append(retirement.MoveForward(self.Income))

        return newPortfolio

    def Print(self):
        print("Net Worth", int(self.NetWorth()))
        print("Income Base", int(self.Income.Base))
        print("Holdings")
        for holding in self.Holdings:
            print(holding.Name, int(holding.SharesHeld), int(holding.CurrentValue), int(holding.CurrentValue * holding.SharesHeld))
        print("Retirement Funds")
        for retirement in self.RetirementFunds:
            print(retirement.Name, int(retirement.CurrentValue))    

    def NetWorth(self):
        return_value = 0

        for holding in self.Holdings:
            return_value += holding.SharesHeld * holding.CurrentValue
        
        for retirement in self.RetirementFunds:
            return_value += retirement.CurrentValue
        
        return return_value