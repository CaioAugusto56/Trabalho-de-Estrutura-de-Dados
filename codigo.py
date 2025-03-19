# Usei as bibliotecas Numpy e csv para fazer a análise do banco de dados do IMDB

import numpy as np
import csv

# Manipulei os arquivos csv transformando em uma matriz

with open("IMDB-Movie-Data.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)
    data_array = np.array(data)

# Transformei os arquivos manipulados em outras variáveis para conseguir fazer a mediana, média, desvio padrão, mínimo e máximo
    
    ranking = (data_array[1:, 8])
    raspagem = ranking.astype(np.float64)
    print(f'Mediana: {np.median(raspagem)}')
    print(f'Média: {np.mean(raspagem)}')
    print(f'Desvio padrão: {np.std(raspagem)}')
    print(f'Máximo: {np.max(raspagem)}')
    print(f'Mínimo: {np.min(raspagem)}')
    print(f'Soma de todos os valores: {np.sum(raspagem)}')
    
