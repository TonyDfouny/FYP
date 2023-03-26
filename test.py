import re

pa='(ROOT (S (NP (PRP نحن)) (VP (VBD اكلنا) (NP (NNP اسد)))))'
liste=re.split(r"[()]",pa)
print(liste)
output=[]
for i in liste:
    if len(re.findall(r'\w+', i))==2:
        output.append(i)
        print (i[0])

print(output)