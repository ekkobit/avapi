# Vantage
### Pandas data frames from Alpha Vantage

Author:
#### Ole Olaussen: olemolaussen@gmail.com


## Documentation

There are python wrappers for the alpha vantage API, such as [alphavantage](https://pypi.org/project/alphavantage/), [alpha-vantage-downloader](https://pypi.org/project/alpha-vantage-downloader/), [alpha_vantage](https://pypi.org/project/alpha_vantage/) and [alphavantage-wrapper](https://pypi.org/project/alphavantage-wrapper/). They all have in common that they have different functions for each of the data types that Alpha Vantage offers. This may be less practical when downloading multiple data types at multiple resolutions in one session. Avapi has a single function that can download any data type from Alpha Vantage: avapi.get_data() takes an url as input and defaults to output a Pandas data frame. There are also options for outputting dictionaries and json content, as well as saving the data as csv or json files. The urls, or API-calls, are all listed in the Alpha Vantage [Documentation](https://www.alphavantage.co/documentation/). The intention is a simple and flexible way to get data from Alpha Vantage into python.    

### Installation

```shell
pip install avapi
```
### Before use

The avapi package converts json data files from [Alpha vantage](https://www.alphavantage.co). Follow instructions on their website to get a free API-key.  Their [documentation](https://www.alphavantage.co/documentation/) provides links to à la carte downloading of historical data and indicators as json files. Substitute the "demo" API-key with your own and modify settings.

#### Examples
##### Single file download

```python
import avapi as aa

api_key = 'demo'
url = 'https://www.alphavantage.co/query?function=VWAP&symbol=MSFT&interval=15min&apikey='

df = aa.get_data(url + api_key)
```

##### Multiple files download

There are limits for a free accounts, up to 5 API requests per minute and 500 requests per day.  In loops, if you don't incorporate time.sleep(), you'll get errors.

```python
import avapi as aa
from time import sleep

api_key = 'demo'
data_path = 'data/'

api_calls = [

{
 'url': 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=',
 'filename': 'MSFT_daily.csv'
},
{
 'url': 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=',
 'filename': 'MSFT_intraday_5min.csv'
}

]


for api_call in api_calls:
    full_path = data_path + api_call['filename']
    aa.get_data(api_call['url'] + api_key, output=None, save_csv=True, csv_path=full_path)
    sleep(15)
```

## Issues

- [x] **Issue 1 -** Fulfill Alpha Vantage's request to preserve content of JSON/CSV responses in both success and error cases.
- [ ] **Issue 2 -** get_data() and get_data_by_url(), where get_data works with keywords instead.
