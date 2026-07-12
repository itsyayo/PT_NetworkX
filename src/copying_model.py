"""
copying_model.py
    Implementa el Algoritmo Copying Model
    Este modelo explica el surgimiento de la Conexión Preferencial de forma "ciega",
    donde los nodos no conocen la red global, sino que imitan las conexiones de otros.
"""

import networkx as nx
import random

def generar_copying_model(N, m, p):
    """
    Genera una red utilizando Copying Model
    
    Parámetros:
        N (int): Número total de nodos.
        m (int): Número de enlaces que el nuevo nodo intentará establecer.
        p (float): Probabilidad de establecer una conexión aleatoria pura.
                   (1-p) será la probabilidad de copiar a los amigos del nodo objetivo.
                   
    Retorna:
        G (nx.Graph): Grafo resultante.
    """
    # Se inicializa una red completamente conectada para tener vecinos base
    G = nx.complete_graph(max(3, m + 1))
    
    for i in range(len(G.nodes()), N):
        G.add_node(i)
        targets = set()
        
        while len(targets) < m:
            # Seleccionar un nodo 'u' de la red de forma equiprobable
            u = random.choice(list(G.nodes()))
            if u == i: 
                continue
                
            if random.random() < p:
                # Evento A: Conexión directa aleatoria
                targets.add(u)
            else:
                # Evento B: Conexión por Copia (Se elige al azar un vecino de 'u')
                vecinos = list(G.neighbors(u))
                if vecinos:
                    v = random.choice(vecinos)
                    if v != i:
                        targets.add(v)
                        
        # Efectuar las conexiones seleccionadas
        for target in targets:
            G.add_edge(i, target)
            
    return G