# Séance 7 — Programmation Orientée Objet en JavaScript

```{admonition} Objectifs
:class: tip
- Comprendre les concepts fondamentaux de la POO (classe, objet, méthode, héritage)
- Déclarer des classes avec `class`, `constructor`, propriétés et méthodes
- Utiliser l'héritage avec `extends` et `super`
- Comprendre la notion d'encapsulation (propriétés privées avec `#`)
- Organiser son code avec les modules ES6 (`import` / `export`)
- Refactoriser CESAG Connect en utilisant des classes
```

---

## 1. Pourquoi la POO ? — Du code procédural au code objet

### Avant la POO — Code procédural

```javascript
// Tout est éparpillé : données et fonctions sans lien formel
const nom = "Diallo";
const prenom = "Amadou";
const note = 14;
const filiere = "MIAGE";

function calculerMention(note) { /* ... */ }
function validerEmail(email)   { /* ... */ }
function afficherEtudiant(nom, prenom, note) { /* ... */ }

// Quand on a 50 étudiants et 30 fonctions, c'est ingérable
```

### Avec la POO — Données + comportements regroupés

```javascript
// Tout ce qui concerne un étudiant est dans la classe Etudiant
class Etudiant {
    constructor(prenom, nom, note, filiere) {
        this.prenom  = prenom;
        this.nom     = nom;
        this.note    = note;
        this.filiere = filiere;
    }

    calculerMention() { /* ... */ }
    valider()         { /* ... */ }
    afficher()        { /* ... */ }
}

// Créer autant d'objets qu'on veut depuis la même "recette"
const amadou = new Etudiant("Amadou", "Diallo", 14, "MIAGE");
const fatou   = new Etudiant("Fatou",  "Sow",   16, "Finance");
```

---

## 2. Les classes — La syntaxe

### Déclaration d'une classe

```javascript
class Etudiant {

    // Le constructeur est appelé automatiquement avec "new"
    constructor(prenom, nom, note, filiere) {
        // "this" désigne l'objet en cours de création
        this.prenom  = prenom;
        this.nom     = nom;
        this.note    = note;
        this.filiere = filiere;
        this.id      = Date.now();  // Valeur calculée automatiquement
        this.actif   = true;        // Valeur par défaut
    }

    // Méthode — une fonction attachée à la classe
    getNomComplet() {
        return `${this.prenom} ${this.nom}`;
    }

    getMention() {
        if (this.note >= 16) return "Très bien";
        if (this.note >= 14) return "Bien";
        if (this.note >= 12) return "Assez bien";
        if (this.note >= 10) return "Passable";
        return "Insuffisant";
    }

    estAdmis() {
        return this.note >= 10;
    }

    toHTML() {
        return `
            <article class="carte" data-id="${this.id}">
                <h3>${this.getNomComplet()}</h3>
                <span class="badge">${this.filiere}</span>
                <p class="${this.estAdmis() ? 'admis' : 'ajourne'}">
                    ${this.note}/20 — ${this.getMention()}
                </p>
            </article>
        `;
    }

    // toString est appelé automatiquement dans un contexte string
    toString() {
        return `${this.getNomComplet()} (${this.filiere} — ${this.getMention()})`;
    }
}
```

### Instancier un objet avec `new`

```javascript
// "new" appelle le constructeur et crée un objet
const amadou = new Etudiant("Amadou", "Diallo", 14, "MIAGE");
const fatou   = new Etudiant("Fatou",  "Sow",   16, "Finance");

// Accéder aux propriétés et méthodes
amadou.prenom;            // "Amadou"
amadou.getNomComplet();   // "Amadou Diallo"
amadou.getMention();      // "Bien"
amadou.estAdmis();        // true
amadou.toHTML();          // "<article>..."

console.log(amadou.toString()); // "Amadou Diallo (MIAGE — Bien)"
console.log(`${amadou}`);       // Même résultat (toString implicite)

