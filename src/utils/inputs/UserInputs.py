from datetime import datetime

class UserInputs:
    def __init__(self):
        self.CurrentYear = datetime.now().year
        self.RetirementYear = 0
        self.RetirementEnd = 0
        self.AnnualIncomeAtRetirement = 0

        self.YearsToRetire = 0
        self.YearsInRetirement = 0
        self.AnticpatedSocialSecurity = 0
    
    def GetUserInputs(self):
        self.YearsToRetire = self._UserInput("How many years until you retire? ")
        self.YearsInRetirement = self._UserInput("How many years of retirement? ")
        self.AnticpatedSocialSecurity = self._UserInput("Anticipated Social Security Benefit Annually? ")
        self.AnnualIncomeAtRetirement = self._UserInput("Annual withdrawal in retirement? ")

        self.RetirementYear = self.CurrentYear + self.YearsToRetire
        self.RetirementEnd = self.RetirementYear + self.YearsInRetirement

    def _UserInput(self, prompt):
        return_value = 0
        uInput = input(prompt)
        try:
            return_value = int(uInput)
        except:
            print("Integer value expected, try again.")
            return_value = self._UserInput(prompt)
        
        return return_value