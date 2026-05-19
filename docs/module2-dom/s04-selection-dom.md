# Séance 4 — Sélectionner et Manipuler le DOM

```{admonition} Objectifs
:class: tip
- Sélectionner des éléments avec `querySelector` et ses variantes
- Lire et modifier le contenu (`textContent`, `innerHTML`)
- Modifier les styles et les classes CSS (`classList`)
- Lire et modifier les attributs (`getAttribute`, `dataset`)
- Créer, insérer et supprimer des éléments dynamiquement
```

---

## 1. Sélectionner des éléments

### Les méthodes de sélection

```javascript
// querySelector — 1 seul élément (le premier trouvé)
// Accepte n'importe quel sélecteur CSS
const titre = document.querySelector("h1");
const carte = document.querySelector(".carte-etudiant");
const bouton = document.querySelector("#btn-inscription");
const premierLien = document.querySelector("nav a");
const champActif = document.querySelector("input:focus");

// querySelectorAll — TOUS les éléments correspondants (NodeList)
const toutesLesCartes = document.querySelectorAll(".carte-etudiant");
const titresH2 = document.querySelectorAll("h2");
const boutonsFiliere = document.querySelectorAll("[data-filiere]");

// Convertir NodeList en tableau pour utiliser map/filter
const cartesArray = Array.from(toutesLesCartes);
// ou : const cartesArray = [...toutesLesCartes];

// Méthodes classiques (encore utilisées)
const appDiv = document.getElementById("app");             // rapide, id uniquement
const items = document.getElementsByClassName("item");     // HTMLCollection (vieux)
const paras = document.getElementsByTagName("p");          // HTMLCollection (vieux)
```

```{admonition} querySelector vs getElementById — lequel choisir ?
:class: tip
`querySelector` est plus flexible (accepte tout sélecteur CSS) et suffit dans la majorité des cas. `getElementById` est légèrement plus rapide mais ne fonctionne que pour les IDs. **Préfère `querySelector` et `querySelectorAll`** dans ton code.
```

### Naviguer dans le DOM

```javascript
const carte = document.querySelector(".carte-etudiant");

// Enfants
carte.children                    // HTMLCollection des enfants directs
carte.firstElementChild           // Premier enfant
carte.lastElementChild            // Dernier enfant
carte.childElementCount           // Nombre d'enfants

// Parent
carte.parentElement               // Élément parent direct
carte.closest(".section-liste")   // Ancêtre le plus proche avec ce sélecteur

// Frères et sœurs
carte.nextElementSibling          // Élément suivant au même niveau
carte.previousElementSibling      // Élément précédent au même niveau
```

### Chercher DANS un élément

```javascript
// Limiter la recherche à un sous-arbre
const section = document.querySelector(".section-etudiants");
const boutonsSection = section.querySelectorAll(".btn-voir");
// Ne cherche que dans section, pas dans toute la page
```

---

## 2. Lire et modifier le contenu

### `textContent` vs `innerHTML`

```javascript
const titre = document.querySelector("#titre-page");

// textContent — texte brut uniquement (sûr)
titre.textContent;              // Lit : "Bienvenue"
titre.textContent = "Bonjour"; // Écrit : remplace tout le texte

// innerHTML — HTML inclus (puissant mais à utiliser avec prudence)
const liste = document.querySelector(".liste-etudiants");
liste.innerHTML;                // Lit le HTML interne
liste.innerHTML = "<li>Nouveau</li>"; // Remplace tout le HTML interne

// innerText — similaire à textContent mais tient compte du CSS
// (plus lent, rarement nécessaire)
```

```{admonition} Sécurité — Attention à innerHTML !
:class: important
N'utilise jamais `innerHTML` avec des données venant de l'utilisateur sans les avoir "nettoyées" — c'est une faille XSS (Cross-Site Scripting). Si le contenu vient d'une saisie utilisateur, utilise `textContent` ou `createTextNode`.

```javascript
// ❌ DANGEREUX si input vient de l'utilisateur
element.innerHTML = userInput;

// ✅ SÛR
element.textContent = userInput;
```
```

### Modifier les valeurs des inputs

```javascript
const champNom = document.querySelector("#nom");
const champEmail = document.querySelector("#email");

// Lire la valeur
const nom = champNom.value;
const email = champEmail.value;

// Écrire une valeur
champNom.value = "Amadou Diallo";

// Vider un champ
champNom.value = "";

// Pour les checkbox et radio
const checkbox = document.querySelector("#accord");
checkbox.checked;               // true ou false
checkbox.checked = true;        // Cocher

// Pour un select
const select = document.querySelector("#filiere");
select.value;                   // La valeur sélectionnée
select.value = "Finance";       // Changer la sélection
```

