# AdminFilters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_list** | **List[str]** | only clients connecting from these IP/Mask are allowed. IP/Mask must be in CIDR notation as defined in RFC 4632 and RFC 4291, for example \&quot;192.0.2.0/24\&quot; or \&quot;2001:db8::/32\&quot; | [optional]
**allow_api_key_auth** | **bool** | API key auth allows to impersonate this administrator with an API key | [optional]
**totp_config** | [**AdminTOTPConfig**](AdminTOTPConfig.md) |  | [optional]
**recovery_codes** | [**List[RecoveryCode]**](RecoveryCode.md) |  | [optional]
**preferences** | [**AdminPreferences**](AdminPreferences.md) |  | [optional]

## Example

```python
from openapi_client.models.admin_filters import AdminFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFilters from a JSON string
admin_filters_instance = AdminFilters.from_json(json)
# print the JSON string representation of the object
print AdminFilters.to_json()

# convert the object into a dict
admin_filters_dict = admin_filters_instance.to_dict()
# create an instance of AdminFilters from a dict
admin_filters_form_dict = admin_filters.from_dict(admin_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
