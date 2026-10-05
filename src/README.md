# Simulación Centralizada de Kademlia (Métrica XOR)

Este módulo contiene la implementación algorítmica de la Tabla Hash Distribuida (DHT) de Kademlia, adaptada para su análisis topológico desde una perspectiva global y centralizada. 

En lugar de intercambiar paquetes de red físicos iterativos (`FIND_NODE`), el algoritmo calcula distancias lógicas ($A \oplus B$) basándose en un oráculo central para emular el llenado progresivo de los $k$-buckets conforme la red escala.

**Topología:** La estructura se modela como un **Grafo No Dirigido** (`nx.Graph`). Esto representa las conexiones como relaciones de visibilidad mutua y simplifica el renderizado de la red, facilitando el análisis estructural de la topología sin la saturación visual de aristas direccionales.

## Estructura del Archivo
- `kademlia_centralizado.py`: Núcleo de la simulación. Asigna de forma autónoma los IDs criptográficos a los nodos y utiliza la métrica XOR para determinar a qué cubeta lógica pertenece cada contacto, estableciendo las aristas correspondientes.

## Uso y Ejecución
Para ejecutar la simulación y generar la topología en formato GEXF, simplemente corre el script desde la terminal:

```bash
python kademlia_centralizado.py
```

El script creará automáticamente un directorio llamado graficas/ (si no existe) y exportará el grafo resultante ahí (por ejemplo, graficas/kad5.gexf). Este archivo puede ser importado directamente a Gephi para su análisis espacial y visualización.

## Parámetros Ajustables
Dentro del bloque de ejecución del script, puedes modificar los siguientes parámetros pasados a la función kademlia():
- iteraciones: Número de nodos a agregar a la red (por ejemplo, 30 o 150).
- k: Capacidad máxima de contactos por cada $k$-bucket. Se sugiere $k=20$ para emular redes reales, o $k \le 5$ para producir visualizaciones de alta claridad.
- bit_space: El límite del espacio de direcciones. Su valor por defecto es 160 (para simular el estándar SHA-1 de Kademlia), pero puede reducirse para experimentos microscópicos.