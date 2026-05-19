# Séance 6 — Formulaires interactifs et Validation JS

```{admonition} Objectifs
:class: tip
- Lire toutes les valeurs d'un formulaire avec JS
- Valider les données avec des conditions et des expressions régulières
- Afficher des messages d'erreur dynamiques ciblés
- Donner un feedback visuel en temps réel (champ par champ)
- Utiliser `FormData` pour récupérer tous les champs d'un coup
```

---

## 1. Lire les valeurs d'un formulaire

```html
<!-- inscription.html -->
<form id="form-inscription">
    <div class="champ">
        <label for="prenom">Prénom *</label>
        <input type="text" id="prenom" name="prenom" required>
        <span class="msg-erreur" id="err-prenom"></span>
    </div>

    <div class="champ">
        <label for="email">Email *</label>
        <input type="email" id="email" name="email" required>
        <span class="msg-erreur" id="err-email"></span>
    </div>

    <div class="champ">
        <label for="filiere">Filière *</label>
        <select id="filiere" name="filiere" required>
            <option value="">-- Choisir --</option>
            <option value="MIAGE">MIAGE</option>
            <option value="Finance">Finance</option>
            <option value="RH">Ressources Humaines</option>
        </select>
        <span class="msg-erreur" id="err-filiere"></span>
    </div>

    <div class="champ">
        <label for="mdp">Mot de passe *</label>
        <input type="password" id="mdp" name="mdp" required>
        <span class="msg-erreur" id="err-mdp"></span>
    </div>

    <div class="champ">
        <label for="mdp-confirm">Confirmer le mot de passe *</label>
        <input type="password" id="mdp-confirm" name="mdp-confirm" required>
        <span class="msg-erreur" id="err-mdp-confirm"></span>
    </div>

    <div class="champ">
        <input type="checkbox" id="cgu" name="cgu">
        <label for="cgu">J'accepte les conditions générales</label>
        <span class="msg-erreur" id="err-cgu"></span>
    </div>

    <button type="submit" id="btn-inscrire">S'inscrire</button>
</form>
```

```javascript
// Lire les valeurs individuellement
const prenom  = document.querySelector("#prenom").value.trim();
const email   = document.querySelector("#email").value.trim();
const filiere = document.querySelector("#filiere").value;
const mdp     = document.querySelector("#mdp").value;
const cgu     = document.querySelector("#cgu").checked;

// FormData — récupérer TOUS les champs en une fois
const form = document.querySelector("#form-inscription");
const donnees = new FormData(form);

donnees.get("prenom");    // Valeur du champ name="prenom"
donnees.get("email");
donnees.get("filiere");

// Convertir en objet classique
const objetDonnees = Object.fromEntries(donnees);
// { prenom: "Amadou", email: "...", filiere: "MIAGE", ... }
```

---

## 2. Les expressions régulières (Regex)

Les regex sont des **motifs de texte** qui permettent de valider le format d'une valeur.

### Syntaxe de base

```javascript
// Créer une regex
const motif = /pattern/flags;
const motif = new RegExp("pattern", "flags");

// Tester si une chaîne correspond au motif
motif.test("ma chaîne");   // → true ou false

// Flags courants
// i → insensible à la casse
// g → toutes les occurrences
// m → multi-ligne
```

### Regex essentielles pour les formulaires

