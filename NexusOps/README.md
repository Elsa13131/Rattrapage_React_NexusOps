# NexusOps

NexusOps est une application web de supervision d'une infrastructure informatique. Elle permet de centraliser les équipements, les incidents et les utilisateurs dans une interface unique, avec un tableau de bord affichant les principales informations de supervision.

Le projet repose sur :
- **Frontend :** React avec TypeScript et Vite.
- **Backend :** Python avec FastAPI.
- **Base de données :** PostgreSQL avec SQLAlchemy.
- **Authentification :** JWT.

## Fonctionnalités

- **Dashboard :** affichage des principaux indicateurs de supervision.
- **Équipements :** consultation des équipements et de leur état.
- **Incidents :** consultation, création et modification des incidents.
- **Utilisateurs :** gestion des utilisateurs et de leurs rôles.
- **Suggestions :** page dédiée aux suggestions d'incidents.
- **Authentification :** connexion et déconnexion avec gestion des rôles.
- **API REST :** communication entre le frontend et le backend.
- **Documentation :** documentation interactive avec Swagger UI.

## Prérequis

- Node.js 22 ou supérieur.
- npm.
- Python 3.12 ou compatible avec les dépendances.
- PostgreSQL.
- Git.

## Installation

### 1. Récupérer le projet

```bash
git clone https://github.com/Elsa13131/Rattrapage_React_NexusOps.git
```

Se placer ensuite dans le dossier contenant `package.json` et `backend/`.

### 2. Installer les dépendances frontend

```bash
npm install
```

### 3. Créer l'environnement virtuel Python

À la racine du projet :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Installer les dépendances backend

```powershell
cd backend
python -m pip install -r requirements.txt
```

### 5. Configurer PostgreSQL

Créer une base de données nommée `nexusops` dans PostgreSQL.

Configurer ensuite la connexion dans le terminal PowerShell :

```powershell
$env:DATABASE_URL = "postgresql+psycopg://postgres:VOTRE_MOT_DE_PASSE@localhost:5432/nexusops"
```

Remplacer `VOTRE_MOT_DE_PASSE` par le mot de passe PostgreSQL de votre installation.

La sauvegarde de la base et les instructions de restauration sont fournies séparément du dépôt Git.

### 6. Configurer la clé JWT

Dans le même terminal :

```powershell
$env:NEXUSOPS_SECRET_KEY = python -c "import secrets; print(secrets.token_hex(32))"
```

Chaque développeur doit utiliser sa propre clé secrète.

### 7. Démarrer le backend

Depuis le dossier `backend` :

```powershell
python -m uvicorn main:app --reload
```

Adresses utiles :

- API : http://127.0.0.1:8000
- Swagger : http://127.0.0.1:8000/docs

### 8. Démarrer le frontend

Ouvrir un deuxième terminal à la racine du projet :

```bash
npm run dev
```

Application : http://localhost:5173

Les deux serveurs doivent rester démarrés pendant l'utilisation.

## Base de données PostgreSQL

Le projet utilise PostgreSQL pour stocker les équipements, les incidents et les utilisateurs.

Les scripts SQL complémentaires