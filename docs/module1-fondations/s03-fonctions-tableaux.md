# Séance 3 — Fonctions, Tableaux, Objets et Boucles

```{admonition} Objectifs
:class: tip
- Maîtriser les 3 façons d'écrire des fonctions
- Manipuler les tableaux avec les méthodes modernes
- Créer et parcourir des objets
- Utiliser `for`, `for...of`, `forEach`, `map`, `filter`, `find`
```

---

## 1. Les fonctions

### 3 façons d'écrire une fonction

```javascript
// 1 — Déclaration de fonction (function declaration)
// Avantage : "hoistée" — utilisable AVANT sa déclaration dans le fichier
function saluer(prenom) {
    return `Bonjour, ${prenom} !`;
}

// 2 — Expression de fonction (function expression)
// La variable est const — la fonction ne peut pas être réassignée
const saluer = function(prenom) {
    return `Bonjour, ${prenom} !`;
};

// 3 — Fonction fléchée (arrow function) — ✅ Style moderne recommandé
const saluer = (prenom) => {
    return `Bonjour, ${prenom} !`;
};

// Raccourci si une seule expression : return implicite
const saluer = (prenom) => `Bonjour, ${prenom} !`;

// Raccourci si un seul paramètre : pas de parenthèses
const doubler = n => n * 2;

// Sans paramètre : parenthèses vides obligatoires
const direBonjour = () => "Bonjour !";
```

### Paramètres et valeurs par défaut

```javascript
// Valeur par défaut si le paramètre n'est pas fourni
function creerEtudiant(prenom, nom, filiere = "MIAGE", annee = 1) {
    return { prenom, nom, filiere, annee };
    // Raccourci ES6 : { prenom: prenom, nom: nom } → { prenom, nom }
}

creerEtudiant("Amadou", "Diallo");
// → { prenom: "Amadou", nom: "Diallo", filiere: "MIAGE", annee: 1 }

creerEtudiant("Fatou", "Sow", "Finance", 2);
// → { prenom: "Fatou", nom: "Sow", filiere: "Finance", annee: 2 }
```

### Le paramètre rest (`...`)

```javascript
// Accepte un nombre variable d'arguments
function calculerMoyenne(...notes) {
    const total = notes.reduce((sum, n) => sum + n, 0);
    return total / notes.length;
}

calculerMoyenne(12, 14, 16, 18);   // 15
calculerMoyenne(10, 12);            // 11
```

### Les fonctions sont des valeurs (first-class)

```javascript
// Une fonction peut être passée en argument
const notes = [10, 14, 8, 16, 12];

// Passer une fonction comme callback
notes.forEach(function(note) {
    console.log(note);
});

// Avec arrow function — plus concis
notes.forEach(note => console.log(note));

// Retourner une fonction depuis une fonction (closure)
function creerMultiplicateur(facteur) {
    return (nombre) => nombre * facteur;
}

const doubler = creerMultiplicateur(2);
const tripler = creerMultiplicateur(3);

doubler(5);  // 10
tripler(5);  // 15
```

---

## 2. Les tableaux (Arrays)

### Créer et accéder

```javascript
// Création
const filieres = ["MIAGE", "Finance", "RH", "MBA"];
const notes = [14, 12, 16, 18, 10];
const mixte = ["texte", 42, true, null, { cle: "valeur" }];
const vide = [];

// Accès par index (commence à 0)
filieres[0]          // "MIAGE"
filieres[3]          // "MBA"
filieres.at(-1)      // "MBA" (dernier élément — méthode moderne)
filieres.length      // 4

// Déstructuration — extraire des valeurs
const [premier, deuxieme, ...reste] = filieres;
// premier = "MIAGE", deuxieme = "Finance", reste = ["RH", "MBA"]
```

### Méthodes de base

