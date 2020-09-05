from langclass import *
import random as r
import math as m
import sys

##################
# hyper-parameters
languages = 'eng deu isl nno'.split(' ')  # languages to add to the source
source = 'gml'  # language to base dataset off of
proportion = 2  # proportion of source to be added


def add_randwords(source, pull, nwords):
    '''returns a dictionary of mixed languages, all of the source + nwords of pull, this can get repeated words'''

    if len(pull.dictionary) > nwords:
        # currently this can get repeated words
        add_dict = [pull.dictionary[r.randint(0, len(pull.dictionary)-1)]
                    for i in range(nwords)]
    else:
        # does not get repeat words, but limits number of words added
        add_dict = pull.dictionary

    new_dictionary = source.dictionary + add_dict
    # randomly shuffle dictionary to avoid stacking languages
    r.shuffle(new_dictionary)

    return new_dictionary, len(add_dict)


# get norwegian nynorsk data files
trn_source = File(filetype='trn').get_language(source)
dev_source = File(filetype='dev').get_language(source)
tst_source = File(filetype='tst').get_language(source)

# first lets try adding 25 proportion (of the source language) more data from another language
add_nwords = m.ceil(trn_source.nwords * proportion)

for lang in languages:
    # get full addition languages to merge into training source language
    trn_lang = File(filetype='trn').get_language(lang)
    # merge languages with 10 proportion of nno language
    new_trn_dict, nadded = add_randwords(trn_source, trn_lang, add_nwords)

    print('training nwords:', trn_source.nwords,
          '| proportion asked:', proportion, '| words to add:', add_nwords)
    print('actual nwords added:', nadded,
          '| proportion of training:', nadded/trn_source.nwords)

    if nadded != add_nwords:
        proportion = nadded/trn_source.nwords

    # create training langauge from new dictionary
    trn_lang = File(new_trn_dict, 'trn')
    # create new name
    name = f'{source}+{int(proportion*100)}r+{lang}'

    # create language object and change name
    new_lang = Language(trn_lang, tst_source, dev_source)
    new_lang.change_name(name)
    # push language object into files
    print(new_lang)
    new_lang.create()
