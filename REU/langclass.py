from os import mkdir, remove, listdir
from sys import exit


def convert(file_line, test=False):
    '''converts a single file line into a dictionary object of word, lemma, tag'''

    lemma, word, tags = file_line.strip().split('\t')

    return {
        "lemma": lemma,
        "word": word,
        "tags": tags
    }


class File:
    '''class for creating a file, to be passed to the Language class'''

    def __init__(self, dictionary=None, filetype=None, name='corgi40', filepath='task0-data/DEVELOPMENT-LANGUAGES/custom/'):
        '''
        dictionary : a list of dictionary objects structured as [{"word", "lemma", "tags"}]

        filetype : needs to be "trn", "dev", "tst", or "hall"

        name : a string for only the name structured as "deu_gml", do not use "."!

        filepath : automatically set to "task0-data/DEVELOPMENT-LANGUAGES/custom/"
    '''
        self.dictionary = dictionary
        self.filepath = filepath

        if '.' not in name:
            self.name = name
        else:
            print('do not use "." in the filename')
            exit()

        if filetype in ['trn', 'dev', 'tst', 'hall']:
            self.filetype = filetype
        elif filetype is None:
            self.filetype = None
        else:
            print('filetype is not "trn", "dev", "tst", or "hall"')
            exit()

        if dictionary is not None:
            self.nwords = len(dictionary)
        else:
            self.nwords = 0

    def __str__(self):
        return f'filepath is: {self.filepath}{self.name}.{self.filetype}\nnumber of words: {self.nwords}'

    def create(self):
        '''saves formatted testing data'''

        fp = f'{self.filepath}{self.name}.{self.filetype}'

        try:
            # creates custom filepath
            mkdir(self.filepath)
        except:
            pass

        try:
            # removes old language files, to append lines in file
            remove(fp)
        except:
            pass

        with open(fp, 'a') as fout:
            for line in self.dictionary:
                fout.write(f'{line["lemma"]}\t{line["word"]}\t{line["tags"]}')
                fout.write('\n')

    def get_language(self, language):
        '''loads object with information on passed in development data for language'''

        if self.filetype == 'tst':
            # test data is taken from gold standard
            lang_fp = 'task0-data/GOLD-TEST'
            full_filepath = [f'{lang_fp}/{file}'
                             for file in listdir(f'{lang_fp}')
                             if language in file and self.filetype in file][0]

        else:
            lang_fp = 'task0-data/DEVELOPMENT-LANGUAGES'
            full_filepath = [f'{lang_fp}/{folder}/{file}'
                             for folder in listdir(lang_fp)
                             if 'custom' not in folder
                             for file in listdir(f'{lang_fp}/{folder}')
                             if language in file and self.filetype in file][0]

        self.name = full_filepath.split('/')[-1].split('.')[0]

        self.dictionary = [convert(line)
                           for line in open(full_filepath)]

        self.nwords = len(self.dictionary)

        return self


class Language:
    '''
    class creates a language from the Train, Test, Development classes, which must be used.

    Hallucination : default None, can pass in this class if created
    '''

    def __init__(self, Train, Test, Development, Hallucination=None):

        if Train.filetype == 'trn':
            self.trn = Train
        else:
            print('train filetype is not "trn"')
            exit()

        if Development.filetype == 'dev':
            self.dev = Development
        else:
            print('train filetype is not "trn"')
            exit()

        if Test.filetype == 'tst':
            self.tst = Test
        else:
            print('train filetype is not "trn"')
            exit()

        if Hallucination is not None:
            if Hallucination.filetype == 'hall':
                self.hall = Hallucination
            else:
                print('train filetype is not "trn"')
                exit()
        else:
            self.hall = None

    def __str__(self):

        sep = '\n--------------\n'

        string = f'{sep}{self.trn}{sep}{self.tst}{sep}{self.dev}{sep}'

        if self.hall is not None:
            string = f'{string}{self.hall}{sep}'

        return string

    def create(self):

        self.trn.create()
        self.tst.create()
        self.dev.create()

        if self.hall is not None:
            self.hall.create()

        print(f'files were saved to {self.trn.filepath}')

    def change_name(self, name):
        '''changes a language name for all files'''
        self.trn.name = name
        self.tst.name = name
        self.dev.name = name

        if self.hall is not None:
            self.hall.name = name