```javascript
const etudiants = ["Amadou", "Fatou", "Ibrahima"];

// Ajouter / Supprimer
etudiants.push("Mariama");        // Ajoute à la fin → 4
etudiants.pop();                   // Retire le dernier → "Mariama"
etudiants.unshift("Ousmane");     // Ajoute au début
etudiants.shift();                 // Retire le premier

// Chercher
etudiants.indexOf("Fatou");       // 1
etudiants.includes("Ibrahima");   // true

// Extraire une partie
etudiants.slice(0, 2);            // ["Amadou", "Fatou"] (sans modifier)

// Modifier en place
etudiants.splice(1, 1);           // Retire 1 élément à l'index 1
etudiants.splice(1, 0, "Aïcha"); // Insère "Aïcha" à l'index 1

// Joindre
etudiants.join(", ");             // "Amadou, Fatou, Ibrahima"

// Trier
["banane", "ananas", "cerise"].sort(); // ["ananas", "banane", "cerise"]
[3, 1, 4, 1, 5].sort((a, b) => a - b); // [1, 1, 3, 4, 5] — tri numérique
```

### Les méthodes fonctionnelles — Le cœur du JS moderne

```javascript
const etudiants = [
    { nom: "Diallo",  note: 14, filiere: "MIAGE"   },
    { nom: "Sow",     note: 16, filiere: "Finance"  },
    { nom: "Ndiaye",  note: 9,  filiere: "MIAGE"    },
    { nom: "Faye",    note: 12, filiere: "RH"       },
    { nom: "Camara",  note: 18, filiere: "Finance"  },
];

// forEach — Exécuter une action sur chaque élément (sans retour)
etudiants.forEach(etudiant => {
    console.log(`${etudiant.nom} : ${etudiant.note}/20`);
});

// map — Transformer chaque élément → nouveau tableau
const noms = etudiants.map(e => e.nom);
// ["Diallo", "Sow", "Ndiaye", "Faye", "Camara"]

const cartes = etudiants.map(e => `
    <div class="carte">
        <h3>${e.nom}</h3>
        <p>${e.note}/20</p>
    </div>
`);

// filter — Garder les éléments qui satisfont la condition → nouveau tableau
const admis = etudiants.filter(e => e.note >= 10);
// [Diallo, Sow, Faye, Camara] — Ndiaye (9) est exclu

const miagistes = etudiants.filter(e => e.filiere === "MIAGE");
// [Diallo, Ndiaye]

// find — Trouver le PREMIER élément qui satisfait → un seul objet
const etudiant = etudiants.find(e => e.nom === "Sow");
// { nom: "Sow", note: 16, filiere: "Finance" }

// findIndex — Trouver l'INDEX du premier élément qui satisfait
const index = etudiants.findIndex(e => e.note > 15);
// 1 (index de Sow)

// some — Au moins un élément satisfait la condition ?
etudiants.some(e => e.note >= 18);   // true (Camara)

// every — Tous les éléments satisfont la condition ?
etudiants.every(e => e.note >= 10);  // false (Ndiaye a 9)

// reduce — Réduire le tableau à une seule valeur
const total = etudiants.reduce((somme, e) => somme + e.note, 0);
// 14 + 16 + 9 + 12 + 18 = 69
const moyenne = total / etudiants.length; // 13.8

// Chaîner les méthodes
const moyenneMiage = etudiants
    .filter(e => e.filiere === "MIAGE")         // [Diallo, Ndiaye]
    .map(e => e.note)                            // [14, 9]
    .reduce((sum, n) => sum + n, 0) / 2;        // 11.5
```

```{admonition} map / filter / reduce — La trinité du JS fonctionnel
:class: tip
Ces 3 méthodes sont au cœur de tout code JavaScript moderne. Mémorise-les :
- **`map`** : transformer (même nombre d'éléments, valeurs différentes)
- **`filter`** : sélectionner (moins d'éléments, même type)
- **`reduce`** : agréger (un seul résultat)

Elles ne modifient jamais le tableau original — elles retournent toujours un **nouveau tableau**.
```

---

## 3. Les objets

