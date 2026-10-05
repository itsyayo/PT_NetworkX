"""
link_selection.py
    Implementa el Algoritmo Link Selection
    Demuestra que elegir una arista al azar en lugar de un nodo al azar
    favorece matemáticamente a los Súper-Hubs, induciendo Conexión Preferencial.
"""

import networkx as nx
import random

def generar_link_selection(N, m=5):
    # Se inicia con un grafo completo de m+1 nodos
    G = nx.complete_graph(m + 1) 
    
    for i in range(m + 1, N):
        G.add_node(i)
        targets = set()
        
        lista_aristas = list(G.edges())
        
        # Prevenir colapsos si por algún motivo la red inicial se vació
        if not lista_aristas:
            continue
            
        while len(targets) < m:
            arista_aleatoria = random.choice(lista_aristas)
            nodo_destino = random.choice(arista_aleatoria)
            
            if nodo_destino != i:
                targets.add(nodo_destino)
                
        # Efectuar las conexiones
        for target in targets:
            G.add_edge(i, target)
            
    return G