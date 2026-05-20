# Séance 7 — Modals, localStorage et partage de données

```{admonition} Objectifs
:class: tip
- Créer des fenêtres modales accessibles (ouverture, fermeture, fond)
- Stocker et lire des données avec `localStorage` et `sessionStorage`
- Sérialiser des objets avec `JSON.stringify` / `JSON.parse`
- Partager des données entre pages via le storage
- Construire un module de stockage réutilisable
```

---

## 1. Les fenêtres modales

Une **modal** est une boîte de dialogue qui s'affiche par-dessus la page, bloquant l'interaction avec le reste jusqu'à fermeture.

### Structure HTML de base

```html
<!-- Bouton déclencheur -->
<button class="btn-voir" data-id="1">Voir le profil</button>

<!-- La modal — cachée par défaut -->
<div class="modal-overlay" id="modal-profil" aria-hidden="true" role="dialog">
    <div class="modal-conteneur">
        <div class="modal-entete">
            <h2 class="modal-titre" id="modal-titre">Profil étudiant</h2>
            <button class="modal-fermer" id="modal-fermer" aria-label="Fermer">✕</button>
        </div>
        <div class="modal-corps" id="modal-corps">
            <!-- Contenu injecté par JS -->
        </div>
        <div class="modal-pied">
            <button class="btn-secondaire" id="modal-annuler">Fermer</button>
            <button class="btn-primaire" id="modal-confirmer">Contacter</button>
        </div>
    </div>
</div>
```

### CSS de la modal

```css
/* Fond semi-transparent */
.modal-overlay {
    position: fixed;
    inset: 0;                          /* top:0; right:0; bottom:0; left:0 */
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.25s ease, visibility 0.25s ease;
}

/* Modal visible */
.modal-overlay.ouverte {
    opacity: 1;
    visibility: visible;
}

/* Boîte de la modal */
.modal-conteneur {
    background: white;
    border-radius: 12px;
    width: 90%;
    max-width: 520px;
    max-height: 90vh;
    overflow-y: auto;
    transform: translateY(-20px) scale(0.97);
    transition: transform 0.25s ease;
}

.modal-overlay.ouverte .modal-conteneur {
    transform: translateY(0) scale(1);
}

/* En-tête */
.modal-entete {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 24px;
    border-bottom: 1px solid #eee;
}

.modal-titre { font-size: 1.1em; font-weight: bold; color: #1A7A2A; }

.modal-fermer {
    background: none;
    border: none;
    font-size: 1.2em;
    cursor: pointer;
    color: #888;
    padding: 4px 8px;
    border-radius: 4px;
    transition: background 0.2s;
}
.modal-fermer:hover { background: #f0f0f0; color: #333; }

.modal-corps { padding: 24px; }

.modal-pied {
    display: flex;
    justify-content: flex-end;
    gap: 12px;
    padding: 16px 24px;
    border-top: 1px solid #eee;
}
```

### JS — Ouvrir et fermer

```javascript
// modules/modal.js

export class Modal {
    constructor(idOverlay) {
        this.overlay = document.querySelector(`#${idOverlay}`);
        this.corps   = this.overlay.querySelector(".modal-corps");
        this.titre   = this.overlay.querySelector(".modal-titre");

        // Fermer sur clic du fond (overlay)
        this.overlay.addEventListener("click", (e) => {
            if (e.target === this.overlay) this.fermer();
        });

        // Fermer sur bouton ✕
        this.overlay.querySelector(".modal-fermer")
            ?.addEventListener("click", () => this.fermer());

        // Fermer sur Escape
        document.addEventListener("keydown", (e) => {
            if (e.key === "Escape" && this.estOuverte()) this.fermer();
        });
    }

    ouvrir(titre, contenuHTML) {
        this.titre.textContent = titre;
        this.corps.innerHTML   = contenuHTML;
        this.overlay.classList.add("ouverte");
        this.overlay.setAttribute("aria-hidden", "false");
        document.body.style.overflow = "hidden"; // Bloquer le scroll
        this.overlay.querySelector(".modal-fermer")?.focus();
    }

    fermer() {
        this.overlay.classList.remove("ouverte");
        this.overlay.setAttribute("aria-hidden", "true");
        document.body.style.overflow = "";
    }

    estOuverte() {
        return this.overlay.classList.contains("ouverte");
    }
}
```

### Utilisation dans app.js

```javascript
import { Modal } from "./modules/modal.js";

