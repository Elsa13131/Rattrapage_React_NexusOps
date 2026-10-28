# NexusOps

NexusOps est une application web de supervision d'une infrastructure
informatique. Elle permet de centraliser les équipements, les incidents
et les utilisateurs dans une interface unique, avec un tableau de bord
affichant les principales informations de supervision.

Le projet repose sur un frontend **React avec TypeScript**, un backend
**FastAPI** et une base de données **SQLite**.

## Fonctionnalités

-   **Dashboard :** affichage des principaux indicateurs, notamment le
    nombre d'équipements, d'utilisateurs et d'incidents ouverts.
-   **Équipements :** consultation des équipements et de leur état
    (`online` ou `offline`).
-   **Incidents :** consultation et création d'incidents avec un niveau
    de gravité, un statut et un équipement associé.
-   **Utilisateurs :** consultation des informations des utilisateurs.
-   **Suggestions :** accès à une page dédiée aux suggestions.
-   **API REST :** gestion des données via des routes HTTP avec FastAPI.
-   **Validation :** vérification des données reçues par l'API avec
    Pydantic.
-   **Base de données :** stockage des données avec SQLite et
    SQLAlchemy.
-   **Documentation :** documentation interactive générée par FastAPI
    avec Swagger UI.

## Prérequis

Avant de commencer, installer :

-   Node.js 22 ou une version plus récente ;
-   npm, installé avec Node.js ;
-   Python 3.12 ou une version compatible avec les dépendances du projet
    ;
-   Git ;
-   un terminal PowerShell ou le terminal intégré de Visual Studio Code.

Pour vérifier les installations :

``` bash
node -v
npm -v
python --version
git --version
```

## Installation

### 1. Récupérer le projet

``` bash
git clone https://github.com/Elsa13131/Rattrapage_React_NexusOps.git
cd Rattrapage_React_NexusOps
cd NexusOps
```

### 2. Installer les dépendances du frontend

Depuis la racine du projet `NexusOps` :

``` bash
npm install
```

### 3. Créer et activer l'environnement virtuel Python

Depuis la racine de `NexusOps`, créer l'environnement virtuel :

``` powershell
python -m venv .venv
```

Activer l'environnement virtuel sous Windows PowerShell :

``` powershell
.\.venv\Scripts\Activate.ps1
```

L'environnement virtuel doit être créé à la racine de `NexusOps`, et non
dans le dossier `backend`.

### 4. Installer les dépendances du backend

Une fois l'environnement virtuel activé, se placer dans le dossier
backend :

``` powershell
cd backend
```

Installer les dépendances nécessaires :

``` powershell
python -m pip install fastapi uvicorn sqlalchemy email-validator
```

Si un fichier `requirements.txt` à jour est présent dans `backend`,
utiliser plutôt :

``` powershell
python -m pip install -r requirements.txt
```

### 5. Démarrer le backend

Depuis le dossier `backend`, avec l'environnement virtuel activé :

``` powershell
python -m uvicorn main:app --reload
```

L'API est accessible à l'adresse :

-   API : http://127.0.0.1:8000
-   Documentation Swagger : http://127.0.0.1:8000/docs

La base SQLite `nexusops.db` se trouve dans le dossier `backend`, selon
la configuration actuelle du projet.

### 6. Démarrer le frontend

Ouvrir un **deuxième terminal** à la racine de `NexusOps`, puis exécuter
:

``` bash
npm run dev
```

L'application est accessible à l'adresse :

http://localhost:5173

Les deux serveurs doivent rester démarrés pendant l'utilisation de
l'application.

## Utilisation

  ---------------------------------------------------------------------------------
  **Commande**                                  **Effet**
  --------------------------------------------- -----------------------------------
  `npm install`                                 Installe les dépendances du
                                                frontend.

  `npm run dev`                                 Démarre le serveur de développement
                                                React avec Vite.

  `npm run build`                               Vérifie le projet et construit la
                                                version de production dans `dist/`.

  `npm run preview`                             Prévisualise la version construite.

  `npm run lint`                                Analyse le code selon la
                                                configuration du projet.

  `python -m venv .venv`                        Crée l'environnement virtuel
                                                Python.

  `.\.venv\Scripts\Activate.ps1`                Active l'environnement virtuel sous
                                                PowerShell.

  `python -m pip install -r requirements.txt`   Installe les dépendances listées
                                                dans `requirements.txt`.

  `python -m uvicorn main:app --reload`         Démarre le serveur FastAPI avec
                                                rechargement automatique.
  ---------------------------------------------------------------------------------

Les commandes Python doivent être exécutées dans un terminal où
l'environnement virtuel est activé.

## Architecture

``` text
NexusOps/
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── database_models.py
│   ├── nexusops.db
│   ├── models/
│   │   ├── equipment.py
│   │   ├── incident.py
│   │   └── user.py
│   ├── routes/
│   │   ├── equipment_routes.py
│   │   ├── incident_routes.py
│   │   └── user_routes.py
│   └── services/
│       ├── equipment_service.py
│       └── incident_service.py
├── src/
│   ├── App.tsx
│   ├── App.css
│   ├── components/
│   ├── pages/
│   │   ├── Dashboard.tsx
│   │   ├── Equipments.tsx
│   │   ├── Incidents.tsx
│   │   ├── Users.tsx
│   │   └── Suggest.tsx
│   ├── services/
│   │   ├── equipmentService.ts
│   │   ├── incidentService.ts
│   │   └── userService.ts
│   ├── types.ts
│   ├── main.tsx
│   └── index.css
├── .venv/
├── package.json
├── package-lock.json
├── index.html
└── README.md
```

