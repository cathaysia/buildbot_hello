# GenerateAdminTotpSecret200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_name** | **str** |  | [optional]
**issuer** | **str** |  | [optional]
**secret** | **str** |  | [optional]
**qr_code** | **bytearray** | QR code png encoded as BASE64 | [optional]

## Example

```python
from openapi_client.models.generate_admin_totp_secret200_response import GenerateAdminTotpSecret200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAdminTotpSecret200Response from a JSON string
generate_admin_totp_secret200_response_instance = GenerateAdminTotpSecret200Response.from_json(json)
# print the JSON string representation of the object
print GenerateAdminTotpSecret200Response.to_json()

# convert the object into a dict
generate_admin_totp_secret200_response_dict = generate_admin_totp_secret200_response_instance.to_dict()
# create an instance of GenerateAdminTotpSecret200Response from a dict
generate_admin_totp_secret200_response_form_dict = generate_admin_totp_secret200_response.from_dict(generate_admin_totp_secret200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
