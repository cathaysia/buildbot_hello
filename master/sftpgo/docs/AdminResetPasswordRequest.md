# AdminResetPasswordRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional]
**password** | **str** |  | [optional]

## Example

```python
from openapi_client.models.admin_reset_password_request import AdminResetPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdminResetPasswordRequest from a JSON string
admin_reset_password_request_instance = AdminResetPasswordRequest.from_json(json)
# print the JSON string representation of the object
print AdminResetPasswordRequest.to_json()

# convert the object into a dict
admin_reset_password_request_dict = admin_reset_password_request_instance.to_dict()
# create an instance of AdminResetPasswordRequest from a dict
admin_reset_password_request_form_dict = admin_reset_password_request.from_dict(admin_reset_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
