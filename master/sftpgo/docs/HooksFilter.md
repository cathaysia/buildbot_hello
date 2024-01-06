# HooksFilter

User specific hook overrides

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_auth_disabled** | **bool** | If true, the external auth hook, if defined, will not be executed | [optional]
**pre_login_disabled** | **bool** | If true, the pre-login hook, if defined, will not be executed | [optional]
**check_password_disabled** | **bool** | If true, the check password hook, if defined, will not be executed | [optional]

## Example

```python
from openapi_client.models.hooks_filter import HooksFilter

# TODO update the JSON string below
json = "{}"
# create an instance of HooksFilter from a JSON string
hooks_filter_instance = HooksFilter.from_json(json)
# print the JSON string representation of the object
print HooksFilter.to_json()

# convert the object into a dict
hooks_filter_dict = hooks_filter_instance.to_dict()
# create an instance of HooksFilter from a dict
hooks_filter_form_dict = hooks_filter.from_dict(hooks_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
