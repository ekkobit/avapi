'''Package for getting and manipulating data from Alpha Vantage

Functions: get_data(), save_to_json(), save_to_csv, to_dict(), open_json(), to_df(), open_json().
'''


__authors__ = "Ole Olaussen"
__email__ = "olemolaussen@gmail.com"


import requests
import json
import pandas as pd
import os


def get_data(url, output='df', save_csv=False, save_json=False, csv_path=None, json_path=None):
    '''Downloads a json file from Alpha Vantage.

    :param url: String. API-call to Alpha Vantage server (url).
    :kwarg output: String. Excepts "dictionary", "json" and 'df'. Default df, for Pandas data frame.
    :kwarg save_csv: Boolean. Default False. Save data as a csv file.
    :kwarg save_json: Boolean. Default False. Save data as a json file.
    :kwarg csv_path: String. Path, incl. filename of where to save csv.
    :kwarg json_path: String. Path, incl. filename of where to save json.
    :return: If output is not None. Returns python dictionary or json content.
    '''
    r = requests.get(url)
    json_content = r.content

    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)

    with open(dir_path + '/response.json', 'wb') as file:
        file.write(json_content)

    if save_to_csv or save_to_json:

        if save_csv:
            if csv_path is not None:
                save_to_csv(json_content, csv_path)
            else:
                print('Reqires csv_path keyword argument.')

        if save_json:
            if json_path is not None:
                save_to_json(json_content, json_path)
            else:
                print('Reqires json_path keyword argument.')

    if output is not None:

        if output == 'df':
            dict = to_dict(json_content)
            df = to_df(dict)
            return df

        if output == 'dictionary':
            dict = to_dict(json_content)
            return dict

        if output == 'json':
            return json_content


def save_to_json(json_content, path):
    ''' Saves json file to directory.

    :param path: String. Path to where file should be saved. Including file name.
    '''

    with open(path, 'wb') as f:
        f.write(json_content)

def save_to_csv(json_content, csv_path):
    '''Saves json content to csv file.

    :param json_content: Contents of json file.
    '''
    dict = to_dict(json_content)
    df = to_df(dict)
    df.to_csv(csv_path)


def to_dict(json_content):
    '''Builds a python dictionary from json file content.

    :param json_content: Contents of json file.
    :return: Dictionary.
    '''

    dict = json.loads(json_content)

    return dict


def open_json(file):
    '''Opens a json data file and reads it to a python dictionary.

    :param file: String. Path to json file.
    :return: Dictionary.
    '''

    with open(file, 'r') as file:
        reader = file.read()

    dict = to_dict(reader)

    return dict


def to_df(dict):
    '''Converts dictionary of json data file, downloaded from Alpha Vantage, to pandas dataframes.

    :param file: String. path to json file
    :return: Pandas data frame. Returns the converted json data file as a data frame.
    '''

    outer = [key for key, value in dict.items()] # Get outer dictionaries

    dates = [key for key, value in dict[outer[1]].items()] # Get timestamps

    columns = [key for key, value in dict[outer[1]][dates[0]].items()] # Get columns

    data = {'date': dates}

    # Populate dictionary with column names (keys) and empty lists (values)
    for column in columns:
        data[column] = []

    # Fill lists with corresponding data
    for date in dates:
        for column in columns:
            data[column].append(dict[outer[1]][date][column])

    df = pd.DataFrame(data) # Convert dict to pandas data frame
    df.set_index('date', inplace=True)

    return df

def response():
    '''Opens and reads last response from Alpha Vantage server.

    :return: Content of response.
    '''

    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)

    with open(dir_path + '/response.json', 'r') as file:
        reader = file.read()
    return reader
