"""Hooks de MkDocs: rellena la portada con el índice y pone nombre a los temas del menú."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from index import notebooks, tablas, titulo_tema, totales  # noqa: E402


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
    for seccion in nav.items:
        for tema in getattr(seccion, "children", None) or []:
            if tema.is_section and tema.children and tema.children[0].is_page:
                tema.title = titulo_tema(tema.children[0].file.src_uri.split("/")[-2])
    return nav


def on_env(env, files, **kwargs):
    # Menú: "Cadenas · Avanzado" -> "Avanzado"; la pestaña del navegador conserva el título completo
    for archivo in files.documentation_pages():
        page = archivo.page
        if page and page.title and " · " in page.title:
            page.meta["title"] = page.title
            page.title = page.title.split(" · ")[-1]
    return env
