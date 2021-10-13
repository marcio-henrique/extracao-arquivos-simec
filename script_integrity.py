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
    if (row['Formato'] in ['Digital', 'Audiovisual']):
        if (type(row['id_zip']) is str):
            #print('rowz')
            rows_zip = zipado[zipado['id'] == row['id']]
            #print(rows_zip)
            for i_zip, r_zip in rows_zip.iterrows():
                if (r_zip['Nome do Arquivo'] != row['Nome do Arquivo']):
                    continue
                    
                print(r_zip['Nome do Arquivo'] + ' - ' + row['Nome do Arquivo'])
                df.at[index, 'Caminho Local'] = r_zip['Caminho Local']
                print (df.at[index, 'Caminho Local'])
                print('OK')
                