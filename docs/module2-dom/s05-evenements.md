# Séance 5 — Événements JavaScript

```{admonition} Objectifs
:class: tip
- Attacher des écouteurs d'événements avec `addEventListener`
- Connaître les types d'événements essentiels
- Utiliser l'objet `event` et ses propriétés
- Comprendre la propagation et `preventDefault`
- Maîtriser la délégation d'événements (pattern essentiel)
```

---

## 1. `addEventListener` — La base

```javascript
// Syntaxe : element.addEventListener(événement, fonction)

const btn = document.querySelector("#btn-inscription");

btn.addEventListener("click", function() {
    console.log("Bouton cliqué !");
});

// Avec arrow function (style moderne)
btn.addEventListener("click", () => {
    console.log("Bouton cliqué !");
});

// Avec une fonction nommée (meilleur pour pouvoir la retirer)
function gererClic() {
    console.log("Cliqué !");
}
btn.addEventListener("click", gererClic);

// Retirer un écouteur (la fonction doit être nommée)
btn.removeEventListener("click", gererClic);
```

```{admonition} addEventListener vs onclick — Lequel utiliser ?
:class: important
```html
<!-- ❌ Ancien style — dans le HTML, difficile à maintenir -->
<button onclick="gererClic()">Cliquer</button>

<!-- ❌ Ancien style — en JS, remplace le précédent -->
btn.onclick = gererClic;

<!-- ✅ Moderne — peut avoir plusieurs écouteurs, séparation HTML/JS -->
btn.addEventListener("click", gererClic);
```
Toujours utiliser `addEventListener`.
```

---

## 2. Les types d'événements essentiels

### Événements de souris

```javascript
const carte = document.querySelector(".carte");

carte.addEventListener("click",      () => console.log("Clic simple"));
carte.addEventListener("dblclick",   () => console.log("Double clic"));
carte.addEventListener("mouseenter", () => carte.classList.add("survol"));
carte.addEventListener("mouseleave", () => carte.classList.remove("survol"));
carte.addEventListener("mousemove",  (e) => console.log(e.clientX, e.clientY));
carte.addEventListener("contextmenu",(e) => {
    e.preventDefault(); // Empêche le menu contextuel natif
    console.log("Clic droit !");
});
```

### Événements de formulaire et clavier

```javascript
const input = document.querySelector("#recherche");
const form = document.querySelector("form");

// Saisie en temps réel
input.addEventListener("input", (e) => {
    console.log("Valeur en cours :", e.target.value);
    rechercherEtudiants(e.target.value);
});

// Changement validé (au blur ou selection)
input.addEventListener("change", (e) => {
    console.log("Valeur finale :", e.target.value);
});

// Focus / Blur
input.addEventListener("focus", () => input.classList.add("actif"));
input.addEventListener("blur",  () => input.classList.remove("actif"));

// Clavier
input.addEventListener("keydown", (e) => {
    if (e.key === "Enter")  soumettre();
    if (e.key === "Escape") input.value = "";
    console.log("Touche :", e.key, "| Code :", e.code, "| Ctrl :", e.ctrlKey);
});

// Soumission de formulaire
form.addEventListener("submit", (e) => {
    e.preventDefault();  // ← TOUJOURS pour gérer la validation soi-même
    console.log("Formulaire soumis !");
});
```

### Événements de la page

```javascript
// DOM entièrement chargé
document.addEventListener("DOMContentLoaded", () => {
    console.log("Page prête !");
    initialiserApp();
});

// Page + images + ressources chargées
window.addEventListener("load", () => {
    console.log("Tout chargé !");
});

// Scroll
window.addEventListener("scroll", () => {
    const scrollY = window.scrollY;
    const nav = document.querySelector("nav");
    nav.classList.toggle("fixe", scrollY > 80);
});

// Redimensionnement
window.addEventListener("resize", () => {
    console.log("Largeur :", window.innerWidth);
});
```

---

## 3. L'objet `event`

Chaque événement passe un objet `event` (souvent `e` ou `evt`) à la fonction :

```javascript
document.querySelector("#btn").addEventListener("click", (event) => {
    // Informations sur l'événement
    event.type;            // "click"
    event.timeStamp;       // Timestamp de l'événement

    // L'élément qui a déclenché l'événement
    event.target;          // L'élément cliqué
    event.target.id;       // Son id
    event.target.value;    // Sa valeur (pour les inputs)
    event.target.dataset;  // Ses attributs data-*

    // L'élément sur lequel l'écouteur est attaché
    event.currentTarget;   // Peut différer de target

    // Position de la souris
    event.clientX;         // Position X relative à la fenêtre
    event.clientY;         // Position Y relative à la fenêtre
    event.pageX;           // Position X relative au document

    // Touches modificatrices
    event.ctrlKey;         // true si Ctrl est enfoncé
    event.shiftKey;        // true si Shift est enfoncé
    event.altKey;          // true si Alt est enfoncé

    // Bloquer le comportement par défaut
    event.preventDefault();

    // Bloquer la propagation
    event.stopPropagation();
});
```