// Vérifier qu'un objet est instance d'une classe
amadou instanceof Etudiant;   // true
amadou instanceof Array;       // false
```

---

## 3. Getters et Setters — Propriétés calculées

```javascript
class Etudiant {
    constructor(prenom, nom, note, filiere) {
        this.prenom  = prenom;
        this.nom     = nom;
        this._note   = note;    // Convention : _ = propriété "interne"
        this.filiere = filiere;
    }

    // Getter — accessible comme une propriété (sans parenthèses)
    get nomComplet() {
        return `${this.prenom} ${this.nom}`;
    }

    get mention() {
        if (this._note >= 16) return "Très bien";
        if (this._note >= 14) return "Bien";
        if (this._note >= 12) return "Assez bien";
        if (this._note >= 10) return "Passable";
        return "Insuffisant";
    }

    get note() {
        return this._note;
    }

    // Setter — validation à l'assignation
    set note(valeur) {
        if (typeof valeur !== "number") throw new TypeError("La note doit être un nombre");
        if (valeur < 0 || valeur > 20)  throw new RangeError("La note doit être entre 0 et 20");
        this._note = valeur;
    }
}

const etudiant = new Etudiant("Amadou", "Diallo", 14, "MIAGE");

// Utilisation comme propriété (pas de parenthèses)
etudiant.nomComplet;   // "Amadou Diallo"
etudiant.mention;      // "Bien"
etudiant.note;         // 14

// Le setter valide automatiquement
etudiant.note = 18;    // ✅ OK
etudiant.note = 25;    // ❌ RangeError: La note doit être entre 0 et 20
etudiant.note = "A";   // ❌ TypeError: La note doit être un nombre
```

---

## 4. Propriétés et méthodes statiques

Les membres **statiques** appartiennent à la **classe elle-même**, pas aux instances :

```javascript
class Etudiant {
    // Compteur partagé par toutes les instances
    static nbEtudiants = 0;

    static NOTE_MINIMUM = 10;
    static FILIERES = ["MIAGE", "Finance", "RH", "MBA"];

    constructor(prenom, nom, note, filiere) {
        this.prenom  = prenom;
        this.nom     = nom;
        this.note    = note;
        this.filiere = filiere;
        Etudiant.nbEtudiants++; // Incrémenter à chaque création
    }

    // Méthode statique — s'appelle sur la classe, pas sur l'instance
    static validerFiliere(filiere) {
        return Etudiant.FILIERES.includes(filiere);
    }

    static fromJSON(json) {
        // Factory method : créer un Etudiant depuis un objet JSON
        return new Etudiant(json.prenom, json.nom, json.note, json.filiere);
    }
}

// Utilisation
Etudiant.validerFiliere("MIAGE");   // true
Etudiant.validerFiliere("Droit");   // false

// Créer depuis un JSON (utile avec fetch !)
const data = { prenom: "Amadou", nom: "Diallo", note: 14, filiere: "MIAGE" };
const etudiant = Etudiant.fromJSON(data);

// Accès au compteur
const e1 = new Etudiant("Amadou", "Diallo", 14, "MIAGE");
const e2 = new Etudiant("Fatou",  "Sow",   16, "Finance");
Etudiant.nbEtudiants;   // 2
```

---

## 5. Encapsulation — Propriétés privées avec `#`

```javascript
class CompteMDPHache {
    // Propriété privée (hors de la classe : inaccessible)
    #mdpHache;
    #tentatives = 0;
    static #MAX_TENTATIVES = 3;

    constructor(email, mdp) {
        this.email   = email;
        this.#mdpHache = this.#hacher(mdp);
    }

    // Méthode privée
    #hacher(mdp) {
        // Simulation (en vrai : bcrypt côté serveur)
        return btoa(mdp + "sel_secret");
    }

    verifierMdp(mdp) {
        if (this.#tentatives >= CompteMDPHache.#MAX_TENTATIVES) {
            throw new Error("Compte bloqué : trop de tentatives échouées.");
        }

        if (this.#hacher(mdp) === this.#mdpHache) {
            this.#tentatives = 0;
            return true;
        }

        this.#tentatives++;
        return false;
    }

    get tentativesRestantes() {
        return CompteMDPHache.#MAX_TENTATIVES - this.#tentatives;
    }
}

const compte = new CompteMDPHache("amadou@cesag.sn", "MonMdp@2025");
compte.verifierMdp("mauvais");      // false
compte.verifierMdp("MonMdp@2025"); // true
compte.#mdpHache;                   // ❌ SyntaxError — propriété privée !
```

