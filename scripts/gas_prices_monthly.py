import csv
#import os
import urllib
#import dataconverters.xls

# first run the extract
# os.system('. scripts/constituents.sh')
source = "http://www.eia.gov/dnav/ng/hist_xls/RNGWHHDm.xls?force_download=true"
xlspath = 'cache/gas_prices_monthly.xls'
path = 'data/gas_prices_monthly.csv'

def execute():
    urllib.urlretrieve(source, xlspath)

    #existingr = csv.reader(open(path))
    #header = existingr.next()
    # { symbol: row } dict
    #existing = dict([ [row[0], row] for row in existingr ])

    import datautil.tabular.xls as xlstab
    reader = xlstab.XlsReader()
    tabdata = reader.read(open(xlspath), sheet_index=1)
    records = tabdata.data

    header = ['Date', 'Price (Dollars per million btu)']
    # data begins on row 4
    records = records[4:]
    records = [ [ fixsymbol(x[0]), x[1] ] for x in records ]
    #print records[0]

    writer = csv.writer(open(path, 'w'), lineterminator='\n')
    writer.writerow(header)
    writer.writerows(records)

def fixsymbol(symbol):
    symbol = symbol.strftime('%Y-%m')
    return symbol

execute()


