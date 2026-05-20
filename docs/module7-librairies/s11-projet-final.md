# Séance 10 — Projet Final : Soutenance

```{admonition} Séance de clôture
:class: tip
Cette séance est consacrée aux **soutenances des projets de groupe**. Chaque groupe présente son application web JavaScript complète pendant **10 minutes**, suivies de **5 minutes de questions**.
```

---

## 1. Récapitulatif du projet

Tout au long de ce cours, tu as construit **CESAG Connect**, un mini-portail étudiant. Le projet de groupe est une **application web originale** de votre choix, qui doit intégrer les compétences acquises.

### Thèmes suggérés

| Thème | Description |
|-------|-------------|
| **Portail étudiant** | Gestion de notes, emploi du temps, absences |
| **Plateforme de quiz** | QCM interactif avec score et timer |
| **Annuaire de l'école** | Répertoire des étudiants et enseignants |
| **Blog CESAG** | Articles, catégories, commentaires |
| **Tableau de bord RH** | Gestion fictive de candidatures |
| **Application météo** | Données en temps réel via API OpenWeatherMap |

---

## 2. Cahier des charges technique

### Obligatoire (pour valider le projet)

```{admonition} Fonctionnalités obligatoires
:class: important
**Structure**
- [ ] 3 à 5 pages HTML interconnectées
- [ ] 1 fichier CSS principal + modules si besoin
- [ ] Code JS organisé en fichiers/modules (au moins `app.js` + 1 module)

**JavaScript fondamental**
- [ ] Manipulation DOM (sélection, modification, création d'éléments)
- [ ] Au moins 3 types d'événements différents
- [ ] Au moins 1 tableau traité avec `map`, `filter` ou `reduce`

**Formulaire**
- [ ] Un formulaire complet avec validation JS
- [ ] Messages d'erreur dynamiques par champ
- [ ] Retour visuel (classe `.valide` / `.invalide`)

**Storage**
- [ ] Utilisation de `localStorage` pour persister au moins 1 donnée
- [ ] Les données persistent après fermeture et réouverture de l'onglet

**Dynamisme**
- [ ] Au moins 1 section affichée dynamiquement depuis un tableau JS ou un fichier JSON
- [ ] Au moins 1 modal (native ou librairie)

**Librairie**
- [ ] Au moins 1 librairie externe utilisée (GSAP, Chart.js, SweetAlert2, Swiper, ou autre)

**Responsive**
- [ ] Le site s'affiche correctement sur mobile (largeur 375px)
```

### Bonus (jusqu'à +3 points)

- `fetch()` d'une API publique réelle
- `async/await` avec gestion d'erreur et loader
- 2 librairies ou plus
- Thème sombre persistant
- Animations GSAP au scroll
- Publication sur GitHub Pages ou Netlify

---

## 3. Grille d'évaluation (20 points)

```{admonition} Barème du projet (60% de la note finale)
:class: note
| Critère | Points | Détails |
|---------|--------|---------|
| **Qualité du code JS** | 5 pts | Organisation, lisibilité, fonctions nommées, pas de duplication |
| **Fonctionnalités** | 5 pts | Les fonctionnalités fonctionnent sans bugs |
| **Formulaire validé** | 3 pts | Validation complète, messages d'erreur, feedback visuel |
| **DOM & événements** | 3 pts | Manipulation correcte, délégation, dynamisme |
| **Design et UX** | 2 pts | Interface soignée, responsive, transitions |
| **Soutenance orale** | 2 pts | Clarté, capacité à expliquer le code |
| **Bonus** | +3 pts | Fetch API, 2e librairie, animations, publication |
```

---

## 4. Déroulé de la soutenance

### Format (10 min présentation + 5 min questions)

**Minutes 1–2 — Démo live (montrez, ne racontez pas)**
- Ouvrez l'application directement dans le navigateur
- Naviguez entre les pages
- Démontrez les fonctionnalités principales

**Minutes 3–5 — Fonctionnalité phare**
- Choisissez la fonctionnalité la plus complexe
- Expliquez le problème qu'elle résout
- Montrez-la en action

**Minutes 6–8 — Le code**
- Ouvrez VS Code et montrez 1 ou 2 fonctions clés
- Expliquez la logique (pas la syntaxe — on connaît JS)
- Montrez comment vous avez utilisé la librairie choisie

**Minutes 9–10 — Ce que vous avez appris**
- Quelle a été la difficulté principale ?
- Qu'est-ce qui vous a surpris positivement ?
- Qu'ajouteriez-vous avec plus de temps ?

