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

# Relative returns for stocks and bonds, compared to the risk-free rate of interest
stock_rel_ret = df[STOCK_KEY] - df[BILL_KEY]
bond_rel_ret = df[BOND_KEY] - df[BILL_KEY]

stock_avg = stock_rel_ret.mean()
bond_avg = bond_rel_ret.mean()

stock_var = stock_rel_ret.var()
bond_var = bond_rel_ret.var()

cov = stock_rel_ret.cov(bond_rel_ret)

def portfolio_return(stock_weight, bond_weight):
    return stock_weight * stock_avg + bond_weight * bond_avg

# http://www.investopedia.com/terms/p/portfolio-variance.asp
def portfolio_variance(stock_weight, bond_weight):
    return stock_weight**2 * stock_var + 2 * stock_weight * bond_weight * cov + bond_weight**2 * bond_var

def sharpe(stock_weight, bond_weight):
    return portfolio_return(stock_weight, bond_weight) + portfolio_variance(stock_weight, bond_weight)

print(sharpe(1, 0))
print(sharpe(0.9, 0.1))
print(sharpe(0.6, 0.4))
print(sharpe(0.3, 0.7))
