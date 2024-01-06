# GroupUserSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_dir** | **str** |  | [optional]
**max_sessions** | **int** |  | [optional]
**quota_size** | **int** |  | [optional]
**quota_files** | **int** |  | [optional]
**permissions** | **Dict[str, List[Permission]]** | hash map with directory as key and an array of permissions as value. Directories must be absolute paths, permissions for root directory (\&quot;/\&quot;) are required | [optional]
**upload_bandwidth** | **int** | Maximum upload bandwidth as KB/s | [optional]
**download_bandwidth** | **int** | Maximum download bandwidth as KB/s | [optional]
**upload_data_transfer** | **int** | Maximum data transfer allowed for uploads as MB | [optional]
**download_data_transfer** | **int** | Maximum data transfer allowed for downloads as MB | [optional]
**total_data_transfer** | **int** | Maximum total data transfer as MB | [optional]
**expires_in** | **int** | Account expiration in number of days from creation. 0 means no expiration | [optional]
**filters** | [**BaseUserFilters**](BaseUserFilters.md) |  | [optional]
**filesystem** | [**FilesystemConfig**](FilesystemConfig.md) |  | [optional]

## Example

```python
from openapi_client.models.group_user_settings import GroupUserSettings

# TODO update the JSON string below
json = "{}"
# create an instance of GroupUserSettings from a JSON string
group_user_settings_instance = GroupUserSettings.from_json(json)
# print the JSON string representation of the object
print GroupUserSettings.to_json()

# convert the object into a dict
group_user_settings_dict = group_user_settings_instance.to_dict()
# create an instance of GroupUserSettings from a dict
group_user_settings_form_dict = group_user_settings.from_dict(group_user_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
