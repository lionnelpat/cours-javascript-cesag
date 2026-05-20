.. Développement Frontend avec JavaScript — CESAG

============================================================
Développement Frontend avec JavaScript
============================================================

.. image:: https://img.shields.io/badge/Niveau-Intermédiaire-orange
   :alt: Niveau intermédiaire

.. image:: https://img.shields.io/badge/Volume-30h-blue
   :alt: 30 heures

.. image:: https://img.shields.io/badge/CESAG-MIAGE-1A7A2A
   :alt: CESAG MIAGE

----

Bienvenue dans le cours **Développement Frontend avec JavaScript**.

Ce cours s'adresse aux étudiants ayant déjà des bases en **HTML et CSS**. L'objectif est de maîtriser JavaScript pour créer des interfaces web dynamiques, interactives et professionnelles.

.. admonition:: Ce que tu sauras faire à la fin
   :class: tip

   - ⚡ Intégrer JavaScript dans une page web et manipuler le DOM
   - ✅ Rendre des formulaires interactifs et valider les données
   - 🧱 Structurer son code avec la Programmation Orientée Objet
   - 🪟 Afficher des modals et partager des données entre pages
   - 🌐 Charger des données dynamiques avec l'API fetch
   - 📦 Installer et utiliser des librairies pour animer une page
   - 🚀 Livrer une application web complète et fonctionnelle

----

Plan détaillé du cours
======================

.. list-table::
   :widths: 6 8 8 38 12 8 8 12
   :header-rows: 1

   * - Séance
     - Module
     - N°
     - Contenu principal
     - TP / Projet fil rouge
     - Type
     - Durée
     - Évaluation
   * - **S1**
     - Module 0
     - Rappel & Env.
     - Révision HTML/CSS · VS Code, Live Server, DevTools · Structure du projet fil rouge *CESAG Connect*
     - Structure HTML/CSS de l'application
     - CM + TP
     - 3h
     - —
   * - **S2**
     - Module 1
     - Fondations JS
     - Variables (let/const) · Types · Opérateurs · Conditions (if/else, ternaire, switch) · Valeurs falsy · Template literals · Débogage console
     - Fonctions logiques métier (mention, validation email, formatage)
     - CM + TP
     - 3h
     - —
   * - **S3**
     - Module 1
     - Fondations JS
     - Fonctions (déclaration, expression, arrow) · Tableaux (map, filter, reduce, find) · Objets · Déstructuration · Spread operator · Boucles
     - Moteur de données : stats, tri, génération HTML des cartes
     - CM + TP
     - 3h
     - —
   * - **S4**
     - Module 2
     - DOM
     - querySelector/All · textContent, innerHTML · classList · dataset · createElement · innerHTML dynamique · Supprimer des éléments
     - Affichage dynamique des cartes, filtres, compteur
     - CM + TP
     - 3h
     - —
   * - **S5**
     - Module 2
     - DOM
     - addEventListener · Objet event · preventDefault · Propagation · closest() · Délégation d'événements · Recherche temps réel
     - CESAG Connect interactif : recherche, filtres, tri, raccourcis clavier
     - CM + TP
     - 3h
     - —
   * - **S6**
     - Module 3
     - Formulaires
     - Lire les valeurs · FormData · Expressions régulières (regex) · Module validation.js · Feedback visuel par champ · Barre de force mot de passe
     - Formulaire d'inscription CESAG validé en temps réel
     - CM + TP
     - 3h
     - —
   * - **S7**
     - Module 4
     - POO
     - Classes JS · Constructeur · Propriétés et méthodes · Héritage (extends) · Encapsulation · Modules ES6 (import/export) · Refactoring CESAG Connect en classes
     - Classe ``Etudiant``, classe ``Catalogue``, classe ``Modal`` réutilisable
     - CM + TP
     - 3h
     - —
   * - **S8**
     - Module 5
     - Modals & Storage
     - Modals CSS+JS accessibles · localStorage / sessionStorage · JSON.stringify/parse · Module storage.js · Partage de données entre pages · Paramètres URL
     - Profils en modal · Persistance des données · Toast de confirmation
     - CM + TP
     - 3h
     - —
   * - **S9**
     - Module 6
     - Fetch API
     - Promises · async/await · fetch() · Gestion erreurs (try/catch) · États de chargement · Promise.all · Consommer une API publique
     - Chargement depuis etudiants.json · Page de détail dynamique · Loader
     - CM + TP
     - 3h
     - **Devoir individuel (40%)**
   * - **S10**
     - Module 7
     - Librairies
     - CDN vs npm · GSAP (animations, ScrollTrigger) · Chart.js (graphiques) · SweetAlert2 (modals/toasts) · Swiper.js (slider) · Lire une documentation
     - CESAG Connect version finale : animations, graphiques, SweetAlert2
     - CM + TP
     - 3h
     - —
   * - **S11** *(Projet)*
     - —
     - Projet final
     - Soutenance des projets de groupe (10 min présentation + 5 min questions) · Grille d'évaluation · Checklist technique
     - Application web complète (3–5 pages, fetch, POO, librairie)
     - Évaluation
     - 3h
     - **Projet groupe (60%)**

----

Modalités d'évaluation
=======================

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Épreuve
     - Coefficient
     - Description
   * - **Devoir individuel sur table** (séance 9)
     - 40 %
     - 1h30 en salle informatique · DOM, événements, formulaire validé, localStorage
   * - **Projet de groupe** (séance 11) — groupes de 3–4
     - 60 %
     - Application web complète · Soutenance 10 min + 5 min questions

----

.. toctree::
   :maxdepth: 1
   :caption: 🔄 Module 0 — Rappel & Environnement

   module0-rappel/index

.. toctree::
   :maxdepth: 1
   :caption: ⚡ Module 1 — Fondations JavaScript

   module1-fondations/index

.. toctree::
   :maxdepth: 1
   :caption: 🌐 Module 2 — Manipuler le DOM

   module2-dom/index

.. toctree::
   :maxdepth: 1
   :caption: ✅ Module 3 — Formulaires & Validation

   module3-formulaires/index

.. toctree::
   :maxdepth: 1
   :caption: 🧱 Module 4 — POO en JavaScript

   module4-poo/index

.. toctree::
   :maxdepth: 1
   :caption: 🪟 Module 5 — Modals & Storage

   module5-modals/index

.. toctree::
   :maxdepth: 1
   :caption: 🌍 Module 6 — Fetch API

   module6-fetch/index

.. toctree::
   :maxdepth: 1
   :caption: 📦 Module 7 — Librairies & Animations

   module7-librairies/index

----

.. admonition:: À propos
   :class: note

   | **Établissement** : CESAG — Dakar, Sénégal
   | **Programme** : Licence MIAGE
   | **Volume horaire** : 30 heures (10 séances × 3h + soutenance)
   | **Prérequis** : Cours HTML & CSS complété
   | **Année académique** : 2025–2026
