# Configuration Docker Hub pour le projet CI/CD

Ce guide explique comment configurer Docker Hub pour le déploiement automatique.

## Prérequis

- Un compte Docker Hub (gratuit) : https://hub.docker.com/signup
- Un repository GitHub
- Un compte Azure actif (pour le déploiement)

## Étape 1: Créer un compte et un token Docker Hub

### 1.1 Créer un compte Docker Hub
Si vous n'avez pas encore de compte, créez-en un sur https://hub.docker.com/signup

### 1.2 Créer un Access Token

1. Connectez-vous à Docker Hub
2. Allez dans **Account Settings** > **Security**
3. Cliquez sur **New Access Token**
4. Donnez un nom au token (ex: `github-actions`)
5. Permissions : **Read, Write, Delete**
6. Cliquez sur **Generate**
7. **IMPORTANT** : Copiez le token immédiatement (il ne sera plus visible après)

Cette commande retourne un JSON. **Copiez tout le JSON**, il sera utilisé pour `AZURE_CREDENTIALS`.

## Étape 2: Configurer les Secrets GitHub

Dans votre repository GitHub, allez dans `Settings > Secrets and variables > Actions` et ajoutez :

### Secrets requis

| Secret | Valeur | Description |
|--------|--------|-------------|
| `DOCKER_USERNAME` | Votre nom d'utilisateur Docker Hub | Ex: `johndoe` |
| `DOCKER_PASSWORD` | Le token d'accès créé à l'étape 1.2 | Ex: `dckr_pat_abc123...` |
| `AZURE_CREDENTIALS` | JSON complet du Service Principal | Obtenu à l'étape 2 |
| `AZURE_RESOURCE_GROUP` | `calculator-rg` | Nom du groupe de ressources Azure |

## Étape 3: Créer un repository Docker Hub (optionnel)

Par défaut, les images publiques seront automatiquement créées lors du premier push.

Si vous voulez un repository privé :
1. Allez sur https://hub.docker.com/repositories
2. Cliquez sur **Create Repository**
3. Nom : `calculator-app`
4. Visibilité : **Private** ou **Public**
5. Cliquez sur **Create**