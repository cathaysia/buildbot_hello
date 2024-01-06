# Role


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional]
**name** | **str** | name is unique | [optional]
**description** | **str** | optional description | [optional]
**created_at** | **int** | creation time as unix timestamp in milliseconds | [optional]
**updated_at** | **int** | last update time as unix timestamp in milliseconds | [optional]
**users** | **List[str]** | list of usernames associated with this group | [optional]
**admins** | **List[str]** | list of admins usernames associated with this group | [optional]

## Example

```python
from openapi_client.models.role import Role

# TODO update the JSON string below
json = "{}"
# create an instance of Role from a JSON string
role_instance = Role.from_json(json)
# print the JSON string representation of the object
print Role.to_json()

# convert the object into a dict
role_dict = role_instance.to_dict()
# create an instance of Role from a dict
role_form_dict = role.from_dict(role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
