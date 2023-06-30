import requests
from bs4 import BeautifulSoup

snp_ids = []
chr = []
posi = []
sign = []
final_posi = []
positions = []

html_txt = requests.get('https://www.ncbi.nlm.nih.gov/snp').text

soup = BeautifulSoup(html_txt, 'lxml')

rprt = soup.find_all('div', class_='rprt')

for every_rprt in rprt:
    supp = every_rprt.find('div', class_='supp')
    ids = supp.find('a') 
    snp_ids.append(ids.text)

for every_rprt in rprt:
    snpsum_dl_left_align = supp.find('dl', class_='snpsum_dl_left_align')
    alles = snpsum_dl_left_align.find('span')
    big_poss = snpsum_dl_left_align.find_all('dd')
    pos = big_poss[2].text.split('(')
    sig = big_poss[6].text
    posi.append(pos)
    sign.append(sig)

for every_pos in posi:
    final_posi.append(every_pos[0])

print(snp_ids)
print(final_posi)
print(sign)

