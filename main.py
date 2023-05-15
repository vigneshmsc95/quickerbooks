import requests

# Endpoint 1: getAccountBalanceBreakdown
company_id = 1
url = f'http://localhost:5000/company/{company_id}/balance-breakdown'
response = requests.get(url)
data = response.json()
print(data)

# Endpoint 2: getIncomeExpenseForDate
company_id = 1
month = 5
year = 2023
url = f'http://localhost:5000/company/{company_id}/income-expense?month={month}&year={year}'
response = requests.get(url)
data = response.json()
print(data)

# Endpoint 3: getTransactionsForInterval
company_id = 1
start_datetime = '2023-05-01T00:00:00'
end_datetime = '2023-05-12T00:00:00'
url = f'http://localhost:5000/company/{company_id}/transactions?start_datetime={start_datetime}&end_datetime={end_datetime}'
response = requests.get(url)
data = response.json()
print(data)




