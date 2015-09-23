# Assignment 2


# Problem 1

foreign_currency = input('Please enter the foreign currency: ')
print(foreign_currency)

foreign_amount = float(input('Please enter amount in ' + foreign_currency + ': '))
print(foreign_amount)

fx_rate = float(input('Please enter the exchange rate: '))
print(fx_rate)

dollar_amount = foreign_amount * fx_rate
print('The equivalent USD amount is: ' + str(dollar_amount))


# Problem 2

stock_ticker = input('Please enter stock ticker: ')
print(stock_ticker)

loc = stock_ticker.find('.')

stock_name = stock_ticker[0:loc:1]
stock_exchange = stock_ticker[loc+1:len(stock_ticker):1]

print(stock_name + ' is traded on ' + stock_exchange)


# Problem 3

full_name = input('Please enter your name in the "Last_Name, First_Name" format: ')
print(full_name)

loc = full_name.find(',')

first_name = full_name[loc+2:len(full_name):1]
first_name_length = str(len(first_name))
last_name = full_name[0:loc:1]

print('Welcome ' + first_name + ' ' + last_name + '! Your first name is ' + first_name_length + ' letters long.')


