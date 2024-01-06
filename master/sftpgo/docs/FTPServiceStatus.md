# FTPServiceStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | [optional]
**bindings** | [**List[FTPDBinding]**](FTPDBinding.md) |  | [optional]
**passive_port_range** | [**FTPPassivePortRange**](FTPPassivePortRange.md) |  | [optional]

## Example

```python
from openapi_client.models.ftp_service_status import FTPServiceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FTPServiceStatus from a JSON string
ftp_service_status_instance = FTPServiceStatus.from_json(json)
# print the JSON string representation of the object
print FTPServiceStatus.to_json()

# convert the object into a dict
ftp_service_status_dict = ftp_service_status_instance.to_dict()
# create an instance of FTPServiceStatus from a dict
ftp_service_status_form_dict = ftp_service_status.from_dict(ftp_service_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
