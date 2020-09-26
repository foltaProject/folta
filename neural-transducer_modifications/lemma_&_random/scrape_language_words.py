import pandas as pd
from os import mkdir
from langclass import *


folder = 'scraped_data/'
filename = 'languages.filedata.csv'

languages = 'nno gml eng deu isl'.split(' ')
filetypes = 'trn dev tst hall'.split(' ')


def get_dataframe(filetype, language):
    '''returns a dataframe object from using the langclass to pull data'''

    words = pd.DataFrame(
        File(filetype=filetype).get_language(language).dictionary)

    words['language'] = language
    words['filetype'] = filetype

    return words


# get list of dataframes and concat together
dataframe = pd.concat([get_dataframe(filetype, language)
                       for language in languages
                       for filetype in filetypes])

try:
    mkdir(folder)
except:
    pass

filepath = f'{folder}{filename}'

dataframe.to_csv(filepath, index=False)

print(f'languages scraped and sent to {filepath}\n')

print(dataframe)
