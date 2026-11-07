# AGENTS.md

This file provides guidance to coding agents when working with code in this repository.

## Project

Python programming and logic exercises, solved and explained in Spanish, as Jupyter notebooks in `src/`.
There are 27 topic folders (`01-tipos-datos-simples` … `27-retos`), ordered from easiest to hardest, and
each folder holds notebooks numbered by difficulty. The notebooks are also published as a static website
(MkDocs + Material + mkdocs-jupyter) on GitHub Pages. There is no package or app: the deliverables are the
notebooks, `INDEX.md` and the website.

## Commands

- `python -m venv .venv`, activate it, then `pip install -r requirements.txt`: notebook dependencies
- `jupyter nbconvert --to notebook --execute --inplace <notebook>`: run a notebook and save its outputs (the kernel's cwd is the notebook folder)
- `python scripts/index.py`: regenerate `INDEX.md`
- `python scripts/statements.py`: copy the notebooks without solutions into `statements/` (gitignored)
- `pip install -r docs/requirements.txt`, then `mkdocs build --strict`: build the website into `site/` (gitignored). Set `NO_MKDOCS_2_WARNING=1` to hide the MkDocs 2 notice

Deploy: `.github/workflows/pages.yml` builds with `--strict` and publishes on every push to `main`. The build
does not execute the notebooks: it renders the outputs saved in them.

## Notebook conventions

- **Spanish everywhere inside notebooks**: statements, identifiers, comments and output. README, AGENTS.md and
  commit messages are in English.
- **Structure**: the first markdown cell is `# <Tema> · <Subtítulo>` (topic notebooks) or `# <Algoritmo>` with the
  idea and its cost in LaTeX (`$O(n \log n)$`) for algorithm notebooks. Each exercise is a markdown cell
  `## N. Título` with a short imperative statement ("Escribir…", "Crear…"), followed by the solution code cells.
- **`## N.` is load-bearing**: `scripts/index.py` counts exercises with it and `scripts/statements.py` blanks
  the code after it. Code cells before the first `## N.` (imports, data download) are kept in the statements copy.
  The ` · ` in the H1 is split by the index and the website menu to drop the topic name.
- **Outputs are committed**: execute every new or edited notebook before committing. No `error` outputs: when an
  exception is part of the exercise, catch it and print it. New notebooks avoid `input()`, so nbconvert can run them.
- **Self-checks**: prefer `assert` against brute force, the standard library or a previous solution, with fixed
  random seeds when the values are printed.
- **Generated files** (data, modules written with `%%writefile`, outputs) live next to the notebook and are
  gitignored: only `.ipynb` is versioned in `src/`. On Windows, multiprocessing uses spawn, so worker functions must
  be in a module written with `%%writefile`, not defined in the notebook.
- **Metadata**: `kernelspec` `{"display_name": ".venv", "language": "python", "name": "python3"}`, nbformat 4.5.
- Comments only when they explain a why the code cannot show; keep them short.

## Adding or renaming notebooks

1. Keep the `NN-` prefix ordered by difficulty inside the folder (rename with `git mv` if needed).
2. Execute the notebook.
3. Run `python scripts/index.py`.
4. Update the exercise and notebook counts in the first bullet of `README.md` (they are printed by the script) and
   the folder comment in **Project Structure**.
5. A new topic folder also needs its display name in `TEMAS` (`scripts/index.py`).

## Website

- `mkdocs.yml` mounts `src/` as `ejercicios/` through mkdocs-jupyter `notebook_dirs` and only includes `*.ipynb`.
- `scripts/mkdocs_hooks.py` fills the placeholders of `docs/index.md` (`{{ ejercicios }}`, `{{ notebooks }}`,
  `{{ temas }}`, `<!-- chips -->`, `<!-- indice -->`) from `scripts/index.py`, names the menu sections with `TEMAS`
  and shortens notebook titles in the menu (the browser tab keeps the full title).
- Look: `docs/stylesheets/extra.css` imitates canirun.ai with `#333b4b` as the primary color (a lighter tint is used
  for text in dark mode), Geist / Geist Mono and Geist Pixel for `h1`. `overrides/main.html` adds the notebook
  download button and the credit footer shared with hectorolisan's other projects.
- `public/cover.webp` is the README cover.

## Commits and license

- Conventional Commits in English and lowercase. The scope is the topic folder without its number, e.g.
  `feat(listas-tuplas-conjuntos): add list comparison question`.
- The project is CC BY-NC-SA 3.0 ES because it adapts statements from the sources listed in the README: keep that
  attribution when adding exercises from new sources.
