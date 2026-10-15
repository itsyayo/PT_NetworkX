import networkx as nx

from optimizacion_2d import generar_optimizacion_2d
from optimizacion_3d import generar_optimizacion_3d

def ejecutar_emulacion():
    tamanos = [
        {'n': 100, 'm': 7},
        {'n': 500, 'm': 5},
        {'n': 1000, 'm': 5}
    ]
    deltas = [10.0, 100.0, 1000.0]
    
    import os
    os.makedirs("graficas_emulacion", exist_ok=True)
    
    for config in tamanos:
        n = config['n']
        m = config['m']
        
        for delta in deltas:
            print(f"Generando Optimización 2D y 3D con delta/alpha = {delta}...")
            
            # Generar 2D
            G_2d = generar_optimizacion_2d(n, delta=delta, m=m)
            nx.write_gexf(G_2d, f"graficas_emulacion/Opt2D_N{n}_m{m}_delta{int(delta)}.gexf")
            
            # Generar 3D
            G_3d = generar_optimizacion_3d(n, alpha=delta, m=m)
            nx.write_gexf(G_3d, f"graficas_emulacion/Opt3D_N{n}_m{m}_alpha{int(delta)}.gexf")
            
    print("\nRedes generadas")

if __name__ == "__main__":
    ejecutar_emulacion()