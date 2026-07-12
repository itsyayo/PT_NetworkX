"""
  configuracion.py
    Archivo de configuración global del proyecto.
    Centraliza todos los parámetros y variables estáticas utilizadas en la 
    generación de los diferentes modelos.
"""

CONFIG = {
    # --- Parámetros Generales ---
    "N_NODOS": 500,               # Cantidad total de nodos que tendrá cada red generada.
    "M_ENLACES": 2,               # Cantidad de enlaces nuevos que cada nodo intenta formar al unirse.
    "CARPETA_SALIDA": "graficas", # Nombre del directorio donde se exportarán los archivos .gexf.
    
    # --- Parámetros para los Modelos de Optimización ---
    "DELTA_2D": 5.0,              # Peso de la penalización en 2D. 
    "ALPHA_3D": 1.5,              # Peso de la penalización en 3D.
    
    # --- Parámetros para Copying Model ---
    "PROB_COPY": 0.5              # Probabilidad 'p' (0 a 1). 
                                  # Define si un nodo se conecta al azar (p) o si "copia" a un vecino (1-p).
}