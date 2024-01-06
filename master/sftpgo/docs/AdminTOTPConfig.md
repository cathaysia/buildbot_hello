# AdminTOTPConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional]
**config_name** | **str** | This name must be defined within the \&quot;totp\&quot; section of the SFTPGo configuration file. You will be unable to save a user/admin referencing a missing config_name | [optional]
**secret** | [**Secret**](Secret.md) |  | [optional]

## Example

```python
from openapi_client.models.admin_totp_config import AdminTOTPConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AdminTOTPConfig from a JSON string
admin_totp_config_instance = AdminTOTPConfig.from_json(json)
# print the JSON string representation of the object
print AdminTOTPConfig.to_json()

# convert the object into a dict
admin_totp_config_dict = admin_totp_config_instance.to_dict()
# create an instance of AdminTOTPConfig from a dict
admin_totp_config_form_dict = admin_totp_config.from_dict(admin_totp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
