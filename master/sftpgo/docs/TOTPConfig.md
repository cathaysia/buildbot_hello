# TOTPConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional]
**issuer** | **str** |  | [optional]
**algo** | [**TOTPHMacAlgo**](TOTPHMacAlgo.md) |  | [optional]

## Example

```python
from openapi_client.models.totp_config import TOTPConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TOTPConfig from a JSON string
totp_config_instance = TOTPConfig.from_json(json)
# print the JSON string representation of the object
print TOTPConfig.to_json()

# convert the object into a dict
totp_config_dict = totp_config_instance.to_dict()
# create an instance of TOTPConfig from a dict
totp_config_form_dict = totp_config.from_dict(totp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
