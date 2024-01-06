# BaseTOTPConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional]
**config_name** | **str** | This name must be defined within the \&quot;totp\&quot; section of the SFTPGo configuration file. You will be unable to save a user/admin referencing a missing config_name | [optional]
**secret** | [**Secret**](Secret.md) |  | [optional]

## Example

```python
from openapi_client.models.base_totp_config import BaseTOTPConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTOTPConfig from a JSON string
base_totp_config_instance = BaseTOTPConfig.from_json(json)
# print the JSON string representation of the object
print BaseTOTPConfig.to_json()

# convert the object into a dict
base_totp_config_dict = base_totp_config_instance.to_dict()
# create an instance of BaseTOTPConfig from a dict
base_totp_config_form_dict = base_totp_config.from_dict(base_totp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
