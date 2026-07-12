"""
experimentos.py
    Lee los parámetros desde configuracion.py, invoca de manera secuencial 
    los algoritmos generadores de redes topológicas y exporta los grafos a formato GEXF
"""

import os
import networkx as nx

from configuracion import CONFIG

from src.optimizacion_2d import generar_optimizacion_2d
from src.optimizacion_3d import generar_optimizacion_3d
from src.copying_model import generar_copying_model
from src.link_selection import generar_link_selection

def automatizar_experimentos():    
    out_dir = CONFIG["CARPETA_SALIDA"]
    os.makedirs(out_dir, exist_ok=True)
    
    N = CONFIG["N_NODOS"]
    M = CONFIG["M_ENLACES"]
    
    # Optimización 2D
    print(f"\nGenerando Modelo de Optimización 2D (N={N})...")
    G_opt2d = generar_optimizacion_2d(N, delta=CONFIG["DELTA_2D"])
    nx.write_gexf(G_opt2d, f"{out_dir}/1_optimizacion_2d.gexf")
    print(f"   [OK] Guardado en {out_dir}/1_optimizacion_2d.gexf")
    
    # Optimización 3D
    print(f"\nGenerando Modelo de Optimización 3D (N={N})...")
    G_opt3d = generar_optimizacion_3d(N, alpha=CONFIG["ALPHA_3D"], m=M)
    nx.write_gexf(G_opt3d, f"{out_dir}/2_optimizacion_3d.gexf")
    print(f"   [OK] Guardado en {out_dir}/2_optimizacion_3d.gexf")
    
    # Copying Model
    print(f"\nGenerando Copying Model (N={N}, p={CONFIG['PROB_COPY']})...")
    G_copy = generar_copying_model(N, m=M, p=CONFIG["PROB_COPY"])
    nx.write_gexf(G_copy, f"{out_dir}/3_copying_model.gexf")
    print(f"   [OK] Guardado en {out_dir}/3_copying_model.gexf")
    
    # Link Selection
    print(f"\nGenerando Link Selection Model (N={N})...")
    G_link = generar_link_selection(N, m=M)
    nx.write_gexf(G_link, f"{out_dir}/4_link_selection.gexf")
    print(f"   [OK] Guardado en {out_dir}/4_link_selection.gexf")
    

if __name__ == "__main__":
    automatizar_experimentos()