const modalProfil = new Modal("modal-profil");

// Ouvrir avec délégation sur la liste
document.querySelector("#liste-etudiants").addEventListener("click", (e) => {
    const btn = e.target.closest(".btn-voir");
    if (!btn) return;

    const id = parseInt(btn.dataset.id);
    const etudiant = etudiants.find(e => e.id === id);

    modalProfil.ouvrir(
        `${etudiant.prenom} ${etudiant.nom}`,
        `
        <div class="profil">
            <img src="images/${id}.jpg" alt="Photo" onerror="this.src='images/avatar.png'">
            <table>
                <tr><td>Filière</td><td>${etudiant.filiere}</td></tr>
                <tr><td>Note</td><td>${etudiant.note}/20</td></tr>
                <tr><td>Email</td><td>${etudiant.email || "—"}</td></tr>
            </table>
        </div>
        `
    );
});
```

---

## 2. localStorage — Persister les données

`localStorage` stocke des données **côté navigateur**, qui **persistent après fermeture** de l'onglet.

```javascript
// ── Écrire ──────────────────────────────────────────────────

// Chaîne simple
localStorage.setItem("langue", "fr");
localStorage.setItem("theme", "clair");

// Objet → on doit le convertir en JSON string
const etudiant = { id: 1, nom: "Diallo", note: 14 };
localStorage.setItem("etudiant-actuel", JSON.stringify(etudiant));

// Tableau
const favoris = [1, 3, 5];
localStorage.setItem("favoris", JSON.stringify(favoris));

// ── Lire ────────────────────────────────────────────────────

const langue = localStorage.getItem("langue");   // "fr"

// Objet → on doit parser le JSON
const etudiantJSON = localStorage.getItem("etudiant-actuel");
const etudiantObj  = etudiantJSON ? JSON.parse(etudiantJSON) : null;

// Tableau
const favorisJSON  = localStorage.getItem("favoris");
const favorisArr   = favorisJSON ? JSON.parse(favorisJSON) : [];

// ── Supprimer ────────────────────────────────────────────────

localStorage.removeItem("langue");         // Supprimer une clé
localStorage.clear();                       // Vider tout le localStorage

// ── Vérifier l'existence ─────────────────────────────────────

localStorage.getItem("langue") !== null    // true si la clé existe
```

### sessionStorage — Données temporaires

Identique à `localStorage` en termes d'API, mais les données **disparaissent à la fermeture de l'onglet** :

```javascript
sessionStorage.setItem("etape-formulaire", "2");
sessionStorage.getItem("etape-formulaire");
sessionStorage.removeItem("etape-formulaire");
sessionStorage.clear();
```

| | `localStorage` | `sessionStorage` |
|---|---|---|
| Durée | Permanent | Onglet ouvert seulement |
| Taille | ~5–10 Mo | ~5 Mo |
| Portée | Même origine | Même onglet + origine |
| Partagé | Tous les onglets | Non |

---

## 3. Module de stockage — `storage.js`

```javascript
// modules/storage.js

const CLE_ETUDIANTS = "cesag_connect_etudiants";
const CLE_THEME     = "cesag_connect_theme";
const CLE_FILTRES   = "cesag_connect_filtres";

// ── Étudiants ────────────────────────────────────────────────

export function sauvegarderEtudiants(etudiants) {
    localStorage.setItem(CLE_ETUDIANTS, JSON.stringify(etudiants));
}

export function chargerEtudiants() {
    const json = localStorage.getItem(CLE_ETUDIANTS);
    return json ? JSON.parse(json) : [];
}

export function ajouterEtudiant(etudiant) {
    const liste = chargerEtudiants();
    const id = liste.length > 0 ? Math.max(...liste.map(e => e.id)) + 1 : 1;
    const nouveau = { ...etudiant, id, dateInscription: new Date().toISOString() };
    liste.push(nouveau);
    sauvegarderEtudiants(liste);
    return nouveau;
}

export function modifierEtudiant(id, modifications) {
    const liste = chargerEtudiants();
    const index = liste.findIndex(e => e.id === id);
    if (index === -1) return null;
    liste[index] = { ...liste[index], ...modifications };
    sauvegarderEtudiants(liste);
    return liste[index];
}

