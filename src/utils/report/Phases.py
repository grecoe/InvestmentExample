import typing
from utils.portfolio.Portfolio import Portfolio
from utils.inputs.UserInputs import UserInputs
from utils.report.Report import Report

class Phases:

    @staticmethod
    def BeginInvestmentPeriod(userInputs: UserInputs, portfolio: Portfolio) -> Report:

        return_report = Report(userInputs)

        # Start calculation on investing year
        startingYear = userInputs.CurrentYear
        # Last year to invest before consuming
        lastInvestingYear = userInputs.RetirementYear

        # Growth Period
        while(True):

            return_report.NetWorth[startingYear] = int(portfolio.NetWorth())
            startingYear += 1
            if(startingYear > lastInvestingYear):
                break

            portfolio = portfolio.MoveForward() 
            return_report.NetChange[startingYear] = int(portfolio.NetWorth()) - return_report.NetWorth[startingYear -1] 

        return_report.EndPortfolio = portfolio
        return return_report

    @staticmethod
    def BeginRetirement(userInputs:UserInputs , portfolio:Portfolio) -> Report:
        return_report = Report(userInputs)

        # Last year to invest before consuming
        lastInvestingYear = userInputs.RetirementYear
        # Last expected retirement year, 80 is pushing it
        lastRetirementYear = userInputs.RetirementEnd

        # Expect no more income except growth from holdings
        portfolio.Income.Base = 0
        for holding in portfolio.Holdings:
            holding.AnnualGrant = 0

        while(True):
            return_report.NetWorth[lastInvestingYear] = int(portfolio.NetWorth())
            lastInvestingYear += 1
            if(lastInvestingYear > lastRetirementYear):
                break
    
            deduction = userInputs.AnnualIncomeAtRetirement - userInputs.AnticpatedSocialSecurity

            # is it in a retirement fund
            for retirementFund in portfolio.RetirementFunds:
                if retirementFund.CurrentValue > 0 and deduction > 0:
                    if retirementFund.CurrentValue >= deduction:
                        retirementFund.CurrentValue -= deduction
                        deduction = 0
                    else:
                        deduction -= retirementFund.CurrentValue
                        retirementFund.CurrentValue = 0

        
            if deduction > 0:
                for holding in portfolio.Holdings:
                    if deduction == 0:
                        break

                    value = holding.CurrentValue * holding.SharesHeld
                    if value > 0:
                        if value >= deduction:
                            sharesSold = deduction / holding.CurrentValue
                            holding.SharesHeld -= sharesSold
                            deduction = 0
                        else:
                            deduction -= value
                            holding.SharesHeld = 0
    
            # Move the ball forward
            portfolio = portfolio.MoveForward() 
            return_report.NetChange[lastInvestingYear] = int(portfolio.NetWorth()) - return_report.NetWorth[lastInvestingYear -1] 

        return_report.EndPortfolio = portfolio
        return return_report
