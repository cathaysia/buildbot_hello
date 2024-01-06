# WebDAVServiceStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | [optional]
**bindings** | [**List[WebDAVBinding]**](WebDAVBinding.md) |  | [optional]

## Example

```python
from openapi_client.models.web_dav_service_status import WebDAVServiceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WebDAVServiceStatus from a JSON string
web_dav_service_status_instance = WebDAVServiceStatus.from_json(json)
# print the JSON string representation of the object
print WebDAVServiceStatus.to_json()

# convert the object into a dict
web_dav_service_status_dict = web_dav_service_status_instance.to_dict()
# create an instance of WebDAVServiceStatus from a dict
web_dav_service_status_form_dict = web_dav_service_status.from_dict(web_dav_service_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
