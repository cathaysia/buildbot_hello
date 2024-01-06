# VirtualFolder

A virtual folder is a mapping between a SFTPGo virtual path and a filesystem path outside the user home directory. The specified paths must be absolute and the virtual path cannot be \"/\", it must be a sub directory. The parent directory for the specified virtual path must exist. SFTPGo will try to automatically create any missing parent directory for the configured virtual folders at user login.

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
**virtual_path** | **str** |  |
**quota_size** | **int** | Quota as size in bytes. 0 means unlimited, -1 means included in user quota. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed | [optional]
**quota_files** | **int** | Quota as number of files. 0 means unlimited, , -1 means included in user quota. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed | [optional]

## Example

```python
from openapi_client.models.virtual_folder import VirtualFolder

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualFolder from a JSON string
virtual_folder_instance = VirtualFolder.from_json(json)
# print the JSON string representation of the object
print VirtualFolder.to_json()

# convert the object into a dict
virtual_folder_dict = virtual_folder_instance.to_dict()
# create an instance of VirtualFolder from a dict
virtual_folder_form_dict = virtual_folder.from_dict(virtual_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
