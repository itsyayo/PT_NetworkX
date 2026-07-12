"""
visualizacion.py
    Provee herramientas analíticas y gráficas para inspeccionar la topología generada.
    Incluye funciones para mapear la distribución de grados en escala logarítmica
    y renderizar grafos espaciales usando mapas de calor.
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def analizar_y_graficar_red(G):
    """
    Genera una interfaz visual con dos subgráficos analíticos:
    1. Gráfica Log-Log de la distribución de grados
    2. Renderizado espacial de la red con mapa de calor según la centralidad de grado
    
    Parámetros:
        G (nx.Graph): Grafo con atributos 'x' e 'y' en sus nodos.
    """
    fig, axs = plt.subplots(1, 2, figsize=(16, 7))
    
    # Distribución Log-Log
    grados = [grado for nodo, grado in G.degree()]
    grados_unicos, counts = np.unique(grados, return_counts=True)
    
    axs[0].loglog(grados_unicos, counts, 'bo', markersize=7, alpha=0.7, markeredgecolor='black')
    axs[0].set_title("Distribución de Grados (P(k))", fontsize=16, fontweight='bold')
    axs[0].set_xlabel("Grado (k) - Escala Logarítmica", fontsize=12)
    axs[0].set_ylabel("Frecuencia - Escala Logarítmica", fontsize=12)
    axs[0].grid(True, which="both", ls="--", alpha=0.5)
    
    # Mapa de Calor
    # Verificación de existencia de coordenadas
    if all('x' in G.nodes[n] and 'y' in G.nodes[n] for n in G.nodes()):
        posiciones = {n: (data['x'], data['y']) for n, data in G.nodes(data=True)}
    else:
        # Fallback a Spring Layout si la red no es geométrica
        posiciones = nx.spring_layout(G, seed=42)
    
    nx.draw_networkx_edges(G, posiciones, ax=axs[1], alpha=0.15, edge_color='gray')
    
    nodos_plot = nx.draw_networkx_nodes(G, posiciones, ax=axs[1], 
                                        node_size=60, 
                                        node_color=grados, 
                                        cmap=plt.cm.plasma,
                                        alpha=0.9,
                                        edgecolors='black', linewidths=0.5)
    
    cbar = plt.colorbar(nodos_plot, ax=axs[1], shrink=0.8)
    cbar.set_label('Centralidad de Grado (Número de enlaces)', fontsize=12)
    
    axs[1].set_title("Topología de la Red", fontsize=16, fontweight='bold')
    axs[1].axis('off')
    
    plt.tight_layout()
    plt.show()