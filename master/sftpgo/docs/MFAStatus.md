# MFAStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | [optional]
**totp_configs** | [**List[TOTPConfig]**](TOTPConfig.md) |  | [optional]

## Example

```python
from openapi_client.models.mfa_status import MFAStatus

# TODO update the JSON string below
json = "{}"
# create an instance of MFAStatus from a JSON string
mfa_status_instance = MFAStatus.from_json(json)
# print the JSON string representation of the object
print MFAStatus.to_json()

# convert the object into a dict
mfa_status_dict = mfa_status_instance.to_dict()
# create an instance of MFAStatus from a dict
mfa_status_form_dict = mfa_status.from_dict(mfa_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
