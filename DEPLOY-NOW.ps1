# DEPLOY-NOW.ps1

# This PowerShell script automates the deployment process for Azure infrastructure, backend FastAPI, and frontend React.

# Ensure you have the necessary Azure CLI installed:
# https://docs.microsoft.com/en-us/cli/azure/install-azure-cli

# Variables
$resourceGroupName = "resume-screening-app-rg"
$location = "East US"
$frontendAppName = "resume-screening-app-frontend"
$backendAppName = "resume-screening-app-backend"
$storageAccountName = "resumeappstorage"

# Login to Azure
az login

# Create Resource Group
az group create --name $resourceGroupName --location $location

# Create Azure Storage Account for React App
az storage account create --name $storageAccountName --resource-group $resourceGroupName --location $location --sku Standard_LRS

# Create Azure App Service Plan
az appservice plan create --name "${frontendAppName}-plan" --resource-group $resourceGroupName --sku B1 --is-linux

# Create and deploy the Azure Static Web App for the frontend
az staticwebapp create --name $frontendAppName --resource-group $resourceGroupName --location $location --source .\frontend --app-artifact-location "build"

# Deploy Backend FastAPI
az webapp create --resource-group $resourceGroupName --plan "${frontendAppName}-plan" --name $backendAppName --runtime "PYTHON:3.8" --deployment-local-git

# Set up continuous deployment using GitHub
az webapp deployment source config --name $backendAppName --resource-group $resourceGroupName --repo-url https://github.com/anjaniiaces/resume-screening-app --branch main --manual-integration

# Output Deployment URLs
Write-Host "Frontend URL: " (az staticwebapp show --name $frontendAppName --resource-group $resourceGroupName --query defaultHostname -o tsv)
Write-Host "Backend URL: " (az webapp show --name $backendAppName --resource-group $resourceGroupName --query defaultHostName -o tsv)