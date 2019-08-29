'''The data module contains fuctions to get data from Alpha Vantage into
python. Data may be saved as csv files or loaded as Pandas data frames.
'''

__authors__ = "Ole Olaussen, Xuan Ling"
__email__ = "ole.olaussen@ekkobit.com, xuan.ling@ekkobit.com"


import requests
import json
import pandas as pd
import os


def get_data(save_to=None, **kwargs):
    r'''Downloads a json file from Alpha Vantage.

    :param save_to: Default None. Where to save csv file if
        ``datatype="csv"`` is provided.
    :type save_to: ``str`` or ``None``
    :param \**kwargs:
        See below

    :Keyword Arguments:
        * *function* (``str``) --
            Any of the Alpha Vantage function types. \
            Such as ``"TIME_SERIES_INTRADAY"``. \
            See their `documentation \
            <https://www.alphavantage.co/documentation/>`_
        * *symbol* (``str``) --
            Company ticker symbol, such as ``"GOOGL"``.
        * *interval* (``str``) --
            ``"1min"``, ``"5min"``, ``"15min"``, ``"30min"`` or ``"60min"``. \
            Also ``"daily"``, ``"weekly"``, ``"monthly"``
        * *outputsize* (``str``) --
            ``"compact"`` (default) or ``"full"``
        * *datatype* (``str``) --
            ``"json"`` (default) or ``"csv"``
        * *apikey* (``str``) --
            You need to get a free API key from `Alpha Vantage \
            <https://www.alphavantage.co/>`_

    The above list is not exhaustive. Please see  `Alpha Vantage docs
    <https://www.alphavantage.co/documentation/>`_ for
    complete listing and what fuction requires which keyword arguments.

    :returns: If datatype is not set to ``"csv"``, a dictionary is returned
    :rtype: ``dict`` [``str``, ``float``]
    '''

    url = 'https://www.alphavantage.co/query?'
    for key, value in kwargs.items():
        url += key + '=' + str(value) + '&'
    url = url[:-1]

    csv = 'datatype' in kwargs and kwargs['datatype'] == 'csv'

    if csv:
        url += '&datatype=csv'

    r = requests.get(url)
    content = r.content

    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)

    with open(dir_path + '/response', 'wb') as file:
        file.write(content)

    if csv:
        if save_to is None:
            print("Missing keyword argument save_to='...'")
        else:
            with open(save_to, 'wb') as file:
                file.write(content)
    else:
        dic = json.loads(content)
        return dic


def to_df(dic):
    '''Converts data dictionary, downloaded from Alpha Vantage, to pandas
    dataframes.

    :param dic: Python dictionary of Alpha Vantage time series data
    :type dic: ``dict`` [``str``, ``float``]
    :returns: Returns the converted dictionary as a Pandas data frame
    :rtype: ``pandas.DataFrame()``
    '''

    # Get outer dictionaries
    outer = [key for key, value in dic.items()]

    # Get timestamps
    dates = [key for key, value in dic[outer[1]].items()]

    # Get columns
    columns = [key for key, value in dic[outer[1]][dates[0]].items()]

    data = {'date': dates}

    # Populate dictionary with column names (keys) and empty lists (values)
    for column in columns:
        data[column] = []

    # Fill lists with corresponding data
    for date in dates:
        for column in columns:
            data[column].append(dic[outer[1]][date][column])

    df = pd.DataFrame(data)  # Convert dict to pandas data frame
    df.set_index('date', inplace=True)

    return df


def response():
    '''Opens and reads last response from Alpha Vantage server.

    :returns: Content of response.
    :rtype: ``str``
    '''

    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)

    with open(dir_path + '/response', 'rb') as file:
        reader = file.read()

    return reader
