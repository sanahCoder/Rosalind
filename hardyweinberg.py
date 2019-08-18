population = [19471,16590,16595,16930,17093,16591]

def phenotypeCalc(population):
    totalIndividuals = 0
    for genotype in population:
        totalIndividuals += (genotype*2)
    recessivePop = 0
    n = 2
    for x in range(3,6):
        recessivePop += population[x]*2*(1/(2**n))
        n = n - 1
    return totalIndividuals - recessivePop

print(phenotypeCalc(population))
