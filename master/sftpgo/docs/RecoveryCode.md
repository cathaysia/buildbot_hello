# RecoveryCode

Recovery codes to use if the user loses access to their second factor auth device. Each code can only be used once, you should use these codes to login and disable or reset 2FA for your account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | [**Secret**](Secret.md) |  | [optional]
**used** | **bool** |  | [optional]

## Example

```python
from openapi_client.models.recovery_code import RecoveryCode

# TODO update the JSON string below
json = "{}"
# create an instance of RecoveryCode from a JSON string
recovery_code_instance = RecoveryCode.from_json(json)
# print the JSON string representation of the object
print RecoveryCode.to_json()

# convert the object into a dict
recovery_code_dict = recovery_code_instance.to_dict()
# create an instance of RecoveryCode from a dict
recovery_code_form_dict = recovery_code.from_dict(recovery_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
