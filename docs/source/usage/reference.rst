#########
Reference
#########


AVAPI is a simple python wrapper for the Alpha Vantage API. AVAPI has one
module: ``avapi.data``. It handles getting and manipulating data from Alpha Vantage.

|

================
Getting the data
================

.. role:: python(code)
    :language: python

If :python:`csv=True`, a csv file will be saved in current working directory.
Otherwise, ``avapi.data.get_data()`` will return a dictionary of Alpha Vantage
data.

|

.. autofunction:: avapi.get_data

|

=========================================
Converting dictionary to pandas.DataFrame
=========================================

When ``avapi.get_data(csv=False)`` downloads data, it converts the Alpha Vantage
server response from ``json`` to python ``dict``. If the data type is a time series,
``avapi.to_df()`` can then convert it to a Pandas data frame.

|

.. autofunction:: avapi.to_df

|

==================
Unexpected results
==================

When you get unexpected results, you might want to check out the latest raw
response from the Alpha Vantage server.

|

.. autofunction:: avapi.response
