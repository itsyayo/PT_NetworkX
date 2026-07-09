import networkx as nx
import random
import math

def generar_optimizacion(N, delta):
    G = nx.Graph()
    # Nodo raíz 
    G.add_node(0, x=0.5, y=0.5, h=0)
    
    for i in range(1, N):
        x_new, y_new = random.uniform(0, 1), random.uniform(0, 1)
        
        mejor_objetivo = None
        menor_costo = float('inf')
        
        for j in G.nodes():
            d_ij = math.sqrt((x_new - G.nodes[j]['x'])**2 + (y_new - G.nodes[j]['y'])**2)
            costo = d_ij + (delta * G.nodes[j]['h'])
            
            if costo < menor_costo:
                menor_costo = costo
                mejor_objetivo = j
                
        G.add_node(i, x=x_new, y=y_new)
        G.add_edge(i, mejor_objetivo)
        
        h_new = nx.shortest_path_length(G, source=i, target=0)
        G.nodes[i]['h'] = h_new
        
    return G

N_nodos = 500

# Caso Estrella (delta pequeño)
G_star = generar_optimizacion(N_nodos, delta=0.2)
nx.write_gexf(G_star, "optimizacion_estrella.gexf")
G_star_hist = generar_optimizacion(N_nodos, delta=0.2)

print("Histograma de grados para el caso Estrella:", nx.degree_histogram(G_star_hist))

# Caso Scale-Free (delta intermedio)
G_sf = generar_optimizacion(N_nodos, delta=5.0)
nx.write_gexf(G_sf, "optimizacion_scalefree.gexf")

# Caso Aleatorio (delta grande)
G_random = generar_optimizacion(N_nodos, delta=30.0)
nx.write_gexf(G_random, "optimizacion_aleatoria.gexf")
