# Key Vault Operations

This repository contains a Python function for updating secrets in Azure Key Vault.

## Prerequisites
1. **Azure Subscription**: You need an Azure subscription with access to Azure Key Vault.
2. **Azure Key Vault**: Create an Azure Key Vault instance in your Azure portal.
3. **Access Policy**: Ensure that your Azure account has the necessary permissions to read and write secrets in the Key Vault. You may need to assign the appropriate access policies to your Azure account or service principal.
4. **az login**: login to your azure portal


## Parameters

- `vault_url`: The URL of the Azure Key Vault where the secret is stored.
- `secret_name`: The name of the secret to be updated.
- `new_secret_value`: The new value to be assigned to the secret.
## Installation
1. **Azure SDK for Python**: Install the Azure SDK for Python using pip:
   ```bash
   pip install azure-identity azure-keyvault-secrets
2. **Run File**:
   ```bash
   python <file-name>.py
