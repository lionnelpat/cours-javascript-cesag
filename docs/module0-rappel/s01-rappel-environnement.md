# Séance 1 — Rappel HTML/CSS & Mise en place de l'environnement

```{admonition} Objectifs de cette séance
:class: tip
- Réviser les notions HTML/CSS essentielles pour ce cours
- Configurer VS Code avec les bons outils
- Comprendre ce que JavaScript apporte à une page web
- Créer la structure du **projet fil rouge** qui évoluera tout au long du cours
```

---

## 1. Ce que tu dois déjà savoir (rappel rapide)

### HTML — La structure

Les éléments clés que l'on utilisera intensément avec JavaScript :

```html
<!-- Identifiants et classes — JS les cible en permanence -->
<div id="app">                      <!-- id : unique, ciblé par getElementById -->
  <section class="liste-etudiants"> <!-- class : ciblée par querySelector -->
    <article class="carte-etudiant" data-id="1">  <!-- data-* : données custom -->
      <h2 class="nom">Amadou Diallo</h2>
      <p class="filiere">MIAGE L1</p>
      <button class="btn-voir" data-id="1">Voir le profil</button>
    </article>
  </section>
</div>
```

```{admonition} Les attributs data-* — Passage obligé avec JS
:class: note
Les attributs `data-*` permettent de stocker des données directement dans le HTML, lisibles depuis JavaScript. Convention : `data-nom-de-la-donnee`. Accès JS : `element.dataset.nomDeLaDonnee`.
```

### CSS — Ce qui interagit avec JS

```css
/* Classes CSS que JS va ajouter/retirer dynamiquement */
.actif { background-color: #1A7A2A; color: white; }
.masque { display: none; }
.visible { display: block; animation: fadeIn 0.3s ease; }
.erreur { border: 2px solid #c62828; background: #fdf0f0; }
.succes { border: 2px solid #1A7A2A; background: #edf7ee; }

/* Transitions pour les animations JS */
.modal {
    opacity: 0;
    transform: translateY(-20px);
    transition: opacity 0.3s ease, transform 0.3s ease;
}
.modal.ouvert {
    opacity: 1;
    transform: translateY(0);
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
}
```

### Flexbox & Grid — Indispensables pour le TP

```css
/* Layout de l'application */
.app-layout {
    display: grid;
    grid-template-columns: 260px 1fr;
    grid-template-rows: 60px 1fr;
    grid-template-areas: "nav nav" "sidebar contenu";
    min-height: 100vh;
}

/* Liste de cartes */
.grille-cartes {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}
```

---

## 2. L'environnement de développement

### VS Code — Configuration optimale

**Extensions indispensables pour ce cours :**

| Extension | Auteur | Utilité |
|-----------|--------|---------|
| **Live Server** | Ritwick Dey | Recharge automatique à la sauvegarde |
| **ESLint** | Microsoft | Détecte les erreurs JS en temps réel |
| **Prettier** | Prettier | Formate le code automatiquement |
| **JavaScript (ES6) snippets** | charalampos | Raccourcis de code JS |
| **Path Intellisense** | Christian Kohler | Autocomplétion des chemins de fichiers |

**Paramètres VS Code recommandés** — `Ctrl+,` → icône `{}` en haut à droite :

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.tabSize": 2,
  "editor.wordWrap": "on",
  "emmet.includeLanguages": { "javascript": "javascriptreact" },
  "liveServer.settings.donotShowInfoMsg": true
}
```

### Les DevTools — Ton meilleur ami

`F12` dans Chrome → **4 onglets essentiels pour JS** :

| Onglet | Raccourci | Usage avec JavaScript |
|--------|-----------|----------------------|
| **Console** | `Ctrl+Shift+J` | Voir les `console.log()`, erreurs, tester du code |
| **Elements** | `Ctrl+Shift+C` | Voir le DOM en direct, les classes CSS |
| **Sources** | — | Débogage pas-à-pas, points d'arrêt |
| **Network** | `Ctrl+Shift+E` | Voir les requêtes fetch() |

```{admonition} La Console est ton terrain d'entraînement
:class: tip
Tu peux taper du JavaScript directement dans la console du navigateur et voir le résultat instantanément. C'est l'outil de test le plus rapide qui soit. Utilise-la constamment pour tester une idée avant de l'écrire dans ton fichier.
```

---

## 3. Qu'est-ce que JavaScript apporte ?

HTML et CSS créent une page **statique**. JavaScript la rend **vivante** :

| Besoin | Sans JS | Avec JS |
|--------|---------|---------|
| Valider un formulaire | Rechargement de page | Feedback instantané, sans rechargement |
| Afficher une modale | Impossible en pur CSS | Ouverture/fermeture dynamique |
| Charger des données | Page entière rechargée | Données insérées sans rechargement |
| Animation au scroll | Limité en CSS | Contrôle total (GSAP, etc.) |
| Sauvegarder des données | Cookie rudimentaire | localStorage, sessionStorage |

### Comment JS est intégré dans une page HTML

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Mon app JS</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <!-- Tout le HTML en premier -->
    <h1 id="titre">Bonjour !</h1>
    <button id="btn-changer">Changer le titre</button>

    <!--
        Le script TOUJOURS en bas du <body>
        → Le HTML est chargé AVANT que JS ne s'exécute
    -->
    <script src="app.js"></script>

</body>
</html>
```

