"""
optimizacion_3d
    Implementa el Modelo de Optimización tridimensional (3D).
    Calcula el costo evaluando la distancia Euclidiana en 3 ejes (x, y, z) 
    y la distancia geodesica hacia el nodo raíz.
"""

import networkx as nx
import random
import math

def generar_optimizacion_3d(N, alpha, m=2):
    """
    Genera una red bajo el modelo de optimización geométrica en 3 dimensiones
    
    Parámetros:
        N (int): Número total de nodos a generar en la red
        alpha (float): Parámetro de penalización topológica (peso de los saltos)
        m (int): Número de enlaces que cada nuevo nodo intentará formar
                       
    Retorna:
        G (nx.Graph): Grafo resultante con atributos espaciales (x, y, z) y topológicos (h)
    """
    G = nx.Graph()
    
    # Nodo raíz en el centro (0.5, 0.5, 0.5)
    G.add_node(0, x=0.5, y=0.5, z=0.5, h=0.0)
    
    for i in range(1, N):
        # Generar coordenadas aleatorias en 3D
        x_new = random.uniform(0, 1)
        y_new = random.uniform(0, 1)
        z_new = random.uniform(0, 1)
        
        costos = []
        
        # Evaluación de la función de costo para todos los nodos existentes
        for j in G.nodes():
            # Costo físico: Distancia Euclidiana en 3D
            d_ij = math.sqrt((x_new - G.nodes[j]['x'])**2 + 
                             (y_new - G.nodes[j]['y'])**2 + 
                             (z_new - G.nodes[j]['z'])**2)
            
            # Costo total = Distancia física 3D + (alpha * Distancia Geodésica)
            costo = d_ij + (alpha * G.nodes[j]['h'])
            costos.append((costo, j))
            
        # Ordenar los nodos de menor a mayor costo y tomar los 'm' mejores
        costos.sort(key=lambda item: item[0])
        mejores_objetivos = [nodo for costo, nodo in costos[:m]]
        
        # Integrar el nodo a la red
        G.add_node(i, x=x_new, y=y_new, z=z_new)
        
        for objetivo in mejores_objetivos:
            G.add_edge(i, objetivo)
            
        # Actualizar la distancia geodésica 
        h_new = nx.shortest_path_length(G, source=i, target=0)
        G.nodes[i]['h'] = float(h_new)
        
    return G