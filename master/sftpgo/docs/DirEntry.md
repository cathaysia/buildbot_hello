# DirEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the file (or subdirectory) described by the entry. This name is the final element of the path (the base name), not the entire path | [optional]
**size** | **int** | file size, omitted for folders and non regular files | [optional]
**mode** | **int** | File mode and permission bits. More details here: https://golang.org/pkg/io/fs/#FileMode. Let&#39;s see some examples: - for a directory mode&amp;2147483648 !&#x3D; 0 - for a symlink mode&amp;134217728 !&#x3D; 0 - for a regular file mode&amp;2401763328 &#x3D;&#x3D; 0  | [optional]
**last_modified** | **datetime** |  | [optional]

## Example

```python
from openapi_client.models.dir_entry import DirEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DirEntry from a JSON string
dir_entry_instance = DirEntry.from_json(json)
# print the JSON string representation of the object
print DirEntry.to_json()

# convert the object into a dict
dir_entry_dict = dir_entry_instance.to_dict()
# create an instance of DirEntry from a dict
dir_entry_form_dict = dir_entry.from_dict(dir_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