**Minutes 11–15 — Questions de l'enseignant**
- "Pourquoi avoir utilisé `localStorage` plutôt que `sessionStorage` ici ?"
- "Que se passe-t-il si le fichier JSON n'est pas accessible ?"
- "Comment fonctionne la délégation d'événements dans cette partie ?"
- "Peux-tu modifier en live la couleur de la barre de navigation ?"

---

## 5. Bonnes pratiques de code à respecter

```javascript
// ✅ Fonctions nommées et documentées
/**
 * Filtre les étudiants par filière et terme de recherche
 * @param {Array} etudiants - Liste complète
 * @param {string} filiere - "MIAGE" | "Finance" | "tous"
 * @param {string} terme - Terme de recherche
 * @returns {Array} - Liste filtrée
 */
function filtrerEtudiants(etudiants, filiere, terme) {
    return etudiants
        .filter(e => filiere === "tous" || e.filiere === filiere)
        .filter(e => {
            const recherche = terme.toLowerCase();
            return e.prenom.toLowerCase().includes(recherche) ||
                   e.nom.toLowerCase().includes(recherche);
        });
}

// ✅ Constantes nommées (pas de "magic numbers")
const DELAI_NOTIFICATION = 3000;  // ms
const NOTE_MINIMUM = 10;
const MAX_FAVORIS = 10;

// ✅ Gestion d'erreur systématique
async function chargerDonnees() {
    try {
        const data = await fetchEtudiants();
        return data;
    } catch (erreur) {
        console.error("[chargerDonnees]", erreur);
        afficherToast("Erreur de chargement", "error");
        return [];  // Valeur par défaut
    }
}

// ✅ Séparation des responsabilités
// logique.js    → fonctions pures (filter, sort, calculs)
// dom.js        → fonctions d'affichage (innerHTML, classList)
// storage.js    → fonctions localStorage
// api.js        → fonctions fetch
// app.js        → orchestration (appelle les autres modules)
```

---

## 6. Checklist avant la soutenance

```{admonition} À vérifier la veille
:class: warning
**Code**
- [ ] Le code est indenté et formaté (Prettier)
- [ ] Pas de `console.log()` oubliés en production
- [ ] Les fichiers sont organisés dans des dossiers logiques
- [ ] Tous les membres comprennent tout le code

**Fonctionnement**
- [ ] L'application fonctionne sans erreur dans la console
- [ ] Les formulaires se valident correctement
- [ ] Les données persistent après rechargement (F5)
- [ ] L'application est responsive sur 375px (DevTools)
- [ ] Les images ont un `alt` et un fallback si manquantes

**Soutenance**
- [ ] Chaque membre a préparé une partie à présenter
- [ ] La démo a été répétée au moins une fois
- [ ] VS Code est ouvert avec les bons fichiers prêts
- [ ] Un exemple de code complexe est prêt à être expliqué

**Bonus**
- [ ] Le projet est publié sur GitHub Pages (lien à partager)
- [ ] Un `README.md` décrit le projet et les fonctionnalités
```

---

## 7. Ressources pour continuer

```{admonition} La suite de ton parcours JS
:class: tip
Maintenant que tu maîtrises les fondations, voici les étapes suivantes :

**Niveau 2 — JavaScript avancé**
- ES Modules (`import` / `export`) et bundlers (Vite)
- Classes et POO en JavaScript
- Gestion avancée des erreurs et types (TypeScript)
- Tests unitaires (Jest, Vitest)

**Niveau 3 — Frameworks**
- **React.js** — Composants, state, hooks (le plus demandé)
- **Vue.js** — Alternative plus progressive
- **Next.js** — React + SSR pour les applications fullstack

**APIs et Backend**
- **Node.js + Express** — Créer sa propre API REST
- **Bases de données** — MongoDB, PostgreSQL avec Prisma

**Références indispensables**
- MDN Web Docs : developer.mozilla.org/fr (la bible)
- JavaScript.info : javascript.info (le meilleur tutoriel complet)
- roadmap.sh/javascript : la feuille de route complète
```

---

```{admonition} 🎓 Félicitations — Cours terminé !
:class: tip
Tu sais maintenant :
- ✅ Manipuler le DOM et réagir aux événements utilisateur
- ✅ Valider des formulaires avec JavaScript
- ✅ Afficher des modals et persister des données
- ✅ Charger des données dynamiques avec `fetch()`
- ✅ Utiliser des librairies professionnelles
- ✅ Structurer un projet JavaScript proprement

**Tu as les fondations pour apprendre React, Vue ou Angular. La suite t'appartient ! 🚀**
```
