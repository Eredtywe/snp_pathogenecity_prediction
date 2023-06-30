import numpy as np
import pandas as pd

file_path = 'snp_result _60000.txt'

snv_data = np.empty((70000,), dtype=f'S{30}')
snp_id = np.empty((70000,), dtype=f'S{30}')
chromosome = np.empty((70000,), dtype=f'S{30}')
position = np.empty((70000,), dtype=f'S{30}')
signature = np.empty((70000,), dtype=f'S{30}')

with open(file_path, 'r') as file:
    lines = file.readlines()

i = 0
k = 1

for line in lines:
    words = line.split()
    
    if words[0] == str(k) + '.':
        snp_id[i] = words[1]
        k += 1
        i += 1

    if line[0:3] == 'SNV':
        temp = line.split(':')
        snv_data[i-1] = temp[1].rstrip('\n')
    
    if words[0] == 'Chromosome:':
        temp = words[1].split(":")
        chromosome[i-1] = temp[0]
        position[i-1] = temp[1]
    
    if words[0] == 'Clinical':
        signature[i-1] = words[2]



data = {'snp_id': snp_id,
        'snv_data': snv_data,
        'chromosome': chromosome,
        'position': position,
        'signature': signature}

df = pd.DataFrame(data)
