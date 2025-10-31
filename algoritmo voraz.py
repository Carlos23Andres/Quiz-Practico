class Objeto:
    def __init__(self, nombre, peso, valor):
        self.nombre = nombre
        self.peso = peso
        self.valor = valor
        self.ratio = valor / peso  # Valor por unidad de peso
    
    def __repr__(self):
        return f"{self.nombre}: peso={self.peso}, valor={self.valor}, ratio={self.ratio:.2f}"

def mochila_fraccional(objetos, capacidad):
    # Ordenar objetos por ratio valor/peso de forma descendente
    objetos_ordenados = sorted(objetos, key=lambda x: x.ratio, reverse=True)
    
    peso_actual = 0
    valor_total = 0
    seleccion = []
    
    print("Objetos ordenados por ratio valor/peso:")
    for obj in objetos_ordenados:
        print(f"  {obj}")
    
    print(f"\nCapacidad de la mochila: {capacidad} kg")
    print("\nProceso de selección:")
    
    for obj in objetos_ordenados:
        if peso_actual + obj.peso <= capacidad:
            # Tomar el objeto completo
            seleccion.append((obj.nombre, 1.0, obj.peso, obj.valor))
            peso_actual += obj.peso
            valor_total += obj.valor
            print(f"  ✓ Tomado completo: {obj.nombre} (peso: {obj.peso} kg, valor: {obj.valor})")
        else:
            # Tomar fracción del objeto
            peso_restante = capacidad - peso_actual
            fraccion = peso_restante / obj.peso
            valor_fraccion = obj.valor * fraccion
            seleccion.append((obj.nombre, fraccion, peso_restante, valor_fraccion))
            valor_total += valor_fraccion
            peso_actual = capacidad
            print(f"  ✓ Tomado parcialmente: {obj.nombre} (fracción: {fraccion:.2f}, peso: {peso_restante} kg, valor: {valor_fraccion:.2f})")
            break  # La mochila está llena
    
    return seleccion, valor_total, peso_actual

# Datos del problema
objetos = [
    Objeto("A", 10, 60),
    Objeto("B", 20, 100),
    Objeto("C", 30, 120)
]

capacidad_maxima = 50

# Resolver el problema
seleccion, valor_total, peso_total = mochila_fraccional(objetos, capacidad_maxima)

# Mostrar resultados
print("\n" + "="*50)
print("RESULTADO FINAL:")
print("="*50)
print(f"Valor total obtenido: {valor_total} monedas de oro")
print(f"Peso total utilizado: {peso_total} kg")
print(f"Capacidad restante: {capacidad_maxima - peso_total} kg")
print("\nObjetos seleccionados:")
for nombre, fraccion, peso, valor in seleccion:
    if fraccion == 1.0:
        print(f"  {nombre}: completo - {peso} kg - {valor} monedas")
    else:
        print(f"  {nombre}: {fraccion:.2f} - {peso} kg - {valor:.2f} monedas")

# Información adicional sobre el algoritmo voraz
print("\n" + "="*50)
print("INFORMACIÓN SOBRE ALGORITMOS VORACES:")
print("="*50)
print("¿Cuándo es apropiado usar un algoritmo voraz?")
print("- Cuando el problema tiene la propiedad de selección voraz (la elección local óptima conduce a una solución global óptima)")
print("- Cuando el problema tiene estructura de subestructura óptima")
print("- En problemas de optimización donde podemos tomar decisiones paso a paso")
print("- Ejemplos: problema de la mochila fraccional, algoritmo de Dijkstra, algoritmo de Prim, algoritmo de Huffman")

print("\nLimitaciones de los algoritmos voraces:")
print("- No siempre encuentran la solución óptima global")
print("- Solo funcionan bien para problemas específicos que cumplen ciertas propiedades")
print("- Requieren una función de selección adecuada")
print("- No reconsideran decisiones tomadas anteriormente")
print("- Ejemplo: en la mochila 0-1 (no fraccional), el algoritmo voraz no garantiza la solución óptima")
