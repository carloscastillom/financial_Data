import os
import pandas as pd
from yahooquery import Ticker

symbols = ['aapl', 'amzn', 'nflx', 'goog', 'fb']

for i in symbols:
    directory = f'directory_{i}'
    if not os.path.exists(directory):
        os.makedirs(directory)
    tk = Ticker(i)
    try:
        income_statement = tk.income_statement()
        print(type(income_statement))  # print the data type of income_statement
        print(income_statement)  # print the content of income_statement

        file_path = os.path.join(directory, 'data.csv')
        income_statement.to_csv(file_path)
    except AttributeError:
        print(f"Income statement data unavailable for {i}")
    #print(df)
