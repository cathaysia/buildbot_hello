# UserTOTPConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional]
**config_name** | **str** | This name must be defined within the \&quot;totp\&quot; section of the SFTPGo configuration file. You will be unable to save a user/admin referencing a missing config_name | [optional]
**secret** | [**Secret**](Secret.md) |  | [optional]
**protocols** | [**List[MFAProtocols]**](MFAProtocols.md) | TOTP will be required for the specified protocols. SSH protocol (SFTP/SCP/SSH commands) will ask for the TOTP passcode if the client uses keyboard interactive authentication. FTP has no standard way to support two factor authentication, if you enable the FTP support, you have to add the TOTP passcode after the password. For example if your password is \&quot;password\&quot; and your one time passcode is \&quot;123456\&quot; you have to use \&quot;password123456\&quot; as password. WebDAV is not supported since each single request must be authenticated and a passcode cannot be reused. | [optional]

## Example

```python
from openapi_client.models.user_totp_config import UserTOTPConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UserTOTPConfig from a JSON string
user_totp_config_instance = UserTOTPConfig.from_json(json)
# print the JSON string representation of the object
print UserTOTPConfig.to_json()

# convert the object into a dict
user_totp_config_dict = user_totp_config_instance.to_dict()
# create an instance of UserTOTPConfig from a dict
user_totp_config_form_dict = user_totp_config.from_dict(user_totp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
