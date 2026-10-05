import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from optimizacion_2d import generar_optimizacion_2d
from optimizacion_3d import generar_optimizacion_3d
from link_selection import generar_link_selection
from copying_model import generar_copying_model
from kademlia_centralizado import kademlia

def analizar_y_graficar_red(G, titulo):
    """
    Calcula métricas clave y dibuja: 
    1) Distribución de Grados 
    2) Mapa de calor de Centralidad
    """
    N = G.number_of_nodes()
    M = G.number_of_edges()
    
    # Calcular Diámetro (solo en el componente más grande si está desconectada)
    if nx.is_connected(G):
        diametro = nx.diameter(G)
    else:
        componente_mayor = max(nx.connected_components(G), key=len)
        subgrafo = G.subgraph(componente_mayor)
        diametro = nx.diameter(subgrafo)
        
    print(f"--- Resultados para: {titulo} ---")
    print(f"Nodos (N): {N}")
    print(f"Enlaces (M): {M} (Esperado: ~{N*5})")
    print(f"Diámetro: {diametro}\n")
    
    # Calcular Grados y Centralidad
    grados = [d for n, d in G.degree()]
    centralidad = nx.degree_centrality(G)
    colores_nodos = list(centralidad.values())
    
    # Extraer posiciones (Si es 2D usa sus coordenadas, si no, usa un layout automático)
    if 'x' in G.nodes[0] and 'y' in G.nodes[0]:
        pos = {n: (datos['x'], datos['y']) for n, datos in G.nodes(data=True)}
    else:
        pos = nx.spring_layout(G, seed=42)
        
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle(titulo, fontsize=16, fontweight='bold')
    
    # Gráfica A: Distribución de Grados
    ax1.hist(grados, bins=20, color='skyblue', edgecolor='black')
    ax1.set_title("Distribución de Grados")
    ax1.set_xlabel("Grado (k)")
    ax1.set_ylabel("Frecuencia (Número de nodos)")
    ax1.grid(axis='y', alpha=0.7)
    
    # Gráfica B: Mapa de Calor de Centralidad
    nodos_dibujo = nx.draw_networkx_nodes(
        G, pos, ax=ax2, 
        node_size=50, 
        node_color=colores_nodos, 
        cmap=plt.cm.plasma, 
        edgecolors='black', linewidths=0.5
    )
    nx.draw_networkx_edges(G, pos, ax=ax2, alpha=0.1, edge_color='gray')
    ax2.set_title("Mapa de Calor (Centralidad de Grado)")
    ax2.axis('off')
    
    # Barra de color para el mapa de calor
    cbar = plt.colorbar(nodos_dibujo, ax=ax2)
    cbar.set_label('Importancia de Centralidad')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    tamanos_n = [100, 500, 1000]
    
    for n in tamanos_n:
        print(f" EXPERIMENTOS PARA N = {n} NODOS")
        
        # OPTIMIZACIÓN 2D (m=5)
        G_opt2d = generar_optimizacion_2d(n, delta=5.0, m=5)
        analizar_y_graficar_red(G_opt2d, f"Optimización 2D (N={n})")
        
        # OPTIMIZACIÓN 3D (m=5)
        G_opt3d = generar_optimizacion_3d(n, alpha=5.0, m=5)
        analizar_y_graficar_red(G_opt3d, f"Optimización 3D (N={n})")
        
        # LINK SELECTION (m=5)
        G_link = generar_link_selection(n, m=5)
        analizar_y_graficar_red(G_link, f"Link Selection (N={n})")
        
        # COPYING MODEL (m=5, p=0.5)
        G_copy = generar_copying_model(n, m=5, p=0.5)
        analizar_y_graficar_red(G_copy, f"Copying Model (N={n}, m=5, p=0.5)")
        
        # KADEMLIA
        # Determinamos 'k' dinámicamente para forzar M ≈ N*5
        k_dinamico = 2 if n == 100 else 1
        G_kad = kademlia(nx.Graph(), iteraciones=n, k=k_dinamico, bit_space=160)
        analizar_y_graficar_red(G_kad, f"Kademlia (N={n}, k={k_dinamico})") 