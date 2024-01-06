# GroupMapping


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | group name | [optional]
**type** | **float** | Group type:   * &#x60;1&#x60; - Primary group   * &#x60;2&#x60; - Secondary group   * &#x60;3&#x60; - Membership only, no settings are inherited from this group type  | [optional]

## Example

```python
from openapi_client.models.group_mapping import GroupMapping

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMapping from a JSON string
group_mapping_instance = GroupMapping.from_json(json)
# print the JSON string representation of the object
print GroupMapping.to_json()

# convert the object into a dict
group_mapping_dict = group_mapping_instance.to_dict()
# create an instance of GroupMapping from a dict
group_mapping_form_dict = group_mapping.from_dict(group_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