### Créer et accéder

```javascript
// Littéral objet
const etudiant = {
    prenom: "Amadou",
    nom: "Diallo",
    age: 20,
    filiere: "MIAGE",
    notes: [14, 12, 16],
    adresse: {                          // Objet imbriqué
        ville: "Dakar",
        quartier: "Plateau"
    }
};

// Accès par point (notation pointée)
etudiant.prenom                         // "Amadou"
etudiant.adresse.ville                  // "Dakar"

// Accès par crochet (utile si clé dynamique)
const cle = "nom";
etudiant[cle]                           // "Diallo"
etudiant["filiere"]                     // "MIAGE"

// Modifier
etudiant.age = 21;

// Ajouter une propriété
etudiant.email = "amadou.diallo@cesag.sn";

// Supprimer une propriété
delete etudiant.age;

// Vérifier l'existence d'une propriété
"prenom" in etudiant                    // true
etudiant.hasOwnProperty("telephone")   // false
```

### Déstructuration d'objet

```javascript
const { prenom, nom, filiere } = etudiant;
// Équivalent à :
// const prenom = etudiant.prenom;
// const nom = etudiant.nom;

// Renommer à la volée
const { prenom: firstName, nom: lastName } = etudiant;

// Valeur par défaut
const { email = "non renseigné" } = etudiant;

// Dans les paramètres de fonction
function afficherEtudiant({ prenom, nom, filiere, note = "—" }) {
    return `${prenom} ${nom} | ${filiere} | ${note}`;
}
afficherEtudiant(etudiant);
```

### Parcourir un objet

```javascript
const config = { theme: "vert", langue: "fr", notifications: true };

// Clés
Object.keys(config)     // ["theme", "langue", "notifications"]

// Valeurs
Object.values(config)   // ["vert", "fr", true]

// Paires clé/valeur
Object.entries(config)
// [["theme", "vert"], ["langue", "fr"], ["notifications", true]]

// Itérer
Object.entries(config).forEach(([cle, valeur]) => {
    console.log(`${cle} : ${valeur}`);
});
```

### Spread operator (`...`) — Copier et fusionner

```javascript
// Copier un objet (copie superficielle)
const original = { nom: "Diallo", note: 14 };
const copie = { ...original };
copie.note = 16;           // Ne modifie pas original

// Fusionner des objets
const base = { filiere: "MIAGE", annee: 1 };
const extra = { email: "test@cesag.sn", actif: true };
const complet = { ...base, ...extra, nom: "Diallo" };
// { filiere: "MIAGE", annee: 1, email: "...", actif: true, nom: "Diallo" }

// Copier et modifier en même temps
const etudiantMaj = { ...etudiant, note: 18, modifie: true };

// Spread sur tableaux
const a = [1, 2, 3];
const b = [4, 5, 6];
const c = [...a, ...b];     // [1, 2, 3, 4, 5, 6]
const d = [...a, 10, ...b]; // [1, 2, 3, 10, 4, 5, 6]
```

---

## 4. Les boucles

### `for` classique

```javascript
for (let i = 0; i < 5; i++) {
    console.log(`Tour ${i}`);
}

// Parcourir un tableau par index
const notes = [14, 12, 16, 18];
for (let i = 0; i < notes.length; i++) {
    console.log(`Note ${i + 1} : ${notes[i]}`);
}
```

### `for...of` — Pour les tableaux (moderne)

```javascript
const filieres = ["MIAGE", "Finance", "RH"];

for (const filiere of filieres) {
    console.log(filiere);
}

// Avec index — utilise entries()
for (const [index, filiere] of filieres.entries()) {
    console.log(`${index + 1}. ${filiere}`);
}
```

### `for...in` — Pour les objets

```javascript
const etudiant = { nom: "Diallo", note: 14, filiere: "MIAGE" };

for (const cle in etudiant) {
    console.log(`${cle} : ${etudiant[cle]}`);
}
```

### `while` et `do...while`

