# EventActionDataRetentionConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folders** | [**List[FolderRetention]**](FolderRetention.md) |  | [optional]

## Example

```python
from openapi_client.models.event_action_data_retention_config import EventActionDataRetentionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EventActionDataRetentionConfig from a JSON string
event_action_data_retention_config_instance = EventActionDataRetentionConfig.from_json(json)
# print the JSON string representation of the object
print EventActionDataRetentionConfig.to_json()

# convert the object into a dict
event_action_data_retention_config_dict = event_action_data_retention_config_instance.to_dict()
# create an instance of EventActionDataRetentionConfig from a dict
event_action_data_retention_config_form_dict = event_action_data_retention_config.from_dict(event_action_data_retention_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
