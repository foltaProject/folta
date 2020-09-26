# from scrape_logs import *

# scrape data for chosen languages only
# no model data
# use functions from scrape_logs
from os import listdir
import pandas as pd


def get_lang_df(languages=['gml', 'nno', 'deu', 'eng', 'isl'], lang_fin='task0-data/DEVELOPMENT-LANGUAGES/'):
    '''
    used to scrape the data for a passed in list of languages.
    '''

    def get_lang_dict(file, path):
        '''returns dictionary of {language, filetype, number of lines in file}
        '''
        family = path.split('/')[2]
        lang_abv = file.split('.')[0]
        ftype = file.split('.')[1]
        length = sum(1 for line in open(path + file, errors='ignore'))

        return {
            "family": family,
            "lang": lang_abv,
            "ftype": ftype,
            "nwords": length
        }

    def main(languages, lang_fin):

        lang_stats = [get_lang_dict(file, lang_fin + folder + '/')
                      for folder in listdir(lang_fin)
                      for file in listdir(lang_fin + folder)
                      if file[0:3] in languages
                      ]

        dataframe = pd.DataFrame(lang_stats)

        savefolder = 'scraped_data'

        try:
            mkdir(savefolder)
        except:
            pass

        fp = savefolder + '/' + '.'.join(languages) + '.csv'
        dataframe.to_csv(fp, index=False)
        print(f'Dataframe is being saved to {fp}')

    main(languages, lang_fin)


get_lang_df()
