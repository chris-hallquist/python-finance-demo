import pandas
import io
import urllib2

STOCK_KEY = "S&P 500"
BILL_KEY = "3-month T.Bill"
BOND_KEY = "10-year T. Bond"

url = "https://raw.githubusercontent.com/chris-hallquist/python-finance-demo/master/stocks_bills_bonds.csv"
data = urllib2.urlopen(url).read()
datafram = pandas.read_csv(io.BytesIO(data))
