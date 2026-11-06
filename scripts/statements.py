"""Copia los notebooks de src a statements/ quitando las soluciones para practicar.

Se conservan el texto y el código anterior al primer ejercicio (imports y preparación de datos);
cada solución se sustituye por una celda de código vacía.
"""

import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SRC = RAIZ / "src"
DESTINO = RAIZ / "statements"


def solo_enunciados(nb):
    celdas, en_ejercicios = [], False
    for celda in nb["cells"]:
        if celda["cell_type"] == "markdown":
            en_ejercicios |= bool(re.match(r"## \d+\.", "".join(celda["source"])))
            celdas.append(celda)
        elif not en_ejercicios:
            celdas.append(celda)
        elif celdas[-1]["cell_type"] == "markdown":
            celdas.append({**celda, "source": [], "outputs": [], "execution_count": None})
    return {**nb, "cells": celdas}


def main():
    rutas = sorted(p for p in SRC.rglob("*.ipynb") if ".ipynb_checkpoints" not in p.parts)
    for ruta in rutas:
        nb = json.loads(ruta.read_text(encoding="utf-8"))
        nuevo = solo_enunciados(nb)
        assert [c for c in nb["cells"] if c["cell_type"] == "markdown"] == [
            c for c in nuevo["cells"] if c["cell_type"] == "markdown"
        ]
        destino = DESTINO / ruta.relative_to(SRC)
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(rutas)} notebooks sin soluciones en {DESTINO.relative_to(RAIZ)}/")


if __name__ == "__main__":
    main()
