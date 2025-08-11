pip install ortools

from ortools.linear_solver import pywraplp

# Crear el solucionador
solver = pywraplp.Solver.CreateSolver('SCIP')

# Datos del problema
n = 16  # Número de cajas
m = 3  # Número de vagones
q = 100  # Capacidad máxima de carga de cada vagón (100 quintales)
p = [34,6,8,17,16,5,13,21,25,31,14,13,33,9,25,25]  # Peso de cada caja
V = range(m)  # Conjunto de vagones
C = range(n)  # Conjunto de cajas

# Variables
x = {}
for i in V:
    for j in C:
        x[i, j] = solver.BoolVar(f'x_{i}_{j}')

y = solver.NumVar(0, q, 'y')

# Función objetivo
z = y

# Restricciones
for i in V:
  solver.Add(y >= sum(p[j]*x[i,j] for j in C))

for j in C:
    solver.Add(sum(x[i, j] for i in V) == 1)

for i in V:
    solver.Add(sum(p[j] * x[i, j] for i in V) <= q)

# Resolver el problema
solver.Minimize(z)
solver.Solve()

# Imprimir resultados
print(f'Carga mínima del vagón con mayor carga: {y.solution_value()} quintales')
print('------Asignaciones------')
for i in V:
    print(f'Vagón {i+1}')
    print(' Caja |', end='')
    for j in C:
        if x[i,j].solution_value() == 1:
            print(f' {j+1:3d} |', end='')
    print('\n Peso |', end='')
    for j in C:
        if x[i,j].solution_value() == 1:
          print(f' {p[j]:3d} |', end='')
    print()