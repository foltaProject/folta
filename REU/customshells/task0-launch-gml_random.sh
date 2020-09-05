run=bash
gpu=1


for lang in gml+25r+eng gml+25r+deu gml+25r+isl gml+25r+nno gml+50r+eng gml+50r+deu gml+50r+isl gml+50r+nno gml+75r+eng gml+75r+deu gml+75r+isl gml+75r+nno gml+100r+eng gml+100r+deu gml+100r+isl gml+100r+nno gml+125r+eng gml+125r+deu gml+125r+isl gml+125r+nno gml+150r+eng gml+150r+deu gml+150r+isl gml+150r+nno gml+175r+eng gml+175r+deu gml+175r+isl gml+175r+nno gml+200r+eng gml+200r+deu gml+200r+isl gml+200r+nno; do
# regular data
echo trm $lang
$run customshells/task0-trm-custom.sh $lang $gpu
echo mono $lang
$run customshells/task0-mono-custom.sh $lang $gpu
done