# SSHServiceStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | [optional]
**bindings** | [**List[SSHBinding]**](SSHBinding.md) |  | [optional]
**host_keys** | [**List[SSHHostKey]**](SSHHostKey.md) |  | [optional]
**ssh_commands** | **List[str]** |  | [optional]
**authentications** | [**List[SSHAuthentications]**](SSHAuthentications.md) |  | [optional]
**macs** | **List[str]** |  | [optional]
**kex_algorithms** | **List[str]** |  | [optional]
**ciphers** | **List[str]** |  | [optional]

## Example

```python
from openapi_client.models.ssh_service_status import SSHServiceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SSHServiceStatus from a JSON string
ssh_service_status_instance = SSHServiceStatus.from_json(json)
# print the JSON string representation of the object
print SSHServiceStatus.to_json()

# convert the object into a dict
ssh_service_status_dict = ssh_service_status_instance.to_dict()
# create an instance of SSHServiceStatus from a dict
ssh_service_status_form_dict = ssh_service_status.from_dict(ssh_service_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
