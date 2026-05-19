# Séance 8 — Fetch API et données dynamiques

```{admonition} Objectifs
:class: tip
- Comprendre les Promises et le modèle asynchrone de JS
- Utiliser `fetch()` pour charger des données
- Maîtriser `async` / `await` pour écrire du code asynchrone lisible
- Lire et afficher des données JSON dans le DOM
- Gérer les erreurs réseau et les états de chargement
- Consommer une API REST publique
```

---

## 1. Le problème : JavaScript est asynchrone

JavaScript est **mono-thread** — il ne peut faire qu'une chose à la fois. Mais certaines opérations prennent du temps (réseau, fichiers, timers). Plutôt que de bloquer, JS les lance et **continue d'exécuter le reste du code** — puis traite le résultat quand il arrive.

```javascript
console.log("1 — Avant le fetch");

fetch("data/etudiants.json")
    .then(response => response.json())
    .then(data => console.log("3 — Données reçues :", data));

console.log("2 — Après le fetch (s'exécute avant la réponse !)");

// Ordre d'affichage :
// 1 — Avant le fetch
// 2 — Après le fetch (s'exécute avant la réponse !)
// 3 — Données reçues : [...]
```

---

## 2. Les Promises — Valeur future

Une **Promise** représente une opération asynchrone qui finira par réussir ou échouer.

```javascript
// États d'une Promise
// ⏳ pending   : en cours
// ✅ fulfilled : succès → .then()
// ❌ rejected  : échec  → .catch()

const maPromesse = new Promise((resolve, reject) => {
    const succes = true;
    if (succes) {
        resolve("Opération réussie !");
    } else {
        reject(new Error("Quelque chose a échoué."));
    }
});

maPromesse
    .then(resultat => console.log(resultat))    // "Opération réussie !"
    .catch(erreur  => console.error(erreur))
    .finally(() => console.log("Terminé (succès ou échec)"));

// Chaîner des Promises
fetch("data/etudiants.json")
    .then(response => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();   // Retourne une Promise
    })
    .then(etudiants => {
        afficherEtudiants(etudiants);
    })
    .catch(erreur => {
        console.error("Erreur :", erreur);
        afficherErreurReseau();
    });
```

---

## 3. `async` / `await` — Le style moderne

`async/await` est du "sucre syntaxique" sur les Promises — même fonctionnement, code plus lisible.

```javascript
// Une fonction async retourne toujours une Promise
async function chargerEtudiants() {
    // await "attend" la résolution de la Promise
    const response = await fetch("data/etudiants.json");
    const etudiants = await response.json();
    return etudiants;
}

// Équivalent EXACT en .then()
function chargerEtudiantsPromesse() {
    return fetch("data/etudiants.json")
        .then(r => r.json());
}

// Utiliser une fonction async
async function initialiserApp() {
    const etudiants = await chargerEtudiants();
    afficherEtudiants(etudiants);
}

initialiserApp();
```

### Gestion des erreurs avec try/catch

```javascript
async function chargerEtudiants() {
    try {
        const response = await fetch("data/etudiants.json");

        if (!response.ok) {
            throw new Error(`Erreur HTTP ${response.status} : ${response.statusText}`);
        }

        const etudiants = await response.json();
        return etudiants;

    } catch (erreur) {
        // Erreur réseau (pas de connexion) ou erreur HTTP
        console.error("Impossible de charger les données :", erreur.message);
        throw erreur; // Relancer pour que l'appelant puisse aussi gérer
    }
}

// Appel avec gestion d'erreur
async function initialiserApp() {
    try {
        afficherChargement(true);
        const etudiants = await chargerEtudiants();
        afficherEtudiants(etudiants);
    } catch (erreur) {
        afficherMessageErreur("Impossible de charger les données. Réessayez.");
    } finally {
        afficherChargement(false);  // Toujours cacher le loader
    }
}
```

---

## 4. Le fichier `data/etudiants.json`

```json
[
    {
        "id": 1,
        "prenom": "Amadou",
        "nom": "Diallo",
        "filiere": "MIAGE",
        "annee": 1,
        "note": 14.5,
        "email": "amadou.diallo@cesag.sn",
        "telephone": "77 123 45 67",
        "photo": "images/etudiants/1.jpg",
        "actif": true,
        "dateInscription": "2025-09-01"
    },
    {
        "id": 2,
        "prenom": "Fatou",
        "nom": "Sow",
        "filiere": "Finance",
        "annee": 2,
        "note": 16.0,
        "email": "fatou.sow@cesag.sn",
        "telephone": "76 987 65 43",
        "photo": "images/etudiants/2.jpg",
        "actif": true,
        "dateInscription": "2024-09-15"
    }
]
```

---

## 5. Module API — `modules/api.js`