```javascript
// while : vérifie la condition AVANT
let tentatives = 0;
while (tentatives < 3) {
    console.log(`Tentative ${tentatives + 1}`);
    tentatives++;
}

// do...while : exécute AU MOINS une fois
let reponse;
do {
    reponse = prompt("Entrez votre nom :");
} while (reponse === "" || reponse === null);
```

### `break` et `continue`

```javascript
// break : sort de la boucle
for (const note of [14, 12, 8, 16, 18]) {
    if (note < 10) {
        console.log("Note éliminatoire trouvée !");
        break;
    }
    console.log(note);
}

// continue : passe à l'itération suivante
for (const note of [14, 12, 8, 16, 18]) {
    if (note < 10) continue;  // Ignore cette note
    console.log(note);         // N'affiche que 14, 12, 16, 18
}
```

---

## Résumé

```{admonition} Ce qu'il faut retenir
:class: tip
| Concept | Usage |
|---------|-------|
| Arrow function | `const fn = (x) => x * 2` |
| Paramètre rest | `function f(...args)` |
| Valeur par défaut | `function f(x = 0)` |
| `map` | Transformer chaque élément |
| `filter` | Sélectionner des éléments |
| `find` | Trouver le premier match |
| `reduce` | Agréger en une valeur |
| Déstructuration objet | `const { nom, age } = objet` |
| Spread | `{ ...objet, nouvelleProp: val }` |
| `for...of` | Parcourir un tableau |
| `for...in` | Parcourir un objet |
```

---

## TP 3 — Moteur de données de CESAG Connect

```{admonition} À faire — 1h30
:class: warning

Crée un fichier `logique.js` (séparé de app.js) avec ce tableau de données et toutes les fonctions demandées :

```javascript
const etudiants = [
    { id: 1, prenom: "Amadou",   nom: "Diallo",   filiere: "MIAGE",   note: 14, actif: true  },
    { id: 2, prenom: "Fatou",    nom: "Sow",      filiere: "Finance", note: 16, actif: true  },
    { id: 3, prenom: "Ibrahima", nom: "Ndiaye",   filiere: "MIAGE",   note: 9,  actif: false },
    { id: 4, prenom: "Mariama",  nom: "Faye",     filiere: "RH",      note: 12, actif: true  },
    { id: 5, prenom: "Ousmane",  nom: "Camara",   filiere: "Finance", note: 18, actif: true  },
    { id: 6, prenom: "Aïcha",    nom: "Ba",       filiere: "MBA",     note: 15, actif: true  },
];
```

**1. Statistiques (4 pts)**
```javascript
function calculerStats(etudiants) {
    // Retourne un objet avec : total, admis, moyenne, meilleure note, pire note
}
console.table(calculerStats(etudiants));
```

**2. Recherche et filtres (4 pts)**
```javascript
function rechercherParFiliere(etudiants, filiere) { /* ... */ }
function rechercherParNom(etudiants, terme) {
    // Recherche dans prenom ET nom, insensible à la casse
}
```

**3. Trier les étudiants (4 pts)**
```javascript
function trierPar(etudiants, critere) {
    // critere peut être "note", "nom", "filiere"
    // Retourne un NOUVEAU tableau trié (ne modifie pas l'original)
}
```

**4. Générer le HTML des cartes (4 pts)**
```javascript
function genererCarteHTML(etudiant) {
    // Retourne une chaîne HTML de carte étudiant
    // Utilise les template literals
    // Inclut les attributs data-id et data-filiere
}

function genererToutesLesCartes(etudiants) {
    return etudiants.map(genererCarteHTML).join("");
}
```

**5. Trouver par ID (2 pts)**
```javascript
function trouverParId(etudiants, id) {
    // Retourne l'étudiant correspondant ou null
}
```

Teste tout avec `console.log()` et `console.table()`.
```

---

*Séance suivante → [Séance 4 — Sélection et manipulation du DOM](../module2-dom/s04-selection-dom)*