---

## 4. `preventDefault` — Contrôler le comportement natif

```javascript
// Empêcher la soumission d'un formulaire (et rechargement de page)
form.addEventListener("submit", (e) => {
    e.preventDefault();
    // → On gère nous-mêmes la soumission (validation, fetch, etc.)
});

// Empêcher la navigation d'un lien
lien.addEventListener("click", (e) => {
    e.preventDefault();
    // → On gère la navigation manuellement (SPA, animation, etc.)
});

// Empêcher le menu contextuel
document.addEventListener("contextmenu", (e) => {
    e.preventDefault();
});

// Empêcher la sélection de texte au double-clic
document.addEventListener("selectstart", (e) => {
    e.preventDefault();
});
```

---

## 5. La propagation des événements (Bubbling)

Les événements "remontent" dans le DOM du fils vers le parent :

```html
<div id="conteneur">          <!-- 3. Reçoit l'événement en dernier -->
    <section id="section">    <!-- 2. Reçoit l'événement en second -->
        <button id="btn">     <!-- 1. Déclenche l'événement -->
            Cliquer
        </button>
    </section>
</div>
```

```javascript
document.querySelector("#btn").addEventListener("click", (e) => {
    console.log("1. Bouton cliqué");
});

document.querySelector("#section").addEventListener("click", (e) => {
    console.log("2. Section reçoit le clic");
    // e.stopPropagation(); // Arrêterait la remontée ici
});

document.querySelector("#conteneur").addEventListener("click", (e) => {
    console.log("3. Conteneur reçoit le clic");
});

// Au clic sur le bouton, la console affiche les 3 messages dans l'ordre
```

---

## 6. La délégation d'événements — Pattern essentiel

Au lieu d'attacher un écouteur sur chaque carte, on en attache **un seul sur le conteneur** :

```{admonition} Pourquoi la délégation ?
:class: tip
Si tu génères des cartes dynamiquement avec `innerHTML`, les éléments créés n'existaient pas au moment où tu as appelé `addEventListener` — ils ne sont donc pas écoutés ! La délégation résout ce problème : on écoute sur le conteneur (qui existe toujours), et on identifie quel enfant a déclenché l'événement.
```

```javascript
// ❌ Sans délégation — ne fonctionne PAS sur les éléments créés dynamiquement
document.querySelectorAll(".btn-voir").forEach(btn => {
    btn.addEventListener("click", gererClic);
    // Si on recrée les cartes avec innerHTML, ces écouteurs sont perdus !
});

// ✅ Avec délégation — fonctionne même après regénération du HTML
const conteneur = document.querySelector("#liste-etudiants");

conteneur.addEventListener("click", (e) => {
    // On vérifie quel élément a été cliqué
    const btnVoir = e.target.closest(".btn-voir");
    const btnSuppr = e.target.closest(".btn-supprimer");

    if (btnVoir) {
        const id = parseInt(btnVoir.dataset.id);
        ouvrirProfil(id);
    }

    if (btnSuppr) {
        const id = parseInt(btnSuppr.dataset.id);
        supprimerEtudiant(id);
    }
});
```

### `closest()` — Trouver l'ancêtre le plus proche

```javascript
conteneur.addEventListener("click", (e) => {
    // e.target peut être un enfant profond du bouton (ex: une icône dans le bouton)
    // closest() remonte jusqu'à trouver le bon ancêtre

    const carte = e.target.closest(".carte-etudiant");
    if (!carte) return; // Clic ailleurs dans le conteneur

    const id = parseInt(carte.dataset.id);
    console.log("Carte cliquée, ID :", id);
});
```

---

## 7. Exemple complet — CESAG Connect interactif