---

## 6. L'héritage avec `extends` et `super`

L'héritage permet de créer une **classe enfant** qui hérite de toutes les propriétés et méthodes d'une **classe parente** et peut en ajouter ou en modifier.

```javascript
// Classe parente
class Personne {
    constructor(prenom, nom, email) {
        this.prenom = prenom;
        this.nom    = nom;
        this.email  = email;
    }

    getNomComplet() {
        return `${this.prenom} ${this.nom}`;
    }

    contacter() {
        return `Contacter ${this.getNomComplet()} : ${this.email}`;
    }

    toString() {
        return this.getNomComplet();
    }
}

// Classe enfant — hérite de Personne
class Etudiant extends Personne {
    constructor(prenom, nom, email, filiere, note) {
        // super() DOIT être appelé en premier dans le constructeur
        super(prenom, nom, email);

        // Propriétés supplémentaires
        this.filiere = filiere;
        this.note    = note;
    }

    // Méthodes supplémentaires
    getMention() {
        if (this.note >= 16) return "Très bien";
        if (this.note >= 14) return "Bien";
        if (this.note >= 12) return "Assez bien";
        if (this.note >= 10) return "Passable";
        return "Insuffisant";
    }

    // Redéfinir (override) une méthode parente
    toString() {
        // super.toString() appelle la méthode de Personne
        return `${super.toString()} — ${this.filiere} — ${this.getMention()}`;
    }
}

// Classe enfant pour les enseignants
class Enseignant extends Personne {
    constructor(prenom, nom, email, matiere, grade) {
        super(prenom, nom, email);
        this.matiere = matiere;
        this.grade   = grade;
    }

    toString() {
        return `${this.grade} ${super.toString()} — ${this.matiere}`;
    }
}
```

```javascript
// Utilisation
const amadou = new Etudiant("Amadou", "Diallo", "amadou@cesag.sn", "MIAGE", 14);
const prof   = new Enseignant("Mamadou", "Ndiaye", "m.ndiaye@cesag.sn", "HTML & CSS", "Dr.");

console.log(`${amadou}`);   // "Amadou Diallo — MIAGE — Bien"
console.log(`${prof}`);     // "Dr. Mamadou Ndiaye — HTML & CSS"

amadou.contacter();         // Hérité de Personne — fonctionne !
amadou instanceof Etudiant; // true
amadou instanceof Personne; // true aussi (héritage)
```

---

## 7. Classe `Catalogue` — Gérer une collection

```javascript
class Catalogue {
    #etudiants = [];

    constructor(etudiants = []) {
        this.#etudiants = etudiants.map(e =>
            e instanceof Etudiant ? e : Etudiant.fromJSON(e)
        );
    }

    // ── Accesseurs ──────────────────────────────────────────

    get tous() {
        return [...this.#etudiants]; // Copie pour protéger la liste interne
    }

    get count() {
        return this.#etudiants.length;
    }

    trouverParId(id) {
        return this.#etudiants.find(e => e.id === id) ?? null;
    }

    // ── Modifications ────────────────────────────────────────

    ajouter(etudiant) {
        if (!(etudiant instanceof Etudiant)) {
            throw new TypeError("Seuls des objets Etudiant peuvent être ajoutés.");
        }
        this.#etudiants.push(etudiant);
        return this;  // Retourner this permet le chaînage
    }

    supprimer(id) {
        const index = this.#etudiants.findIndex(e => e.id === id);
        if (index === -1) throw new Error(`Étudiant ${id} introuvable.`);
        this.#etudiants.splice(index, 1);
        return this;
    }

    // ── Filtres et tri ───────────────────────────────────────

    filtrerParFiliere(filiere) {
        if (filiere === "tous") return this.tous;
        return this.#etudiants.filter(e => e.filiere === filiere);
    }

    rechercher(terme) {
        const t = terme.toLowerCase();
        return this.#etudiants.filter(e =>
            e.prenom.toLowerCase().includes(t) ||
            e.nom.toLowerCase().includes(t)
        );
    }

    trierPar(critere = "nom") {
        return [...this.#etudiants].sort((a, b) => {
            switch (critere) {
                case "note-desc": return b.note - a.note;
                case "note-asc":  return a.note - b.note;
                case "nom":       return a.nom.localeCompare(b.nom);
                default:          return 0;
            }
        });
    }

    // ── Statistiques ─────────────────────────────────────────

    get stats() {
        const notes = this.#etudiants.map(e => e.note);
        return {
            total:      this.count,
            admis:      this.#etudiants.filter(e => e.estAdmis()).length,
            moyenne:    (notes.reduce((s, n) => s + n, 0) / notes.length).toFixed(2),
            max:        Math.max(...notes),
            min:        Math.min(...notes),
        };
    }

    // ── Persistance ──────────────────────────────────────────

    sauvegarder() {
        localStorage.setItem("catalogue", JSON.stringify(this.#etudiants));
        return this;
    }

    static charger() {
        const json = localStorage.getItem("catalogue");
        const data = json ? JSON.parse(json) : [];
        return new Catalogue(data);
    }
}
```

