import io
import requests

token = '25D26255F6924F31BD86503A4253BEA0'

def queryStock(stockArray, startDate, endDate):
    for stock in stockArray:
        url='http://ws.nasdaqdod.com/v1/NASDAQAnalytics.asmx/GetEndOfDayData'
        data = {'_Token' : '%s' % token,
        'Symbols' : '%s' % stock,
        'StartDate' : '%s' % startDate,
        'EndDate' : '%s' % endDate,
        'MarketCenters' : '' }
        r = requests.get(url, params = data)
        with io.FileIO(stock + startDate.replace('/', '.')[:-5] + 'to' + endDate.replace('/', '.')[:-5] + ".xml", 'w') as f:
            f.write(r.text)
            f.close()
        return r.text