```javascript
// app.js — Version séance 5

const etudiants = [
    { id: 1, prenom: "Amadou",   nom: "Diallo",   filiere: "MIAGE",   note: 14 },
    { id: 2, prenom: "Fatou",    nom: "Sow",      filiere: "Finance", note: 16 },
    { id: 3, prenom: "Ibrahima", nom: "Ndiaye",   filiere: "MIAGE",   note: 9  },
    { id: 4, prenom: "Mariama",  nom: "Faye",     filiere: "RH",      note: 12 },
];

let etudiantsFiltres = [...etudiants]; // Copie pour les filtres

// ── Affichage ──────────────────────────────────────────────
function afficherEtudiants(liste) {
    const conteneur = document.querySelector("#liste-etudiants");
    const compteur  = document.querySelector("#compteur");

    compteur.textContent = `${liste.length} étudiant(s)`;

    if (liste.length === 0) {
        conteneur.innerHTML = `<p class="vide">Aucun résultat.</p>`;
        return;
    }

    conteneur.innerHTML = liste.map(e => `
        <article class="carte" data-id="${e.id}" data-filiere="${e.filiere}">
            <h3>${e.prenom} ${e.nom}</h3>
            <span class="badge">${e.filiere}</span>
            <p class="note">${e.note}/20</p>
            <div class="carte-actions">
                <button class="btn-voir" data-id="${e.id}">Voir</button>
                <button class="btn-suppr" data-id="${e.id}">✕</button>
            </div>
        </article>
    `).join("");
}

// ── Délégation d'événements sur la liste ──────────────────
document.querySelector("#liste-etudiants")
    .addEventListener("click", (e) => {

    const btnVoir = e.target.closest(".btn-voir");
    const btnSuppr = e.target.closest(".btn-suppr");

    if (btnVoir) {
        const id = parseInt(btnVoir.dataset.id);
        const etudiant = etudiants.find(e => e.id === id);
        alert(`${etudiant.prenom} ${etudiant.nom} — ${etudiant.note}/20`);
    }

    if (btnSuppr) {
        const id = parseInt(btnSuppr.dataset.id);
        if (confirm("Supprimer cet étudiant ?")) {
            etudiantsFiltres = etudiantsFiltres.filter(e => e.id !== id);
            afficherEtudiants(etudiantsFiltres);
        }
    }
});

// ── Filtres par filière ────────────────────────────────────
document.querySelector("#filtres").addEventListener("click", (e) => {
    const btn = e.target.closest(".btn-filtre");
    if (!btn) return;

    document.querySelectorAll(".btn-filtre")
        .forEach(b => b.classList.remove("actif"));
    btn.classList.add("actif");

    const filiere = btn.dataset.filiere;
    etudiantsFiltres = filiere === "tous"
        ? [...etudiants]
        : etudiants.filter(et => et.filiere === filiere);

    afficherEtudiants(etudiantsFiltres);
});

// ── Recherche en temps réel ────────────────────────────────
document.querySelector("#recherche").addEventListener("input", (e) => {
    const terme = e.target.value.toLowerCase().trim();
    etudiantsFiltres = etudiants.filter(et =>
        et.prenom.toLowerCase().includes(terme) ||
        et.nom.toLowerCase().includes(terme)
    );
    afficherEtudiants(etudiantsFiltres);
});

// ── Initialisation ─────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
    afficherEtudiants(etudiants);
});
```

---

## Résumé

```{admonition} Ce qu'il faut retenir
:class: tip
| Concept | Usage |
|---------|-------|
| `addEventListener(evt, fn)` | Attacher un écouteur |
| `e.target` | L'élément qui a déclenché l'événement |
| `e.target.value` | Valeur d'un input dans un événement |
| `e.target.dataset.x` | Attribut `data-x` de l'élément cliqué |
| `e.preventDefault()` | Bloquer le comportement natif |
| `e.stopPropagation()` | Arrêter la remontée |
| `e.target.closest(css)` | Remonter au bon ancêtre |
| `input` | Événement saisie en temps réel |
| `submit` | Soumission de formulaire |
| `DOMContentLoaded` | DOM prêt (à mettre dans document) |
| Délégation | Écouter sur le parent, tester `closest()` |
```

---

## TP 5 — CESAG Connect Full Interactif

```{admonition} À faire — 1h30
:class: warning

**1. Barre de recherche temps réel (4 pts)**
- Champ `<input type="search" id="recherche" placeholder="Rechercher un étudiant...">`
- Sur l'événement `input` : filtre sur nom + prénom (insensible à la casse)
- Affiche le nombre de résultats en temps réel
- Si aucun résultat : message "Aucun étudiant trouvé pour '...'"

**2. Tri interactif (4 pts)**
- `<select id="tri">` avec options : Note ↓ | Note ↑ | Nom A→Z | Filière
- Sur l'événement `change` : trie et réaffiche la liste
- Le tri s'applique en combinaison avec le filtre actif

**3. Sélection de carte (3 pts)**
- Au clic sur une carte (délégation sur le conteneur)
- Ajoute la classe `.selectionnee` à la carte cliquée
- Retire `.selectionnee` de toutes les autres cartes
- Affiche les détails de l'étudiant dans un panneau `<aside id="details">`

**4. Raccourci clavier (3 pts)**
- `Ctrl + F` : met le focus sur le champ de recherche
- `Escape` : vide la recherche et réaffiche tous les étudiants
- `Entrée` sur une carte sélectionnée : ouvre la fiche détail (S7)

**5. Scroll et navigation (2 pts)**
- Au scroll > 100px : ajoute la classe `.fixe` sur la nav (fond opaque, ombre)
- Un bouton "↑ Haut" apparaît en `position: fixed` après 300px de scroll
```

---

*Séance suivante → [Séance 6 — Formulaires interactifs et validation](../module3-formulaires/s06-validation)*
