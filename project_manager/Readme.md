```markdown
# Plateforme de Gestion de Projets

## 📖 Description

Cette application permet aux entreprises de gérer leurs projets, suivre l’avancement des tâches, assigner des membres et générer des rapports d’avancement.  
L’application repose sur une architecture en N-tiers, garantissant une séparation claire des responsabilités et une maintenabilité optimale.

---

## 🏗 Architecture

L’application est conçue selon une architecture en N-tiers :

1. **Couche Présentation :**  
   - API REST avec Django REST Framework (DRF)  
   - Interface utilisateur (Django Templates + Bootstrap)

2. **Couche Métier :**  
   - Services implémentant la logique métier  
   - DTOs pour la communication entre les couches

3. **Couche Données :**  
   - Modèles Django  
   - Base de données PostgreSQL  

### Diagramme d’Architecture

```
┌───────────────────────────────┐
│         Client (Front-end)    │
└───────────────▲───────────────┘
                │   API REST
┌───────────────▼───────────────┐
│        Django + DRF (Back-end)│
│ - Vues API                    │
│ - Sérialiseurs                │
│ - Services Métier             │
└───────────────▲───────────────┘
                │    ORM
┌───────────────▼───────────────┐
│  PostgreSQL (Base de données) │
└───────────────────────────────┘
```

---

## ⚙ Installation et Configuration

### 1️⃣ Prérequis
- Python 3.10+
- PostgreSQL
- Git

### 2️⃣ Cloner le projet

```bash
git clone https://github.com/Maeva109/Project_management.git
cd Project_management/project_manager 
```

### 3️⃣ Créer un environnement virtuel et installer les dépendances

```bash
python -m venv venv
source venv/bin/activate    # Sur Windows : venv\Scripts\activate
pip install -r requirements.txt
```

### 4️⃣ Configurer PostgreSQL

Créez une base de données PostgreSQL et mettez à jour le fichier `.env` avec les informations suivantes :

```env
DATABASE_NAME=gestion_projets
DATABASE_USER=postgres
DATABASE_PASSWORD=mot_de_passe
DATABASE_HOST=localhost
DATABASE_PORT=5432
SECRET_KEY=super_secret_key
```

### 5️⃣ Appliquer les migrations et lancer le serveur

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 🔥 Exemples d’Utilisation de l’API

### 🔑 Authentification (JWT)

**Inscription**

```http
POST /api/auth/register/
Content-Type: application/json

{
    "username": "john",
    "password": "motdepasse"
}
```

**Connexion**

```http
POST /api/auth/login/
Content-Type: application/json

{
    "username": "john",
    "password": "motdepasse"
}
```

**Réponse :**

```json
{
    "access": "TOKEN_JWT",
    "refresh": "TOKEN_REFRESH"
}
```

---

### 📂 Gestion des Projets

**Créer un projet**

```http
POST /api/projects/
Authorization: Bearer TOKEN_JWT
Content-Type: application/json

{
    "name": "Projet A",
    "description": "Un projet test",
    "start_date": "2024-04-01",
    "end_date": "2024-06-01"
}
```

**Liste des projets**

```http
GET /api/projects/
Authorization: Bearer TOKEN_JWT
```

---

### 📌 Gestion des Tâches

**Ajouter une tâche**

```http
POST /api/tasks/
Authorization: Bearer TOKEN_JWT
Content-Type: application/json

{
    "title": "Créer la base de données",
    "project": 1,
    "assigned_to": 2
}
```

---

## 🛠 Tests

Pour exécuter l'ensemble des tests unitaires et d'intégration :

```bash
python manage.py test
```

---

## 🚀 Déploiement

L’application peut être déployée avec Docker ou sur des plateformes PaaS comme Heroku.  
N’oubliez pas de mettre à jour les configurations d’environnement (variables d’environnement, secrets, etc.) en production.

---

## 📜 Licence

Ce projet est sous licence MIT.
```

Ce README est prêt à être complété avec des diagrammes UML ou d’autres détails spécifiques à votre projet. N’oubliez pas de committer et pousser vos modifications sur GitHub.