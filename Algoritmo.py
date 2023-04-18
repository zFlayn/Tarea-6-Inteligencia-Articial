import random
import time
import math

def generate_random_instance(n, max_cost):
    # Genera una instancia aleatoria del problema de ruta más corta con n nodos y costos máximos de max_cost
    # Retorna una matriz de adyacencia de tamaño n x n
    return [[random.randint(1, max_cost) if i != j else 0 for j in range(n)] for i in range(n)]

def simulated_annealing(cost_matrix, initial_temperature, final_temperature, cooling_rate):
    # Implementación de Recocido Simulado para el problema de ruta más corta
    # Retorna una lista con el mejor camino encontrado y su costo
    
    # Función para calcular el costo de un camino
    def cost(path):
        return sum([cost_matrix[path[i]][path[i+1]] for i in range(len(path)-1)])
    
    n = len(cost_matrix)
    current_solution = list(range(n))
    best_solution = current_solution.copy()
    temperature = initial_temperature
    
    while temperature > final_temperature:
        # Generar una nueva solución vecina de la solución actual
        i, j = random.sample(range(n), 2)
        new_solution = current_solution.copy()
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        
        # Calcular la diferencia de costo entre la solución vecina y la solución actual
        delta = cost(new_solution) - cost(current_solution)
        
        # Si la solución vecina es mejor que la solución actual, aceptar la solución vecina como la nueva solución actual
        if delta < 0:
            current_solution = new_solution
            
            # Si la nueva solución es mejor que la mejor solución encontrada hasta el momento, actualizar la mejor solución
            if cost(current_solution) < cost(best_solution):
                best_solution = current_solution.copy()
        # Si la solución vecina es peor que la solución actual, aceptar la solución vecina como la nueva solución actual con una cierta probabilidad
        else:
            p = random.uniform(0, 1)
            if p < math.exp(-delta/temperature):
                current_solution = new_solution
        
        # Disminuir la temperatura
        temperature *= cooling_rate
    
    return best_solution, cost(best_solution)

# Ejemplo de uso
n = 10
max_cost = 100
cost_matrix = generate_random_instance(n, max_cost)

initial_temperature = 100
final_temperature = 0.1
cooling_rate = 0.99

start_time = time.time()
best_path, best_cost = simulated_annealing(cost_matrix, initial_temperature, final_temperature, cooling_rate)
end_time = time.time()

print(f"Mejor camino encontrado: {best_path}")
print(f"Costo del mejor camino encontrado: {best_cost}")
print(f"Tiempo de compilación: {end_time - start_time} segundos")
