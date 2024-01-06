# APIKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | unique key identifier | [optional]
**name** | **str** | User friendly key name | [optional]
**key** | **str** | We store the hash of the key. This is just like a password. For security reasons this field is omitted when you search/get API keys | [optional]
**scope** | [**APIKeyScope**](APIKeyScope.md) |  | [optional]
**created_at** | **int** | creation time as unix timestamp in milliseconds | [optional]
**updated_at** | **int** | last update time as unix timestamp in milliseconds | [optional]
**last_use_at** | **int** | last use time as unix timestamp in milliseconds. It is saved at most once every 10 minutes | [optional]
**expires_at** | **int** | expiration time as unix timestamp in milliseconds | [optional]
**description** | **str** | optional description | [optional]
**user** | **str** | username associated with this API key. If empty and the scope is \&quot;user scope\&quot; the key can impersonate any user | [optional]
**admin** | **str** | admin associated with this API key. If empty and the scope is \&quot;admin scope\&quot; the key can impersonate any admin | [optional]

## Example

```python
from openapi_client.models.api_key import APIKey

# TODO update the JSON string below
json = "{}"
# create an instance of APIKey from a JSON string
api_key_instance = APIKey.from_json(json)
# print the JSON string representation of the object
print APIKey.to_json()

# convert the object into a dict
api_key_dict = api_key_instance.to_dict()
# create an instance of APIKey from a dict
api_key_form_dict = api_key.from_dict(api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
