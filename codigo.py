import numpy as np
import csv

with open("IMDB-Movie-Data.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)
    data_array = np.array(data)
    
    ranking = (data_array[1:, 8])
    raspagem = ranking.astype(np.float64)
    print(f'Média: {np.mean(raspagem)}')
    print(f'Máximo: {np.max(raspagem)}')
    print(f'Mínimo: {np.min(raspagem)}')
    print(f'Soma de todos os valores: {np.sum(raspagem)}')
    