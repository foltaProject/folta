# change hyp file to be 'lemma predictedword, tag'

from os import listdir, mkdir
from datetime import datetime
import pandas as pd


def create_hyp_tsvcsv(languages=['gml', 'nno', 'deu', 'eng', 'isl'], devfilepath='task0-data/DEVELOPMENT-LANGUAGES/', tsvfilepath='checkpoints/sigmorphon20-task0/', tsvfout=None, scrapetsv=True, createhyp=True, testtype='dev'):
    '''
    takes languages to search for, 
    filepaths to 'devfilepath/<family>/<lang>.dev' and 'tsvfilepath/<model>/<drop>/<lang>.decode.dev.tsv', 
    then creates hypothesis files for evaluation script, and creates csv file with all relevant information
    '''

    def align_filepaths(languages, devfilepath, tsvfilepath, testtype):
        '''
        takes all languages, initial development data path, and inition model output path,
        then returns the full tsv and development filepath lists
        '''

        if testtype == 'tst':
            tsv_type = 'test'
        elif testtype == 'dev':
            tsv_type = 'dev'
        else:
            print(
                'Filetypes could not be found, please try adjusting the testtype parameter.')
            return None, None

        try:
            tsvfilelist = [f'{tsvfilepath}{folder1}/{folder2}/{file}'
                           for language in languages
                           for folder1 in listdir(tsvfilepath)
                           for folder2 in listdir(f'{tsvfilepath}{folder1}/')
                           for file in listdir(f'{tsvfilepath}{folder1}/{folder2}/')
                           if language in file and 'tsv' in file and tsv_type in file]

            devfilelist = [f'{devfilepath}{folder1}/{file}'
                           for language in languages
                           for folder1 in listdir(devfilepath)
                           for file in listdir(f'{devfilepath}{folder1}/')
                           if language in file and testtype in file]

            return tsvfilelist, devfilelist

        except:
            print('filepaths are not correct')

    def get_dict(tsvline, devline, family, language, model):
        '''
        takes the tsv and dev line and returns a dictionsary object of data
        '''
        # scrape data from lines
        predicted, true, loss, distance = tsvline.split('\t')
        lemma, trueword, tag = devline.split('\t')

        if true == predicted:
            truevalue = 1
        else:
            truevalue = 0

        return {
            "family": family, "language": language, "model": model, "prediction": predicted.replace(" ", ""), "truth": trueword, "lemma": lemma, "tag": tag, "loss": loss, "distance": distance, "is_correct": truevalue
        }

    def dict_and_hyp(dev, tsv, wdir, createhyp):
        '''
        takes full development and tsv data paths to create a
        list of dictionary objects to return, and writes a hypothesis file
        '''

        devlines = [line
                    for line in open(dev)]

        tsvlines = [line
                    for i, line in enumerate(open(tsv))
                    if i > 0]

        if len(devlines) == len(tsvlines):
            tot_words = len(devlines)
        else:
            print(f'files are not the same length:\n{dev}\n{tsv}')
            return None

        family = dev.split('/')[2]
        language = dev.split('/')[-1].split('.')[0]
        model = tsv.split('/')[2]

        if createhyp:
            try:
                mkdir(f'{wdir}{model}/')
            except:
                pass

            hypfp = f'{wdir}{model}/{language}.hyp'

            with open(hypfp, 'w') as hypfout:
                for i in range(tot_words):
                    # hyp file needs lemma, PREDICTEDword, tag
                    lemma, word, tag = devlines[i].split('\t')
                    # does this need guessed word or true word????
                    hypfout.write(f'{lemma}\t{word}\t{tag}')
                hypfout.close()
                print(f'finished writing {hypfp}')

        # dict needs pred, true, stem, pos, loss, dist
        dictlist = [get_dict(tsvlines[i], devlines[i], family, language, model)
                    for i in range(tot_words)]

        return dictlist

    def main(languages, devfilepath, tsvfilepath, tsvfout, scrapetsv, createhyp, testtype):

        # get all filepaths for tsv and dev files
        tsvlist, devlist = align_filepaths(
            languages, devfilepath, tsvfilepath, testtype)

        # set up working directory for saving hyp files
        date = datetime.today().strftime('%Y-%m-%d')
        wdir = f'{date}_hypfiles/'

        csvsavefolder = 'scraped_data'

        if tsvfout is None:
            tsvfout = f'{csvsavefolder}/{date}-tsv.predictions.csv'
        else:
            tsvfout = f'{csvsavefolder}/{tsvfout}'

        try:
            mkdir(wdir)
        except:
            pass

        try:
            mkdir(csvsavefolder)
        except:
            pass

        # writes hyp files and returns list of dictions
        dictlists = [dict_and_hyp(devfile, tsvfile, wdir, createhyp)
                     for lang in languages
                     for devfile in devlist
                     if lang in devfile
                     for tsvfile in tsvlist
                     if lang in tsvfile]

        if scrapetsv:

            dflist = [pd.DataFrame(filedict)
                      for filedict in dictlists]

            dataframe = pd.concat(dflist)

            dataframe.to_csv(tsvfout, index=False)
            print(f'Dataframe is being saved to {tsvfout}')

    main(languages, devfilepath, tsvfilepath,
         tsvfout, scrapetsv, createhyp, testtype)


# create_hyp_tsvcsv()
