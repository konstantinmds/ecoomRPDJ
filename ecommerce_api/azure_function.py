from ecommerce_api.settings import AZURE_ACCOUNT_NAME
from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
  account_name = 'djangoaccountstorage1'
  account_key = "YskH4SZfThHBz4ia9DPefjOINfzDHMjinlr/t1eX0WNWcKVjiOh7XeF3rLkrWzT7bD22FCS2qbUD4MIaRiSh4Q=="
  azure_container = 'media'
  expiration_secs = None


class AzureStaticStorage(AzureStorage):
  account_name = 'djangoaccountstorage1'
  account_key = "YskH4SZfThHBz4ia9DPefjOINfzDHMjinlr/t1eX0WNWcKVjiOh7XeF3rLkrWzT7bD22FCS2qbUD4MIaRiSh4Q=="
  azure_container = 'static'
  expiration_secs = None