```javascript
// Email
const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
regexEmail.test("amadou@cesag.sn");    // true
regexEmail.test("pas-un-email");       // false

// Téléphone sénégalais (7x xxx xx xx ou +221 7x...)
const regexTel = /^(\+221\s?)?(7[0-9])\s?[0-9]{3}\s?[0-9]{2}\s?[0-9]{2}$/;
regexTel.test("77 123 45 67");         // true
regexTel.test("+221 77 123 45 67");    // true

// Mot de passe fort (min 8 car., 1 majuscule, 1 chiffre, 1 spécial)
const regexMdp = /^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*]).{8,}$/;
regexMdp.test("MonMdp@2025");          // true
regexMdp.test("faible");               // false

// Nom (lettres, espaces, tirets, accents)
const regexNom = /^[a-zA-ZÀ-ÿ\s\-']{2,50}$/;
regexNom.test("Amadou Diallo");        // true
regexNom.test("A");                    // false (trop court)

// Code étudiant (2 lettres + 4 chiffres)
const regexCode = /^[A-Z]{2}[0-9]{4}$/;
regexCode.test("CS2025");              // true

// URL
const regexURL = /^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._+~#=]{2,256}\.[a-z]{2,6}/;
```

```{admonition} Déchiffrer une regex — Lexique rapide
:class: note
| Symbole | Signification |
|---------|---------------|
| `^` | Début de la chaîne |
| `$` | Fin de la chaîne |
| `.` | N'importe quel caractère |
| `*` | 0 fois ou plus |
| `+` | 1 fois ou plus |
| `?` | 0 ou 1 fois |
| `{n,m}` | Entre n et m fois |
| `[abc]` | a, b ou c |
| `[^abc]` | Tout sauf a, b, c |
| `[a-z]` | Lettre minuscule |
| `[0-9]` | Chiffre |
| `\s` | Espace, tab, retour |
| `\d` | Chiffre (= `[0-9]`) |
| `\w` | Lettre, chiffre ou `_` |
| `(?=...)` | Lookahead (condition) |
```

---

## 3. Architecture de validation — Le module `validation.js`

```javascript
// modules/validation.js

// ── Fonctions de validation ──────────────────────────────────

export function validerPrenom(valeur) {
    if (!valeur) return "Le prénom est obligatoire.";
    if (valeur.length < 2) return "Le prénom doit contenir au moins 2 caractères.";
    if (valeur.length > 50) return "Le prénom ne peut pas dépasser 50 caractères.";
    if (!/^[a-zA-ZÀ-ÿ\s\-']+$/.test(valeur)) return "Le prénom ne doit contenir que des lettres.";
    return null; // null = valide !
}

export function validerEmail(valeur) {
    if (!valeur) return "L'email est obligatoire.";
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(valeur)) return "Format d'email invalide.";
    return null;
}

export function validerMotDePasse(valeur) {
    if (!valeur) return "Le mot de passe est obligatoire.";
    if (valeur.length < 8) return "Le mot de passe doit contenir au moins 8 caractères.";
    if (!/[A-Z]/.test(valeur)) return "Le mot de passe doit contenir au moins une majuscule.";
    if (!/[0-9]/.test(valeur)) return "Le mot de passe doit contenir au moins un chiffre.";
    return null;
}

export function validerConfirmation(mdp, confirmation) {
    if (!confirmation) return "Veuillez confirmer votre mot de passe.";
    if (mdp !== confirmation) return "Les mots de passe ne correspondent pas.";
    return null;
}

export function validerFiliere(valeur) {
    const filieres = ["MIAGE", "Finance", "RH", "MBA"];
    if (!valeur) return "Veuillez choisir une filière.";
    if (!filieres.includes(valeur)) return "Filière invalide.";
    return null;
}
```

---

## 4. Affichage des erreurs — Feedback visuel

```javascript
// modules/validation.js (suite)

// ── Afficher / Cacher une erreur ─────────────────────────────

export function afficherErreur(idChamp, message) {
    const champ = document.querySelector(`#${idChamp}`);
    const msgEl = document.querySelector(`#err-${idChamp}`);

    champ.classList.add("invalide");
    champ.classList.remove("valide");
    msgEl.textContent = message;
    msgEl.classList.add("visible");
}

export function afficherSucces(idChamp) {
    const champ = document.querySelector(`#${idChamp}`);
    const msgEl = document.querySelector(`#err-${idChamp}`);

    champ.classList.remove("invalide");
    champ.classList.add("valide");
    msgEl.textContent = "";
    msgEl.classList.remove("visible");
}

