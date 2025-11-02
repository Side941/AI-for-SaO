# ga_tsp.py
import random
import copy

# =========================
# Individual Representation
# =========================
class Individual:
    def __init__(self, gene):
        self.gene = gene
        self.fitness = 0

# =========================
# Fitness Function
# =========================
def total_distance(ind, dist_matrix):
    route = ind.gene
    dist = sum(dist_matrix[route[i], route[i+1]] for i in range(len(route)-1))
    dist += dist_matrix[route[-1], route[0]]  # Return to start
    return dist

# =========================
# Selection (Tournament)
# =========================
def selection(population):
    P = len(population)
    new_pop = []
    for _ in range(P):
        i1, i2 = random.sample(range(P), 2)
        winner = population[i1] if population[i1].fitness < population[i2].fitness else population[i2]
        new_pop.append(copy.deepcopy(winner))
    return new_pop

# =========================
# Crossover (Ordered Crossover)
# =========================
def crossover(parents):
    P = len(parents)
    N = len(parents[0].gene)
    offspring = []
    for i in range(0, P, 2):
        p1, p2 = parents[i], parents[i+1]
        a, b = sorted(random.sample(range(N), 2))
        child1_gene = [None]*N
        child2_gene = [None]*N
        child1_gene[a:b] = p1.gene[a:b]
        child2_gene[a:b] = p2.gene[a:b]
        def fill_remaining(child, parent):
            parent_cities = [c for c in parent.gene if c not in child]
            return [c if c is not None else parent_cities.pop(0) for c in child]
        child1_gene = fill_remaining(child1_gene, p2)
        child2_gene = fill_remaining(child2_gene, p1)
        offspring.append(Individual(child1_gene))
        offspring.append(Individual(child2_gene))
    return offspring

# =========================
# Mutation (Swap)
# =========================
def mutation(offspring, MUTRATE=0.1):
    N = len(offspring[0].gene)
    for ind in offspring:
        if random.random() < MUTRATE:
            a, b = random.sample(range(N), 2)
            ind.gene[a], ind.gene[b] = ind.gene[b], ind.gene[a]
    return offspring
