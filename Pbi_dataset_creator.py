punjabi_data_file = open('Pbi.txt','r',encoding='utf-8')
punjabi_data = punjabi_data_file.readlines()
punjabi_data_file.close()

html_head_code = r'''
<?xml version="1.0" ?>
<Doc id="punjabi_dataset pbi01" lang="punjabi">
<Header type='text'>
    <encodingDesc>
        <projectDesc>Punjabi Corpora</projectDesc>
        <samplingDesc>This Document contain Only 10 sentences of punjabi data</samplingDesc>
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
    <langUsage>Punjabi</langUsage>
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

with open('Pbi_CorpusDataset_50k.html','w',encoding='utf-8') as dataset_file:
    dataset_file.write(html_head_code+'\n')
    for i in range(50000):
        dataset_file.write('<p>'+punjabi_data[i].replace('\n','')+'<p></br>')
    dataset_file.write(html_foot_code)
dataset_file.close()