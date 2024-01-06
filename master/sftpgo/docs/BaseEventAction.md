# BaseEventAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional]
**name** | **str** | unique name | [optional]
**description** | **str** | optional description | [optional]
**type** | [**EventActionTypes**](EventActionTypes.md) |  | [optional]
**options** | [**BaseEventActionOptions**](BaseEventActionOptions.md) |  | [optional]
**rules** | **List[str]** | list of event rules names associated with this action | [optional]

## Example

```python
from openapi_client.models.base_event_action import BaseEventAction

# TODO update the JSON string below
json = "{}"
# create an instance of BaseEventAction from a JSON string
base_event_action_instance = BaseEventAction.from_json(json)
# print the JSON string representation of the object
print BaseEventAction.to_json()

# convert the object into a dict
base_event_action_dict = base_event_action_instance.to_dict()
# create an instance of BaseEventAction from a dict
base_event_action_form_dict = base_event_action.from_dict(base_event_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
