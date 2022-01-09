# -*- coding: utf-8 -*-
"""
20.12.2021
Molecular Networks
Assignment 3
Exercise 1
Stephanie Hoffmann, Lizzy Friese
"""

from cobra import Model, Reaction, Metabolite
from cobra.flux_analysis import flux_variability_analysis

""" 1) We build the given model for the core 
carbon metabolic network"""

#create a model 
model = Model('core_carbon')

#exchange reactions
Tc1 = Reaction('Tc1')
Tc1.upper_bound = 10.5
Tc2 = Reaction('Tc2')
Tc2.upper_bound =10.5
Tf = Reaction ('Tf')
Tf.upper_bound = 5
Th = Reaction ('Th')
Th.upper_bound = 5
To2 = Reaction('To2')
To2.upper_bound = 15
Td = Reaction('Td')
Td.upper_bound = 12
Te = Reaction('Te')
Te.upper_bound= 12

#internal reactions
R1 = Reaction('R1')
R2 = Reaction('R2')
R2.lower_bound = -1000
R2.upper_bound = 1000
R3 = Reaction('R3')
R4 = Reaction('R4')
R5a = Reaction('R5a')
R5b = Reaction('R5b')
R6 = Reaction('R6')
R7 = Reaction('R7')
R8 = Reaction('R8')
R8.lower_bound = -1000
R8.upper_bound=1000
Rres = Reaction('Rres')
Rres.upper_bound =0
Rres.lower_bound =0
Growth = Reaction('Growth')

#Metabolites
#we only need the internal metabolites
#Carbon1 = Metabolite('Carbon1')
#Carbon2 = Metabolite('Carbon2')
A = Metabolite('A')
#F_ext = Metabolite('F_ext')
F = Metabolite('F')
#H_ext = Metabolite('H_ext')
H = Metabolite('H')
#O2_ext = Metabolite('O2_ext')
O2 = Metabolite('O2')
D = Metabolite('D')
#D_ext = Metabolite('D_ext')
E = Metabolite('E')
#E_ext = Metabolite('E_ext')
ATP = Metabolite('ATP')
B = Metabolite('B')
C = Metabolite('C')
NADH = Metabolite('NADH')
G = Metabolite('G')
Biomass = Metabolite('Biomass')

#create reactions with stochiometry
Tc1.add_metabolites({
    #Carbon1: -1.0,
    A: 1.0
    })
Tc2.add_metabolites({
    #Carbon2: -1.0,
    A: 1.0
    })
Tf.add_metabolites({
   # F_ext: -1.0,
    F: 1.0
    })
Th.add_metabolites({
   # H_ext:-1.0,
    H: 1.0
    })
To2.add_metabolites({
    #O2_ext: -1.0,
    O2: 1.0
    })
Td.add_metabolites({
    D:-1.0,
    #D_ext: 1.0
    })
Te.add_metabolites({
    E:-1.0,
    #E_ext: 1.0
    })
R1.add_metabolites({
    A:-1.0,
    ATP:-1.0,
    B:1.0
    })
R2.add_metabolites({
    B:-1.0,
    C: 1.0,
    ATP: 2.0,
    NADH: 2.0,
    })
R3.add_metabolites({
    B: -1.0,
    F: 1.0
    })
R4.add_metabolites({
    C: -1.0,
    G: 1.0
    })
R5a.add_metabolites({
    G: -1.0,
    C: 0.8,
    NADH: 2.0
    })
R5b.add_metabolites({
    G: -1.0,
    C: 0.8,
    NADH: 2.0
    })
R6.add_metabolites({
    C: -1.0,
    ATP: 2.0,
    D: 3.0
    })
R7.add_metabolites({
    C: -1.0,
    NADH: -4.0,
    E: 3.0
    })
R8.add_metabolites({
    G: -1.0,
    ATP: -1.0,
    NADH: -2.0,
    H: 1.0
    })
Rres.add_metabolites({
    O2: -1.0,
    NADH: -1.0,
    ATP: 1.0
    })
Growth.add_metabolites({
    C: -1.0,
    F: -1.0,
    H: -1.0,
    ATP: -10.0,
    #Biomass: 1.0
    })
#add reactions  to the model
model.add_reactions([Tc1,Tc2,Tf,Th,To2,Td,Te,R1,R2,R3,R4,R5a,R5b,R6,R7,R8,Rres,Growth])

print("Reactions")
print("---------")
for x in model.reactions:
    print("%s : %s" % (x.id, x.reaction))


""" 2) We perform an FBA to maximize the flux through Reaction "Growth" """

#add objective
model.objective = 'Growth'
solution = model.optimize()

print(f'The {model.objective.direction} value of a flux through reaction "Growth" is {model.objective.value}')

""" 3) We perform a FVA. Somehow there comes a runtime error when we try to
perform the FVA on all reactions at the same time. For one reaction we gat a result. 
Form our calculations would assume that there is no internal cycle since we 
do not have unbounded flow through any reaction. But from the sketch of the 
network on the exercise sheet we would have assumed that there is a cycle """
for i in range(0,18):
    print(flux_variability_analysis(model,model.reactions[i]))



"""4) We performed single knock-out experiments. We set Reaction.upper_bound =0
and Reaction.lower_bound =0. 
Blocking out .... results in a max flow of .... through "Growth"
            Tc1                             3.5
            Tc2                             3.5
            Tf                              3.172
            Th                              3.518
            To2                             1.333
            Td                              2.281
            Te                              3.009
            R1                              1.883
            R2                              1.883
            R3                              3.518
            R4                              3.244
            R5a                             3.518
            R5b                             3.518
            R6                              2.281
            R7                              3.009
            R8                              3.518
            Rres                            1.333
            
Looking at the values of the remaining fluxes we consider To2 ans Rres as
essential. Also R1 and R2 seem to play an important role. 
"""



