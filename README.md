venv-ia) ➜  ~ /home/andres/Documentos/venv-ia/bin/python /home/andres/Documentos/Punto2.py
Objetos ordenados por ratio valor/peso:
  A: peso=10, valor=60, ratio=6.00
  B: peso=20, valor=100, ratio=5.00
  C: peso=30, valor=120, ratio=4.00

Capacidad de la mochila: 50 kg

Proceso de selección:
  ✓ Tomado completo: A (peso: 10 kg, valor: 60)
  ✓ Tomado completo: B (peso: 20 kg, valor: 100)
  ✓ Tomado parcialmente: C (fracción: 0.67, peso: 20 kg, valor: 80.00)

==================================================
RESULTADO FINAL:
==================================================
Valor total obtenido: 240.0 monedas de oro
Peso total utilizado: 50 kg
Capacidad restante: 0 kg

Objetos seleccionados:
  A: completo - 10 kg - 60 monedas
  B: completo - 20 kg - 100 monedas
  C: 0.67 - 20 kg - 80.00 monedas

==================================================
INFORMACIÓN SOBRE ALGORITMOS VORACES:
==================================================
¿Cuándo es apropiado usar un algoritmo voraz?
- Cuando el problema tiene la propiedad de selección voraz (la elección local óptima conduce a una solución global óptima)
- Cuando el problema tiene estructura de subestructura óptima
- En problemas de optimización donde podemos tomar decisiones paso a paso
- Ejemplos: problema de la mochila fraccional, algoritmo de Dijkstra, algoritmo de Prim, algoritmo de Huffman

Limitaciones de los algoritmos voraces:
- No siempre encuentran la solución óptima global
- Solo funcionan bien para problemas específicos que cumplen ciertas propiedades
- Requieren una función de selección adecuada
- No reconsideran decisiones tomadas anteriormente
- Ejemplo: en la mochila 0-1 (no fraccional), el algoritmo voraz no garantiza la solución óptima
(venv-ia) ➜  ~ 
