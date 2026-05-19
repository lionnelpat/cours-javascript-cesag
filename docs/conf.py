project = "Développement Frontend avec JavaScript"
copyright = "2025, CESAG — Dakar"
author = "CESAG — Licence MIAGE"
release = "2025-2026"
language = "fr"

extensions = ["myst_parser"]

myst_enable_extensions = ["colon_fence", "deflist", "tasklist", "html_image"]

source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#1A7A2A",
        "color-brand-content": "#1A7A2A",
        "color-sidebar-background": "#f4f9f4",
        "color-sidebar-background-border": "#c8dfc8",
        "color-sidebar-caption-text": "#1A7A2A",
        "color-sidebar-link-text": "#2c2c2c",
        "color-sidebar-link-text--top-level": "#111111",
        "color-sidebar-item-background--hover": "#dceede",
        "color-sidebar-item-background--current": "#E8420A",
        "color-background-primary": "#ffffff",
        "color-background-secondary": "#f7faf7",
        "color-background-border": "#dde8dd",
        "color-foreground-primary": "#1c1c1c",
        "color-foreground-secondary": "#444444",
        "color-code-background": "#f4f8f4",
        "color-code-foreground": "#1c2e1c",
        "color-link": "#1A7A2A",
        "color-link--hover": "#E8420A",
        "color-link-underline": "transparent",
        "color-link-underline--hover": "#E8420A",
    },
    "navigation_with_keys": True,
}

html_title = "Frontend JS — CESAG MIAGE"
html_short_title = "JS CESAG"

# Métadonnées
html_meta = {
    "description": "Support de cours Introduction au langage JavaScript — Licence 2 MIAGE, CESAG Dakar",
    "keywords": "JavaScript, développement web, CESAG, MIAGE, Dakar",
    "author": "PATRICK LIONNEL DOOKO - Model Technologie"
}

# ─────────────────────────────────────────────────────────────────────────────
# -- Export PDF (LaTeX/pdflatex) -----------------------------------------------
# ─────────────────────────────────────────────────────────────────────────────

latex_engine = "pdflatex"

latex_elements = {
    "papersize": "a4paper",
    "pointsize": "11pt",
    "preamble": r"""
\setcounter{tocdepth}{3}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage{xcolor}
\definecolor{cesagvert}{HTML}{1A7A2A}
\definecolor{cesagorange}{HTML}{E8420A}
\usepackage{titlesec}
\titleformat{\chapter}[block]
  {\normalfont\LARGE\bfseries\color{cesagvert}}
  {\thechapter.}{1em}{}
\titleformat{\section}[block]
  {\normalfont\Large\bfseries\color{cesagvert}}
  {\thesection}{1em}{}
\titleformat{\subsection}[block]
  {\normalfont\large\bfseries\color{cesagvert!80!black}}
  {\thesubsection}{1em}{}
\usepackage[colorlinks=true,
            linkcolor=cesagvert,
            urlcolor=cesagvert,
            citecolor=cesagvert]{hyperref}
\setlength{\parskip}{0.5em}
\setlength{\parindent}{0pt}
""",
    "maketitle": r"""
\begin{titlepage}
\centering
\vspace*{2cm}
{\color{cesagvert}\rule{\textwidth}{2pt}}\par
\vspace{1cm}
{\LARGE\bfseries\color{cesagvert}
Introduction au Langage JavaScript}
\vspace{0.8cm}
{\color{cesagorange}\rule{\textwidth}{1pt}}\par
\vspace{1.2cm}
{\large CESAG --- Centre Africain d'Études Supérieures en Gestion\\
Licence 1 MIAGE --- Dakar, Sénégal\par}
\vspace{0.6cm}
{\large Année académique 2025--2026\par}
\vfill
{\small\color{gray} Support de cours --- Patrick Lionnel Dooko --- Model Technologie}
\end{titlepage}
""",
    "extraclassoptions": "openany",
    "sphinxsetup": "verbatimwithframe=false",
}

latex_documents = [
    (
        "index",
        "cours-js-cesag.tex",
        "Introduction au Langage JavaScript",
        "CESAG — Licence 2 MIAGE",
        "manual",
    ),
]

numfig = True

# ─────────────────────────────────────────────────────────────────────────────
# -- Export ePub ---------------------------------------------------------------
# ─────────────────────────────────────────────────────────────────────────────

epub_title = "Introduction au Langage JavaScript"
epub_author = "CESAG — Licence 2 MIAGE"
epub_publisher = "CESAG — Centre Africain d'Études Supérieures en Gestion, Dakar"
epub_copyright = "2026, CESAG — Dakar"
epub_language = "fr"
epub_uid = "cesag-cours-js-2025-2026"
epub_show_urls = "no"
