import numpy as np

def read(path, rows):
    return np.loadtxt(path, dtype='i', max_rows=rows)
    
if __name__ == '__main__':
    path = './data/ta20_10.txt'
    l = read(path, 10)
    print(l)
