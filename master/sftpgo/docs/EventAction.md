# EventAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional]
**name** | **str** | unique name | [optional]
**description** | **str** | optional description | [optional]
**type** | [**EventActionTypes**](EventActionTypes.md) |  | [optional]
**options** | [**BaseEventActionOptions**](BaseEventActionOptions.md) |  | [optional]
**rules** | **List[str]** | list of event rules names associated with this action | [optional]
**order** | **int** | execution order | [optional]
**relation_options** | [**EventActionOptions**](EventActionOptions.md) |  | [optional]

## Example

```python
from openapi_client.models.event_action import EventAction

# TODO update the JSON string below
json = "{}"
# create an instance of EventAction from a JSON string
event_action_instance = EventAction.from_json(json)
# print the JSON string representation of the object
print EventAction.to_json()

# convert the object into a dict
event_action_dict = event_action_instance.to_dict()
# create an instance of EventAction from a dict
event_action_form_dict = event_action.from_dict(event_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
