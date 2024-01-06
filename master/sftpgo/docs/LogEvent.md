# LogEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional]
**timestamp** | **int** | unix timestamp in nanoseconds | [optional]
**event** | [**LogEventType**](LogEventType.md) |  | [optional]
**protocol** | [**EventProtocols**](EventProtocols.md) |  | [optional]
**username** | **str** |  | [optional]
**ip** | **str** |  | [optional]
**message** | **str** |  | [optional]
**role** | **str** |  | [optional]
**instance_id** | **str** |  | [optional]

## Example

```python
from openapi_client.models.log_event import LogEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LogEvent from a JSON string
log_event_instance = LogEvent.from_json(json)
# print the JSON string representation of the object
print LogEvent.to_json()

# convert the object into a dict
log_event_dict = log_event_instance.to_dict()
# create an instance of LogEvent from a dict
log_event_form_dict = log_event.from_dict(log_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
