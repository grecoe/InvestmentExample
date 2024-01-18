
class Overview:
    def __init__(self):
        self.ReportOutput = []

    
    def AddUserInputs(self, userInputs):
        self.ReportOutput.append("Investment Started: {}".format(userInputs.CurrentYear))
        self.ReportOutput.append("Retirement Year   : {}".format(userInputs.RetirementYear))        
        self.ReportOutput.append("Retirement End    : {}".format(userInputs.RetirementEnd))    

        self.ReportOutput.append("Annual Retirement Withdrawal: {}".format(userInputs.AnnualIncomeAtRetirement))    
        self.ReportOutput.append("Annual Social Security      : {}".format(userInputs.AnticpatedSocialSecurity))    

    def AddPortfolio(self, portfolio, title):
        self.ReportOutput.append(f"\nPortfolio At {title} ->")
        self.ReportOutput.append("\nHoldings:")
        for holding in portfolio.Holdings:
            value = holding.CurrentValue * holding.SharesHeld
            self.ReportOutput.append(f"{holding.Name:10} -  ${int(value):10}")

        self.ReportOutput.append("\nRetirement Funds:")
        for fund in portfolio.RetirementFunds:
            self.ReportOutput.append(f"{fund.Name:10} -  ${int(fund.CurrentValue):10}")        

    def DefineNetWorthChange(self,report):
        self.ReportOutput.append("\nValue Changes:")
        col1 = "Year"
        col2 = "Value"
        col3 = "Change"

        self.ReportOutput.append(f"\n{col1:10}{col2:10}{col3:10}")

        for year in report.NetWorth.keys():
            networth = report.NetWorth[year]
            netchange = 0
            if year in report.NetChange.keys():
                netchange = report.NetChange[year]
            self.ReportOutput.append(f"{year:10}{networth:10}{netchange:10}")

        