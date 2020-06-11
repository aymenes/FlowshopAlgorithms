from random import shuffle, randrange, sample, random
from makespan import makespan
import data

def genetic(data):
    population_size = 100
    taux_mutation = 0.1
    iterations = 100
    #job_count = len(data)
    job_count = len(data[0])
    print('job_count = {}'.format(job_count))

    # Generer une les individus de la population aleatoirement
    population = [sample(list(range(1, job_count + 1)), job_count) for _ in range(0, population_size)] # same repeated individual

    for individu in population:
        print('{} : {}'.format(individu, makespan(individu, data)))
    population_avec_qualite = evaluer_qualite(population, data)    
    print(population_avec_qualite)
    """
    for _ in range(0, iterations):
        parents = choisir_parents(population_avec_qualite)
        enfants = breed(parents)
        muter(enfants, taux_mutation)
        population_avec_qualite = merge(population_avec_qualite, evaluer_qualite(enfants, data))
    return choisir_meilleur(population_avec_qualite)[0]
    """

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
    
data = [[54, 83, 15, 71, 77, 36, 53, 38, 27, 87, 76, 91, 14, 29, 12, 77, 32, 87, 68, 94],
 [79,  3, 11, 99, 56, 70, 99, 60,  5, 56,  3, 61, 73, 75, 47, 14, 21, 86,  5, 77],
 [16, 89, 49, 15, 89, 45, 60, 23, 57, 64,  7,  1, 63, 41, 63, 47, 26, 75, 77, 40],
 [66, 58, 31, 68, 78, 91, 13, 59, 49, 85, 85,  9, 39, 41, 56, 40, 54, 77, 51, 31],
 [58, 56, 20, 85, 53, 35, 53, 41, 69, 13, 86, 72,  8, 49, 47, 87, 58, 18, 68, 28]]

genetic(data)
