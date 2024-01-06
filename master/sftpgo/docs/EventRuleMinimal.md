# EventRuleMinimal


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
**actions** | [**List[EventActionMinimal]**](EventActionMinimal.md) |  | [optional]

## Example

```python
from openapi_client.models.event_rule_minimal import EventRuleMinimal

# TODO update the JSON string below
json = "{}"
# create an instance of EventRuleMinimal from a JSON string
event_rule_minimal_instance = EventRuleMinimal.from_json(json)
# print the JSON string representation of the object
print EventRuleMinimal.to_json()

# convert the object into a dict
event_rule_minimal_dict = event_rule_minimal_instance.to_dict()
# create an instance of EventRuleMinimal from a dict
event_rule_minimal_form_dict = event_rule_minimal.from_dict(event_rule_minimal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
