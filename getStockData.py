import io
import requests

token = '25D26255F6924F31BD86503A4253BEA0'
start = '9/1/2015'
end = '9/18/2015'
arr = ['GOOG', 'APPL']

def queryStock(stockArray, startDate, endDate):
    result = [];
    print(stockArray)
    for stock in stockArray:
        print(stock)
        url='http://ws.nasdaqdod.com/v1/NASDAQAnalytics.asmx/GetEndOfDayData'
        data = {'_Token' : '%s' % token,
        'Symbols' : '%s' % stock,
        'StartDate' : '%s' % startDate,
        'EndDate' : '%s' % endDate,
        'MarketCenters' : '' }
        r = requests.get(url, params = data)
        with io.FileIO(stock + startDate[:-4] + endDate[:-4] + ".xml", 'w') as f:
            f.write(r.text)
            f.close()

queryStock(arr, start, end)
