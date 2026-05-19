# Séance 9 — Librairies JS et Animations

```{admonition} Objectifs
:class: tip
- Installer une librairie via CDN et via npm
- Utiliser **GSAP** pour des animations fluides
- Créer des graphiques avec **Chart.js**
- Afficher des modals stylisées avec **SweetAlert2**
- Créer des sliders/carrousels avec **Swiper.js**
- Comprendre comment lire une documentation de librairie
```

---

## 1. Installer une librairie — CDN vs npm

### Via CDN (Content Delivery Network) — Simple et rapide

```html
<!-- Dans le <head> ou avant </body> -->

<!-- GSAP (animations) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>

<!-- Chart.js (graphiques) -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<!-- SweetAlert2 (modals stylisées) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.min.css">
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.all.min.js"></script>

<!-- Swiper.js (slider/carrousel) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

<!-- Ton script APRÈS les librairies -->
<script src="app.js"></script>
```

✅ **Avantages CDN** : rapide à mettre en place, aucune configuration, parfait pour les projets simples.

❌ **Inconvénients** : dépendance réseau, versions potentiellement obsolètes à terme.

### Via npm — Pour les projets sérieux

```bash
# Dans le terminal, dans le dossier du projet
npm init -y                      # Crée package.json
npm install gsap                 # Installe GSAP
npm install chart.js             # Installe Chart.js
npm install sweetalert2          # Installe SweetAlert2
npm install swiper               # Installe Swiper.js

# Les librairies sont dans node_modules/
# On les importe avec ES Modules (si on utilise un bundler comme Vite)
```

```javascript
// Avec npm + Vite/Webpack
import { gsap } from "gsap";
import Chart from "chart.js/auto";
import Swal from "sweetalert2";
import Swiper from "swiper";
```

```{admonition} CDN pour ce cours
:class: note
Dans ce cours, nous utiliserons le **CDN** pour simplifier la mise en place. Le `npm` + bundler sera abordé dans le cours React/Vue avancé.
```

---

## 2. GSAP — GreenSock Animation Platform

GSAP est la librairie d'animation JS la plus puissante et performante.

### Installation

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
```

### `gsap.to()` — Animer vers un état

```javascript
// Animer un élément vers un état final
gsap.to(".carte", {
    duration: 0.5,      // Durée en secondes
    opacity: 1,
    y: 0,               // translateY
    ease: "power2.out", // Courbe d'accélération
});

// Animer plusieurs éléments avec décalage
gsap.to(".carte", {
    duration: 0.4,
    opacity: 1,
    y: 0,
    stagger: 0.1,       // 0.1s de délai entre chaque carte
    ease: "back.out(1.2)",
});

// Depuis un état initial (from → état actuel)
gsap.from(".hero-titre", {
    duration: 0.8,
    opacity: 0,
    y: -40,
    ease: "power3.out",
});

// fromTo — état initial → état final
gsap.fromTo(".logo",
    { opacity: 0, scale: 0.5 },    // état initial
    { opacity: 1, scale: 1, duration: 0.6, ease: "elastic.out(1, 0.5)" }  // état final
);
```

### Les propriétés animables

```javascript
gsap.to(".element", {
    // Position
    x: 100,         // translateX en px
    y: -50,         // translateY en px
    xPercent: -50,  // translateX en %
    yPercent: -50,  // translateY en %

    // Taille
    width: 200,
    height: 150,
    scale: 1.2,
    scaleX: 2,
    scaleY: 0.5,

    // Rotation
    rotation: 360,   // en degrés
    rotationX: 45,   // 3D
    rotationY: 180,  // 3D

    // Visibilité
    opacity: 0.5,

    // CSS direct
    backgroundColor: "#1A7A2A",
    borderRadius: "50%",
    fontSize: "2em",

    // Timing
    duration: 1,
    delay: 0.3,
    ease: "power2.inOut",

    // Callbacks
    onStart: () => console.log("Animation démarrée"),
    onComplete: () => console.log("Animation terminée"),
});
```

### Timeline — Séquencer des animations

```javascript
// Une timeline joue les animations dans l'ordre
const tl = gsap.timeline({ delay: 0.2 });

