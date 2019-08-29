.. AVAPI documentation master file, created by
   sphinx-quickstart on Wed Aug 28 18:20:54 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation
=============

There are other python wrappers for the alpha vantage API, such as
`alphavantage <https://pypi.org/project/alphavantage/>`_,
`alpha-vantage-downloader <https://pypi.org/project/alpha-vantage-downloader/>`_,
`alpha_vantage <https://pypi.org/project/alpha_vantage/>`_ and
`alphavantage-wrapper <https://pypi.org/project/alphavantage-wrapper/>`_. They
all have in common that they have different functions for each of the data
types that Alpha Vantage offers. This may be less practical when downloading
multiple data types at multiple resolutions in one session. Avapi has a single
function that can download any data type from Alpha Vantage: ``avapi.get_data()``
takes ``**kwargs`` as input and outputs a  dictionary, unless ``datatype="csv"`` is
given, in which case a csv file is saved. If the data type is time series,
``avapi.to_df()`` converts it to a Pandas data frame. The intention is a simple and
flexible way to get data from Alpha Vantage into python.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage/quickstart
   usage/reference

|

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
