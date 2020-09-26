def merge_files(lang1, lang2, lang3, lang4, lang5):
    '''
    Merges training data for all five languages and dev/test data from low resource languages
    '''

    #open .dev files for languages 4 and 5 and read into list
    d1 = open('task0-data/DEVELOPMENT-LANGUAGES/germanic/' + lang4 + ".dev")
    d2 = open('task0-data/DEVELOPMENT-LANGUAGES/germanic/' + lang5 + ".dev")
    dev1 = [line for line in d1]
    dev2 = [line for line in d2]
    d1.close()
    d2.close()
    
    #create output .dev file, named all_langs.dev, and write contents of lists in
    #also create .txt file with note of where the data splits
    output_dev = open('task0-data/DEVELOPMENT-LANGUAGES/custom/' + "all_langs.dev", "w")
    counter = 0
    for ln in dev1:
        output_dev.write(ln)
        counter += 0
    for ln in dev2:
        output_dev.write(ln)
    output_dev.close()
    
    text = open('task0-data/DEVELOPMENT-LANGUAGES/custom/' + "all_langs_breaks.txt", "w")
    text.write("Break point for dev files: " + str(counter) + "\n")
    
    #read .trn files for langs 1 through 3 into lists and write contents into new .trn file
    tr1 = open('task0-data/DEVELOPMENT-LANGUAGES/germanic/' + lang1 + ".trn")
    tr2 = open('task0-data/DEVELOPMENT-LANGUAGES/germanic/' + lang2 + ".trn")
    tr3 = open('task0-data/DEVELOPMENT-LANGUAGES/germanic/' + lang3 + ".trn")
    trn1 = [line for line in tr1]
    trn2 = [line for line in tr2]
    trn3 = [line for line in tr3]
    tr1.close()
    tr2.close()
    tr3.close()
    
    output_trn = open('task0-data/DEVELOPMENT-LANGUAGES/custom/' + "all_langs.trn", "w")
    for ln in trn1:
        output_trn.write(ln)
    for ln in trn2:
        output_trn.write(ln)
    for ln in trn3:
        output_trn.write(ln)
    output_trn.close()
    
    #combine .tst files for languages 4 and 5, and add to note of where the data splits
    ts1 = open('task0-data/GOLD-TEST/' + lang4 + ".tst")
    ts2 = open('task0-data/GOLD-TEST/' + lang5 + ".tst")
    tst1 = [line for line in ts1]
    tst2 = [line for line in ts2]
    output_tst = open('task0-data/DEVELOPMENT-LANGUAGES/custom/' + "all_langs.tst", "w")
    
    counter = 0
    for ln in tst1:
        output_tst.write(ln)
        counter += 1
    for ln in tst2:
        output_tst.write(ln)
    output_tst.close()
    
    text.write("Break point for test files: " + str(counter) + "\n")
    text.close()
    

#train on English and German, test on Middle Low German
merge_files("eng", "deu", "isl", "nno", "gml")
