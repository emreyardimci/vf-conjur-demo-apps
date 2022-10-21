from os import environ as env
from conjur import Client

conjur_url = env["CONJUR_APPLIANCE_URL"]
account = env["CONJUR_ACCOUNT"]
cert_file = env["CONJUR_SSL_CERTIFICATE"]

username = "host/ai-video-portal"
with open("/tmp/cert-file", "w") as f:
    f.write(cert_file)

with open("/run/conjur/access-token", "r") as f:
    api_key = f.read()

conjur_client = Client(
     account=account,
     ca_bundle="/tmp/cert-file",
     api_key=api_key,
     debug=True,
     http_debug=True,
     login_id=username,
     password=api_key,
     ssl_verify=True,
     url=conjur_url)

from datetime import datetime, timedelta
conjur_client._api.api_token_expiration = datetime.now() + timedelta(hours=24)
conjur_client._api._api_token = api_key


print(conjur_client.list())
print("*"*10)
print(conjur_client.get("Vault/ConjurUAT/ai-video-portal/Database-Oracle Reconcile-MONGODB_USERNAME/username"))
print("*"*10)
print(conjur_client.get("Vault/ConjurUAT/ai-video-portal/Database-Oracle Reconcile-MONGODB_USERNAME/password"))
