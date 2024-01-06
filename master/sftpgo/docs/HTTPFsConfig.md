# HTTPFsConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | HTTP/S endpoint URL. SFTPGo will use this URL as base, for example for the &#x60;stat&#x60; API, SFTPGo will add &#x60;/stat/{name}&#x60; | [optional]
**username** | **str** |  | [optional]
**password** | [**Secret**](Secret.md) |  | [optional]
**api_key** | [**Secret**](Secret.md) |  | [optional]
**skip_tls_verify** | **bool** |  | [optional]
**equality_check_mode** | **int** | Defines how to check if this config points to the same server as another config. If different configs point to the same server the renaming between the fs configs is allowed:  * &#x60;0&#x60; username and endpoint must match. This is the default  * &#x60;1&#x60; only the endpoint must match  | [optional]

## Example

```python
from openapi_client.models.httpfs_config import HTTPFsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPFsConfig from a JSON string
httpfs_config_instance = HTTPFsConfig.from_json(json)
# print the JSON string representation of the object
print HTTPFsConfig.to_json()

# convert the object into a dict
httpfs_config_dict = httpfs_config_instance.to_dict()
# create an instance of HTTPFsConfig from a dict
httpfs_config_form_dict = httpfs_config.from_dict(httpfs_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
