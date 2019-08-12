AVapi
=====

Get data from Alpha Vantage into python.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Author: #### Ole Olaussen: ole@ekkobit.com

Documentation
-------------

There are other python wrappers for the alpha vantage API, such as
`alphavantage`_, `alpha-vantage-downloader`_, `alpha_vantage`_ and
`alphavantage-wrapper`_. They all have in common that they have
different functions for each of the data types that Alpha Vantage
offers. This may be less practical when downloading multiple data types
at multiple resolutions in one session. Avapi has a single function that
can download any data type from Alpha Vantage: avapi.get_data() takes
\**kwargs as input and outputs a dictionary, unless datatype=“csv” is
given, in which case a csv file is saved. If the data type is time
series, avapi.to_df() converts it to a Pandas data frame. The intention
is a simple and flexible way to get data from Alpha Vantage into python.

Installation
~~~~~~~~~~~~

.. code:: shell

   pip install avapi

Before use
~~~~~~~~~~

Follow instructions on the `Alpha vantage`_ website to get a free
API-key. The `docs`_ provide all necessary info for à la carte
downloading of historical data and indicators. Please checkout Alpha
Vantage `support`_ and read through the `Frequently Asked Questions`_.

Examples
^^^^^^^^

The “demo” api-key only works for these specific examples. If you modify
the code you also need to provide your own api-key.

Single file download
''''''''''''''''''''

.. code:: python

   import avapi as aa
   import pandas as pd

   data = aa.get_data(function='VWAP', symbol='MSFT',
                      interval='15min', apikey='demo')

   df = aa.to_df(data)
   df.head()

Multiple files download
'''''''''''''''''''''''

There are limits for free accounts: up to 5 API requests per minute and
500 requests per day. In loops, if you don’t incorporate time.sleep(),
you might get errors.

.. code:: python

   import avapi as aa
   import pandas as pd
   from time import sleep

   data_path = 'data/'

   data_calls = [

   {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'MSFT',
    'apikey': 'demo',
    'datatype': 'csv',
   },
   {
    'function':'TIME_SERIES_INTRADAY',
    'symbol': 'MSFT',
    'interval': '5min',
    'apikey': 'demo',
    'datatype': 'csv',

   }
   ]


   for call in data_calls:
       save_to = data_path + call['function'] + '_' + call['symbol'] + '.csv'
       data = aa.get_data(save_to=save_to, **call)
       sleep(15)

Unexpected results
''''''''''''''''''

If you get unexpected results, you may check the latest, original
response from the Alpha Vantage server in the following way:

.. code:: python

   response = aa.response()
   print(response)

Issues
------

-  ☒ **Issue 1 -** Fulfill Alpha Vantage’s request to preserve content
   of JSON/CSV responses in both success and error cases.
-  ☒ **Issue 2 -** Make get_data() work w

.. _alphavantage: https://pypi.org/project/alphavantage/
.. _alpha-vantage-downloader: https://pypi.org/project/alpha-vantage-downloader/
.. _alpha_vantage: https://pypi.org/project/alpha_vantage/
.. _alphavantage-wrapper: https://pypi.org/project/alphavantage-wrapper/
.. _Alpha vantage: https://www.alphavantage.co
.. _docs: https://www.alphavantage.co/documentation/
.. _support: https://www.alphavantage.co/support/#support
.. _Frequently Asked Questions: https://www.alphavantage.co/support/#support