tl.from(".nav", { opacity: 0, y: -60, duration: 0.5 })
  .from(".hero-titre", { opacity: 0, y: 40, duration: 0.6 }, "-=0.2") // Commence 0.2s avant la fin de la précédente
  .from(".hero-texte", { opacity: 0, y: 20, duration: 0.5 }, "-=0.3")
  .from(".btn-hero", { opacity: 0, scale: 0.8, duration: 0.4 }, "-=0.2")
  .from(".carte", { opacity: 0, y: 30, stagger: 0.08 }, "-=0.1");
```

### ScrollTrigger — Animation au défilement

```javascript
// Enregistrer le plugin
gsap.registerPlugin(ScrollTrigger);

// Animation déclenchée au scroll
gsap.from(".section-stats .chiffre", {
    scrollTrigger: {
        trigger: ".section-stats",
        start: "top 80%",       // Déclenche quand le haut de la section atteint 80% de la fenêtre
        end: "bottom 20%",
        toggleActions: "play none none reverse",
    },
    opacity: 0,
    y: 40,
    stagger: 0.15,
    duration: 0.6,
});

// Parallax au scroll
gsap.to(".hero-image", {
    scrollTrigger: {
        trigger: ".hero",
        start: "top top",
        end: "bottom top",
        scrub: true,            // Animation liée directement au scroll
    },
    y: 150,
});
```

### Animer l'entrée des cartes

```javascript
// Appeler après afficherEtudiants()
function animer CartesMail() {
    gsap.from(".carte-etudiant", {
        opacity: 0,
        y: 30,
        scale: 0.95,
        stagger: 0.08,
        duration: 0.4,
        ease: "power2.out",
        clearProps: "all",  // Nettoie les styles GSAP après l'animation
    });
}
```

---

## 3. Chart.js — Graphiques et visualisations

### Installation

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

### Graphique en barres

```html
<canvas id="graphique-notes" width="600" height="300"></canvas>
```

```javascript
const etudiants = await fetchEtudiants();

// Préparer les données
const labels = etudiants.map(e => `${e.prenom} ${e.nom}`);
const notes  = etudiants.map(e => e.note);
const couleurs = notes.map(n => n >= 16 ? "#1A7A2A" : n >= 12 ? "#E8420A" : "#c62828");

// Créer le graphique
const ctx = document.querySelector("#graphique-notes").getContext("2d");

const graphique = new Chart(ctx, {
    type: "bar",  // "bar" | "line" | "pie" | "doughnut" | "radar" | "polarArea"
    data: {
        labels,
        datasets: [{
            label: "Notes /20",
            data: notes,
            backgroundColor: couleurs,
            borderRadius: 6,
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: false },
            title: {
                display: true,
                text: "Notes des étudiants — CESAG Connect",
                font: { size: 16 }
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                max: 20,
                ticks: { stepSize: 2 }
            }
        }
    }
});

// Mettre à jour un graphique existant
graphique.data.datasets[0].data = nouvelleDonnees;
graphique.update();

// Détruire un graphique
graphique.destroy();
```

### Graphique en anneau — Répartition par filière

```javascript
function afficherGraphiqueFiliere(etudiants) {
    const filieres = {};
    etudiants.forEach(e => {
        filieres[e.filiere] = (filieres[e.filiere] || 0) + 1;
    });

    new Chart(document.querySelector("#graphique-filieres"), {
        type: "doughnut",
        data: {
            labels: Object.keys(filieres),
            datasets: [{
                data: Object.values(filieres),
                backgroundColor: ["#1A7A2A", "#E8420A", "#185FA5", "#BA7517"],
                borderWidth: 2,
                borderColor: "white",
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: "bottom" }
            }
        }
    });
}
```

---

## 4. SweetAlert2 — Modals et confirmations stylisées

### Installation

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.min.css">
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.all.min.js"></script>
```

### Utilisation

```javascript
// Alert simple
Swal.fire("Bonjour !", "Bienvenue sur CESAG Connect.", "success");

// Confirmation
const result = await Swal.fire({
    title: "Supprimer cet étudiant ?",
    text: "Cette action est irréversible.",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Oui, supprimer",
    cancelButtonText: "Annuler",
    confirmButtonColor: "#c62828",
    cancelButtonColor: "#1A7A2A",
});

if (result.isConfirmed) {
    supprimerEtudiant(id);
    Swal.fire("Supprimé !", "L'étudiant a été supprimé.", "success");
}

// Toast (notification légère)
const Toast = Swal.mixin({
    toast: true,
    position: "top-end",
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
});

Toast.fire({ icon: "success", title: "Inscription réussie !" });
Toast.fire({ icon: "error",   title: "Email invalide." });
Toast.fire({ icon: "info",    title: "Chargement en cours..." });

// Formulaire dans une modal
const { value: email } = await Swal.fire({
    title: "Contacter l'étudiant",
    input: "email",
    inputLabel: "Votre email",
    inputPlaceholder: "votre@email.com",
    showCancelButton: true,
});

if (email) {
    console.log("Email saisi :", email);
}
```

