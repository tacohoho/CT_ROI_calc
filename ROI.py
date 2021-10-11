class roiCalc:
    totalMonthlyIncome = 0
    totalMonthlyExpenses = 0
    totalMonthlyCashFlow = 0
    cashOnCashROI = 0

    def calculateIncome(self):
        ask = int(input('We will first calculate your total monthly income.\nHow much do you make from rent?'))
        self.totalMonthlyIncome = ask

    def calculateExpenses(self):
        annualTax = int(input('Next we will calculate your total monthly expenses.\nWhat is your your estimated annual tax for this property?'))
        insurance = int(input('What is your estimated monthly insurance?'))
        utility = int(input('How much do you pay for utilities monthly?'))
        self.totalMonthlyExpenses = annualTax / 12 + insurance + utility

    def calculateCashFlow(self):
        self.totalMonthlyCashFlow = self.totalMonthlyIncome - self.totalMonthlyExpenses
        print(f'Your total monthly cash flow is: {self.totalMonthlyCashFlow}')

    def calculateRIO(self):
        costOfProperty = int(input('What is the purchase price of the rental property?'))
        closingCosts = int(input('What are the estimated closing costs of this property?'))
        rehab = int(input('What is the rehab budget?'))

        self.cashOnCashRIO = self.totalMonthlyCashFlow * 6 / (costOfProperty + closingCosts + rehab)
        print(f'Your return on investment is {self.cashOnCashRIO}%')

        
        
        
def run():
                
    ask = input('Welcome to the ROI calculator! Do you want to calculate a Return On Investment for a potential rental property? (Y/N)').lower().strip()

    if ask == 'y':
        roi = roiCalc()
        roi.calculateIncome()
        roi.calculateExpenses()
        roi.calculateCashFlow()
        roi.calculateRIO()
    elif ask == 'n':
        print('Okay. Have a nice day!')
    else:
        print('Please enter a valid input')
        run()

    ask = input('Do you want to calculate another Return On Investment for a potential rental property? (Y/N)').lower().strip()
    if ask == 'y':
        run()
    elif ask == 'n':
        print('Okay. Have a nice day!')
    else:
        print('Please enter a valid input')
        run()

run()