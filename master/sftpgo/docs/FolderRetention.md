# FolderRetention


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | virtual directory path as seen by users, if no other specific retention is defined, the retention applies for sub directories too. For example if retention is defined for the paths \&quot;/\&quot; and \&quot;/sub\&quot; then the retention for \&quot;/\&quot; is applied for any file outside the \&quot;/sub\&quot; directory | [optional]
**retention** | **int** | retention time in hours. All the files with a modification time older than the defined value will be deleted. 0 means exclude this path | [optional]
**delete_empty_dirs** | **bool** | if enabled, empty directories will be deleted | [optional]
**ignore_user_permissions** | **bool** | if enabled, files will be deleted even if the user does not have the delete permission. The default is \&quot;false\&quot; which means that files will be skipped if the user does not have permission to delete them. File patterns filters will always be silently ignored | [optional]

## Example

```python
from openapi_client.models.folder_retention import FolderRetention

# TODO update the JSON string below
json = "{}"
# create an instance of FolderRetention from a JSON string
folder_retention_instance = FolderRetention.from_json(json)
# print the JSON string representation of the object
print FolderRetention.to_json()

# convert the object into a dict
folder_retention_dict = folder_retention_instance.to_dict()
# create an instance of FolderRetention from a dict
folder_retention_form_dict = folder_retention.from_dict(folder_retention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
