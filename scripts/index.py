"""Genera INDEX.md con todos los notebooks: tema, dificultad, número de ejercicios y enlace."""

import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SRC = RAIZ / "src"

TEMAS = {
    "01-tipos-datos-simples": "Tipos de datos simples",
    "02-cadenas": "Cadenas",
    "03-condicionales": "Condicionales",
    "04-bucles": "Bucles",
    "05-listas-tuplas-conjuntos": "Listas, tuplas y conjuntos",
    "06-diccionarios": "Diccionarios",
    "07-funciones": "Funciones",
    "08-programacion-funcional": "Programación funcional",
    "09-recursividad": "Recursividad",
    "10-modulos-estandar": "Módulos estándar",
    "11-ficheros": "Ficheros",
    "12-clases-objetos": "Clases y objetos",
    "13-algoritmos-basicos": "Algoritmos básicos",
    "14-busqueda": "Búsqueda",
    "15-ordenacion": "Ordenación",
    "16-arrays": "Arrays",
    "17-grafos": "Grafos",
    "18-programacion-dinamica": "Programación dinámica",
    "19-numpy-pandas": "NumPy y pandas",
    "20-visualizacion": "Visualización",
    "21-web-y-apis": "Web y APIs",
    "22-librerias-cientificas": "Librerías científicas",
    "23-herramientas": "Herramientas",
    "24-bases-de-datos": "Bases de datos",
    "25-machine-learning": "Machine learning",
    "26-simulacion-y-probabilidad": "Simulación y probabilidad",
    "27-retos": "Retos",
}
NIVELES = ("Básico", "Intermedio", "Avanzado")


def titulo_tema(carpeta):
    return TEMAS.get(carpeta, carpeta.split("-", 1)[-1].replace("-", " ").capitalize())


def dificultad(nombre, posicion, total):
    for nivel in NIVELES:
        if nivel.lower().replace("á", "a") in nombre:
            return nivel
    # Los notebooks de cada tema van de menos a más difíciles
    return NIVELES[posicion * len(NIVELES) // total]


def notebooks():
    temas = {}
    for carpeta in sorted(p for p in SRC.iterdir() if p.is_dir()):
        rutas = sorted(carpeta.glob("*.ipynb"))
        for i, ruta in enumerate(rutas):
            celdas = json.loads(ruta.read_text(encoding="utf-8"))["cells"]
            textos = ["".join(c["source"]) for c in celdas if c["cell_type"] == "markdown"]
            lineas = [linea for texto in textos for linea in texto.splitlines()]
            temas.setdefault(carpeta.name, []).append({
                "ruta": f"{carpeta.name}/{ruta.name}",
                # "Cadenas · Avanzado" -> "Avanzado": el tema ya va en el encabezado
                "titulo": next((linea[2:].strip() for linea in lineas if linea.startswith("# ")), ruta.stem).split(" · ")[-1],
                "dificultad": dificultad(ruta.stem, i, len(rutas)),
                "ejercicios": sum(bool(re.match(r"## \d+\.", texto)) for texto in textos),
            })
    return temas


def totales(temas):
    filas = [nb for nbs in temas.values() for nb in nbs]
    return sum(nb["ejercicios"] for nb in filas), len(filas)


def tablas(temas, prefijo, con_id=False):
    """Una tabla por tema; `prefijo` es la ruta hasta las carpetas de src y `con_id` fija el ancla (attr_list)."""
    partes = []
    for carpeta, nbs in temas.items():
        filas = "\n".join(
            f"| [{nb['titulo']}]({prefijo}{nb['ruta']}) | {nb['dificultad']} | {nb['ejercicios']} |" for nb in nbs
        )
        partes.append(
            f"## {titulo_tema(carpeta)}{f' {{#{carpeta}}}' if con_id else ''}\n\n"
            f"| Notebook | Dificultad | Ejercicios |\n| --- | --- | ---: |\n{filas}\n"
        )
    return "\n".join(partes)


def main():
    temas = notebooks()
    ejercicios, total = totales(temas)
    texto = (
        "# Índice de ejercicios\n\n"
        f"{ejercicios} ejercicios en {total} notebooks. Generado con `python scripts/index.py`.\n\n"
        "La dificultad sale del nombre del notebook (`basico`, `intermedio`, `avanzado`) "
        "o, si no lo indica, de su posición dentro del tema.\n\n"
        + tablas(temas, "src/")
    )
    (RAIZ / "INDEX.md").write_text(texto, encoding="utf-8")
    print(f"INDEX.md: {ejercicios} ejercicios en {total} notebooks")


if __name__ == "__main__":
    main()
