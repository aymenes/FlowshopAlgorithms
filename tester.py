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


'''
x = []
y = []
y100 = []
y200 = []
y300 = []

path = './data/ta20_10.txt'
matrice = dataReader.read(path, 10)
for _ in range(10):
	x.append(_ + 1)
	start = time()
	population = 100
	result = algorithme_genetique.genetic(matrice, population, 0.1, 100)
	print('  Population : {}'.format(population))
	print('  Ordre : {}'.format(result[0]))
	print('  Makespan : {}'.format(result[1]))
	end = time()
	#y.append(end - start)
	#y100.append(end - start)
	y100.append(result[1])
	print('  Temps d\'execution : {:.6}s'.format(end - start))
	print()

for _ in range(10):
	#x.append(_ + 1)
	start = time()
	population = 200
	result = algorithme_genetique.genetic(matrice, population, 0.1, 100)
	print('  Population : {}'.format(population))
	print('  Ordre : {}'.format(result[0]))
	print('  Makespan : {}'.format(result[1]))
	end = time()
	#y.append(end - start)
	#y200.append(end - start)
	y200.append(result[1])
	print('  Temps d\'execution : {:.6}s'.format(end - start))
	print()

for _ in range(10):
	#x.append(_ + 1)
	start = time()
	population = 300
	result = algorithme_genetique.genetic(matrice, population, 0.1, 100)
	print('  Population : {}'.format(population))
	print('  Ordre : {}'.format(result[0]))
	print('  Makespan : {}'.format(result[1]))
	end = time()
	#y.append(end - start)
	#y300.append(end - start)
	y300.append(result[1])
	print('  Temps d\'execution : {:.6}s'.format(end - start))
	print()

plt.plot(x,y100, label='Population = 100')
plt.plot(x,y200, label='Population = 200')
plt.plot(x,y300, label='Population = 300')
plt.xlabel('Test')
plt.ylabel('Temps d\'execution')
plt.show()
'''
'''
path = './data/ta20_10.txt'
matrice = dataReader.read(path, 10)
start = time()
result = algorithme_genetique.genetic(matrice, 100, 0.1, 100)
print('  Ordre : {}'.format(result[0]))
print('  Makespan : {}'.format(result[1]))
end = time()
print('  Temps d\'execution : {:.6}s'.format(end - start))

path = './data/ta20_20.txt'
matrice = dataReader.read(path, 20)
start = time()
result = algorithme_genetique.genetic(matrice, 100, 0.1, 100)
print('  Ordre : {}'.format(result[0]))
print('  Makespan : {}'.format(result[1]))
end = time()
print('  Temps d\'execution : {:.6}s'.format(end - start))

'''