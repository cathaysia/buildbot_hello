# ConnectionStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | connected username | [optional]
**connection_id** | **str** | unique connection identifier | [optional]
**client_version** | **str** | client version | [optional]
**remote_address** | **str** | Remote address for the connected client | [optional]
**connection_time** | **int** | connection time as unix timestamp in milliseconds | [optional]
**command** | **str** | Last SSH/FTP command or WebDAV method | [optional]
**last_activity** | **int** | last client activity as unix timestamp in milliseconds | [optional]
**protocol** | **str** |  | [optional]
**active_transfers** | [**List[Transfer]**](Transfer.md) |  | [optional]
**node** | **str** | Node identifier, omitted for single node installations | [optional]

## Example

```python
from openapi_client.models.connection_status import ConnectionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionStatus from a JSON string
connection_status_instance = ConnectionStatus.from_json(json)
# print the JSON string representation of the object
print ConnectionStatus.to_json()

# convert the object into a dict
connection_status_dict = connection_status_instance.to_dict()
# create an instance of ConnectionStatus from a dict
connection_status_form_dict = connection_status.from_dict(connection_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
