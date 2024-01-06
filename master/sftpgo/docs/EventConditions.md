# EventConditions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_events** | **List[str]** |  | [optional]
**provider_events** | **List[str]** |  | [optional]
**schedules** | [**List[Schedule]**](Schedule.md) |  | [optional]
**idp_login_event** | **int** | IDP login events:   - &#x60;0&#x60; any login event   - &#x60;1&#x60; user login event   - &#x60;2&#x60; admin login event  | [optional]
**options** | [**ConditionOptions**](ConditionOptions.md) |  | [optional]

## Example

```python
from openapi_client.models.event_conditions import EventConditions

# TODO update the JSON string below
json = "{}"
# create an instance of EventConditions from a JSON string
event_conditions_instance = EventConditions.from_json(json)
# print the JSON string representation of the object
print EventConditions.to_json()

# convert the object into a dict
event_conditions_dict = event_conditions_instance.to_dict()
# create an instance of EventConditions from a dict
event_conditions_form_dict = event_conditions.from_dict(event_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