export function reinitialiserChamp(idChamp) {
    const champ = document.querySelector(`#${idChamp}`);
    const msgEl = document.querySelector(`#err-${idChamp}`);
    champ.classList.remove("invalide", "valide");
    msgEl.textContent = "";
}
```

```css
/* style.css — Styles des états de validation */

/* Champ normal */
.champ input,
.champ select,
.champ textarea {
    width: 100%;
    padding: 10px 14px;
    border: 2px solid #ddd;
    border-radius: 6px;
    font-size: 15px;
    transition: border-color 0.2s, box-shadow 0.2s;
}

/* Champ valide */
.champ input.valide,
.champ select.valide {
    border-color: #1A7A2A;
    background-color: #f0f9f0;
}

/* Champ invalide */
.champ input.invalide,
.champ select.invalide {
    border-color: #c62828;
    background-color: #fdf0f0;
}

/* Focus */
.champ input:focus,
.champ select:focus {
    outline: none;
    border-color: #1A7A2A;
    box-shadow: 0 0 0 3px rgba(26, 122, 42, 0.15);
}

/* Message d'erreur */
.msg-erreur {
    display: none;
    color: #c62828;
    font-size: 13px;
    margin-top: 4px;
}

.msg-erreur.visible {
    display: block;
}
```

---

## 5. Validation complète du formulaire

```javascript
// app.js ou inscription.js

import {
    validerPrenom, validerEmail, validerMotDePasse,
    validerConfirmation, validerFiliere,
    afficherErreur, afficherSucces
} from "./modules/validation.js";

// ── Validation champ par champ (en temps réel) ──────────────

document.querySelector("#prenom").addEventListener("blur", (e) => {
    const erreur = validerPrenom(e.target.value.trim());
    erreur ? afficherErreur("prenom", erreur) : afficherSucces("prenom");
});

document.querySelector("#email").addEventListener("blur", (e) => {
    const erreur = validerEmail(e.target.value.trim());
    erreur ? afficherErreur("email", erreur) : afficherSucces("email");
});

document.querySelector("#mdp").addEventListener("input", (e) => {
    const erreur = validerMotDePasse(e.target.value);
    erreur ? afficherErreur("mdp", erreur) : afficherSucces("mdp");

    // Mettre à jour la barre de force
    mettreAJourForceMdp(e.target.value);
});

// ── Validation globale à la soumission ──────────────────────

