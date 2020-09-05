run=bash
gpu=1


#for lang in deu_isl_nno; do
for lang in deu_isl_nno_targ; do
# regular data
echo trm $lang
$run customshells/task0-trm-custom.sh $lang $gpu
echo mono $lang
$run customshells/task0-mono-custom.sh $lang $gpu
done
