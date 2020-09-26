from datacollection.scrape_hyp_tsv2csv import *


#################
# scraping tsv files from model output

ran_languages = 'nno+25p+eng nno+25p+deu nno+25p+isl nno+25p+nno nno+50p+eng nno+50p+deu nno+50p+isl nno+50p+nno nno+75p+eng nno+75p+deu nno+75p+isl nno+75p+nno nno+100p+eng nno+100p+deu nno+84p+isl nno+125p+eng nno+125p+deu nno+150p+eng nno+150p+deu nno+161p+eng nno+161p+deu gml+25p+eng gml+25p+deu gml+25p+nno gml+25p+isl gml+50p+eng gml+50p+deu gml+50p+nno gml+50p+isl gml+75p+eng gml+75p+deu gml+75p+nno gml+75p+isl gml+100p+eng gml+100p+deu gml+100p+nno gml+100p+isl nno+82p+nno gml+125p+eng gml+125p+deu gml+125p+isl gml+125p+nno gml+150p+eng gml+150p+deu gml+150p+isl gml+142p+nno gml+175p+eng gml+175p+deu gml+175p+isl gml+200p+eng gml+200p+deu gml+200p+isl'
modeloutput_fp = 'modeloutput/customdata/'

# pass in list of langugae names to scrape, model output file path
# filename for csv (if you dont want the basic name), and false for creating hypothesis files
create_hyp_tsvcsv(languages=ran_languages.split(' '),
                  tsvfilepath=modeloutput_fp, tsvfout='8-13-20.lemma.tst.predictions.csv', createhyp=False, testtype='tst')


# repeat but for random method augmentations
ran_languages = 'nno+25r+eng nno+25r+deu nno+25r+isl nno+25r+nno nno+50r+eng nno+50r+deu nno+50r+isl nno+50r+nno nno+75r+eng nno+75r+deu nno+75r+isl nno+75r+nno nno+100r+eng nno+100r+deu nno+100r+isl nno+100r+nno nno+125r+eng nno+125r+deu nno+125r+isl nno+150r+eng nno+150r+deu nno+150r+isl nno+175r+eng nno+175r+deu nno+175r+isl nno+200r+eng nno+200r+deu nno+200r+isl gml+25r+eng gml+25r+deu gml+25r+isl gml+25r+nno gml+50r+eng gml+50r+deu gml+50r+isl gml+50r+nno gml+75r+eng gml+75r+deu gml+75r+isl gml+75r+nno gml+100r+eng gml+100r+deu gml+100r+isl gml+100r+nno gml+125r+eng gml+125r+deu gml+125r+isl gml+125r+nno gml+150r+eng gml+150r+deu gml+150r+isl gml+150r+nno gml+175r+eng gml+175r+deu gml+175r+isl gml+175r+nno gml+200r+eng gml+200r+deu gml+200r+isl gml+200r+nno'

create_hyp_tsvcsv(languages=ran_languages.split(' '),
                  tsvfilepath=modeloutput_fp, tsvfout='8-13-20.random.tst.predictions.csv', createhyp=False, testtype='tst')