Cette arborescence présente l'organisation générale du projet. Les noms
ou la présence de certains fichiers peuvent varier selon la version du
dépôt.

### Frontend --- React et TypeScript

-   `App.tsx` : définit le routage principal et l'accès aux pages.
-   `components/` : contient les composants réutilisables, notamment la
    navigation et les éléments d'affichage.
-   `pages/` : contient les pages de l'application.
-   `services/` : regroupe les fonctions qui effectuent les appels HTTP
    vers le backend.
-   `types.ts` : définit les types TypeScript utilisés pour les données
    métier.
-   `main.tsx` : point d'entrée de l'application React.
-   `index.css` et `App.css` : contiennent les styles de base et les
    styles de l'application.

Vite est utilisé pour le serveur de développement et la construction du
frontend.

### Backend --- FastAPI

-   `main.py` : initialise l'application FastAPI et enregistre les
    routeurs.
-   `database.py` : configure la connexion à SQLite et les sessions
    SQLAlchemy.
-   `database_models.py` : définit les modèles correspondant aux tables
    de la base de données.
-   `models/` : contient les modèles Pydantic utilisés pour valider les
    données des requêtes.
-   `routes/` : définit les points d'entrée HTTP de l'API.
-   `services/` : contient la logique de gestion des équipements et des
    incidents.

FastAPI génère automatiquement la documentation OpenAPI et l'interface
Swagger UI.

### Base de données --- SQLite

SQLite permet de conserver les données entre les redémarrages du
serveur. La base de données est stockée dans `backend/nexusops.db`,
selon la configuration actuelle.

Les principales entités sont :

-   **Équipement :** identifiant, nom et état.
-   **Incident :** identifiant, titre, gravité, statut et identifiant de
    l'équipement associé.
-   **Utilisateur :** informations et rôle des utilisateurs, selon les
    fonctionnalités effectivement implémentées.

Les tables sont initialisées par SQLAlchemy si cette initialisation est
configurée au démarrage de l'application.

## API REST

L'API est accessible à partir de :

``` text
http://127.0.0.1:8000
```

La liste des routes disponibles et leurs paramètres peuvent être
consultés dans Swagger :

http://127.0.0.1:8000/docs

Les méthodes HTTP principales sont :

  -----------------------------------------------------------------------
  **Méthode**                         **Utilisation**
  ----------------------------------- -----------------------------------
  `GET`                               Récupérer une liste ou un élément.

  `POST`                              Créer une ressource.

  `PUT`                               Modifier une ressource existante,
                                      si la route est implémentée.

  `DELETE`                            Supprimer une ressource existante,
                                      si la route est implémentée.
  -----------------------------------------------------------------------

### Exemples de routes

  -----------------------------------------------------------------------
  **Route**                           **Fonction**
  ----------------------------------- -----------------------------------
  `GET /equipments`                   Récupérer les équipements.

  `GET /equipments/{equipment_id}`    Récupérer un équipement par son
                                      identifiant.

  `POST /equipments`                  Créer un équipement.

  `GET /incidents`                    Récupérer les incidents.

  `GET /incidents/{incident_id}`      Récupérer un incident par son
                                      identifiant.

  `POST /incidents`                   Créer un incident associé à un
                                      équipement existant.
  -----------------------------------------------------------------------

Les routes de modification et de suppression dépendent de leur
implémentation effective dans le backend.

## Données et fonctionnement

Le frontend communique avec l'API FastAPI, et les données principales
sont stockées dans SQLite.

Pour créer un incident, il faut notamment fournir un titre, une gravité,
un statut et l'identifiant d'un équipement existant.

Les données envoyées à l'API sont validées par les modèles Pydantic. Les
routes peuvent renvoyer des codes HTTP comme `200` pour une requête
réussie, `201` pour une création et `404` lorsqu'une ressource
recherchée est introuvable.

Chaque copie locale du projet possède sa propre base SQLite, sauf
configuration spécifique. Les données ne sont donc pas automatiquement
partagées entre collaborateurs.

## Dépannage

### Le module `uvicorn` est introuvable

Vérifier que l'environnement virtuel est activé, puis installer les
dépendances :

``` powershell
python -m pip install fastapi uvicorn sqlalchemy email-validator
```

### Erreur `email_validator`

Installer le module manquant :

``` powershell
python -m pip install email-validator
```

### Erreur de connexion au backend

Vérifier que le serveur FastAPI est démarré et que l'adresse utilisée
par le frontend correspond à :

``` text
http://127.0.0.1:8000
```

### Erreur lors de l'accès à SQLite

Vérifier la configuration dans `database.py`, le chemin de la base et
les droits d'accès au dossier `backend`.

### Erreur lors de l'activation du `.venv`

Depuis la racine de `NexusOps`, utiliser :

``` powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloque l'activation, lire le message d'erreur avant de
modifier la politique d'exécution.

## Technologies utilisées

-   **React** : création de l'interface utilisateur.
-   **TypeScript** : typage statique du frontend.
-   **Vite** : serveur de développement et outil de construction.
-   **React Router** : navigation entre les pages.
-   **Python** : développement du backend.
-   **FastAPI** : création de l'API REST.
-   **Pydantic** : validation des données.
-   **SQLAlchemy** : interaction avec la base de données.
-   **SQLite** : stockage des données.
-   **Uvicorn** : serveur utilisé pour exécuter FastAPI.
-   **Git et GitHub** : gestion du code source et collaboration.

## Objectif du projet

NexusOps a pour objectif de mettre en pratique le développement d'une
application web complète, de l'interface utilisateur jusqu'à la
persistance des données, avec une architecture séparant le frontend,
l'API REST et la base de données.
