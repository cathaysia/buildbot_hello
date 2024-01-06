# ConditionPattern


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern** | **str** |  | [optional]
**inverse_match** | **bool** |  | [optional]

## Example

```python
from openapi_client.models.condition_pattern import ConditionPattern

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionPattern from a JSON string
condition_pattern_instance = ConditionPattern.from_json(json)
# print the JSON string representation of the object
print ConditionPattern.to_json()

# convert the object into a dict
condition_pattern_dict = condition_pattern_instance.to_dict()
# create an instance of ConditionPattern from a dict
condition_pattern_form_dict = condition_pattern.from_dict(condition_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
