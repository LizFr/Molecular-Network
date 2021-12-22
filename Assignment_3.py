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
R2 = Reaction('R2')
R3 = Reaction('R3')
R4 = Reaction('R4')
R5a = Reaction('R5a')
R5b = Reaction('R5b')
R6 = Reaction('R6')
R7 = Reaction('R7')
R8 = Reaction('R8')
Rres = Reaction('Rres')
Growth = Reaction('Growth')
#Metabolites
Carbon1 = Metabolite('Carbon1')
Carbon2 = Metabolite('Carbon2')
A = Metabolite('A')
F_ext = Metabolite('F_ext')
F = Metabolite('F')
H_ext = Metabolite('H_ext')
H = Metabolite('H')
O2_ext = Metabolite('O2_ext')
O2 = Metabolite('O2')
D = Metabolite('D')
D_ext = Metabolite('D_ext')
E = Metabolite('E')
E_ext = Metabolite('E_ext')
ATP = Metabolite('ATP')
B = Metabolite('B')
C = Metabolite('C')
NADH = Metabolite('NADH')
G = Metabolite('G')
Biomass = Metabolite('Biomass')
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
    NADH: 2.0
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

print("")
print("Genes")
print("-----")
for x in model.genes:
    associated_ids = (i.id for i in x.reactions)
    print("%s is associated with reactions: %s" %
          (x.id, "{" + ", ".join(associated_ids) + "}"))
