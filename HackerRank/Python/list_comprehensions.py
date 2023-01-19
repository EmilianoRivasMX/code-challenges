"""
You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i+j+k is not equal to n.

Remember:
    0 <= i <= x
    0 <= j <= y
    0 <= k <= z
"""

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
n = int(input("n: "))

i = [x for x in range(x+1)]
j = [y for y in range(y+1)]
k = [z for z in range(z+1)]

print(f"\nRango de i: {i}")
print(f"Rango de j: {j}")
print(f"Rango de k: {k}")

# First solution
# permutacoines = []
# posibles_coordenadas = []

# for x in i:
#     for y in j:
#         for z in k:
#             permutacoines.append([x,y,z])
#             if x+y+z != 3:
#                 posibles_coordenadas.append([x,y,z])

# Second solutcion
permutaciones = [[x,y,z] for x in i for y in j for z in k]
posibles_coordenadas = [p for p in permutaciones if sum(p) != n]

print(f"\nLista de permutaciones:\n{permutaciones}")
print(f"\nArray final:\n{posibles_coordenadas}")