---

## 5. Swiper.js — Slider et carrousel

### Installation

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
```

### Structure HTML

```html
<div class="swiper" id="slider-actus">
    <div class="swiper-wrapper">
        <div class="swiper-slide">
            <article class="carte-actu">...</article>
        </div>
        <div class="swiper-slide">
            <article class="carte-actu">...</article>
        </div>
    </div>
    <div class="swiper-pagination"></div>
    <div class="swiper-button-prev"></div>
    <div class="swiper-button-next"></div>
</div>
```

### Initialisation JS

```javascript
const swiper = new Swiper("#slider-actus", {
    slidesPerView: 1,
    spaceBetween: 20,
    loop: true,
    autoplay: {
        delay: 4000,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    // Responsive
    breakpoints: {
        640:  { slidesPerView: 2 },
        1024: { slidesPerView: 3 },
    },
});
```

---

## 6. Lire une documentation de librairie

```{admonition} Compétence clé — S'auto-former sur une librairie
:class: tip
En tant que développeur, tu passeras ta carrière à apprendre de nouvelles librairies. La méthode :

1. **README** : comprendre ce que fait la librairie (30 secondes)
2. **Installation** : CDN ou npm, copier le code d'installation
3. **Getting Started** : trouver l'exemple minimal qui fonctionne
4. **API Reference** : chercher les options dont tu as besoin
5. **Exemples** / Demos : voir ce que d'autres ont fait
6. **GitHub Issues** : si ça ne marche pas, chercher le problème

Les documentations à connaître :
- **GSAP** : greensock.com/docs
- **Chart.js** : chartjs.org/docs
- **SweetAlert2** : sweetalert2.github.io
- **Swiper.js** : swiperjs.com/swiper-api
```

---

## Résumé

```{admonition} Ce qu'il faut retenir
:class: tip
| Librairie | Usage | Méthode clé |
|-----------|-------|-------------|
| **GSAP** | Animations CSS/JS | `gsap.from()`, `gsap.to()`, `ScrollTrigger` |
| **Chart.js** | Graphiques | `new Chart(canvas, config)` |
| **SweetAlert2** | Modals/toasts stylisés | `Swal.fire()`, `Swal.mixin()` |
| **Swiper.js** | Sliders/carrousels | `new Swiper(selector, options)` |
| **CDN** | Sans npm | `<script src="https://cdn...">` |
| **npm** | Projets bundlés | `npm install xxx` puis `import` |
```

---

## TP 9 — CESAG Connect : Version finale animée

```{admonition} À faire — 1h30
:class: warning

**1. Animation d'entrée avec GSAP (4 pts)**
- Animation de la page au chargement : nav → hero → cartes (avec stagger)
- Les cartes s'animent à chaque nouveau filtre (`gsap.from(".carte", ...)`)
- Au scroll : les sections `.section-stats` et `.section-formations` s'animent

**2. Graphiques avec Chart.js (4 pts)**
- Graphique barres : notes de tous les étudiants (couleur selon mention)
- Graphique anneau : répartition par filière
- Les graphiques se mettent à jour quand un filtre est appliqué

**3. SweetAlert2 partout (4 pts)**
- Remplacer tous les `alert()` et `confirm()` natifs par Swal
- Toast de succès après inscription
- Confirmation avec Swal avant suppression d'un étudiant
- Modal Swal pour "Contacter l'étudiant" (avec input email)

**4. Slider des actualités (3 pts)**
- Section "Actualités CESAG" avec Swiper.js
- 5 cartes d'actualités fictives
- Autoplay, pagination, navigation, responsive (1→2→3 slides)

**5. Bonus — Thème sombre (2 pts)**
- Bouton bascule clair/sombre
- `document.body.classList.toggle("theme-sombre")`
- Sauvegarder la préférence dans `localStorage`
- Animation de transition : `gsap.to("body", { backgroundColor: "...", color: "..." })`
```

---

*Séance suivante → [Séance 10 — Projet Final : Soutenance](s10-projet-final)*
