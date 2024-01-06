# GenerateAdminTotpSecretRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_name** | **str** | name of the configuration to use to generate the secret | [optional]

## Example

```python
from openapi_client.models.generate_admin_totp_secret_request import GenerateAdminTotpSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAdminTotpSecretRequest from a JSON string
generate_admin_totp_secret_request_instance = GenerateAdminTotpSecretRequest.from_json(json)
# print the JSON string representation of the object
print GenerateAdminTotpSecretRequest.to_json()

# convert the object into a dict
generate_admin_totp_secret_request_dict = generate_admin_totp_secret_request_instance.to_dict()
# create an instance of GenerateAdminTotpSecretRequest from a dict
generate_admin_totp_secret_request_form_dict = generate_admin_totp_secret_request.from_dict(generate_admin_totp_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
