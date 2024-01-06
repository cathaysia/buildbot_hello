# AdminGroupMappingOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_to_users_as** | **float** | Add to new users as:   * &#x60;0&#x60; - the admin&#39;s group will be added as membership group for new users   * &#x60;1&#x60; - the admin&#39;s group will be added as primary group for new users   * &#x60;2&#x60; - the admin&#39;s group will be added as secondary group for new users  | [optional]

## Example

```python
from openapi_client.models.admin_group_mapping_options import AdminGroupMappingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGroupMappingOptions from a JSON string
admin_group_mapping_options_instance = AdminGroupMappingOptions.from_json(json)
# print the JSON string representation of the object
print AdminGroupMappingOptions.to_json()

# convert the object into a dict
admin_group_mapping_options_dict = admin_group_mapping_options_instance.to_dict()
# create an instance of AdminGroupMappingOptions from a dict
admin_group_mapping_options_form_dict = admin_group_mapping_options.from_dict(admin_group_mapping_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
