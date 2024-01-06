# EventActionOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_failure_action** | **bool** |  | [optional]
**stop_on_failure** | **bool** |  | [optional]
**execute_sync** | **bool** |  | [optional]

## Example

```python
from openapi_client.models.event_action_options import EventActionOptions

# TODO update the JSON string below
json = "{}"
# create an instance of EventActionOptions from a JSON string
event_action_options_instance = EventActionOptions.from_json(json)
# print the JSON string representation of the object
print EventActionOptions.to_json()

# convert the object into a dict
event_action_options_dict = event_action_options_instance.to_dict()
# create an instance of EventActionOptions from a dict
event_action_options_form_dict = event_action_options.from_dict(event_action_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
