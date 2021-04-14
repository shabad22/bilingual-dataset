english_data_file = open('Eng.txt','r',encoding='utf-8')
english_data = english_data_file.readlines()
english_data_file.close()

html_head_code = r'''
<?xml version="1.0" ?>
<Doc id="english_dataset eng01" lang="english">
<Header type='text'>
    <encodingDesc>
        <projectDesc>English Corpora</projectDesc>
        <samplingDesc>This Document contain Only 10 sentences of english data</samplingDesc>
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
    <langUsage>English</langUsage>
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

with open('Eng_CorpusDataset_50k.html','w',encoding='utf-8') as dataset_file:
    dataset_file.write(html_head_code+'\n')
    for i in range(100000):
        dataset_file.write('<p>'+english_data[i].replace('\n','')+'<p>')
    dataset_file.write(html_foot_code)
dataset_file.close()