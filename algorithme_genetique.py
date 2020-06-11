from random import shuffle, randrange, sample, random
from time import time
from makespan import makespan
import data as dataReader

def genetic(data):
    population_size = 100
    taux_mutation = 0.1
    iterations = 100
    job_count = len(data[0])
    print('jobs = {}   machines = {} '.format(job_count, len(data)))

    # Generer une les individus de la population aleatoirement
    population = [sample(list(range(1, job_count + 1)), job_count) for _ in range(0, population_size)] # same repeated individual

    population_avec_qualite = evaluer_qualite(population, data)    

    for _ in range(0, iterations):
        parents = choisir_parents(population_avec_qualite)
        enfants = breed(parents)
        muter(enfants, taux_mutation)
        population_avec_qualite = merge(population_avec_qualite, evaluer_qualite(enfants, data))
    return choisir_meilleur(population_avec_qualite)

def evaluer_qualite(population, data):
    return [(individual, makespan(individual, data)) for individual in population]

def choisir_parents(population):
    parents = []
    for _ in range(0, len(population)):
        # Prendre un echantillon aleatoire
        echantillon = sample(population, 5)
        parents.append(choisir_meilleur(echantillon))
    return parents

def breed(parents):
    shuffle(parents)
    enfants = []
    for i in range(1, len(parents), 2):
        enfants += pmx(parents[i - 1][0], parents[i][0])
    return enfants

def muter(enfants, taux_mutation):
    for enfant in enfants:
        if random() <= taux_mutation:
            left = randrange(0, len(enfant))
            right = randrange(left, len(enfant))
           
            tmp = enfant[left]
            enfant[left] = enfant[right]
            enfant[right] = tmp   

def merge(parents, enfants):
    both = parents + enfants
    both.sort(key=lambda x: x[1])
    return both[:len(parents)]

def choisir_meilleur(population):
    return min(population, key=lambda x: x[1])

def translate(x, d):
    while x in d and x != d[x]:
        x = d[x]
    return x

def pmx(a, b):
    length = len(a)
    left = randrange(0, length + 1)
    right = randrange(left, length + 1)
    
    a2 = a[left:right]
    b2 = b[left:right]
    d = dict(zip(a2, b2))
    d_inv = dict(zip(b2, a2))
   
    enfant1 = list(map(lambda x: translate(x, d_inv), a[0:left])) + b2 + list(map(lambda x: translate(x, d_inv), a[right:length + 1]))
    enfant2 = list(map(lambda x: translate(x, d), b[0:left])) + a2 + list(map(lambda x: translate(x, d), b[right:length + 1]))
    
    return [enfant1, enfant2]     
    

path = './data/ta20_5.txt'
matrice = dataReader.read(path, 5)
start = time()
print(genetic(matrice))
end = time()
print(end - start)

path = './data/ta20_10.txt'
matrice = dataReader.read(path, 10)
start = time()
print(genetic(matrice))
end = time()
print(end - start)

path = './data/ta20_20.txt'
matrice = dataReader.read(path, 20)
start = time()
print(genetic(matrice))
end = time()
print(end - start)
