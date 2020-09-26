def merge_files(lang1, lang2, lang3):
    '''
    Takes three language names as strings
    Outputs trn files for merging the first two, and uses the third file for the tst and dev data
    '''

    #open .dev files for language 3 and read into list
    d = open('task0-data/DEVELOPMENT-LANGUAGES/germanic/' + lang3 + ".dev")
    dev = [line for line in d]
    d.close()
    
    #create output .dev file, named lang1_lang2_lang3.dev, and write contents of list in
    output_dev = open('task0-data/DEVELOPMENT-LANGUAGES/custom/' + lang1 + "_" + lang2 + "_" + lang3 +  ".dev", "w")
    for ln in dev:
        output_dev.write(ln)
    output_dev.close()
    
    #read .trn files for langs 1 and 2 into lists and write contents into new .trn file
    tr1 = open('task0-data/DEVELOPMENT-LANGUAGES/germanic/' + lang1 + ".trn")
    tr2 = open('task0-data/DEVELOPMENT-LANGUAGES/germanic/' + lang2 + ".trn")
    trn1 = [line for line in tr1]
    trn2 = [line for line in tr2]
    tr1.close()
    tr2.close()
    
    output_trn = open('task0-data/DEVELOPMENT-LANGUAGES/custom/' + lang1 + "_" + lang2 + "_" + lang3 + ".trn", "w")
    for ln in trn1:
        output_trn.write(ln)
    for ln in trn2:
        output_trn.write(ln)
    output_trn.close()
    
    #open .tst file for language 3 and copy it into a new file, renaming it to match .dev and .trn files
    ts = open('task0-data/GOLD-TEST/' + lang3 + ".tst")
    tst = [line for line in ts]
    output_tst = open('task0-data/DEVELOPMENT-LANGUAGES/custom/' + lang1 + "_" + lang2 + "_" + lang3 + ".tst", "w")
    for ln in tst:
        output_tst.write(ln)
    output_tst.close()
    
    #return output_dev, output_trn, output_tst

#train on English and German, test on Middle Low German
merge_files("eng", "deu", "gml")
#train on German and Icelandic, test on Norwegian Nynorsk
merge_files("deu", "isl", "nno")