### Usage du Catalogue avec chaînage

```javascript
const catalogue = new Catalogue();

catalogue
    .ajouter(new Etudiant("Amadou", "Diallo", "amadou@cesag.sn", "MIAGE", 14))
    .ajouter(new Etudiant("Fatou",  "Sow",   "fatou@cesag.sn",  "Finance", 16))
    .ajouter(new Etudiant("Ibrahima", "Ndiaye", "ibrahima@cesag.sn", "MIAGE", 9))
    .sauvegarder();

catalogue.count;              // 3
catalogue.stats;              // { total: 3, admis: 2, moyenne: "13.00", max: 16, min: 9 }
catalogue.filtrerParFiliere("MIAGE");  // [Amadou, Ibrahima]
catalogue.rechercher("sow");           // [Fatou]
catalogue.trierPar("note-desc");       // [Fatou, Amadou, Ibrahima]

// Recharger depuis localStorage
const catalogueSauvegarde = Catalogue.charger();
```

---

## 8. Les modules ES6 — `import` / `export`

Les modules permettent de **diviser le code en fichiers** et de n'importer que ce dont on a besoin.

```javascript
// ─── models/Etudiant.js ───────────────────────────────────
export class Etudiant {
    // ... (code complet vu plus haut)
}

// ─── models/Catalogue.js ─────────────────────────────────
import { Etudiant } from "./Etudiant.js";

export class Catalogue {
    // ... (code complet vu plus haut)
}

// ─── ui/Modal.js ─────────────────────────────────────────
export class Modal {
    constructor(idOverlay) {
        this.overlay = document.querySelector(`#${idOverlay}`);
        // ... (code vu en S8)
    }

    ouvrir(titre, contenu) { /* ... */ }
    fermer() { /* ... */ }
}

// ─── app.js ──────────────────────────────────────────────
import { Catalogue } from "./models/Catalogue.js";
import { Etudiant  } from "./models/Etudiant.js";
import { Modal     } from "./ui/Modal.js";

const catalogue   = Catalogue.charger();
const modalProfil = new Modal("modal-profil");

