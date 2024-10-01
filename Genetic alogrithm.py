import random

#Constants
TARGET_PHRASE ="Hello, World!" #The target phrase to be matched
POPULATION_SIZE = 100 #Number of individuals in the population
MUTATION_RATE = 0.01 #Probability of muttation

#Generate initial population
def generate_population():
    population = []
    for _ in range(POPULATION_SIZE):
        individual = '' .join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.!') for _ in range(len(TARGET_PHRASE)))
        population.append(individual)
    return population

#Calculate fitness score
def calculate_fitness(individual):
    score = 0
    for i in range(len(TARGET_PHRASE)):
        if individual[i] == TARGET_PHRASE[i]:
            score += 1
    return score

# Select parents based on fitness
def select_parents(population):
    parents = []
    for _ in range(2):
        parents.append(max(population, key=calculate_fitness))
    return parents

#Create offspring through crossover
def crossover(parents):
    offspring = ""
    crossover_point = random.randint(0, len(TARGET_PHRASE) - 1)
    for i in range(len(TARGET_PHRASE)):
        if i <= crossover_point:
            offspring += parents[0][i]
        else:
            offspring += parents[1][i]
    return offspring

#Mutate offspring
def mutate(offspring):
    mutated_offspirng = ""
    for i in range(len(offspring)):
        if random.random() < MUTATION_RATE:
            mutated_offspirng += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.!')
        else:
            mutated_offspring += offspring[i]
    return mutated_offspring

#Main genetic algorithm
def genetic_algorithm():
    population = generate_population()
    genertion = 1

    while True:
        print(f"Generation {generation} - Best Fit: {max(population, key=calculate_fitness)}")
    
    if TARGET_PHRASE in population:
        break

    new_population = []
    for _ in range(POPULATION_SIZE // 2):
        parents = select_parents(population)
        offspirng = crossover(parents)
        mutated_offspring = mutate(offspring)
        new_population.extend([offspring, mutated_offspring])

    population = new_population
    generation += 1

    #Run the genetic algorithm
    genetic_algorithm()