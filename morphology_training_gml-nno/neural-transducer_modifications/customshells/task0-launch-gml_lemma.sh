run=bash
gpu=1


for lang in gml+25p+eng gml+25p+deu gml+25p+nno gml+25p+isl gml+50p+eng gml+50p+deu gml+50p+nno gml+50p+isl gml+75p+eng gml+75p+deu gml+75p+nno gml+75p+isl gml+100p+eng gml+100p+deu gml+100p+nno gml+100p+isl gml+125p+eng gml+125p+deu gml+125p+isl gml+125p+nno gml+150p+eng gml+150p+deu gml+150p+isl gml+142p+nno gml+175p+eng gml+175p+deu gml+175p+isl gml+200p+eng gml+200p+deu gml+200p+isl; do
# regular data
echo trm $lang
$run customshells/task0-trm-custom.sh $lang $gpu
echo mono $lang
$run customshells/task0-mono-custom.sh $lang $gpu
done