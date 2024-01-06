# ServicesStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh** | [**SSHServiceStatus**](SSHServiceStatus.md) |  | [optional]
**ftp** | [**FTPServiceStatus**](FTPServiceStatus.md) |  | [optional]
**webdav** | [**WebDAVServiceStatus**](WebDAVServiceStatus.md) |  | [optional]
**data_provider** | [**DataProviderStatus**](DataProviderStatus.md) |  | [optional]
**defender** | [**ServicesStatusDefender**](ServicesStatusDefender.md) |  | [optional]
**mfa** | [**MFAStatus**](MFAStatus.md) |  | [optional]
**allow_list** | [**ServicesStatusDefender**](ServicesStatusDefender.md) |  | [optional]
**rate_limiters** | [**ServicesStatusRateLimiters**](ServicesStatusRateLimiters.md) |  | [optional]

## Example

```python
from openapi_client.models.services_status import ServicesStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesStatus from a JSON string
services_status_instance = ServicesStatus.from_json(json)
# print the JSON string representation of the object
print ServicesStatus.to_json()

# convert the object into a dict
services_status_dict = services_status_instance.to_dict()
# create an instance of ServicesStatus from a dict
services_status_form_dict = services_status.from_dict(services_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
