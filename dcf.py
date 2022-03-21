import yfinance as yf

# Stock Intinsic Value Calculation
stock = yf.Ticker("tsla")
outstandingshares=stock.info['sharesOutstanding'] # Fetch number of shares

#Assumptions
required_rate=0.07 #discount rate or WACC
perpetual_rate=0.02 #assumes the business will continue to generate Free Cash Flow (FCF) at a normalized state forever (perpetuity)
cashflowgrowthrate=0.03 #appx subtract year 1 cash flows from year 2 cash flows and then divide by year 1 cash flows

years =[1,2,3,4]

freecashflow = [-221714,968000,2701000,3483000] #Last 4 years, in 1000s of $

futurefreecashflow = []
discountfactor = []
discountedfuturefreecashflow =[]

terminalvalue = freecashflow[-1] *(1+perpetual_rate)/(required_rate-perpetual_rate)
#print(terminalvalue)

for year in years:
    cashflow=freecashflow[-1]*(1+cashflowgrowthrate)**year
    futurefreecashflow.append(cashflow)
    discountfactor.append((1+required_rate)**year)

#print(discountfactor)
#print(futurefreecashflow)

for i in range (0, len(years)):
    discountedfuturefreecashflow.append(futurefreecashflow[i]/discountfactor[i])

#print(discountedfuturefreecashflow)

discountedterminalvalue=terminalvalue/(1+required_rate)**4
discountedfuturefreecashflow.append(discountedterminalvalue)

todaysvalue=sum(discountedfuturefreecashflow)

fairvalue=todaysvalue*1000/outstandingshares

print("The fair value of TSLA is ${}".format(round(fairvalue,2)))