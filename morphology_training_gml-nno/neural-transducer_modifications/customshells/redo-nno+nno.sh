run=bash
gpu=0


for lang in nno+25p+nno nno+50p+nno nno+75p+nno nno+82p+nno; do
# regular data
echo trm $lang
$run customshells/task0-trm-custom.sh $lang $gpu
echo mono $lang
$run customshells/task0-mono-custom.sh $lang $gpu
done