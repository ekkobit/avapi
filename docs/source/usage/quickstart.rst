##########
Quickstart
##########

`Alpha Vantage docs
<https://www.alphavantage.co/documentation/>`_

**Is a python wrapper for the Alpha Vantage API really neccesary?**

Not really. If you are content with downloading csv files and you don't want to
or can't include a wrapper in your project or workflow, getting data from Alpha
Vantage is fairly straight forward. Referencing the
`docs <https://www.alphavantage.co/documentation/>`_, you could do something
like:

.. code-block:: python

    import requests

    url = 'https://www.alphavantage.co/query?'
    url += 'function=TIME_SERIES_INTRADAY'
    url += '&symbol=MSFT'
    url += '&interval=5min'
    url += '&apikey=demo'
    url += '&datatype=csv'

    save_to = 'MSFT_5min_intraday.csv'

    r = requests.get(url)
    content = r.content

    with open(save_to, 'wb') as file:
        file.write(content)


************
Installation
************

.. code-block:: python

    pip install avapi

==========
Before use
==========

Follow instructions on the `Alpha vantage <https://www.alphavantage.co>`_ website
to get a free API-key.  The `docs <https://www.alphavantage.co/documentation/>`_
provide all necessary info for à la carte downloading of historical data and
indicators. Please checkout Alpha Vantage
`support <https://www.alphavantage.co/support/#support>`_ and read through the
`Frequently Asked Questions <https://www.alphavantage.co/support/#support>`_.

********
Examples
********

The "demo" api-key only works for these specific examples and a limited number
of times. If you modify the code you also need to provide your own api-key.

===============
Single download
===============

.. code-block:: python

    import avapi as aa
    import pandas as pd

    data = aa.get_data(function='VWAP', symbol='MSFT',
                       interval='15min', apikey='demo')

    df = aa.to_df(data)
    df.head()


=======================
Multiple files download
=======================

There are limits for free accounts: up to 5 API requests per minute and 500
requests per day.  In loops, if you don't incorporate ``time.sleep()``, you might
get errors.

.. code-block:: python

    import avapi as aa
    import pandas as pd
    from time import sleep


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

    for i in range(len(data_calls)):
        save_to = str(i) + '.csv'
        data = aa.get_data(save_to=save_to, **data_calls[i])
        sleep(15)

==================
Unexpected results
==================

If you get unexpected results, you may check the latest, original response from
the Alpha Vantage server in the following way:

.. code-block:: python

    response = aa.response()
    print(response)
