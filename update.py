from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

def update_keyvault_secret(vault_url, secret_name, new_secret_value):
    # Authenticate using default Azure credentials
    credential = DefaultAzureCredential()

    # Create a SecretClient instance to interact with Azure Key Vault
    secret_client = SecretClient(vault_url=vault_url, credential=credential)

    # Retrieve the existing secret from Azure Key Vault
    existing_secret = secret_client.get_secret(secret_name)

    # Update the secret value in Azure Key Vault
    updated_secret = secret_client.set_secret(secret_name, new_secret_value)

    # Print confirmation message and old/new secret values
    print(f"Secret '{secret_name}' updated successfully.")
    print(f"Old Secret Value: {existing_secret.value}")
    print(f"New Secret Value: {updated_secret.value}")

# Example usage
vault_url = "https://<key vault name>.vault.azure.net/"
secret_name = <your-secret-name>
new_secret_value = <secret-value>

update_keyvault_secret(vault_url, secret_name, new_secret_value)