export function supprimerEtudiant(id) {
    const liste = chargerEtudiants().filter(e => e.id !== id);
    sauvegarderEtudiants(liste);
}

// ── Thème ────────────────────────────────────────────────────

export function sauvegarderTheme(theme) {
    localStorage.setItem(CLE_THEME, theme);
}

export function chargerTheme() {
    return localStorage.getItem(CLE_THEME) || "clair";
}
```

---

## 4. Partager des données entre pages

```javascript
// Page A (inscription.html) — Après validation du formulaire
import { ajouterEtudiant } from "./modules/storage.js";

form.addEventListener("submit", (e) => {
    e.preventDefault();
    // ... validation ...
    if (formulaireValide) {
        const nouvelEtudiant = ajouterEtudiant({ prenom, nom, email, filiere });
        // Stocker l'ID pour la page de confirmation
        sessionStorage.setItem("derniere-inscription", JSON.stringify(nouvelEtudiant));
        // Rediriger vers la page principale
        window.location.href = "index.html?nouveau=1";
    }
});

// Page B (index.html) — Au chargement
import { chargerEtudiants } from "./modules/storage.js";

document.addEventListener("DOMContentLoaded", () => {
    // Lire les paramètres URL
    const params = new URLSearchParams(window.location.search);

    if (params.get("nouveau") === "1") {
        const dernierJSON = sessionStorage.getItem("derniere-inscription");
        if (dernierJSON) {
            const dernier = JSON.parse(dernierJSON);
            afficherNotification(`Bienvenue, ${dernier.prenom} ! Inscription réussie.`);
            sessionStorage.removeItem("derniere-inscription");
        }
    }

    // Charger et afficher les étudiants depuis le storage
    const etudiants = chargerEtudiants();
    afficherEtudiants(etudiants.length > 0 ? etudiants : etudiantsDefaut);
});
```

---

## Résumé

```{admonition} Ce qu'il faut retenir
:class: tip
| Concept | Usage |
|---------|-------|
| `classList.toggle("ouverte")` | Afficher/cacher la modal |
| `position: fixed; inset: 0` | Fond couvrant tout l'écran |
| `document.body.style.overflow = "hidden"` | Bloquer le scroll |
| `e.key === "Escape"` | Fermer au clavier |
| `localStorage.setItem(clé, valeur)` | Sauvegarder (chaîne) |
| `localStorage.getItem(clé)` | Lire |
| `localStorage.removeItem(clé)` | Supprimer |
| `JSON.stringify(objet)` | Objet → chaîne JSON |
| `JSON.parse(json)` | Chaîne JSON → objet |
| `sessionStorage` | Temporaire (durée de vie = onglet) |
| `window.location.href` | Rediriger vers une autre page |
| `new URLSearchParams(...)` | Lire les paramètres d'URL |
```

---

## TP 7 — CESAG Connect : Profils et persistance

```{admonition} À faire — 1h30
:class: warning

**1. Modal de profil étudiant (5 pts)**
- Clic sur "Voir le profil" → modal avec toutes les infos de l'étudiant
- Fermeture : bouton ✕, clic sur le fond, touche Escape
- Animation CSS (opacity + translateY)
- Bouton "Contacter" dans le pied : ouvre `mailto:` de l'étudiant

**2. Persistance avec localStorage (5 pts)**
- Au chargement : charger les étudiants depuis `localStorage`
- Si vide : charger les données par défaut et les sauvegarder
- Après inscription (TP6) : `ajouterEtudiant()` et redirection vers `index.html`
- Badge "Nouveau" sur les cartes inscrites depuis moins de 24h

**3. Favoris (3 pts)**
- Bouton "♡" sur chaque carte
- Au clic : ajoute/retire l'ID des favoris dans `localStorage`
- Les cartes favorites s'affichent en premier
- Filtre "Favoris uniquement" dans la barre de filtres

**4. Notification de confirmation (2 pts)**
- Après retour depuis `inscription.html?nouveau=1`
- Toast notification en haut à droite : "Bienvenue [prénom] !"
- Disparaît après 3 secondes (`setTimeout`)
```

---

*Séance suivante → [Séance 8 — Fetch API et données dynamiques](../module6-fetch/s09-fetch-api)*