document.querySelector("#form-inscription").addEventListener("submit", (e) => {
    e.preventDefault();

    const prenom    = document.querySelector("#prenom").value.trim();
    const email     = document.querySelector("#email").value.trim();
    const filiere   = document.querySelector("#filiere").value;
    const mdp       = document.querySelector("#mdp").value;
    const mdpConf   = document.querySelector("#mdp-confirm").value;
    const cgu       = document.querySelector("#cgu").checked;

    // Valider chaque champ
    const erreurs = {
        prenom:      validerPrenom(prenom),
        email:       validerEmail(email),
        filiere:     validerFiliere(filiere),
        mdp:         validerMotDePasse(mdp),
        "mdp-confirm": validerConfirmation(mdp, mdpConf),
    };

    if (!cgu) erreurs.cgu = "Vous devez accepter les conditions générales.";

    // Afficher toutes les erreurs
    let formulaireValide = true;
    for (const [champ, erreur] of Object.entries(erreurs)) {
        if (erreur) {
            afficherErreur(champ, erreur);
            formulaireValide = false;
        } else {
            afficherSucces(champ);
        }
    }

    // Si tout est valide → traiter
    if (formulaireValide) {
        const etudiant = { prenom, email, filiere };
        console.log("Inscription réussie :", etudiant);
        afficherMessageSucces("Inscription enregistrée avec succès !");
        e.target.reset();
    } else {
        // Focus sur le premier champ en erreur
        document.querySelector(".invalide")?.focus();
    }
});
```

---

## 6. Indicateur de force du mot de passe

```javascript
function mettreAJourForceMdp(mdp) {
    const barre = document.querySelector("#force-mdp");
    const texte = document.querySelector("#texte-force");

    let score = 0;
    if (mdp.length >= 8)              score++;
    if (/[A-Z]/.test(mdp))           score++;
    if (/[a-z]/.test(mdp))           score++;
    if (/[0-9]/.test(mdp))           score++;
    if (/[!@#$%^&*]/.test(mdp))      score++;

    const niveaux = ["", "Très faible", "Faible", "Moyen", "Fort", "Très fort"];
    const couleurs = ["", "#c62828", "#E8420A", "#f57c00", "#1A7A2A", "#0d5e1e"];

    barre.style.width   = `${score * 20}%`;
    barre.style.backgroundColor = couleurs[score] || "#ddd";
    texte.textContent   = niveaux[score] || "";
    texte.style.color   = couleurs[score] || "#888";
}
```

```html
<!-- HTML de la barre de force -->
<div class="force-conteneur">
    <div class="force-barre">
        <div id="force-mdp" style="height:4px; border-radius:2px; transition: width 0.3s, background-color 0.3s;"></div>
    </div>
    <span id="texte-force" style="font-size:13px;"></span>
</div>
```

---

## Résumé

```{admonition} Ce qu'il faut retenir
:class: tip
| Concept | Usage |
|---------|-------|
| `input.value.trim()` | Valeur nettoyée des espaces |
| `select.value` | Option sélectionnée |
| `checkbox.checked` | Vrai/faux |
| `regex.test(valeur)` | Tester un format |
| `e.preventDefault()` | Bloquer la soumission native |
| `blur` | Valider quand le champ perd le focus |
| `input` | Valider en temps réel (frappe par frappe) |
| Retourner `null` | Convention : null = valide |
| `FormData` | Lire tous les champs en une fois |
| `classList.add("invalide")` | Feedback visuel sur le champ |
```

---

## TP 6 — Formulaire d'inscription CESAG validé

```{admonition} À faire — 1h30
:class: warning

### Objectif
Créer le formulaire d'inscription complet avec validation JS temps réel.

**1. HTML du formulaire (2 pts)**
- Tous les champs : prénom, nom, email, filière (select), date de naissance, téléphone, mot de passe, confirmation, CGU
- Chaque champ a un `id`, un `name`, et un `<span class="msg-erreur" id="err-[champ]">`

**2. Module validation.js (5 pts)**
- `validerNom(v)` : obligatoire, 2–50 car., lettres uniquement
- `validerEmail(v)` : obligatoire, regex email
- `validerTelephone(v)` : optionnel, mais si renseigné → regex tel sénégalais
- `validerDateNaissance(v)` : obligatoire, étudiant doit avoir entre 16 et 35 ans
- `validerMotDePasse(v)` : min 8 car., 1 majuscule, 1 chiffre
- `validerConfirmation(mdp, conf)` : identiques
- `afficherErreur(id, msg)` et `afficherSucces(id)`

**3. Validation temps réel (4 pts)**
- Sur l'événement `blur` de chaque champ : valider et afficher le retour
- Sur l'événement `input` du mot de passe : barre de force

**4. Validation à la soumission (4 pts)**
- Valider TOUS les champs
- Bloquer si au moins une erreur
- Si tout valide : afficher un message de succès + reset du formulaire
- Focus automatique sur le premier champ en erreur

**5. CSS des états (3 pts)**
- `.valide` : bordure verte + fond légèrement vert
- `.invalide` : bordure rouge + fond légèrement rouge
- `.msg-erreur.visible` : affiché en rouge sous le champ
- Barre de force du mot de passe animée
```

---

*Séance suivante → [Séance 7 — Modals et localStorage](../module4-modals/s07-modals-storage)*
