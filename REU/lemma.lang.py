from langclass import *
import random as r
import math as m
import sys

##################
# hyper-parameters
languages = 'nno'.split(' ')
source = 'nno'
proportion = 1


def add_lemmawords(source, pull, nwords):
    '''returns a dictionary of mixed languages, this can get repeated words'''

    possible_dict = [dictionary
                     for dictionary in pull.dictionary
                     if dictionary['lemma'] in dictionary['word']]

    if len(possible_dict) > nwords:
        # currently this can get repeated words
        add_dict = [possible_dict[r.randint(0, len(possible_dict)-1)]
                    for i in range(nwords)]
    else:
        add_dict = possible_dict

    new_dictionary = source.dictionary + add_dict
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
    new_trn_dict, nadded = add_lemmawords(trn_source, trn_lang, add_nwords)

    print('training nwords:', trn_source.nwords,
          '| proportion asked:', proportion, '| words to add:', add_nwords)
    print('actual nwords added:', nadded,
          '| proportion of training:', nadded/trn_source.nwords)

    if nadded != add_nwords:
        proportion = nadded/trn_source.nwords

    # create training langauge from new dictionary
    trn_lang = File(new_trn_dict, 'trn')
    # create new name
    name = f'{source}+{int(proportion*100)}p+{lang}'

    # create language object and change name
    new_lang = Language(trn_lang, tst_source, dev_source)
    new_lang.change_name(name)
    # push language object into files
    print(new_lang)
    new_lang.create()
