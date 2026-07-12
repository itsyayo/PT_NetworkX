# Análisis y Generación de Redes Complejas: Mecanismos y Optimización

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![NetworkX](https://img.shields.io/badge/NetworkX-Graph_Analysis-lightgrey)](https://networkx.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Data_Viz-orange)](https://matplotlib.org/)

**Proyecto Terminal - Ingeniería en Computación** **Universidad Autónoma Metropolitana - Unidad Cuajimalpa (UAM-C)**

Este repositorio contiene la arquitectura de software y los modelos algorítmicos desarrollados para el estudio de **Redes Complejas y Sistemas Distribuidos**. El proyecto simula, analiza y visualiza cómo emergen las topologías libres de escala (*Scale-Free*) a partir de algoritmos descentralizados locales y modelos de optimización espacial.

---

## Descripción del Proyecto

En los sistemas distribuidos reales, no existe un controlador central que dicte la topología de la red. Este proyecto implementa mecanismos algorítmicos que demuestran cómo la **Conexión Preferencial** (el fenómeno donde "el rico se hace más rico") ocurre de forma orgánica mediante el comportamiento individual de los nodos.

Los modelos implementados se basan en la literatura clásica de Ciencia de Redes (A.-L. Barabási) y en el Modelo de Optimización de Fabrikant:
1. **Modelo de Optimización 2D y 3D:** Formación de Súper-Hubs mediante el *trade-off* entre el costo físico (distancia Euclidiana) y el beneficio topológico (saltos hacia el Gateway).
2. **Modelo de Copia (Copying Model):** Emulación de dinámicas sociales y de la WWW donde los nodos imitan las conexiones de sus vecinos.
3. **Selección de Enlaces (Link Selection):** Demostración analítica de cómo la elección aleatoria de aristas, en lugar de vértices, induce una centralidad de grado dominada por Hubs.

---

## Arquitectura del Repositorio

El código está estructurado bajo principios de Ingeniería de Software (modularidad, separación de configuraciones y pruebas unitarias):

```text
PT_NetworkX/
│
├── src/                          # Código fuente y lógica de algoritmos
│   ├── __init__.py
│   ├── optimizacion_2d.py        # Algoritmo de Fabrikant en 2 dimensiones
│   ├── optimizacion_3d.py        # Algoritmo de Fabrikant en 3 dimensiones
│   ├── copying_model.py          # Implementación del Copying Model
│   ├── link_selection.py         # Implementación de Link Selection
│   └── visualizacion.py          # Renderizado de mapas de calor y gráficas Log-Log
│
├── graficas/                     # Directorio de salida automatizada
│   └── (Archivos .gexf generados)
│
├── configuracion.py              # Variables y parámetros globales
├── experimentos.py               # Orquestador principal de simulaciones
└── README.md                     # Documentación del proyecto
