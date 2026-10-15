"""
kademlia_centralizado.py
    Implementación centralizada de la Tabla Hash Distribuida (DHT) de Kademlia.
    Simula la creación de una topología P2P basada en la métrica de distancia XOR.
    Los enlaces del grafo representan la pertenencia a los k-buckets de cada nodo.
"""

import networkx as nx
import random
import math

def calcular_distancia_xor(id1, id2):
    """Calcula la distancia lógica entre dos nodos usando la métrica XOR"""
    return id1 ^ id2

def obtener_indice_bucket(distancia):
    """
    Determina a qué k-bucket pertenece un contacto basado en la distancia XOR
    El índice corresponde a la posición del bit más significativo
    """
    if distancia == 0:
        return 0
    return int(math.log2(distancia))

def kademlia(G_inicial, iteraciones, k=20, bit_space=160):
    """
    Simula el crecimiento de una red Kademlia de forma centralizada
    
    Parámetros:
        G_inicial (nx.Graph): Grafo de partida
        iteraciones (int): Cantidad de nodos nuevos a agregar
        k (int): Tamaño máximo de cada k-bucket 
        bit_space (int): Espacio de direcciones de los identificadores
        
    Retorna:
        G (nx.Graph): Red final donde las aristas indican que 
                        un nodo conoce a otro
    """
    G = nx.Graph(G_inicial)
    
    # Función auxiliar para agregar contactos
    def agregar_contacto(nodo_origen, nodo_destino):
        if nodo_origen == nodo_destino:
            return
            
        distancia = calcular_distancia_xor(G.nodes[nodo_origen]['id'], G.nodes[nodo_destino]['id'])
        idx_bucket = obtener_indice_bucket(distancia)
        
        # Si el bucket no existe en el diccionario del nodo, lo creamos
        if idx_bucket not in G.nodes[nodo_origen]['k_buckets']:
            G.nodes[nodo_origen]['k_buckets'][idx_bucket] = []
            
        bucket = G.nodes[nodo_origen]['k_buckets'][idx_bucket]
        
        # Si el destino no está en el bucket y hay espacio, lo agregamos
        if nodo_destino not in bucket:
            if len(bucket) < k:
                bucket.append(nodo_destino)
                # Agregamos el enlace al grafo
                G.add_edge(nodo_origen, nodo_destino)
            else:
                # Si el bucket está lleno, en el protocolo real se hace un PING al más viejo
                # Al ser una simulación centralizada, simplemente lo ignoramos
                pass

    # Determinar el ID numérico para el siguiente nodo a insertar
    id_contador = max(G.nodes()) + 1 if len(G.nodes()) > 0 else 0
    
    for _ in range(iteraciones):
        nuevo_nodo = id_contador
        
        # Generar un Identificador Kademlia aleatorio
        id_kademlia = random.getrandbits(bit_space)
        # print(f"Agregando nodo {nuevo_nodo} con ID: {id_kademlia}")
        
        # Evitar colisiones de ID
        while any(datos.get('id') == id_kademlia for n, datos in G.nodes(data=True)):
            id_kademlia = random.getrandbits(bit_space)
            
        # Agregar el nodo al grafo con sus atributos iniciales
        G.add_node(nuevo_nodo, id=id_kademlia, k_buckets={})
        
        if len(G.nodes()) > 1:
            # Conectarse a un nodo existente
            nodos_existentes = [n for n in G.nodes() if n != nuevo_nodo]
            nodo_bootstrap = random.choice(nodos_existentes)
            
            # Se conocen mutuamente
            agregar_contacto(nuevo_nodo, nodo_bootstrap)
            agregar_contacto(nodo_bootstrap, nuevo_nodo)
            
            # Llenar los k-buckets
            # Ordenamos todos los nodos de la red según su distancia XOR al nodo nuevo
            # (En el protocolo real, esto se hace iterativamente con FIND_NODE)
            nodos_existentes.sort(key=lambda x: calcular_distancia_xor(id_kademlia, G.nodes[x]['id']))
            
            for nodo_v in nodos_existentes:
                agregar_contacto(nuevo_nodo, nodo_v)
                # Kademlia fomenta la simetría: el nodo consultado también intenta guardarnos
                agregar_contacto(nodo_v, nuevo_nodo) 
                
        id_contador += 1
        
    return G

if __name__ == "__main__":
    
    # Red inicial vacía
    G_ini = nx.Graph()
    
    # Ejecutar 150 iteraciones con buckets de tamaño k=5
    # G_final = kademlia(G_ini, iteraciones=150, k=5, bit_space=160)
    
    # Ejecutar 25 iteraciones con buckets de tamaño k=2
    G_final = kademlia(G_ini, iteraciones=500, k=1, bit_space=160)
    
    print(f"Red Kademlia generada.")
    print(f"Nodos totales: {G_final.number_of_nodes()}")
    print(f"Enlaces totales (contactos en buckets): {G_final.number_of_edges()}")
    
    import os
    os.makedirs("graficas", exist_ok=True)
    nx.write_gexf(G_final, "graficas/kad5.gexf")