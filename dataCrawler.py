from bs4 import BeautifulSoup

html_file = open('biCorpusDataset.xml','r',encoding='utf-8') 
html_code = html_file.read()
soup  = BeautifulSoup(html_code,'html')

for num,i in enumerate(soup.find_all('pa')):
    print('Line No.'+str(num)+' '+i.text)