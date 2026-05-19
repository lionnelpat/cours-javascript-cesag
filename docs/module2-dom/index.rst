.. _module2:

====================================
Module 2 — Manipuler le DOM
====================================

Le **DOM** (Document Object Model) est la représentation en mémoire de ta page HTML sous forme d'arbre d'objets JavaScript. C'est l'interface entre ton code JS et ce que l'utilisateur voit à l'écran.

.. admonition:: Le DOM, c'est quoi concrètement ?
   :class: note

   Quand le navigateur charge une page HTML, il construit un arbre d'objets en mémoire. Chaque balise HTML devient un **nœud** (node). JavaScript peut lire, modifier, créer ou supprimer ces nœuds — et la page se met à jour instantanément, sans rechargement.

   ```
   document
   └── html
       ├── head
       │   └── title
       └── body
           ├── header
           │   └── h1
           ├── main
           │   ├── section
           │   └── div.cartes
           └── footer
   ```

.. toctree::
   :maxdepth: 2

   s04-selection-dom
   s05-evenements
