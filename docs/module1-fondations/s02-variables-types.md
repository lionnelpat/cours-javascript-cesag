# Séance 2 — Variables, types, conditions et opérateurs

```{admonition} Objectifs
:class: tip
- Déclarer des variables avec `let`, `const`, `var`
- Connaître les types de données JS
- Écrire des conditions `if/else`, ternaires, `switch`
- Utiliser la console pour déboguer
- Comprendre la coercition de type (les pièges de JS)
```

---

## 1. Les variables

### `var`, `let`, `const` — Lequel utiliser ?

```javascript
// var — ANCIEN, à éviter (portée function, peut être redéclaré)
var nom = "Amadou";
var nom = "Fatou"; // ← pas d'erreur ! C'est le problème.

// let — MODERNE, valeur modifiable (portée bloc)
let age = 20;
age = 21;           // ✅ OK — modification autorisée
let age = 22;       // ❌ Erreur — ne peut pas être redéclaré

// const — MODERNE, référence constante (portée bloc)
const CESAG = "Centre Africain d'Études Supérieures en Gestion";
CESAG = "autre";    // ❌ Erreur — ne peut pas être réassigné
```

```{admonition} Règle d'or — const par défaut
:class: tip
Utilise **toujours `const`** par défaut. Passe à **`let`** uniquement si tu sais que la valeur changera. N'utilise **jamais `var`** dans du code moderne.

Cette règle force à réfléchir : "Est-ce que cette valeur doit changer ?" Si oui → `let`. Sinon → `const`.
```

### La portée (scope)

```javascript
// Portée globale
const langue = "fr";

function maFonction() {
    // Portée locale — visible uniquement dans cette fonction
    const message = "Bonjour";
    console.log(langue);   // ✅ Accès à la portée globale
    console.log(message);  // ✅ Accès local
}

console.log(message); // ❌ ReferenceError — message n'existe pas ici

// Portée bloc (let/const)
if (true) {
    let x = 10;
    const y = 20;
}
console.log(x); // ❌ ReferenceError — x limité au bloc if
```

---

## 2. Les types de données

### Les 7 types primitifs

```javascript
// String — chaîne de caractères
const nom = "Amadou Diallo";
const filiere = 'MIAGE L1';
const message = `Bonjour, ${nom} !`;  // Template literal (backtick)

// Number — entiers ET décimaux (un seul type)
const age = 20;
const moyenne = 14.5;
const MAX = Infinity;
const erreur = NaN;       // Not a Number (résultat d'opération invalide)

// Boolean — vrai ou faux
const estEtudiant = true;
const estMajeur = false;

// null — absence intentionnelle de valeur
const photo = null;       // "pas de photo pour l'instant"

// undefined — variable déclarée mais pas encore assignée
let adresse;
console.log(adresse);     // undefined

// Symbol — identifiant unique (avancé)
const id = Symbol("id");

// BigInt — très grands entiers
const grandNombre = 9007199254740991n;
```

### Le type complexe — Object

```javascript
// Objet
const etudiant = {
    nom: "Diallo",
    prenom: "Amadou",
    age: 20,
    actif: true
};

// Tableau (Array) — un objet spécial
const filieres = ["MIAGE", "Finance", "RH", "MBA"];

// Fonction — aussi un objet en JS !
const saluer = function(nom) { return `Bonjour, ${nom} !`; };
```

### Vérifier le type — `typeof`

```javascript
typeof "texte"        // "string"
typeof 42             // "number"
typeof true           // "boolean"
typeof undefined      // "undefined"
typeof null           // "object"  ← bug historique de JS !
typeof {}             // "object"
typeof []             // "object"  ← tableaux aussi
typeof function(){}   // "function"

// Pour distinguer tableau d'objet :
Array.isArray([1, 2, 3])  // true
Array.isArray({a: 1})     // false
```

---

## 3. Les opérateurs

### Opérateurs arithmétiques

