import pandas as pd
train=pd.read_csv('pacifier.tsv', sep='\t', header=0)
print(train)
train.to_excel("pacifier.xlsx")
