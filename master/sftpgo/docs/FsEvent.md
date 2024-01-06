# FsEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional]
**timestamp** | **int** | unix timestamp in nanoseconds | [optional]
**action** | [**FsEventAction**](FsEventAction.md) |  | [optional]
**username** | **str** |  | [optional]
**fs_path** | **str** |  | [optional]
**fs_target_path** | **str** |  | [optional]
**virtual_path** | **str** |  | [optional]
**virtual_target_path** | **str** |  | [optional]
**ssh_cmd** | **str** |  | [optional]
**file_size** | **int** |  | [optional]
**elapsed** | **int** | elapsed time as milliseconds | [optional]
**status** | [**FsEventStatus**](FsEventStatus.md) |  | [optional]
**protocol** | [**EventProtocols**](EventProtocols.md) |  | [optional]
**ip** | **str** |  | [optional]
**session_id** | **str** |  | [optional]
**fs_provider** | [**FsProviders**](FsProviders.md) |  | [optional]
**bucket** | **str** |  | [optional]
**endpoint** | **str** |  | [optional]
**open_flags** | **str** |  | [optional]
**role** | **str** |  | [optional]
**instance_id** | **str** |  | [optional]

## Example

```python
from openapi_client.models.fs_event import FsEvent

# TODO update the JSON string below
json = "{}"
# create an instance of FsEvent from a JSON string
fs_event_instance = FsEvent.from_json(json)
# print the JSON string representation of the object
print FsEvent.to_json()

# convert the object into a dict
fs_event_dict = fs_event_instance.to_dict()
# create an instance of FsEvent from a dict
fs_event_form_dict = fs_event.from_dict(fs_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
