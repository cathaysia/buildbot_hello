# AdminGroupMapping


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | group name | [optional]
**options** | [**AdminGroupMappingOptions**](AdminGroupMappingOptions.md) |  | [optional]

## Example

```python
from openapi_client.models.admin_group_mapping import AdminGroupMapping

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGroupMapping from a JSON string
admin_group_mapping_instance = AdminGroupMapping.from_json(json)
# print the JSON string representation of the object
print AdminGroupMapping.to_json()

# convert the object into a dict
admin_group_mapping_dict = admin_group_mapping_instance.to_dict()
# create an instance of AdminGroupMapping from a dict
admin_group_mapping_form_dict = admin_group_mapping.from_dict(admin_group_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
