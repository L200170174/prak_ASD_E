import re

f = open('Indonesia.txt', 'r', encoding = 'latin1')
teks = f.read()
f.close

pola = r'me+\w+'

print(re.findall(pola, teks))
