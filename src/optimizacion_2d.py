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

def generar_optimizacion_2d(N, delta):
    """
    Genera una red bajo el modelo de optimización geométrica en 2 dimensiones
    
    Parámetros:
        N (int): Número total de nodos a generar en la red.
        delta (float): Parámetro de penalización topológica. Define qué tanto le importa
                       al nuevo nodo estar a pocos saltos del nodo raíz.
                       
    Retorna:
        G (nx.Graph): El grafo resultante con atributos espaciales (x, y) y topológicos (h).
    """
    G = nx.Graph()
    
    # Se inicializa el nodo raíz en el centro del plano (0.5, 0.5)
    # Su distancia topológica (h) es 0 por definición.
    G.add_node(0, x=0.5, y=0.5, h=0.0)
    
    for i in range(1, N):
        # Asignación de coordenadas espaciales aleatorias en un cuadrado unitario [0,1]
        x_new, y_new = random.uniform(0, 1), random.uniform(0, 1)
        
        mejor_objetivo = None
        menor_costo = float('inf')
        
        # Evaluación de la función de costo para todos los nodos existentes
        for j in G.nodes():
            # Costo físico: Distancia Euclidiana
            d_ij = math.sqrt((x_new - G.nodes[j]['x'])**2 + (y_new - G.nodes[j]['y'])**2)
            
            # Costo total = Distancia Euclidiana + (delta * Distancia Topológica del candidato)
            costo = (delta * d_ij) + (G.nodes[j]['h'])
            
            if costo < menor_costo:
                menor_costo = costo
                mejor_objetivo = j
                
        # Integración del nodo a la red conectándolo al objetivo más "barato"
        G.add_node(i, x=x_new, y=y_new)
        G.add_edge(i, mejor_objetivo)
        
        # Actualización de la distancia geodesica
        h_new = nx.shortest_path_length(G, source=i, target=0)
        G.nodes[i]['h'] = float(h_new)
        
    return G