import numpy as np

def read(path):
    return np.loadtxt(path, dtype='i', max_rows=5)
    
if __name__ == '__main__':
    path = './data/ta20_5.txt'
    l = read(path)
    print(l)