```javascript
const a = 10, b = 3;

console.log(a + b);   // 13  — addition
console.log(a - b);   // 7   — soustraction
console.log(a * b);   // 30  — multiplication
console.log(a / b);   // 3.333... — division
console.log(a % b);   // 1   — modulo (reste de la division)
console.log(a ** b);  // 1000 — puissance (10³)

// Opérateurs d'assignation
let score = 0;
score += 5;    // score = score + 5  → 5
score -= 2;    // score = score - 2  → 3
score *= 2;    // score = score * 2  → 6
score++;       // score = score + 1  → 7 (post-incrément)
++score;       // score = score + 1  → 8 (pré-incrément)
score--;       // 7
```

### Opérateurs de comparaison

```javascript
// == et != : comparaison AVEC coercition (à éviter)
"5" == 5    // true  ← JS convertit "5" en nombre
null == undefined // true

// === et !== : comparaison STRICTE (type + valeur)
"5" === 5   // false ← types différents
5 === 5     // true

console.log(10 > 5);   // true
console.log(10 >= 10); // true
console.log(5 < 3);    // false
console.log(5 <= 5);   // true
```

```{admonition} Toujours utiliser === et !== !
:class: important
`==` fait de la coercition de type implicite, ce qui produit des résultats surprenants :
```javascript
0 == false   // true ← dangereux !
"" == false  // true ← dangereux !
[] == false  // true ← dangereux !
```
`===` compare strictement le type ET la valeur. **Toujours utiliser `===`.**
```

### Opérateurs logiques

```javascript
// && — ET logique (les deux doivent être vrais)
true && true    // true
true && false   // false

// || — OU logique (au moins un doit être vrai)
true || false   // true
false || false  // false

// ! — NON (inverse)
!true    // false
!false   // true

// Exemples pratiques
const age = 20;
const aUnCompte = true;

if (age >= 18 && aUnCompte) {
    console.log("Accès autorisé");
}

// ?? — Nullish Coalescing (valeur par défaut si null/undefined)
const photo = null;
const photoAffichee = photo ?? "avatar-defaut.png";
// → "avatar-defaut.png"

// || pour valeur par défaut (attention : 0 et "" sont falsy !)
const nom = "" || "Anonyme";  // → "Anonyme" (car "" est falsy)
const nom2 = "" ?? "Anonyme"; // → "" (car "" n'est pas null/undefined)
```

---

## 4. Les conditions

### `if / else if / else`

```javascript
const note = 14;

if (note >= 16) {
    console.log("Très bien");
} else if (note >= 14) {
    console.log("Bien");
} else if (note >= 12) {
    console.log("Assez bien");
} else if (note >= 10) {
    console.log("Passable");
} else {
    console.log("Insuffisant");
}
```

### L'opérateur ternaire

```javascript
// Syntaxe : condition ? valeur_si_vrai : valeur_si_faux
const age = 20;
const statut = age >= 18 ? "Majeur" : "Mineur";
console.log(statut); // "Majeur"

// Usage courant : affichage conditionnel
const note = 12;
const mention = note >= 16 ? "TB" : note >= 14 ? "B" : note >= 12 ? "AB" : "P";
```

### `switch`

```javascript
const filiere = "MIAGE";

switch (filiere) {
    case "MIAGE":
        console.log("Mathématiques et Informatique Appliquées");
        break;
    case "Finance":
        console.log("Master Finance");
        break;
    case "RH":
        console.log("Master Ressources Humaines");
        break;
    default:
        console.log("Filière inconnue");
}
```

### Les valeurs "falsy" — Pièges classiques

En JavaScript, ces valeurs sont considérées comme **fausses** dans un contexte booléen :

```javascript
// Valeurs FALSY (fausses)
if (false)     { /* non exécuté */ }
if (0)         { /* non exécuté */ }
if ("")        { /* non exécuté */ }  // chaîne vide
if (null)      { /* non exécuté */ }
if (undefined) { /* non exécuté */ }
if (NaN)       { /* non exécuté */ }

// Toutes les autres valeurs sont TRUTHY (vraies)
if ("0")       { /* exécuté ! — chaîne non vide */ }
if ([])        { /* exécuté ! — tableau vide est truthy */ }
if ({})        { /* exécuté ! — objet vide est truthy */ }
if (-1)        { /* exécuté ! — tout nombre ≠ 0 est truthy */ }
```

---

## 5. Les template literals (gabarits de chaîne)

