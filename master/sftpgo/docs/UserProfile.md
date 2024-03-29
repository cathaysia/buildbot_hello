# UserProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional]
**description** | **str** |  | [optional]
**allow_api_key_auth** | **bool** | If enabled, you can impersonate this user, in REST API, using an API key. If disabled user credentials are required for impersonation | [optional]
**public_keys** | **List[str]** |  | [optional]

## Example

```python
from openapi_client.models.user_profile import UserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfile from a JSON string
user_profile_instance = UserProfile.from_json(json)
# print the JSON string representation of the object
print UserProfile.to_json()

# convert the object into a dict
user_profile_dict = user_profile_instance.to_dict()
# create an instance of UserProfile from a dict
user_profile_form_dict = user_profile.from_dict(user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
