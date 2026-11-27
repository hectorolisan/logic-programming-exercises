"""Comprueba las convenciones de todos los notebooks de src sin ejecutarlos (lo usa el CI)."""

import json
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src"


def problemas(nb):
    celdas = nb["cells"]
    if not celdas or celdas[0]["cell_type"] != "markdown" or not "".join(celdas[0]["source"]).startswith("# "):
        yield "la primera celda no es un H1"
    textos = ["".join(c["source"]) for c in celdas if c["cell_type"] == "markdown"]
    numeros = [int(m.group(1)) for t in textos if (m := re.match(r"## (\d+)\.", t))]
    if not numeros:
        yield "no hay ejercicios `## N.`"
    elif numeros != list(range(1, len(numeros) + 1)):
        yield f"numeración no consecutiva: {numeros}"
    if any(re.search(r"^## \d+\.", t, re.M) and not re.match(r"## \d+\.", t) for t in textos):
        yield "un `## N.` no empieza su celda"
    if nb["metadata"].get("kernelspec", {}).get("name") != "python3":
        yield "kernelspec distinto de python3"
    for i, celda in enumerate(celdas):
        for salida in celda.get("outputs", []):
            if salida["output_type"] == "error":
                yield f"celda {i}: salida de error {salida['ename']}"


def main():
    fallos = 0
    rutas = sorted(p for p in SRC.rglob("*.ipynb") if ".ipynb_checkpoints" not in p.parts)
    for ruta in rutas:
        for problema in problemas(json.loads(ruta.read_text(encoding="utf-8"))):
            print(f"{ruta.relative_to(SRC).as_posix()}: {problema}")
            fallos += 1
    print(f"{len(rutas)} notebooks revisados, {fallos} problemas")
    sys.exit(1 if fallos else 0)


if __name__ == "__main__":
    main()
