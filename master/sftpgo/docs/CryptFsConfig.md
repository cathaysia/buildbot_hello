# CryptFsConfig

Crypt filesystem configuration details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passphrase** | [**Secret**](Secret.md) |  | [optional]
**read_buffer_size** | **int** | The read buffer size, as MB, to use for downloads. 0 means no buffering, that&#39;s fine in most use cases. | [optional]
**write_buffer_size** | **int** | The write buffer size, as MB, to use for uploads. 0 means no buffering, that&#39;s fine in most use cases. | [optional]

## Example

```python
from openapi_client.models.crypt_fs_config import CryptFsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CryptFsConfig from a JSON string
crypt_fs_config_instance = CryptFsConfig.from_json(json)
# print the JSON string representation of the object
print CryptFsConfig.to_json()

# convert the object into a dict
crypt_fs_config_dict = crypt_fs_config_instance.to_dict()
# create an instance of CryptFsConfig from a dict
crypt_fs_config_form_dict = crypt_fs_config.from_dict(crypt_fs_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
