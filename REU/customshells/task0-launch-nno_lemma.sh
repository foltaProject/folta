run=bash
gpu=0


for lang in nno+25p+eng nno+25p+deu nno+25p+isl nno+12p+nno nno+50p+eng nno+50p+deu nno+50p+isl nno+75p+eng nno+75p+deu nno+75p+isl nno+100p+eng nno+100p+deu nno+84p+isl nno+125p+eng nno+125p+deu nno+150p+eng nno+150p+deu nno+161p+eng nno+161p+deu; do
# regular data
echo trm $lang
$run customshells/task0-trm-custom.sh $lang $gpu
echo mono $lang
$run customshells/task0-mono-custom.sh $lang $gpu
done