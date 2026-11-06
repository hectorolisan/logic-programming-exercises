# Logic Programming Exercises

- 335 Python programming and logic exercises, solved and explained in Spanish
- Organized by topic and ordered from easiest to hardest
- Each exercise shows the statement followed by its solution, with outputs already rendered
- Covers language fundamentals plus classic algorithms: searching, sorting, arrays, graphs and dynamic programming
- Interactive Jupyter Notebook workflow, standard library only (plus `matplotlib` for a few plots)

## Requirements

- Python 3.10 or newer
- `pip` (Python package manager)

## Installation

1. Clone the repository or download the project files.

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

```bash
source .venv/bin/activate     # Linux/macOS
.venv\Scripts\activate        # Windows
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

```
logic-programming-exercises/
├── public/                          # Static assets
├── src/
│   ├── 01-tipos-datos-simples/      # Variables, operators, input/output
│   ├── 02-cadenas/                  # Strings
│   ├── 03-condicionales/            # if / elif / else
│   ├── 04-bucles/                   # for / while
│   ├── 05-listas-tuplas-conjuntos/  # Lists, tuples, sets, matrices
│   ├── 06-diccionarios/             # Dictionaries
│   ├── 07-funciones/                # Functions and applications (finance, simulations)
│   ├── 08-programacion-funcional/   # map, filter, reduce, comprehensions, async
│   ├── 09-recursividad/             # Recursion
│   ├── 10-modulos-estandar/         # random, datetime, re
│   ├── 11-ficheros/                 # Text, CSV, JSON, SQLite, internet files
│   ├── 12-clases-objetos/           # Classes and objects
│   ├── 13-algoritmos-basicos/       # Euclid, Union-Find, Huffman
│   ├── 14-busqueda/                 # Linear, binary, DFS, BFS
│   ├── 15-ordenacion/               # Bubble, selection, insertion, counting, merge, quick, heap
│   ├── 16-arrays/                   # Boyer-Moore, missing numbers, Kadane, Floyd, Quick Select, KMP
│   ├── 17-grafos/                   # Flood fill, Lee, topological sort, Dijkstra, Bellman-Ford, Floyd-Warshall, Kruskal
│   └── 18-programacion-dinamica/    # Subset sum, 0/1 knapsack
├── requirements.txt                 # Project dependencies
├── .gitignore
└── README.md
```

Topic folders hold one or more notebooks numbered by difficulty (`01-basico`, `02-intermedio`, `03-avanzado`…). Algorithm folders hold one notebook per algorithm, also ordered by difficulty.

### Dependencies

- `ipykernel`: Runs the notebooks with the virtual environment
- `matplotlib`: Plots in the finance and simulation exercises

## Usage

1. Open any notebook in VS Code or Jupyter:

```bash
jupyter notebook src/01-tipos-datos-simples/01-basico.ipynb
```

2. Run the cells sequentially. Some exercises ask for keyboard input with `input()`, and some download data files from the internet (they are saved next to the notebook and ignored by Git).

## Sources

The statements are adapted and translated from:

- [Ejercicios de Programación con Python](https://aprendeconalf.es/docencia/python/ejercicios/), Alfredo Sánchez Alberca (CC BY-NC-SA 3.0 ES)
- *Introducción a la Programación con Python*, Andrés Marzal and Isabel Gracia (selection of its exercises)
- [Top 50 Ejemplos y Ejercicios](https://ellibrodepython.com/ejemplos-ejercicios-python), El Libro De Python (only exercises solvable with the standard library)
- [30 Days Of Python](https://github.com/Asabeneh/30-Days-Of-Python), Asabeneh Yetayeh
- Classic algorithms list (arrays, basics, searching, sorting and graphs)

All solutions are original.
