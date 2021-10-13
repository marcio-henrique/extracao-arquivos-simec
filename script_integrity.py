import pandas as pd
import numpy as np
import os
import hashlib
import math

def generate_file_md5(filename, blocksize=2**20):
    m = hashlib.md5()
#     os.path.join(rootdir, filename)
    with open( filename, "rb" ) as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update( buf )
    return m.hexdigest()

df = pd.read_csv(
         'dados/com_hash.csv',
         dtype=str,
    )
	
for index, row in df.iterrows():
    if (row['Formato'] in ['Digital', 'Audiovisual'] and type(row['md5 local']) is not str):
        if (type(row['id_zip']) is str):
            file_path = '../../' + row['Edital'] + '/zip/' + row['id'] + '/' + row['Caminho Local']
            print(row['id'] + ' - ' + row['id_zip'])
        elif (math.isnan(row['id_zip'])):
            file_path = 'arquivos/' + row['Edital'] + '/' + row['id'] + '/' + row['Nome do Arquivo']
            print(row['id'])
        else:
            print('opaa')
            continue
        
        try:
            md5 = generate_file_md5(file_path)
            df.at[index, 'md5 local'] = md5
            print(md5)
            print('OK')
        except Exception as e:
            print(e)
            break
