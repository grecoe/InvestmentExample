import sys
import argparse
from utils.portfolio.Portfolio import Portfolio
from utils.inputs.UserInputs import UserInputs
from utils.report.Phases import Phases
from utils.report.Overview import Overview


# You prepare the parser the way you want it.....
parser = argparse.ArgumentParser(description='Portfolio Tool')
parser.add_argument("-portfolio", required=True, type=str, help="Portfolio JSON")
programargs = parser.parse_args(sys.argv[1:])

# Get user information required
userInputs = UserInputs()
userInputs.GetUserInputs()

# Load portfolio and income data
portfolio = Portfolio(programargs.portfolio)

# Overview is the report to output
overview = Overview()
overview.AddUserInputs(userInputs)

# Let assets accrue
investment_report = Phases.BeginInvestmentPeriod(userInputs, portfolio)
overview.AddPortfolio(investment_report.EndPortfolio, "Investment Period End")

# Start living off assets
retire_report = Phases.BeginRetirement(userInputs, investment_report.EndPortfolio)
overview.AddPortfolio(retire_report.EndPortfolio, "Retirement Period End")

# Now get all the networth and netchange combined
investment_report.Append(retire_report)
overview.DefineNetWorthChange(investment_report)


with open("RetirementReport.txt", "w") as retirement_file:
    for data in overview.ReportOutput:
        retirement_file.write(f"{data}\n")