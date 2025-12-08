Pour déployer sur Azure Container Instances, vous avez besoin d'un Service Principal :

```bash
# Variables
RESOURCE_GROUP="nom-de-votre-resource-group"
LOCATION="francecentral"

# Récupérer l'ID de subscription
SUBSCRIPTION_ID=$(az account show --query id -o tsv)

# Créer le service principal
az ad sp create-for-rbac \
  --name "nom-de-votre-service-principal" \
  --role contributor \
  --scopes /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP \
  --sdk-auth
```