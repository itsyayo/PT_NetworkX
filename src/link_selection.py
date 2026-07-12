"""
link_selection.py
    Implementa el Algoritmo Link Selection
    Demuestra que elegir una arista al azar en lugar de un nodo al azar
    favorece matemáticamente a los Súper-Hubs, induciendo Conexión Preferencial.
"""

import networkx as nx
import random

def generar_link_selection(N, m):
    """
    Genera una red utilizando Link Selection
    
    Parámetros:
        N (int): Número total de nodos.
        m (int): Número de enlaces nuevos a establecer por cada nodo entrante.
        
    Retorna:
        G (nx.Graph): Grafo resultante.
    """
    # Triángulo cerrado
    G = nx.complete_graph(3)
    
    for i in range(len(G.nodes()), N):
        G.add_node(i)
        targets = set()
        
        while len(targets) < m:
            # Seleccionamos un ENLACE al azar en lugar de un nodo
            # Matemáticamente, los hubs están presentes en la mayoría de las aristas
            arista_aleatoria = random.choice(list(G.edges()))
            
            # Seleccionamos aleatoriamente uno de los dos extremos de la arista
            nodo_destino = random.choice(arista_aleatoria)
            
            if nodo_destino != i:
                targets.add(nodo_destino)
                
        # Efectuar las conexiones
        for target in targets:
            G.add_edge(i, target)
            
    return G