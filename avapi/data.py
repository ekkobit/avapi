'''Package for getting and manipulating data from Alpha Vantage

Functions: get_data(), save_to_json(), save_to_csv, to_dict(), open_json(),
to_df(), open_json().
'''

__authors__ = "Ole Olaussen"
__email__ = "ole@ekkobit.com"


import requests
import json
import pandas as pd
import os


def get_data(save_to=None, **kwargs):
    '''Downloads a json file from Alpha Vantage.

    :kwarg save_to: String. Default None. Where to save csv file if kwarg
     datatype="csv" is provided.
    :**kwargs: Alpha Vantage function parameters.
    :return: Dictionary. If datatype is not "csv", a dictionary is returned.
    '''

    url = 'https://www.alphavantage.co/query?'
    for key, value in kwargs.items():
        url += key + '=' + value + '&'
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
    '''Converts dictionary of json data file, downloaded from Alpha Vantage,
       to pandas dataframes.

    :param dic: Python dictionary of Alpha Vantage time series data.
    :return: Pandas data frame. Returns the converted json data file as a data
        frame.
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

    :return: Content of response.
    '''

    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)

    with open(dir_path + '/response', 'rb') as file:
        reader = file.read()

    return reader
