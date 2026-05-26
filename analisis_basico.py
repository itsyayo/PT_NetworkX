import networkx as nx
import matplotlib.pyplot as plt

def main():
    # Instanciar un grafo simple (no dirigido)
    G = nx.Graph()

    # Agregar las aristas
    aristas = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C')]
    G.add_edges_from(aristas)

    # Calcular el grado de cada nodo
    grados = dict(G.degree())
    
    # La cercanía se calcula como el recíproco de la suma de las distancias más cortas desde un nodo a todos los demás nodos
    cercania = nx.closeness_centrality(G)
    
    # La intermediación se calcula como la cantidad de veces que un nodo actúa como puente a lo largo del camino más corto entre otros dos nodos
    intermediacion = nx.betweenness_centrality(G, normalized=False) 
    
    # Calculamos el coeficiente de agrupamiento para cada nodo
    agrupamiento = nx.clustering(G)

    # Imprimir en consola
    print("REPORTE DEL GRAFO")
    for nodo in G.nodes():
        print(f"\nNodo {nodo}:")
        print(f"  - Grado (k): {grados[nodo]}")
        print(f"  - Centralidad de Cercanía: {cercania[nodo]:.2f}")
        print(f"  - Centralidad de Intermediación: {intermediacion[nodo]:.2f}")
        print(f"  - Coef. de Agrupamiento: {agrupamiento[nodo]:.2f}")

    # Visualizar la red
    plt.figure(figsize=(6, 4))
    # spring_layout acomoda los nodos de forma estética
    posiciones = nx.spring_layout(G, seed=42) 
    
    nx.draw(G, posiciones, with_labels=True, node_color='lightcoral', 
            node_size=2000, font_size=14, font_weight='bold', edge_color='gray')
    
    plt.title("Análisis de Red - PT Eduardo")
    plt.show()

if __name__ == "__main__":
    main()