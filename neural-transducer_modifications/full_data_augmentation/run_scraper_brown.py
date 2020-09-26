from datacollection.scrape_hyp_tsv2csv import *


#################
# scraping tsv files from model output

ran_languages = 'all_langs_targ deu_isl_nno_targ eng_deu_gml_targ'
modeloutput_fp = 'modeloutput/customdata/'

# pass in list of langugae names to scrape, model output file path
# filename for csv (if you dont want the basic name), and false for creating hypothesis files
create_hyp_tsvcsv(languages=ran_languages.split(' '),
                  tsvfilepath=modeloutput_fp, tsvfout='mixed_data.predictions.csv', createhyp=False)
