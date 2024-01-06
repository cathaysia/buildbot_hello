# AzureBlobFsConfig

Azure Blob Storage configuration details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** |  | [optional]
**account_name** | **str** | Storage Account Name, leave blank to use SAS URL | [optional]
**account_key** | [**Secret**](Secret.md) |  | [optional]
**sas_url** | [**Secret**](Secret.md) |  | [optional]
**endpoint** | **str** | optional endpoint. Default is \&quot;blob.core.windows.net\&quot;. If you use the emulator the endpoint must include the protocol, for example \&quot;http://127.0.0.1:10000\&quot; | [optional]
**upload_part_size** | **int** | the buffer size (in MB) to use for multipart uploads. If this value is set to zero, the default value (5MB) will be used. | [optional]
**upload_concurrency** | **int** | the number of parts to upload in parallel. If this value is set to zero, the default value (5) will be used | [optional]
**download_part_size** | **int** | the buffer size (in MB) to use for multipart downloads. If this value is set to zero, the default value (5MB) will be used. | [optional]
**download_concurrency** | **int** | the number of parts to download in parallel. If this value is set to zero, the default value (5) will be used | [optional]
**access_tier** | **str** |  | [optional]
**key_prefix** | **str** | key_prefix is similar to a chroot directory for a local filesystem. If specified the user will only see contents that starts with this prefix and so you can restrict access to a specific virtual folder. The prefix, if not empty, must not start with \&quot;/\&quot; and must end with \&quot;/\&quot;. If empty the whole container contents will be available | [optional]
**use_emulator** | **bool** |  | [optional]

## Example

```python
from openapi_client.models.azure_blob_fs_config import AzureBlobFsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AzureBlobFsConfig from a JSON string
azure_blob_fs_config_instance = AzureBlobFsConfig.from_json(json)
# print the JSON string representation of the object
print AzureBlobFsConfig.to_json()

# convert the object into a dict
azure_blob_fs_config_dict = azure_blob_fs_config_instance.to_dict()
# create an instance of AzureBlobFsConfig from a dict
azure_blob_fs_config_form_dict = azure_blob_fs_config.from_dict(azure_blob_fs_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
