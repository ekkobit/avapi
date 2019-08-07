URLS = \

{
'intraday': 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' \
+ ticker + '&interval=' + interval + '&outputsize=' + outputsize + '&apikey=' + api_key \
+ '&datatype=' datatype,

'daily': 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + ticker \
+ '&outputsize=' + outputsize' + &apikey=' + api_key + '&datatype=' datatype,

'daily_adjusted': 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + \
ticker + '&outputsize=' + outputsize + '&apikey=' + api_key + '&datatype=' datatype,

}