document.addEventListener("DOMContentLoaded", () => {
    afficherEtudiants(catalogue.tous);
});
```

```html
<!-- Dans le HTML : type="module" est obligatoire pour les imports -->
<script type="module" src="app.js"></script>
```

```{admonition} type="module" — Deux effets importants
:class: note
Quand tu utilises `type="module"` :
1. `import`/`export` fonctionnent
2. Le script est automatiquement **différé** (équivalent à `defer`) — plus besoin de mettre le `<script>` en bas du `<body>`
3. Le code est en **mode strict** par défaut (`"use strict"`)
4. Les variables déclarées ne sont pas globales (elles restent dans leur module)
```

---

## 9. Refactorisation de CESAG Connect

Voici la nouvelle structure du projet après application de la POO :

```
cesag-connect/
├── index.html
├── inscription.html
├── etudiant.html
├── style.css
├── app.js                    ← Point d'entrée (type="module")
└── src/
    ├── models/
    │   ├── Personne.js       ← Classe de base
    │   ├── Etudiant.js       ← extends Personne
    │   └── Catalogue.js      ← Gère la collection
    ├── ui/
    │   ├── Modal.js          ← Composant Modal réutilisable
    │   ├── Toast.js          ← Notifications légères
    │   └── Renderer.js       ← Génération du HTML (toHTML, etc.)
    └── utils/
        ├── validation.js     ← Fonctions de validation
        └── storage.js        ← Couche localStorage
```

---

## Résumé

```{admonition} Ce qu'il faut retenir
:class: tip
| Concept | Syntaxe | Usage |
|---------|---------|-------|
| Classe | `class Nom { }` | Modèle pour créer des objets |
| Constructeur | `constructor(...) { this.x = x; }` | Initialisation |
| Instance | `new Nom(args)` | Créer un objet depuis la classe |
| Méthode | `nomMethode() { }` | Fonction attachée à la classe |
| Getter | `get prop() { return ... }` | Propriété calculée (sans `()`) |
| Setter | `set prop(v) { this._p = v; }` | Validation à l'assignation |
| Statique | `static prop` / `static methode()` | Appartient à la classe, pas à l'instance |
| Privé | `#nomProp` | Inaccessible hors de la classe |
| Héritage | `class Enfant extends Parent` | Hérite props + méthodes |
| Super | `super(args)` / `super.methode()` | Appelle le parent |
| Export | `export class Nom` | Rendre disponible à l'import |
| Import | `import { Nom } from "./fichier.js"` | Utiliser dans un autre fichier |
| `type="module"` | `<script type="module">` | Activer les modules dans le HTML |
```

---

## TP 7 — Refactoriser CESAG Connect en POO

```{admonition} À faire — 1h30
:class: warning

### Objectif
Réécrire le cœur de CESAG Connect en utilisant des classes et des modules.

**1. Classe `Etudiant` (5 pts)**
Dans `src/models/Etudiant.js` :
- Propriétés : `prenom`, `nom`, `email`, `filiere`, `note`, `id` (auto), `dateInscription` (auto)
- Getter `nomComplet`, getter `mention`, getter `estAdmis`
- Setter `note` avec validation (0–20)
- Méthode `toHTML()` qui retourne la carte HTML
- Méthode statique `fromJSON(obj)` et `validerFiliere(filiere)`
- `export class Etudiant`

**2. Classe `Catalogue` (6 pts)**
Dans `src/models/Catalogue.js` :
- Propriété privée `#etudiants`
- Getter `tous`, getter `count`, getter `stats`
- Méthodes `ajouter()`, `supprimer()`, `trouverParId()`
- Méthodes `filtrerParFiliere()`, `rechercher()`, `trierPar()`
- Méthodes `sauvegarder()` et méthode statique `charger()`
- Chaînage possible sur `ajouter()` et `sauvegarder()`

**3. Classe `Modal` (3 pts)**
Dans `src/ui/Modal.js` :
- Constructeur prend l'id de l'overlay
- Méthodes `ouvrir(titre, contenuHTML)` et `fermer()`
- Fermeture sur Escape, clic fond, bouton ✕

**4. Intégration dans app.js (3 pts)**
- `import` des classes
- `const catalogue = Catalogue.charger()` au démarrage
- Délégation d'événements sur le catalogue
- Toutes les fonctions du TP5 réécrites pour utiliser `catalogue.filtrerParFiliere()`, `catalogue.rechercher()`, etc.

**5. `type="module"` et organisation (3 pts)**
- `<script type="module" src="app.js">` dans le HTML
- Fichiers dans `src/models/` et `src/ui/`
- Aucune variable globale dans `app.js` (tout passe par les classes)
```

---

*Séance suivante → [Séance 8 — Modals et localStorage](../module5-modals/s08-modals-storage)*