Les backticks `` ` `` permettent d'insérer des expressions dans des chaînes :

```javascript
const prenom = "Amadou";
const nom = "Diallo";
const note = 14.5;

// Ancienne méthode (concaténation — à éviter)
const msg1 = "Bonjour, " + prenom + " " + nom + " ! Ta note est : " + note + "/20";

// Template literal (moderne — à utiliser)
const msg2 = `Bonjour, ${prenom} ${nom} ! Ta note est : ${note}/20`;

// Expressions dans les backticks
const msg3 = `Résultat : ${note >= 10 ? "Admis" : "Ajourné"}`;

// Multi-ligne
const html = `
  <div class="carte">
    <h2>${prenom} ${nom}</h2>
    <p>Note : ${note}/20</p>
  </div>
`;
```

---

## 6. Débogage avec la console

```javascript
// Afficher une valeur
console.log("Valeur :", maVariable);

// Afficher un objet lisiblement
console.log(JSON.stringify(monObjet, null, 2));

// Grouper des messages
console.group("Infos étudiant");
console.log("Nom :", nom);
console.log("Note :", note);
console.groupEnd();

// Tableau formaté
console.table([{nom: "Diallo", note: 14}, {nom: "Sow", note: 16}]);

// Mesurer le temps d'exécution
console.time("mon-calcul");
// ... code à mesurer ...
console.timeEnd("mon-calcul");

// Erreur et avertissement
console.error("Erreur critique !");
console.warn("Attention, valeur nulle !");
```

---

## Résumé

```{admonition} Ce qu'il faut retenir
:class: tip
| Concept | À retenir |
|---------|-----------|
| `const` | Par défaut pour toute variable |
| `let` | Seulement si la valeur change |
| `var` | Ne jamais utiliser |
| `===` | Toujours utiliser (jamais `==`) |
| Template literals | `` `Bonjour ${nom}` `` |
| Falsy values | `false, 0, "", null, undefined, NaN` |
| `typeof` | Vérifier le type d'une variable |
| `??` | Valeur par défaut si null/undefined |
```

---

## TP 2 — Logique métier de CESAG Connect

```{admonition} À faire — 1h30
:class: warning

### Dans la console DevTools (30 min)
Teste les expressions suivantes dans la console Chrome et note les résultats :
1. `typeof null` — surprise ?
2. `"5" === 5` vs `"5" == 5`
3. `0 || "valeur par défaut"` vs `0 ?? "valeur par défaut"`
4. `[] == false` — pourquoi ?

### Dans app.js (1h)
Écris les fonctions suivantes (sans DOM pour l'instant, juste logique) :

**1. Calculer la mention (5 pts)**
```javascript
function calculerMention(note) {
    // Retourne "Très bien", "Bien", "Assez bien", "Passable", ou "Insuffisant"
    // Utilise un ternaire ou switch
}
console.log(calculerMention(17)); // "Très bien"
console.log(calculerMention(11)); // "Passable"
```

**2. Valider un email (5 pts)**
```javascript
function estEmailValide(email) {
    // Retourne true si l'email contient @ et un point après
    // Pour l'instant : vérifie juste que email.includes("@") && email.includes(".")
    // On fera la vraie validation avec regex en S6
}
```

**3. Formater un étudiant (5 pts)**
```javascript
const etudiant = { prenom: "Amadou", nom: "Diallo", filiere: "MIAGE", note: 14.5 };

function formaterEtudiant(etudiant) {
    const mention = calculerMention(etudiant.note);
    return `${etudiant.prenom} ${etudiant.nom} — ${etudiant.filiere} — ${mention} (${etudiant.note}/20)`;
}
console.log(formaterEtudiant(etudiant));
// → "Amadou Diallo — MIAGE — Bien (14.5/20)"
```

**4. Générer un identifiant (5 pts)**
```javascript
function genererIdEtudiant(prenom, nom, annee) {
    // Retourne "AD-2025" pour Amadou Diallo, 2025
    // Première lettre du prénom + Première lettre du nom + "-" + annee
}
```
```

---

*Séance suivante → [Séance 3 — Fonctions, tableaux et objets](s03-fonctions-tableaux)*
