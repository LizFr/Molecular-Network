# -*- coding: utf-8 -*-
"""
20.12.2021
Molecular Networks
Assignment 3
Stephanie Hoffann, Lizzy Friese
"""
import cobra
from cobra import Model, Reaction, Metabolite
#create a model 
model = Model('core_carbon')

'''sind die maximum transport rates vielleicht
dann auch upper bounds?'''

#exchange reactions
Tc1 = Reaction('Tc1')
Tc2 = Reaction('Tc2')
Tf = Reaction ('Tf')
Th = Reaction ('Th')
To2 = Reaction('To2')
Td = Reaction('Td')
Te = Reaction('Te')

#internal reactions
R1 = Reaction('R1')
#ich glaube mit den bounds kann man die reversible machen 
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
Growth = Reaction('Growth')

#Metabolites
# compartement i= internal, e= external 
Carbon1 = Metabolite('Carbon1', compartment='e')
Carbon2 = Metabolite('Carbon2',compartment='e')
A = Metabolite('A',compartment='i')
F_ext = Metabolite('F_ext',compartment='e')
F = Metabolite('F',compartment='i')
H_ext = Metabolite('H_ext',compartment='e')
H = Metabolite('H',compartment='i')
O2_ext = Metabolite('O2_ext',compartment='e')
O2 = Metabolite('O2',compartment='i')
D = Metabolite('D',compartment='i')
D_ext = Metabolite('D_ext',compartment='e')
E = Metabolite('E',compartment='i')
E_ext = Metabolite('E_ext',compartment='e')
ATP = Metabolite('ATP',compartment='i')
B = Metabolite('B',compartment='i')
C = Metabolite('C',compartment='i')
NADH = Metabolite('NADH',compartment='i')
G = Metabolite('G',compartment='i')
Biomass = Metabolite('Biomass',compartment='i')

#create reactions with stochiometry
Tc1.add_metabolites({
    Carbon1: -1.0,
    A: 1.0
    
    })
Tc2.add_metabolites({
    Carbon2: -1.0,
    A: 1.0
    })
Tf.add_metabolites({
    F_ext: -1.0,
    F: 1.0
    })
Th.add_metabolites({
    H_ext:-1.0,
    H:1.0
    })
To2.add_metabolites({
    O2_ext: -1.0,
    O2: 1.0
    })
Td.add_metabolites({
    D:-1.0,
    D_ext: 1.0
    })
Te.add_metabolites({
    E:-1.0,
    E_ext: 1.0
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
    Biomass: 1.0
    })
#add reactions  to the model
model.add_reactions([Tc1,Tc2,Tf,Th,To2,Td,Te,R1,R2,R3,R4,R5a,R5b,R6,R7,R8,Rres,Growth])
#add objective
model.objective = 'Growth'
print(model.objective.expression)
print(model.objective.direction)
solution = model.optimize()
print(solution)
'''


print(f'{len(model.reactions)} reactions')
print(f'{len(model.metabolites)} metabolites')
# Iterate through the the objects in the model
print("Reactions")
print("---------")
for x in model.reactions:
    print("%s : %s" % (x.id, x.reaction))

print("")
print("Metabolites")
print("-----------")
for x in model.metabolites:
    print('%9s : %s' % (x.id, x.formula))
#FBA
solution = model.optimize()
print(solution.objective_value)
print(model.summary())
'''
