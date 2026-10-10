# NexusOps
App qui permet de surveiller son infrastructure numérique au même endroit : équipements,
incidents et utilisateurs centralisés dans un tableau de bord unique.

## Installation
Prérequis : Node.js 22 ou plus (`node -v`), Git.

```bash
git clone https://github.com/Elsa13131/Rattrapage_React_NexusOps.git
cd Rattrapage_React_NexusOps
cd NexusOps
npm install
npx json-server --watch db.json --port 3001
npm run dev
```

L'application s'ouvre sur http://localhost:5173 avec 3 équipements,
2 incidents et 3 utilisateurs de démonstration, et une page Dashboard affichant nombres d'equipement/ utilisateur / et incident ouvert.

## Utilisation

| Commande                        | Effet                                                    |
|---------------------------------|----------------------------------------------------------|
| `npx json-server --watch db.json --port 3001` | Démarre la fausse API REST utilisée par l'application |
| `npm run dev`                  | Serveur de développement avec rechargement automatique   |
| `npm run build`                | Vérifie les types et construit la version dans `dist/`   |
| `npm run preview`              | Sert la version construite                               |
| `npm run lint`                 | Analyse le code avec Oxlint                              |

Les données sont fictives : `db.json` contient les équipements,
les incidents et les utilisateurs de démonstration.

## Architecture

```text
src/
├── App.tsx          routage principal et assemblage des pages
├── App.css          styles globaux de l'application
├── components/      composants d'affichage et de navigation
├── pages/           écrans du tableau de bord, équipements, incidents, utilisateurs et suggestions
├── services/        appels HTTP vers la fausse API JSON Server
├── types/           types TypeScript pour les données métier
├── main.tsx         point d'entrée React
└── index.css        styles de base et reset global
```

Le projet repose sur React, Vite, React Router et une API locale
fictive via json-server.