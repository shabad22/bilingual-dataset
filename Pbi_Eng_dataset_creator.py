punjabi_data_file = open('Pbi.txt','r',encoding='utf-8')
punjabi_data = punjabi_data_file.readlines()
punjabi_data_file.close()

english_data_file = open('Eng.txt','r',encoding='utf-8')
english_data = english_data_file.readlines()
english_data_file.close()

html_head_code = r'''
<?xml version="1.0" ?>
<Doc id="bilingual_dataset bi01" lang="bi-lingual">
<Header type='text'>
    <encodingDesc>
        <projectDesc>Bi-lingual Corpora</projectDesc>
        <samplingDesc>This Document contain Only 10 sentences of bilingual data</samplingDesc>
    </encodingDesc>
    <sourceDesc>
        <source>Wikipeida</source>
        <source>Gyan  Nidhi</source>
        <source>TDIL</source>
    </sourceDesc>
    <creation>
        <date>27-May-2020</date>
        <inputter>Manpreet Singh Lehal</inputter>
        <proof></proof>
    </creation>
    <langUsage>Punjabi, English</langUsage>
    <wsdUsage>
        <writingSystem id="ISO/IEC 10646">Universal Multiple-Octet Coded Character Set(UCS).</writingSystem>
    </wsdUsage>
    <textClass>
        <channel mode="w">print</channel>
        <domain type="public"></domain>
    </textClass>
</Header>
<text><body>
'''
html_foot_code = r'''</body></text></html></Doc>'''

with open('biCorpusDataset_50k.xml','w',encoding='utf-8') as dataset_file:
    dataset_file.write(html_head_code+'\n')
    for i in range(50000):
        dataset_file.write('<pa>'+punjabi_data[i].replace('\n','')+'</pa></br>\n'+'<en>'+english_data[i].replace('\n','')+'</en></br></br>')
    dataset_file.write(html_foot_code)
dataset_file.close()