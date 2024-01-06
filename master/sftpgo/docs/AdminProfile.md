# AdminProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional]
**description** | **str** |  | [optional]
**allow_api_key_auth** | **bool** | If enabled, you can impersonate this admin, in REST API, using an API key. If disabled admin credentials are required for impersonation | [optional]

## Example

```python
from openapi_client.models.admin_profile import AdminProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AdminProfile from a JSON string
admin_profile_instance = AdminProfile.from_json(json)
# print the JSON string representation of the object
print AdminProfile.to_json()

# convert the object into a dict
admin_profile_dict = admin_profile_instance.to_dict()
# create an instance of AdminProfile from a dict
admin_profile_form_dict = admin_profile.from_dict(admin_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
