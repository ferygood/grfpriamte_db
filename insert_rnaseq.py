# insert RNA seq expression

import pandas as pd

fpkm_file = "../preprocess_data/nhprtr_refseq_sFPKM.csv"

# tfprimate.primate_rnaseq.py
# does this table include all AceView data?
# modified the function for data?

def preprocess_data(fpkm_file):
    data = pd.read_csv(fpkm_file, sep='\t', header=None, comment='#')
    header = []
    with open(fpkm_file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                header.append(line.strip().split('\t'))
            else:
                break
    
    header[7][0] = 'gene_symbol'
    header[7][12] = 'sumofreads'
    data.columns = [x.replace('#','') for x in header[7]]
    data.columns = [x.replace('BrainLeft', 'Brain') for x in data.columns]
    #data.columns = [x.replace('BrainRight', 'Brain') for x in data.columns]
    data.columns = [x.replace('Heart1', 'Heart') for x in data.columns]
    
    data.drop('Heart2_notThm_MST', axis=1, inplace=True)
    data.drop('Liver_mRNA_CMM', axis=1, inplace=True)
    data.drop('Liver_mRNA_CMC', axis=1, inplace=True)
    data.drop('BrainRight_MST', axis=1, inplace=True)
    
    samples = data.columns[13:]
    data[samples] = data[samples].replace({"NE/": "", "NA/":""}, regex=True)
    data[samples] = data[samples].astype(float)
    
    return data, samples

data, samples = preprocess_data(fpkm_file)

for col in data.columns:
    print(col)