```{admonition} Pourquoi le script en bas du body ?
:class: important
JavaScript a besoin que les éléments HTML existent dans la page pour les manipuler. Si le `<script>` est dans le `<head>`, il s'exécute avant que le HTML soit construit — et `getElementById("titre")` retourne `null`. En bas du `<body>`, tout le HTML est déjà chargé.

**Alternative moderne :** `<script src="app.js" defer>` dans le `<head>` — `defer` dit au navigateur d'attendre que le HTML soit prêt.
```

---

## 4. Le projet fil rouge — "CESAG Connect"

Tout au long des 10 séances, tu vas construire une **application web progressive** appelée **CESAG Connect** — un mini-portail étudiant.

### Fonctionnalités qui s'ajoutent séance par séance

| Séance | Ce qui s'ajoute |
|--------|-----------------|
| S1 | Structure HTML/CSS de base |
| S2–S3 | Logique JS fondamentale, console |
| S4–S5 | Interactions DOM (boutons, listes) |
| S6 | Formulaire d'inscription validé |
| S7 | Modal de détail étudiant + localStorage |
| S8 | Chargement des données depuis un fichier JSON |
| S9 | Animations GSAP + graphique Chart.js |
| S10 | Soutenance du projet personnel |

### Structure de fichiers du projet

```
cesag-connect/
├── index.html              ← Page principale (liste des étudiants)
├── inscription.html        ← Formulaire d'inscription (S6)
├── etudiant.html           ← Fiche détail d'un étudiant (S7)
├── style.css               ← Styles globaux
├── app.js                  ← JS principal
├── modules/
│   ├── validation.js       ← Module validation formulaire (S6)
│   ├── storage.js          ← Module localStorage (S7)
│   └── api.js              ← Module fetch (S8)
└── data/
    └── etudiants.json      ← Données simulées (S8)
```

---

## TP 1 — Structure de CESAG Connect

```{admonition} À faire — 1h30
:class: warning

### Objectif
Créer la structure HTML/CSS complète du projet fil rouge.

### Étape 1 — index.html (30 min)
Crée `index.html` avec :
- Navigation : logo "CESAG Connect" + liens (Accueil, Inscription, À propos)
- Section hero : titre + sous-titre + bouton "S'inscrire"
- Section "Nos étudiants" : grille de 6 cartes d'étudiants (données fictives)
- Chaque carte : photo placeholder, nom, filière, bouton "Voir le profil"
- Footer : copyright + liens

**Attributs data-* obligatoires** sur chaque carte et bouton :
```html
<article class="carte-etudiant" data-id="1" data-filiere="miage">
    ...
    <button class="btn-profil" data-id="1">Voir le profil</button>
</article>
```

### Étape 2 — style.css (40 min)
- Layout Grid pour la page complète
- Navigation Flexbox avec fond `#1A7A2A`
- Grille de cartes avec `flex-wrap: wrap; gap: 20px`
- Cartes avec `box-shadow`, `border-radius: 12px`, hover `translateY(-4px)`
- Classes utilitaires prêtes pour JS : `.masque`, `.actif`, `.erreur`, `.succes`
- Transitions CSS sur les éléments interactifs

### Étape 3 — app.js (20 min)
Crée `app.js` et lie-le en bas du `<body>`. Pour l'instant :
```javascript
// Test de connexion JS ↔ HTML
console.log("CESAG Connect — JS chargé !");
console.log("Nombre de cartes :", document.querySelectorAll(".carte-etudiant").length);
```
→ Ouvre la console DevTools et vérifie que le message s'affiche.

### Rendu
Dossier `cesag-connect/` avec `index.html`, `style.css`, `app.js`
```

---

*Séance suivante → [Séance 2 — Variables, types et conditions](../module1-fondations/s02-variables-types)*