```javascript
// modules/api.js

const BASE_URL = "data";  // Pour les fichiers JSON locaux
// const BASE_URL = "https://api.cesag.sn/v1";  // Pour une vraie API

// ── Chargement des étudiants ─────────────────────────────────

export async function fetchEtudiants() {
    const response = await fetch(`${BASE_URL}/etudiants.json`);
    if (!response.ok) throw new Error(`Erreur ${response.status}`);
    return response.json();
}

export async function fetchEtudiant(id) {
    const etudiants = await fetchEtudiants();
    const etudiant = etudiants.find(e => e.id === id);
    if (!etudiant) throw new Error(`Étudiant ${id} introuvable`);
    return etudiant;
}

// ── Simulation de POST (sans vrai serveur) ───────────────────

export async function simulerInscription(donnees) {
    // Simuler un délai réseau
    await new Promise(resolve => setTimeout(resolve, 800));

    // Simuler une validation serveur
    if (!donnees.email.includes("@cesag.sn")) {
        throw new Error("Email doit être un email CESAG.");
    }

    return { ...donnees, id: Date.now(), statut: "inscrit" };
}

// ── Consommer une API publique (exemple) ─────────────────────

export async function fetchPaysAfrique() {
    const response = await fetch(
        "https://restcountries.com/v3.1/region/africa?fields=name,flags,capital,population"
    );
    if (!response.ok) throw new Error("API pays indisponible");
    const pays = await response.json();
    return pays.sort((a, b) => a.name.common.localeCompare(b.name.common));
}
```

---

## 6. États de chargement — UX essentielle

```javascript
// L'utilisateur doit toujours savoir ce qui se passe

function afficherChargement(visible) {
    const loader = document.querySelector("#loader");
    const contenu = document.querySelector("#contenu-principal");

    if (visible) {
        loader.classList.remove("masque");
        contenu.classList.add("opaque");
    } else {
        loader.classList.add("masque");
        contenu.classList.remove("opaque");
    }
}

function afficherErreurReseau(message = "Erreur de chargement. Veuillez réessayer.") {
    const conteneur = document.querySelector("#liste-etudiants");
    conteneur.innerHTML = `
        <div class="erreur-reseau">
            <p>⚠️ ${message}</p>
            <button onclick="initialiserApp()">Réessayer</button>
        </div>
    `;
}

// Utilisation complète
async function initialiserApp() {
    try {
        afficherChargement(true);

        const etudiants = await fetchEtudiants();
        afficherEtudiants(etudiants);

    } catch (erreur) {
        console.error(erreur);
        afficherErreurReseau();
    } finally {
        afficherChargement(false);
    }
}
```

```html
<!-- HTML du loader -->
<div id="loader" class="masque">
    <div class="spinner"></div>
    <p>Chargement des étudiants...</p>
</div>
```

```css
/* CSS spinner */
.spinner {
    width: 40px;
    height: 40px;
    border: 4px solid #eee;
    border-top-color: #1A7A2A;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
    margin: 0 auto 12px;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

.masque { display: none; }
.opaque { opacity: 0.4; pointer-events: none; }
```

---

## 7. Requêtes parallèles avec `Promise.all`

```javascript
// Charger plusieurs ressources simultanément
async function chargerTout() {
    try {
        // Lance les 3 fetches en même temps (pas l'un après l'autre)
        const [etudiants, formations, actualites] = await Promise.all([
            fetchEtudiants(),
            fetch("data/formations.json").then(r => r.json()),
            fetch("data/actualites.json").then(r => r.json()),
        ]);

        afficherEtudiants(etudiants);
        afficherFormations(formations);
        afficherActualites(actualites);

    } catch (erreur) {
        // Si UNE des requêtes échoue, catch est déclenché
        console.error("Une ressource n'a pas pu être chargée :", erreur);
    }
}
```

---

## Résumé

```{admonition} Ce qu'il faut retenir
:class: tip
| Concept | Usage |
|---------|-------|
| `fetch(url)` | Effectuer une requête HTTP |
| `response.ok` | `true` si statut 200–299 |
| `response.json()` | Parser la réponse en objet JS |
| `async function` | Déclarer une fonction asynchrone |
| `await` | Attendre la résolution d'une Promise |
| `try / catch / finally` | Gérer les erreurs async |
| `throw new Error(msg)` | Lever une erreur manuellement |
| `Promise.all([p1, p2])` | Attendre plusieurs Promises en parallèle |
| État de chargement | Toujours afficher un loader + gérer l'erreur |
```

---

## TP 8 — CESAG Connect : données dynamiques

```{admonition} À faire — 1h30 (+ Devoir individuel)
:class: warning

**1. Charger depuis etudiants.json (5 pts)**
- Créer `data/etudiants.json` avec au moins 8 étudiants complets
- Au chargement de `index.html` : `fetchEtudiants()` puis `afficherEtudiants()`
- Loader visible pendant le chargement
- Gestion d'erreur avec message et bouton "Réessayer"

**2. Page de détail dynamique (4 pts)**
- `etudiant.html?id=3` : charger et afficher les données de l'étudiant #3
- Lire l'id avec `new URLSearchParams(window.location.search).get("id")`
- Si l'id n'existe pas : rediriger vers `index.html`

**3. Filtre + recherche + fetch (3 pts)**
- La recherche et les filtres fonctionnent sur les données chargées via fetch
- `rechercherEtudiants()` et `filtrerParFiliere()` s'appliquent après le chargement

**4. Bonus — API pays (2 pts)**
- Une section "Étudiants internationaux" qui charge et affiche les pays depuis `restcountries.com`
- Avec `Promise.all` : charger les étudiants ET les pays en même temps

---

### 🎯 Devoir Individuel (40% de la note finale)
**À faire en salle — 1h30 — Semaine suivante**

Le sujet portera sur :
- Manipulation DOM (sélection, modification, création)
- Gestion d'événements (click, input, submit)
- Validation d'un formulaire avec messages d'erreur
- Lecture/écriture dans localStorage
```

---

*Séance suivante → [Séance 9 — Librairies et Animations](../module6-librairies/s09-librairies)*
