import os
import pandas as pd
from yahooquery import Ticker


symbols = ['fb', 'aapl', 'amzn', 'nflx', 'goog']

for i in symbols:
    tk = Ticker(i)
    df = tk.income_statement()
    print(df)
    
