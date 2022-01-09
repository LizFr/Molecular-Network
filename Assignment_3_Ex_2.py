# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 09:05:11 2022
Molecular Networks
Assignment 3
Exercise 2
Stephanie Hoffmann, Lizzy Friese
"""

from cobra import Model, Reaction, Metabolite
from cobra.flux_analysis.loopless import add_loopless, loopless_solution
from cobra.flux_analysis import pfba
from cobra.flux_analysis import flux_variability_analysis
import pandas

"""1) We build the model of the given metabolic network."""

#create Model
model = Model('Exercise_2')

#Reactions
R1 = Reaction('R1')
R1.upper_bound = 1
R2 = Reaction('R2')
R3 = Reaction('R3')
R3.lower_bound = -1
R4 = Reaction('R4')
R5 = Reaction('R5')
R5.lower_bound = -1000
R6 = Reaction('R6')
R7 = Reaction('R7')
R7.upper_bound = 1
R8 = Reaction('R8')
R9 = Reaction('R9')

#Metabolites
A = Metabolite('A')
B = Metabolite('B')
C = Metabolite('C')
D = Metabolite('D')

#add Metabolites to Reaction
R1.add_metabolites({
    A: 1.0
    })
R2.add_metabolites({
    B: -1.0,
    A: 1.0
    })
R3.add_metabolites({
    B: -1.0
    })
R4.add_metabolites({
    A: -1.0,
    C: 1.0
    })
R5.add_metabolites({
    A: -1.0,
    D: 1.0
    })
R6.add_metabolites({
    D: -1.0,
    B: 1.0
    })
R7.add_metabolites({
    C: 1.0
    })
R8.add_metabolites({
    C: -1.0,
    D: 1.0
    })
R9.add_metabolites({
    D: -1.0
    })

#add reactions to the model 
model.add_reactions([R1,R2,R3,R4,R5,R6,R7,R8,R9])
print("Reactions")
print("---------")
for x in model.reactions:
    print("%s : %s" % (x.id, x.reaction))
    
""" 2) We perform a FBA maximizing the flux through reaction 5"""

#add objective
model.objective = 'R5'
solution = model.optimize()

print(f'The {model.objective.direction} value of a flux through reaction R5 is {model.objective.value}')

"""3) We compute the corresponding loopless solution"""

loopless = loopless_solution(model)
print(loopless)

"""4) We perform a FVA """
print("FVA")
print("---------")
for i in range(0,9):
    print(flux_variability_analysis(model,model.reactions[i]))

"""5) We perform a loopless FVA and look at the looples solution fluxes"""
print("FVA loopless")
print("---------")
for i in range(0,9):
    print(flux_variability_analysis(model,model.reactions[i],loopless = True) )

with model:
    add_loopless(model)
    solution = model.optimize()
print("loopless solution flux: R1 = %.1f" % solution.fluxes["R1"])
print("loopless solution flux: R2 = %.1f" % solution.fluxes["R2"])
print("loopless solution flux: R3 = %.1f" % solution.fluxes["R3"])
print("loopless solution flux: R4 = %.1f" % solution.fluxes["R4"])
print("loopless solution flux: R5 = %.1f" % solution.fluxes["R5"])
print("loopless solution flux: R6 = %.1f" % solution.fluxes["R6"])
print("loopless solution flux: R7 = %.1f" % solution.fluxes["R7"])
print("loopless solution flux: R8 = %.1f" % solution.fluxes["R8"])
print("loopless solution flux: R9 = %.1f" % solution.fluxes["R9"])

