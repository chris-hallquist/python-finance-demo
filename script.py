import io
import numpy as np
import pandas as pd
import urllib2

YEAR_KEY = "Year"
STOCK_KEY = "S&P 500"
BILL_KEY = "3-month T.Bill"
BOND_KEY = "10-year T. Bond"

# http://stackoverflow.com/questions/25669588/convert-percent-string-to-float-in-pandas-read-csv
def p2f(x):
    return float(x.strip('%'))/100

converters = {
        YEAR_KEY: int,
        STOCK_KEY: p2f,
        BILL_KEY: p2f,
        BOND_KEY: p2f
        }

url = "https://raw.githubusercontent.com/chris-hallquist/python-finance-demo/master/stocks_bills_bonds.csv"
data = urllib2.urlopen(url).read()
df = pd.read_csv(io.BytesIO(data), converters=converters)

print(df)
