import random

# Lista de prefijos y sufijos realistas para nombres
prefijos = ['Ana', 'Emilia', 'Lucía', 'Carla', 'María', 'Sofía', 'Isabella', 'Alicia', 'Catalina', 'Valentina', 'Gabriela', 'Clara', 'Elena', 'Rosa', 'Olivia', 'Camila', 'Marta', 'Paula', 'Adriana', 'Amelia', 'Fátima', 'Gloria', 'Irene', 'Julia', 'Lorena', 'Nuria', 'Paloma', 'Rita', 'Sara', 'Teresa', 'Victoria']
sufijos = ['Álvarez', 'González', 'López', 'Pérez', 'Martínez', 'García', 'Fernández', 'Rodríguez', 'Sánchez', 'Ruiz', 'Romero', 'Ramírez', 'Álvarez', 'Torres', 'Flores', 'Molina', 'Ortega', 'Rubio', 'Gómez', 'Ortiz', 'Vega', 'Castillo', 'Navarro', 'Cortés', 'Reyes', 'Herrera', 'Medina', 'León', 'Ramos', 'Silva', 'Méndez']

# Función para generar una matriz de nombres y saldos aleatorios
def generar_matriz(n):
    # Crea una lista vacía para almacenar los nombres y saldos
    matriz = []
    
    # Genera n nombres aleatorios con saldos aleatorios y los añade a la matriz
    for i in range(n):
        nombre = random.choice(prefijos) + ' ' + random.choice(sufijos)
        saldo = round(random.uniform(10, 100000),10)
        matriz.append({'Nombre': nombre, 'Saldo': saldo})
    
    return matriz

# Genera una matriz de 10 nombres aleatorios con saldos aleatorios e imprime la matriz
matriz = generar_matriz(10)
for fila in matriz:
    print(fila)
