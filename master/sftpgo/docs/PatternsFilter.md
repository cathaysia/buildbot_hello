# PatternsFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | virtual path as seen by users, if no other specific filter is defined, the filter applies for sub directories too. For example if filters are defined for the paths \&quot;/\&quot; and \&quot;/sub\&quot; then the filters for \&quot;/\&quot; are applied for any file outside the \&quot;/sub\&quot; directory | [optional]
**allowed_patterns** | **List[str]** | list of, case insensitive, allowed shell like patterns. Allowed patterns are evaluated before the denied ones | [optional]
**denied_patterns** | **List[str]** | list of, case insensitive, denied shell like patterns | [optional]
**deny_policy** | **int** | Policies for denied patterns   * &#x60;0&#x60; - default policy. Denied files/directories matching the filters are visible in directory listing but cannot be uploaded/downloaded/overwritten/renamed   * &#x60;1&#x60; - deny policy hide. This policy applies the same restrictions as the default one and denied files/directories matching the filters will also be hidden in directory listing. This mode may cause performance issues for large directories  | [optional]

## Example

```python
from openapi_client.models.patterns_filter import PatternsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of PatternsFilter from a JSON string
patterns_filter_instance = PatternsFilter.from_json(json)
# print the JSON string representation of the object
print PatternsFilter.to_json()

# convert the object into a dict
patterns_filter_dict = patterns_filter_instance.to_dict()
# create an instance of PatternsFilter from a dict
patterns_filter_form_dict = patterns_filter.from_dict(patterns_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
