# BaseVirtualFolder

Defines the filesystem for the virtual folder and the used quota limits. The same folder can be shared among multiple users and each user can have different quota limits or a different virtual path.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional]
**name** | **str** | unique name for this virtual folder | [optional]
**mapped_path** | **str** | absolute filesystem path to use as virtual folder | [optional]
**description** | **str** | optional description | [optional]
**used_quota_size** | **int** |  | [optional]
**used_quota_files** | **int** |  | [optional]
**last_quota_update** | **int** | Last quota update as unix timestamp in milliseconds | [optional]
**users** | **List[str]** | list of usernames associated with this virtual folder | [optional]
**filesystem** | [**FilesystemConfig**](FilesystemConfig.md) |  | [optional]

## Example

```python
from openapi_client.models.base_virtual_folder import BaseVirtualFolder

# TODO update the JSON string below
json = "{}"
# create an instance of BaseVirtualFolder from a JSON string
base_virtual_folder_instance = BaseVirtualFolder.from_json(json)
# print the JSON string representation of the object
print BaseVirtualFolder.to_json()

# convert the object into a dict
base_virtual_folder_dict = base_virtual_folder_instance.to_dict()
# create an instance of BaseVirtualFolder from a dict
base_virtual_folder_form_dict = base_virtual_folder.from_dict(base_virtual_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
