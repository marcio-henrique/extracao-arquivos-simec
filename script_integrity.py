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
         'dados/atual.csv',
         dtype=str,
    )
	
    
for index, row in df.iterrows():
    if (row['Formato'] in ['Digital', 'Audiovisual'] and type(row['md5 servidor']) is not str):
        if (type(row['id_zip']) is str):
            file_path = row['edital sv'] + '/zip/' + row['id'] + '/' + row['Caminho Local']
            print(row['id'] + ' - ' + row['id_zip'])
        elif (math.isnan(row['id_zip'])):
            file_path = row['edital sv'] + '/' + row['id'] + '/' + row['Nome do Arquivo']
            print(row['id'])
        else:
            print('opaa')
            continue
        
        try:
            md5 = generate_file_md5(file_path)
            df.at[index, 'md5 servidor'] = md5
            print(md5)
            print('OK')
            df.to_csv('dados/atual.csv', index = False)
        except Exception as e:
            print(e)
            continue


#PNLD 2020 - Obras Didaticas - Anos Finais do Ensino Fundamental/zip/4636/fp_AUDVISU_matematica_7_PNLD2020_18080_matematicacompreensaoepratica/fp_AUDVISU_licenca_aberta_matematica_7_PNLD2020_18080_matematicacompreensaoepratica/aviacao_e_a_matematica_matematica_7_PNLD2020_18080_matematicacompreensaoepratica/aviacao_MCP7_OR_G20.pdf