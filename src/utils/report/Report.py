
class Report:
    def __init__(self, userInputs):
        self.UserInputs = userInputs
        self.NetWorth = {}
        self.NetChange = {}
        self.EndPortfolio = None

        self.AppendedPortfolio = None

    def Append(self, report):
        for netWorthKey in report.NetWorth.keys():
            self.NetWorth[netWorthKey] = report.NetWorth[netWorthKey]
        for netChangeKey in report.NetChange.keys():
            self.NetChange[netChangeKey] = report.NetChange[netChangeKey]

        self.AppendedPortfolio = report.EndPortfolio
