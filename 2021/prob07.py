import math
mats = input()

mCombos  = { 
    'CONCRETE RUBBER':0.90,
    'CONCRETE WOOD':0.62,
    'CONCRETE STEEL':0.57,
    'WOOD RUBBER':0.80,
    'WOOD WOOD':0.42,
    'WOOD STEEL':0.30,
    'WOOD CONCRETE':0.62,
    'WOOD ICE':0.05,
    'STEEL RUBBER':0.70,
    'STEEL WOOD':0.30,
    'STEEL STEEL':0.74,
    'STEEL CONCRETE':0.57,
    'STEEL ICE':0.03,
    'RUBBER RUBBER':1.15,
    'RUBBER WOOD':0.80,
    'RUBBER STEEL':0.70,
    'RUBBER CONCRETE':0.90,
    'RUBBER ICE':0.15,
    'ICE RUBBER':0.15,
    'ICE WOOD':0.05,
    'ICE STEEL':0.03,    
}

for combo in mCombos:
    if (combo == mats):
        friction = mCombos[combo]
        deg = round(math.degrees(math.atan(friction)), 1)
        sFriction = "{:.2f}".format(friction)
        print(sFriction, deg)
        break