---

## 3. Modifier les styles et classes

### Modifier les styles inline

```javascript
const carte = document.querySelector(".carte");

// Lecture et écriture des styles (camelCase en JS)
carte.style.backgroundColor = "#1A7A2A";
carte.style.color = "white";
carte.style.borderRadius = "8px";
carte.style.display = "none";          // Cacher
carte.style.display = "block";         // Afficher

// Lire un style calculé (tient compte du CSS)
const styles = window.getComputedStyle(carte);
styles.fontSize;                        // "16px"
styles.backgroundColor;                 // "rgb(26, 122, 42)"
```

### `classList` — La bonne façon de gérer les classes

```javascript
const carte = document.querySelector(".carte");

// Ajouter une classe
carte.classList.add("actif");
carte.classList.add("surligne", "anime");  // Plusieurs à la fois

// Retirer une classe
carte.classList.remove("masque");

// Basculer (ajoute si absent, retire si présent)
carte.classList.toggle("ouvert");
carte.classList.toggle("theme-sombre");

// Vérifier si une classe est présente
carte.classList.contains("actif");         // true ou false

// Remplacer une classe par une autre
carte.classList.replace("ancien-style", "nouveau-style");

// Lire toutes les classes
carte.classList.toString();               // "carte actif surligne"
```

```{admonition} classList.toggle — Indispensable pour les menus et modals
:class: tip
`toggle` est parfait pour les éléments qui basculent entre deux états : menu ouvert/fermé, thème clair/sombre, carte sélectionnée/non sélectionnée.

```javascript
btnMenu.addEventListener("click", () => {
    navLiens.classList.toggle("ouvert");
    btnMenu.classList.toggle("actif");
});
```
```

---

## 4. Lire et modifier les attributs

```javascript
const lien = document.querySelector("a.lien-externe");

// Lire un attribut
lien.getAttribute("href");              // "https://www.cesag.sn"
lien.getAttribute("target");           // "_blank"

// Modifier un attribut
lien.setAttribute("href", "https://example.com");
lien.setAttribute("title", "Nouveau titre");

// Supprimer un attribut
lien.removeAttribute("target");

// Vérifier l'existence
lien.hasAttribute("disabled");         // false

// Attributs booléens
const input = document.querySelector("input");
input.disabled = true;                  // Désactive le champ
input.required = false;                 // Enlève required

// Attributs data-*  ← TRÈS utilisés avec JS
const carte = document.querySelector(".carte-etudiant");
carte.dataset.id;                       // Lit data-id
carte.dataset.filiere;                  // Lit data-filiere

carte.dataset.id = "42";               // Modifie data-id
carte.dataset.etat = "selectionne";    // Crée data-etat
```

---

## 5. Créer et insérer des éléments

### Méthode complète — `createElement`

```javascript
// 1. Créer l'élément
const nouvelleCarte = document.createElement("article");

// 2. Lui donner des classes et attributs
nouvelleCarte.classList.add("carte-etudiant");
nouvelleCarte.dataset.id = "7";

// 3. Lui donner du contenu
nouvelleCarte.innerHTML = `
    <h3 class="nom">Kofi Mensah</h3>
    <p class="filiere">MBA</p>
    <button class="btn-voir" data-id="7">Voir le profil</button>
`;

// 4. L'insérer dans le DOM
const conteneur = document.querySelector(".grille-cartes");
conteneur.appendChild(nouvelleCarte);         // À la fin
conteneur.prepend(nouvelleCarte);              // Au début
conteneur.insertBefore(nouvelleCarte, reference); // Avant un élément

// insertAdjacentHTML — Insérer du HTML sans remplacer le contenu
conteneur.insertAdjacentHTML("beforeend", `<div class="carte">...</div>`);
// Positions : "beforebegin" | "afterbegin" | "beforeend" | "afterend"
```

### Méthode rapide — Modifier `innerHTML` du conteneur

```javascript
// ✅ Bonne pratique pour afficher une liste entière
function afficherEtudiants(etudiants) {
    const conteneur = document.querySelector(".grille-cartes");

    if (etudiants.length === 0) {
        conteneur.innerHTML = `
            <p class="vide">Aucun étudiant trouvé.</p>
        `;
        return;
    }

    conteneur.innerHTML = etudiants
        .map(e => `
            <article class="carte-etudiant" data-id="${e.id}" data-filiere="${e.filiere}">
                <img src="images/${e.id}.jpg"
                     alt="Photo de ${e.prenom} ${e.nom}"
                     onerror="this.src='images/avatar.png'">
                <div class="carte-corps">
                    <h3>${e.prenom} ${e.nom}</h3>
                    <span class="badge-filiere">${e.filiere}</span>
                    <p class="note">${e.note}/20</p>
                </div>
                <button class="btn-voir" data-id="${e.id}">Voir le profil</button>
            </article>
        `)
        .join("");
}
```

