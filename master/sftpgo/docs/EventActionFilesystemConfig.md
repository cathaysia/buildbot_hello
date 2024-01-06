# EventActionFilesystemConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FilesystemActionTypes**](FilesystemActionTypes.md) |  | [optional]
**renames** | [**List[KeyValue]**](KeyValue.md) |  | [optional]
**mkdirs** | **List[str]** |  | [optional]
**deletes** | **List[str]** |  | [optional]
**exist** | **List[str]** |  | [optional]
**copy** | [**List[KeyValue]**](KeyValue.md) |  | [optional]
**compress** | [**EventActionFsCompress**](EventActionFsCompress.md) |  | [optional]

## Example

```python
from openapi_client.models.event_action_filesystem_config import EventActionFilesystemConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EventActionFilesystemConfig from a JSON string
event_action_filesystem_config_instance = EventActionFilesystemConfig.from_json(json)
# print the JSON string representation of the object
print EventActionFilesystemConfig.to_json()

# convert the object into a dict
event_action_filesystem_config_dict = event_action_filesystem_config_instance.to_dict()
# create an instance of EventActionFilesystemConfig from a dict
event_action_filesystem_config_form_dict = event_action_filesystem_config.from_dict(event_action_filesystem_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
