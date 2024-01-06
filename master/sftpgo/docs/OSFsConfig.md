# OSFsConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_buffer_size** | **int** | The read buffer size, as MB, to use for downloads. 0 means no buffering, that&#39;s fine in most use cases. | [optional]
**write_buffer_size** | **int** | The write buffer size, as MB, to use for uploads. 0 means no buffering, that&#39;s fine in most use cases. | [optional]

## Example

```python
from openapi_client.models.osfs_config import OSFsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of OSFsConfig from a JSON string
osfs_config_instance = OSFsConfig.from_json(json)
# print the JSON string representation of the object
print OSFsConfig.to_json()

# convert the object into a dict
osfs_config_dict = osfs_config_instance.to_dict()
# create an instance of OSFsConfig from a dict
osfs_config_form_dict = osfs_config.from_dict(osfs_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
