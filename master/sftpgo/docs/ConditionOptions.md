# ConditionOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | [**List[ConditionPattern]**](ConditionPattern.md) |  | [optional]
**group_names** | [**List[ConditionPattern]**](ConditionPattern.md) |  | [optional]
**role_names** | [**List[ConditionPattern]**](ConditionPattern.md) |  | [optional]
**fs_paths** | [**List[ConditionPattern]**](ConditionPattern.md) |  | [optional]
**protocols** | **List[str]** |  | [optional]
**provider_objects** | **List[str]** |  | [optional]
**min_size** | **int** |  | [optional]
**max_size** | **int** |  | [optional]
**concurrent_execution** | **bool** | allow concurrent execution from multiple nodes | [optional]

## Example

```python
from openapi_client.models.condition_options import ConditionOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionOptions from a JSON string
condition_options_instance = ConditionOptions.from_json(json)
# print the JSON string representation of the object
print ConditionOptions.to_json()

# convert the object into a dict
condition_options_dict = condition_options_instance.to_dict()
# create an instance of ConditionOptions from a dict
condition_options_form_dict = condition_options.from_dict(condition_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
