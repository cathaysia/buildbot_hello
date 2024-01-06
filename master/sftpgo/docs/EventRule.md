# EventRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional]
**name** | **str** | unique name | [optional]
**status** | **int** | status:   * &#x60;0&#x60; disabled   * &#x60;1&#x60; enabled  | [optional]
**description** | **str** | optional description | [optional]
**created_at** | **int** | creation time as unix timestamp in milliseconds | [optional]
**updated_at** | **int** | last update time as unix timestamp in millisecond | [optional]
**trigger** | [**EventTriggerTypes**](EventTriggerTypes.md) |  | [optional]
**conditions** | [**EventConditions**](EventConditions.md) |  | [optional]
**actions** | [**List[EventAction]**](EventAction.md) |  | [optional]

## Example

```python
from openapi_client.models.event_rule import EventRule

# TODO update the JSON string below
json = "{}"
# create an instance of EventRule from a JSON string
event_rule_instance = EventRule.from_json(json)
# print the JSON string representation of the object
print EventRule.to_json()

# convert the object into a dict
event_rule_dict = event_rule_instance.to_dict()
# create an instance of EventRule from a dict
event_rule_form_dict = event_rule.from_dict(event_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
