# AdminPreferences


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hide_user_page_sections** | **int** | Allow to hide some sections from the user page. These are not security settings and are not enforced server side in any way. They are only intended to simplify the user page in the WebAdmin UI. 1 means hide groups section, 2 means hide filesystem section, \&quot;users_base_dir\&quot; must be set in the config file otherwise this setting is ignored, 4 means hide virtual folders section, 8 means hide profile section, 16 means hide ACLs section, 32 means hide disk and bandwidth quota limits section, 64 means hide advanced settings section. The settings can be combined | [optional]
**default_users_expiration** | **int** | Defines the default expiration for newly created users as number of days. 0 means no expiration | [optional]

## Example

```python
from openapi_client.models.admin_preferences import AdminPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPreferences from a JSON string
admin_preferences_instance = AdminPreferences.from_json(json)
# print the JSON string representation of the object
print AdminPreferences.to_json()

# convert the object into a dict
admin_preferences_dict = admin_preferences_instance.to_dict()
# create an instance of AdminPreferences from a dict
admin_preferences_form_dict = admin_preferences.from_dict(admin_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
