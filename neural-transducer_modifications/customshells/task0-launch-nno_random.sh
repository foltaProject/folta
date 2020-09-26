run=bash
gpu=1

# nno+25r+eng nno+25r+deu nno+25r+isl nno+25r+nno nno+50r+eng nno+50r+deu nno+50r+isl nno+50r+nno nno+75r+eng nno+75r+deu 
for lang in nno+75r+isl nno+75r+nno nno+100r+eng nno+100r+deu nno+100r+isl nno+100r+nno nno+125r+eng nno+125r+deu nno+125r+isl nno+150r+eng nno+150r+deu nno+150r+isl nno+175r+eng nno+175r+deu nno+175r+isl nno+200r+eng nno+200r+deu nno+200r+isl; do
# regular data
echo trm $lang
$run customshells/task0-trm-custom.sh $lang $gpu
echo mono $lang
$run customshells/task0-mono-custom.sh $lang $gpu
done