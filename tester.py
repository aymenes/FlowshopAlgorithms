import algorithme_genetique
import data as dataReader
from time import time
import matplotlib.pyplot as plt

def varier_iteration():
	x = []
	y = []
	population = 100
	for iteration in range(1, 201, 10):
		x.append(iteration)
		start = time()
		population = 100
		result = algorithme_genetique.genetic(matrice, population, 0.1, iteration)
		print('  Nombre d\'iterations : {}'.format(iteration))
		print('  Ordre : {}'.format(result[0]))
		print('  Makespan : {}'.format(result[1]))
		end = time()
		y.append(result[1])
		print('  Temps d\'execution : {:.6}s'.format(end - start))
		print()

	plt.plot(x,y)
	plt.xlabel('Test')
	plt.ylabel('Makespan')
	plt.show()

path = './data/ta20_10.txt'
matrice = dataReader.read(path, 10)
varier_iteration()
