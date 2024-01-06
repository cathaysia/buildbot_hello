# EventActionFsCompress


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Full path to the (zip) archive to create. The parent dir must exist | [optional]
**paths** | **List[str]** | paths to add the archive | [optional]

## Example

```python
from openapi_client.models.event_action_fs_compress import EventActionFsCompress

# TODO update the JSON string below
json = "{}"
# create an instance of EventActionFsCompress from a JSON string
event_action_fs_compress_instance = EventActionFsCompress.from_json(json)
# print the JSON string representation of the object
print EventActionFsCompress.to_json()

# convert the object into a dict
event_action_fs_compress_dict = event_action_fs_compress_instance.to_dict()
# create an instance of EventActionFsCompress from a dict
event_action_fs_compress_form_dict = event_action_fs_compress.from_dict(event_action_fs_compress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
