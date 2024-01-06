# Admin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional]
**status** | **int** | status:   * &#x60;0&#x60; user is disabled, login is not allowed   * &#x60;1&#x60; user is enabled  | [optional]
**username** | **str** | username is unique | [optional]
**description** | **str** | optional description, for example the admin full name | [optional]
**password** | **str** | Admin password. For security reasons this field is omitted when you search/get admins | [optional]
**email** | **str** |  | [optional]
**permissions** | [**List[AdminPermissions]**](AdminPermissions.md) |  | [optional]
**filters** | [**AdminFilters**](AdminFilters.md) |  | [optional]
**additional_info** | **str** | Free form text field | [optional]
**groups** | [**List[AdminGroupMapping]**](AdminGroupMapping.md) | Groups automatically selected for new users created by this admin. The admin will still be able to choose different groups. These settings are only used for this admin UI and they will be ignored in REST API/hooks. | [optional]
**created_at** | **int** | creation time as unix timestamp in milliseconds. It will be 0 for admins created before v2.2.0 | [optional]
**updated_at** | **int** | last update time as unix timestamp in milliseconds | [optional]
**last_login** | **int** | Last user login as unix timestamp in milliseconds. It is saved at most once every 10 minutes | [optional]
**role** | **str** | If set the admin can only administer users with the same role. Role admins cannot have the following permissions: \&quot;manage_admins\&quot;, \&quot;manage_apikeys\&quot;, \&quot;manage_system\&quot;, \&quot;manage_event_rules\&quot;, \&quot;manage_roles\&quot;, \&quot;manage_ip_lists\&quot; | [optional]

## Example

```python
from openapi_client.models.admin import Admin

# TODO update the JSON string below
json = "{}"
# create an instance of Admin from a JSON string
admin_instance = Admin.from_json(json)
# print the JSON string representation of the object
print Admin.to_json()

# convert the object into a dict
admin_dict = admin_instance.to_dict()
# create an instance of Admin from a dict
admin_form_dict = admin.from_dict(admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