### Supprimer des éléments

```javascript
// Supprimer un élément
const carte = document.querySelector(".carte-etudiant[data-id='3']");
carte.remove();                                     // Moderne

// Vider un conteneur
const conteneur = document.querySelector(".grille-cartes");
conteneur.innerHTML = "";                            // Rapide
// ou : while (conteneur.firstChild) conteneur.removeChild(conteneur.firstChild);

// Remplacer un élément
const ancien = document.querySelector("#ancien");
const nouveau = document.createElement("div");
nouveau.textContent = "Nouveau contenu";
ancien.replaceWith(nouveau);
```

---

## 6. Exemple complet — Afficher les étudiants

```javascript
// data/etudiants.js (pour l'instant, données en dur)
const etudiants = [
    { id: 1, prenom: "Amadou", nom: "Diallo", filiere: "MIAGE", note: 14 },
    { id: 2, prenom: "Fatou",  nom: "Sow",    filiere: "Finance", note: 16 },
    { id: 3, prenom: "Ibrahima", nom: "Ndiaye", filiere: "MIAGE", note: 9 },
];

function afficherEtudiants(liste) {
    const conteneur = document.querySelector("#liste-etudiants");
    const compteur = document.querySelector("#compteur");

    compteur.textContent = `${liste.length} étudiant(s)`;

    conteneur.innerHTML = liste.map(e => `
        <article class="carte" data-id="${e.id}">
            <h3>${e.prenom} ${e.nom}</h3>
            <p class="filiere">${e.filiere}</p>
            <p class="note ${e.note >= 10 ? 'admis' : 'ajourne'}">
                ${e.note}/20
            </p>
            <button class="btn-profil" data-id="${e.id}">
                Voir le profil
            </button>
        </article>
    `).join("");
}

// Appel initial
afficherEtudiants(etudiants);
```

---

## Résumé

```{admonition} Ce qu'il faut retenir
:class: tip
| Méthode | Usage |
|---------|-------|
| `querySelector(css)` | 1 élément (premier trouvé) |
| `querySelectorAll(css)` | Tous les éléments (NodeList) |
| `element.textContent` | Lire/écrire du texte brut |
| `element.innerHTML` | Lire/écrire du HTML |
| `element.value` | Valeur d'un input/select |
| `element.style.prop` | Style inline (camelCase) |
| `classList.add/remove` | Ajouter/retirer une classe |
| `classList.toggle` | Basculer une classe |
| `classList.contains` | Vérifier une classe |
| `dataset.nomProp` | Lire/écrire `data-nom-prop` |
| `createElement(tag)` | Créer un élément |
| `conteneur.innerHTML = html` | Injecter du HTML |
| `element.remove()` | Supprimer un élément |
```

---

## TP 4 — Affichage dynamique dans CESAG Connect

```{admonition} À faire — 1h30
:class: warning

### Objectif
Connecter les fonctions logiques du TP3 à l'affichage HTML.

**1. Afficher les cartes (4 pts)**
- Au chargement de la page, appelle `afficherEtudiants(etudiants)`
- La grille HTML doit être générée dynamiquement (pas de HTML statique dans les cartes)
- Inclus les attributs `data-id` et `data-filiere` sur chaque carte

**2. Compteur dynamique (2 pts)**
```javascript
function mettreAJourCompteur(liste) {
    const el = document.querySelector("#compteur");
    el.textContent = `${liste.length} étudiant(s) affiché(s)`;
}
```

**3. Filtres par filière (5 pts)**
- Ajoute des boutons filtres : Tous | MIAGE | Finance | RH | MBA
- Au clic sur un bouton :
  - Filtre le tableau avec `.filter()`
  - Relance `afficherEtudiants()` avec le tableau filtré
  - Ajoute la classe `.actif` sur le bouton cliqué, la retire des autres
  - Met à jour le compteur

**4. Bascule affichage (3 pts)**
- Ajoute un bouton "Masquer les ajournés"
- Au clic : filtre les étudiants avec note < 10
- Le texte du bouton change : "Masquer les ajournés" ↔ "Afficher tous"
- Utilise `classList.toggle` sur le bouton et une variable booléenne

**5. Message vide (2 pts)**
- Si le filtre donne 0 résultats, affiche un message "Aucun étudiant dans cette filière"
```

---

*Séance suivante → [Séance 5 — Événements JavaScript](s05-evenements)*
