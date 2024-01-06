# ValidateAdminTotpSecretRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_name** | **str** | name of the configuration to use to validate the passcode | [optional]
**passcode** | **str** | passcode to validate | [optional]
**secret** | **str** | secret to use to validate the passcode | [optional]

## Example

```python
from openapi_client.models.validate_admin_totp_secret_request import ValidateAdminTotpSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateAdminTotpSecretRequest from a JSON string
validate_admin_totp_secret_request_instance = ValidateAdminTotpSecretRequest.from_json(json)
# print the JSON string representation of the object
print ValidateAdminTotpSecretRequest.to_json()

# convert the object into a dict
validate_admin_totp_secret_request_dict = validate_admin_totp_secret_request_instance.to_dict()
# create an instance of ValidateAdminTotpSecretRequest from a dict
validate_admin_totp_secret_request_form_dict = validate_admin_totp_secret_request.from_dict(validate_admin_totp_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
