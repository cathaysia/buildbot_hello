# EventActionCommandConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | absolute path to the command to execute | [optional]
**args** | **List[str]** | command line arguments | [optional]
**timeout** | **int** |  | [optional]
**env_vars** | [**List[KeyValue]**](KeyValue.md) |  | [optional]

## Example

```python
from openapi_client.models.event_action_command_config import EventActionCommandConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EventActionCommandConfig from a JSON string
event_action_command_config_instance = EventActionCommandConfig.from_json(json)
# print the JSON string representation of the object
print EventActionCommandConfig.to_json()

# convert the object into a dict
event_action_command_config_dict = event_action_command_config_instance.to_dict()
# create an instance of EventActionCommandConfig from a dict
event_action_command_config_form_dict = event_action_command_config.from_dict(event_action_command_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
