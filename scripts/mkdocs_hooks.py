"""Hooks de MkDocs: rellena la portada con el índice y pone nombre a los temas del menú y los agrupa."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from index import notebooks, tablas, titulo_tema, totales  # noqa: E402
from mkdocs.structure.nav import Navigation, Section, _add_parent_links, _add_previous_and_next_links  # noqa: E402

# Menú por bloques sin renumerar las carpetas (renombrarlas rompería las URL publicadas)
BLOQUES = {
    "Fundamentos de Python": range(1, 13),
    "Algoritmos y estructuras de datos": [13, 14, 15, 16, 17, 18, 27, 30, 31, 32, 33, 34],
    "Ciencia de datos": [19, 20, 22, 26, 35, 37],
    "Aplicaciones: web, datos e IA": [21, 23, 24, 25, 28, 29, 36],
}


def on_page_markdown(markdown, page, **kwargs):
    if page.file.src_uri != "index.md":
        return markdown
    temas = notebooks()
    ejercicios, total = totales(temas)
    chips = "\n".join(f'<a class="chip" href="#{carpeta}">{titulo_tema(carpeta)}</a>' for carpeta in temas)
    return (
        markdown.replace("{{ ejercicios }}", str(ejercicios))
        .replace("{{ notebooks }}", str(total))
        .replace("{{ temas }}", str(len(temas)))
        .replace("<!-- chips -->", chips)
        .replace("<!-- indice -->", tablas(temas, "ejercicios/", con_id=True))
    )


def on_nav(nav, **kwargs):
    items = []
    for seccion in nav.items:
        temas = [t for t in getattr(seccion, "children", None) or [] if t.is_section and t.children and t.children[0].is_page]
        if not temas:
            items.append(seccion)
            continue
        por_numero = {}
        for tema in temas:
            carpeta = tema.children[0].file.src_uri.split("/")[-2]
            tema.title = titulo_tema(carpeta)
            por_numero[int(carpeta[:2])] = tema
        for titulo, numeros in BLOQUES.items():
            items.append(Section(titulo, [por_numero.pop(n) for n in numeros if n in por_numero]))
        assert not por_numero, f"temas sin bloque en BLOQUES: {sorted(por_numero)}"
    pages = [p for item in items for p in _paginas(item)]
    _add_previous_and_next_links(pages)
    _add_parent_links(items)
    return Navigation(items, pages)


def _paginas(item):
    return [p for hijo in item.children for p in _paginas(hijo)] if item.is_section else [item] if item.is_page else []


def on_env(env, files, **kwargs):
    # Menú: "Cadenas · Avanzado" -> "Avanzado"; la pestaña del navegador conserva el título completo
    for archivo in files.documentation_pages():
        page = archivo.page
        if page and page.title and " · " in page.title:
            page.meta["title"] = page.title
            page.title = page.title.split(" · ")[-1]
    return env
