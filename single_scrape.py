import requests
from bs4 import BeautifulSoup

html_txt = requests.get('https://www.ncbi.nlm.nih.gov/snp/?term=htt').text

soup = BeautifulSoup(html_txt, 'lxml')

rprt = soup.find('div', class_='rprt')

supp = rprt.find('div', class_='supp')

ids = supp.find('a') 

snpsum_dl_left_align = supp.find('dl', class_='snpsum_dl_left_align')

alles = snpsum_dl_left_align.find('span')

big_poss = snpsum_dl_left_align.find_all('dd')


for id in ids:
    print(id.text)

for alle in alles:
    print(alle.text)

pos = big_poss[2].text.split('(')
sig = big_poss[6].text
print(pos[0])
print(sig)