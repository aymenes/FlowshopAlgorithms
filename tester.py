from algorithme_genetique import genetic
from algo_genetique_recherche_locale import genetic_rt
#import algorithme_genetique, algo_genetique_recherche_locale
import data as dataReader
import matplotlib.pyplot as plt
from random import shuffle, randrange, sample, random
from time import time
from makespan import makespan


path = './data/ta20_20.txt'
matrice = dataReader.read(path, 20)

population_size = 100
job_count = 20

# Generer une les individus de la population aleatoirement
initPop = [sample(list(range(1, job_count + 1)), job_count) for _ in range(0, population_size)] # same repeated individual

print('Algorithme Hybride :')
start = time()
#result = genetic(matrice, initPop, 100, 0.1, 200, limit=2400)
result = genetic_rt(matrice, initPop, 100, 0.1, 200, limit=2400)
print('  Ordre : {}'.format(result[0]))
print('  Makespan : {}'.format(result[1]))
end = time()
print('  Temps d\'execution : {:.6}s'.format(end - start))
'''
print('Generation,Makespan')
for i in range(len(x)):
    print('{},{}'.format(x[i], y[i]))
plt.plot(x,y)
plt.xlabel('Generation')
plt.ylabel('Makespan')
plt.show()
'''

print('Algorithme Genetique :')
start = time()
result = genetic(matrice, initPop, 100, 0.1, 200, limit=2400)
print('  Ordre : {}'.format(result[0]))
print('  Makespan : {}'.format(result[1]))
end = time()
print('  Temps d\'execution : {:.6}s'.format(end - start))
