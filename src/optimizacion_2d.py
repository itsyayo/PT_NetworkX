"""
optimizacion_2d.py
    Implementa el Modelo de Optimización en un espacio 2D
    Demuestra cómo la topología de Súper-Hubs puede surgir no por preferencia directa, 
    sino por un equilibrio (trade-off) entre minimizar el costo físico y 
    minimizar el costo topológico.
"""

import networkx as nx
import random
import math

def generar_optimizacion_2d(N, delta, m=5):
    G = nx.Graph()
    
    # Nodo raíz en el centro con distancia topológica 0
    G.add_node(0, x=0.5, y=0.5, h=0.0)
    
    for i in range(1, N):
        x_new, y_new = random.uniform(0, 1), random.uniform(0, 1)
        costos = []
        
        # Evaluar la función de costo para todos los nodos existentes
        for j in G.nodes():
            d_ij = math.sqrt((x_new - G.nodes[j]['x'])**2 + (y_new - G.nodes[j]['y'])**2)
            costo = (delta * d_ij) + G.nodes[j]['h']
            costos.append((costo, j))
            
        # Ordenar de menor a mayor costo
        costos.sort(key=lambda x: x[0])
        
        # Seleccionar los 'm' mejores candidatos
        mejores_objetivos = [nodo for costo, nodo in costos[:m]]
        
        G.add_node(i, x=x_new, y=y_new)
        
        for target in mejores_objetivos:
            G.add_edge(i, target)
            
        G.nodes[i]['h'] = float(nx.shortest_path_length(G, source=i, target=0))
        
    return G