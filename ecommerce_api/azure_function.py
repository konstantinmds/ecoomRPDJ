from ecommerce_api.settings import AZURE_ACCOUNT_NAME
from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
  account_name = 'djangoaccountstorage1'
  azure_container = 'media'
  expiration_secs = None


class AzureStaticStorage(AzureStorage):
  account_name = 'djangoaccountstorage1'
    azure_container = 'static'
  expiration_secs = None
