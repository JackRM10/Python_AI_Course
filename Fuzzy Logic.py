import numpy as np
import skfuzzy as fuzz

# Input variables
x = np.arange(0, 11, 1) # Inputrange from 0 to 10

#Define fuzzy sets for the input variable
low = fuzz.trimf(x, [0, 0, 5]) #Triangular fuzzy set for low values
medium = fuzz.trimf(x, [2, 5, 8]) #Triangular fuzzy set for medium values
high = fuzz.trimf(x, [5, 10, 10]) #Triangular fuzzy set for high values

#Define fuzzy rules
rule1 = np.fmax(low, medium) # Rule: If input is low or medium, then output is high
rule2 = np.fmin(medium, high) # Rule: If input is medium and high, then output is low

#Apply fuzzy rules to determine the fuzzy relation between input and output 
relation = np.fmax(rule1, rule2)

#Defuzzify the relation to obtain a crisp output
output = fuzz.defuzz(x, relation, 'centroid')

#Display the crisp output
print("Output:", output)
