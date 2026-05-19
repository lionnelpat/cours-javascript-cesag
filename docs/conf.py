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
