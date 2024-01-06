# Secret

The secret is encrypted before saving, so to set a new secret you must provide a payload and set the status to \"Plain\". The encryption key and additional data will be generated automatically. If you set the status to \"Redacted\" the existing secret will be preserved

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Set to \&quot;Plain\&quot; to add or update an existing secret, set to \&quot;Redacted\&quot; to preserve the existing value | [optional]
**payload** | **str** |  | [optional]
**key** | **str** |  | [optional]
**additional_data** | **str** |  | [optional]
**mode** | **int** | 1 means encrypted using a master key | [optional]

## Example

```python
from openapi_client.models.secret import Secret

# TODO update the JSON string below
json = "{}"
# create an instance of Secret from a JSON string
secret_instance = Secret.from_json(json)
# print the JSON string representation of the object
print Secret.to_json()

# convert the object into a dict
secret_dict = secret_instance.to_dict()
# create an instance of Secret from a dict
secret_form_dict = secret.from_dict(secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
