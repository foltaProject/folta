run=bash
gpu=1


for lang in gml+175p+deu gml+175p+isl gml+200p+eng gml+200p+deu gml+200p+isl nno+125p+eng nno+125p+deu nno+150p+eng nno+150p+deu nno+161p+eng nno+161p+deu; do
# regular data
echo trm $lang
$run customshells/task0-trm-custom.sh $lang $gpu
echo mono $lang
$run customshells/task0-mono-custom.sh $lang $gpu
done