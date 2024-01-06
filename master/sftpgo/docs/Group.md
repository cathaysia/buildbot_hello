# Group


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional]
**name** | **str** | name is unique | [optional]
**description** | **str** | optional description | [optional]
**created_at** | **int** | creation time as unix timestamp in milliseconds | [optional]
**updated_at** | **int** | last update time as unix timestamp in milliseconds | [optional]
**user_settings** | [**GroupUserSettings**](GroupUserSettings.md) |  | [optional]
**virtual_folders** | [**List[VirtualFolder]**](VirtualFolder.md) | mapping between virtual SFTPGo paths and folders | [optional]
**users** | **List[str]** | list of usernames associated with this group | [optional]
**admins** | **List[str]** | list of admins usernames associated with this group | [optional]

## Example

```python
from openapi_client.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print Group.to_json()

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_form_dict = group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
