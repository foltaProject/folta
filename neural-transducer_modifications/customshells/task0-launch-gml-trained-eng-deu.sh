run=bash
gpu=0


#for lang in eng_deu_gml; do
for lang in eng_deu_gml_targ; do
# regular data
echo trm $lang
$run customshells/task0-trm-custom.sh $lang $gpu
echo mono $lang
$run customshells/task0-mono-custom.sh $lang $gpu
done
