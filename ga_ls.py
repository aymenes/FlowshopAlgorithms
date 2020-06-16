from random import shuffle, randrange, sample, random
from time import time
from makespan import makespan
import data as dataReader

def genetic1(data, populationInitiale, taille_population = 100, taux_mut = 0.1, maxIterations = 100, limit = 99999):
    population_size = taille_population
    taux_mutation = taux_mut
    #iterations = maxIterations
    job_count = len(data[0])
    print('jobs = {}   machines = {} '.format(job_count, len(data)))

    # Generer une les individus de la population aleatoirement
    #population = [sample(list(range(1, job_count + 1)), job_count) for _ in range(0, population_size)] # same repeated individual

    #population_avec_qualite = evaluer_qualite(population, data)    
    population_avec_qualite = evaluer_qualite(populationInitiale, data)

    score = 9999999
    iteration = 0
    while score > limit && iteration < maxIterations::
        iteration += 1
        parents = choisir_parents(population_avec_qualite)
        enfants = croisement(parents)
        mutation(enfants, taux_mutation)
        population_avec_qualite = union(population_avec_qualite, evaluer_qualite(enfants, data))
        meilleurIndividu = choisir_meilleur(population_avec_qualite)

        if meilleurIndividu[1] < score:
            score = meilleurIndividu[1]
            print('new : {} makespan = {}'.format(meilleurIndividu[0], meilleurIndividu[1]))
    print(iteration)
    return meilleurIndividu

def genetic2(data, populationInitiale, taille_population = 100, taux_mut = 0.1, maxIterations = 100, limit = 99999):
    population_size = taille_population
    taux_mutation = taux_mut
    #iterations = maxIterations
    job_count = len(data[0])
    print('jobs = {}   machines = {} '.format(job_count, len(data)))

    # Generer une les individus de la population aleatoirement
    #population = [sample(list(range(1, job_count + 1)), job_count) for _ in range(0, population_size)] # same repeated individual
    #population_avec_qualite = evaluer_qualite(population, data)
    population_avec_qualite = evaluer_qualite(populationInitiale, data)

    score = 9999999
    iteration = 0
    while score > limit && iteration < maxIterations:
        iteration += 1
        parents = choisir_parents(population_avec_qualite)
        #print(parents[0])
        enfants = croisement(parents)
        
        mutationAvancee(enfants, taux_mutation, data)
        population_avec_qualite = union(population_avec_qualite, evaluer_qualite(enfants, data))
        meilleurIndividu = choisir_meilleur(population_avec_qualite)

        if meilleurIndividu[1] < score:
            score = meilleurIndividu[1]
            print('new : {} makespan = {}'.format(meilleurIndividu[0], meilleurIndividu[1]))
    print(iteration)
    return meilleurIndividu

    #for _ in range(0, iterations):
        
    #return choisir_meilleur(population_avec_qualite)

def evaluer_qualite(population, data):
    return [(individual, makespan(individual, data)) for individual in population]

def choisir_parents(population):
    parents = []
    for _ in range(0, len(population)):
        # Prendre un echantillon aleatoire de 5 individus
        echantillon = sample(population, 5)

        # Choisir le meilleur des 5
        parents.append(choisir_meilleur(echantillon))
    return parents

def croisement(parents):
    shuffle(parents)
    enfants = []
    for i in range(1, len(parents), 2):
        enfants += merge(parents[i - 1][0], parents[i][0])
    return enfants

def mutation(enfants, taux_mutation):
    for i in range(len(enfants)):
        enfant = enfants[i]
        if random() <= taux_mutation:
            left = randrange(0, len(enfant))
            right = randrange(left, len(enfant))
           
            tmp = enfant[left]
            enfant[left] = enfant[right]
            enfant[right] = tmp

            enfants[i] = enfant

def mutationAvancee(enfants, taux_mutation, data):
    for i in range(len(enfants)):
        enfant = enfants[i]
        qualiteEnfant = makespan(enfant, data)
        enfantTmp = enfant
        for _ in range(5):
            left = randrange(0, len(enfantTmp))
            right = randrange(left, len(enfantTmp))
            tmp = enfantTmp[left]
            enfantTmp[left] = enfantTmp[right]
            enfantTmp[right] = tmp

        qualiteEnfant2 = makespan(enfantTmp, data)
        if(qualiteEnfant2 < qualiteEnfant):
            enfants[i] = enfantTmp

def union(parents, enfants):
    both = parents + enfants
    both.sort(key=lambda x: x[1])
    return both[:len(parents)]

def choisir_meilleur(population):
    return min(population, key=lambda x: x[1])

def translate(x, d):
    while x in d and x != d[x]:
        x = d[x]
    return x

def merge(a, b):
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

'''
path = './data/ta20_5.txt'
matrice = dataReader.read(path, 5)
start = time()
result = genetic(matrice, 100, 0.1, 100)
print('  Ordre : {}'.format(result[0]))
print('  Makespan : {}'.format(result[1]))
end = time()
print('  Temps d\'execution : {:.6}s'.format(end - start))

path = './data/ta20_10.txt'
matrice = dataReader.read(path, 10)
start = time()
result = genetic(matrice, 100, 0.1, 100)
print('  Ordre : {}'.format(result[0]))
print('  Makespan : {}'.format(result[1]))
end = time()
print('  Temps d\'execution : {:.6}s'.format(end - start))
'''
path = './data/ta20_20.txt'
matrice = dataReader.read(path, 20)

population_size = 100
job_count = 20

initPop = [sample(list(range(1, job_count + 1)), job_count) for _ in range(0, population_size)] # same repeated individual

start = time()
result = genetic2(matrice, initPop, 100, 0.3, 100, limit=2400)
print('  Ordre : {}'.format(result[0]))
print('  Makespan : {}'.format(result[1]))
end = time()
print('  Temps d\'execution : {:.6}s'.format(end - start))

path = './data/ta20_20.txt'
matrice = dataReader.read(path, 20)
start = time()
result = genetic1(matrice, initPop, 100, 0.3, 100, limit=2400)
print('  Ordre : {}'.format(result[0]))
print('  Makespan : {}'.format(result[1]))
end = time()
print('  Temps d\'execution : {:.6}s'.format(end - start))

