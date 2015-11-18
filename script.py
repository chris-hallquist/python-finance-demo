import pandas
import io
import urllib2

url = "https://raw.githubusercontent.com/chris-hallquist/python-finance-demo/master/stocks_bills_bonds.csv"
data = urllib2.urlopen(url).read()
datafram = pandas.read_csv(io.BytesIO(data))
