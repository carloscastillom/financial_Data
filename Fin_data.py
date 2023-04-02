import os
import pandas as pd
from yahooquery import Ticker
import time

symbols = ['aapl', 'amzn', 'nflx', 'goog', 'fb', 'BYND']
directory ='directory'
start_time = time.time()  # record the start time
for i in symbols:
    if not os.path.exists(directory):
        os.makedirs(directory)
    tk = Ticker(i)
    try:
        income_statement = tk.income_statement()
        print(type(income_statement))  # print the data type of income_statement
        print(income_statement)  # print the content of income_statement
        print(time.time())  # print the content of income_statement

        file_path = os.path.join(directory, f'{i}_.csv')
        income_statement.to_csv(file_path)
    except AttributeError:
        print(f"Income statement data unavailable for {i}")

end_time = time.time()  # record the end time
print(f"Total execution time: {end_time - start_time} seconds")  # print the total execution time
