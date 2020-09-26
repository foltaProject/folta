from os import listdir
from datetime import datetime
import pandas as pd


def get_logs_data(logs_fin='checkpoints/sigmorphon20-task0/',
                  dev_lang_fin='task0-data/DEVELOPMENT-LANGUAGES/',
                  save=True, print_progress=True):
    '''returns data from the outputted logs file,
    and the development languages.

    Parameters
    ----------
    logs_fin : leave as checkpoints, or <path passed>/mtype/foo.log
    dev_lang_fin : leave as blank, or <path passed>/family/files
    save : save dataframe to csv, default is False
    print_progress : print progress messages, default is False

    Returns
    -------
    pandas dataframe of all completed models for each language and their statistics
    '''

    def get_time(time):
        '''gets time from 'h:m:s'
        '''

        if len(time) > 3:
            # more than one day occured
            days = int(time[1])
            hms = [int(i) for i in time[3].split(':')]
            hms = [hms[0] + (24*days), hms[1], hms[2]]
        else:
            hms = [int(i) for i in time[1].split(':')]

        # convert hms to seconds
        seconds = (hms[0]*60*60) + (hms[1]*60) + (hms[2])

        return seconds

    def get_log_dict(mtype, logfin):
        '''returns dictionary of {language abbreviation, }
        '''

        if 'checkpoints' not in logfin:
            lang_abv = logfin.split('/')[2].split('.')[0]
        else:
            lang_abv = logfin.split('/')[-1].split('.')[0]

        with open(logfin, 'r', errors='ignore') as fin:
            load_line = None  # line for last model being loaded
            last_epoch_line = None  # line for last epoch
            for line in fin:
                if 'load model' in line:
                    load_line = line
                if load_line is None:
                    if 'at epoch' in line and '-1' not in line:
                        last_epoch_line = line
                pass
            fin.close()

        try:
            date_ran = str(line).split('-')[1].split(' ')[1]
            accuracy = float(str(line).split('-')[3].split(' ')[4])
            distance = float(str(line).split('-')[3].split(' ')[6].strip())
            if load_line is not None:
                nll = float(load_line.split('_')[1].split('acc')[0][0:-1])
                epoch_chosen = int(load_line.split('_')[-1].strip())
            if last_epoch_line is not None:
                totepoch = int(last_epoch_line.split(' ')[-1].strip())

            # adjust time based off num days ran
            # passed str object of 'h:m:s' or 'x days, h:m:s'
            time_ran = get_time(str(line).split('-')[2].split(' '))
        except:
            print(f'{lang_abv} is still in progress, cannot get stats.')
            date_ran = None
            accuracy = None
            distance = None
            nll = None
            epoch_chosen = None
            totepoch = None
            time_ran = None
            pass

        return {
            "lang": lang_abv,
            "mtype": mtype,
            "date": date_ran,
            "time_ran(s)": time_ran,
            "tot_epoch": totepoch,
            "mepoch": epoch_chosen,
            "nll": nll,
            "accuracy": accuracy,
            "distance": distance
        }

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

    def check_hall(mtype, file):
        '''checks to make sure only hall modeltypes are
        assigned to hall filetypes
        '''
        if 'hall' in mtype and 'hall' not in file:
            return False
        elif 'hall' not in mtype and 'hall' in file:
            return False
        else:
            return True

    def get_filepaths(logs_fin):
        '''checks if filepath passed is checkpoints or
        usercreated folder of '<path passed>/mtype/foo.log'
        '''

        if logs_fin in 'checkpoints/sigmorphon20-task0/':
            # filepath
            model_types = [folder1
                           for folder1 in listdir(logs_fin)]

            file_paths = [logs_fin + folder1 + '/' + folder2 + '/'
                          for folder1 in listdir(logs_fin)
                          for folder2 in listdir(logs_fin + folder1 + '/')]
        else:
            model_types = [folder1
                           for folder1 in listdir(logs_fin)]

            file_paths = [logs_fin + folder1 + '/'
                          for folder1 in listdir(logs_fin)]

        return model_types, file_paths

    def get_model_df(mtype, model_fin):
        '''pass in modeltype and filepath to folder of logs,
        returns dataframe
        '''

        languages = [file.split('.')[0]
                     for file in listdir(model_fin)
                     if 'log' in file]

        log_stats = [get_log_dict(mtype, model_fin + file)
                     for file in listdir(model_fin)
                     if 'log' in file]

        lang_stats = [get_lang_dict(file, dev_lang_fin + folder + '/')
                      for folder in listdir(dev_lang_fin)
                      for file in listdir(dev_lang_fin + folder)
                      if file[0:3] in languages and check_hall(mtype, file)
                      ]

        log_df = pd.DataFrame(log_stats)
        lang_df = pd.DataFrame(lang_stats)

        dataframe = pd.merge(lang_df, log_df, on='lang')

        return dataframe

    def main(logs_fin, dev_lang_fin, save, print_progress):

        if print_progress is True:
            print('Script is starting, getting modeltypes and filepaths.')

        model_types, file_paths = get_filepaths(logs_fin)

        df_list = [get_model_df(mtype, file_paths[i])
                   for i, mtype in enumerate(model_types)]

        if print_progress is True:
            print('All dataframes successfully created, merging dataframes.')

        dataframe = pd.concat(df_list).sort_values('lang')

        if save is True:
            savefolder = 'scraped_data'

            try:
                mkdir(savefolder)
            except:
                pass

            date = datetime.today().strftime('%Y-%m-%d')
            fp = savefolder + '/' + date + '-completed_log_data.csv'
            dataframe.to_csv(fp, index=False)
            print(f'Dataframe is being saved to {fp}')

        if print_progress is True:
            print('Returning dataframe object.')
            print(dataframe.head(25))
        return dataframe

    main(logs_fin, dev_lang_fin, save, print_progress)


get_logs_data()
