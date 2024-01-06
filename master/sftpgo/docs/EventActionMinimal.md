# EventActionMinimal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional]
**order** | **int** | execution order | [optional]
**relation_options** | [**EventActionOptions**](EventActionOptions.md) |  | [optional]

## Example

```python
from openapi_client.models.event_action_minimal import EventActionMinimal

# TODO update the JSON string below
json = "{}"
# create an instance of EventActionMinimal from a JSON string
event_action_minimal_instance = EventActionMinimal.from_json(json)
# print the JSON string representation of the object
print EventActionMinimal.to_json()

# convert the object into a dict
event_action_minimal_dict = event_action_minimal_instance.to_dict()
# create an instance of EventActionMinimal from a dict
event_action_minimal_form_dict = event_action_minimal.from_dict(event_action_minimal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
