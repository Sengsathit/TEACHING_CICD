# Calculatrice Django - Projet de démonstration CI/CD

Projet simpliste de démonstration pour enseigner les concepts de CI/CD avec GitHub Actions, Docker et Azure.

## 📋 Objectifs pédagogiques

Ce projet démontre :
- ✅ Tests unitaires avec pytest
- ✅ Linting du code avec flake8
- ✅ Conteneurisation avec Docker
- ✅ Pipeline CI/CD avec GitHub Actions
- ✅ Déploiement automatique sur Azure Container Instances

## 🚀 Installation locale

### Prérequis
- Python 3.11+
- pip

### Étapes d'installation

1. **Cloner le repository**
```bash
git clone <votre-repo>
cd ci-cd
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Effectuer les migrations**
```bash
python manage.py migrate
```

5. **Lancer le serveur de développement**
```bash
python manage.py runserver
```

6. **Accéder à l'application**
   - Ouvrez votre navigateur à l'adresse : http://localhost:8000

## 🧪 Tests et Qualité du Code

### Exécuter les tests unitaires
```bash
pytest -v
```

### Vérifier le linting
```bash
flake8 .
```

## 🐳 Docker

### Build de l'image Docker
```bash
docker build -t calculator-app .
```

### Lancer le conteneur localement
```bash
docker run -p 8000:8000 calculator-app
```

## 🔄 Pipeline CI/CD

Le pipeline GitHub Actions s'exécute automatiquement sur chaque push vers `main` et comprend :

### 1. **Lint** (Flake8)
- Vérifie la qualité du code
- S'assure du respect des conventions PEP8

### 2. **Test** (Pytest)
- Exécute tous les tests unitaires
- Vérifie que les fonctions fonctionnent correctement

### 3. **Build & Push**
- Construit l'image Docker
- Pousse l'image vers Azure Container Registry
- Tags: `latest` et SHA du commit

### 4. **Deploy**
- Déploie automatiquement sur Azure Container Instances
- Redémarre le conteneur avec la nouvelle image

## ⚙️ Configuration des Secrets GitHub

Pour que le pipeline fonctionne, configurez les secrets suivants dans GitHub :

### Azure Container Registry (ACR)
- `ACR_LOGIN_SERVER` : URL de votre ACR (ex: `myregistry.azurecr.io`)
- `ACR_USERNAME` : Nom d'utilisateur ACR
- `ACR_PASSWORD` : Mot de passe ACR

### Azure Container Instances (ACI)
- `AZURE_CREDENTIALS` : Credentials JSON pour Azure (service principal)
- `AZURE_RESOURCE_GROUP` : Nom du groupe de ressources Azure

### Créer les credentials Azure
```bash
az ad sp create-for-rbac \
  --name "github-actions-sp" \
  --role contributor \
  --scopes /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP> \
  --sdk-auth
```

## 📁 Structure du Projet

```
ci-cd/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Pipeline CI/CD
├── calculator/                # Application Django
│   ├── static/
│   │   └── calculator/
│   │       └── style.css
│   ├── templates/
│   │   └── calculator/
│   │       └── index.html
│   ├── utils.py              # Fonctions testables
│   ├── views.py              # Vues Django
│   ├── tests.py              # Tests unitaires
│   └── urls.py
├── myproject/                # Configuration Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Dockerfile                # Configuration Docker
├── requirements.txt          # Dépendances Python
├── .flake8                   # Configuration linter
└── manage.py
```

## 🎓 Concepts enseignés

### 1. Tests Unitaires
Les tests se trouvent dans `calculator/tests.py` et couvrent :
- Fonctions utilitaires (add, subtract, multiply, divide)
- Vues Django
- Gestion des erreurs

### 2. Linting
Configuration flake8 dans `.flake8` pour :
- Maintenir la qualité du code
- Respecter les conventions Python (PEP8)
- Détecter les erreurs potentielles

### 3. Docker
Le `Dockerfile` démontre :
- Image multi-stage (optimisation)
- Bonnes pratiques de sécurité
- Configuration pour production

### 4. CI/CD
Le workflow `.github/workflows/ci-cd.yml` montre :
- Jobs séquentiels avec dépendances
- Tests automatisés avant déploiement
- Déploiement conditionnel (uniquement sur main)

## 🔧 Modifications pour démonstration

Pour démontrer le pipeline CI/CD aux étudiants :

1. **Modifier une fonction** dans `calculator/utils.py`
2. **Commit et push** vers la branche main
3. **Observer** le pipeline dans l'onglet "Actions" de GitHub
4. **Vérifier** le déploiement automatique

Exemple de modification :
```python
def add(a, b):
    """Nouvelle version avec logging."""
    result = a + b
    print(f"Addition: {a} + {b} = {result}")
    return result
```

## 📝 License

Projet éducatif - Libre d'utilisation pour l'enseignement
