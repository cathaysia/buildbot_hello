# FilesystemConfig

Storage filesystem details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**FsProviders**](FsProviders.md) |  | [optional]
**osconfig** | [**OSFsConfig**](OSFsConfig.md) |  | [optional]
**s3config** | [**S3Config**](S3Config.md) |  | [optional]
**gcsconfig** | [**GCSConfig**](GCSConfig.md) |  | [optional]
**azblobconfig** | [**AzureBlobFsConfig**](AzureBlobFsConfig.md) |  | [optional]
**cryptconfig** | [**CryptFsConfig**](CryptFsConfig.md) |  | [optional]
**sftpconfig** | [**SFTPFsConfig**](SFTPFsConfig.md) |  | [optional]
**httpconfig** | [**HTTPFsConfig**](HTTPFsConfig.md) |  | [optional]

## Example

```python
from openapi_client.models.filesystem_config import FilesystemConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FilesystemConfig from a JSON string
filesystem_config_instance = FilesystemConfig.from_json(json)
# print the JSON string representation of the object
print FilesystemConfig.to_json()

# convert the object into a dict
filesystem_config_dict = filesystem_config_instance.to_dict()
# create an instance of FilesystemConfig from a dict
filesystem_config_form_dict = filesystem_config.from_dict(filesystem_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
