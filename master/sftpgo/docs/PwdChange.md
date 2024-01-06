# PwdChange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** |  | [optional]
**new_password** | **str** |  | [optional]

## Example

```python
from openapi_client.models.pwd_change import PwdChange

# TODO update the JSON string below
json = "{}"
# create an instance of PwdChange from a JSON string
pwd_change_instance = PwdChange.from_json(json)
# print the JSON string representation of the object
print PwdChange.to_json()

# convert the object into a dict
pwd_change_dict = pwd_change_instance.to_dict()
# create an instance of PwdChange from a dict
pwd_change_form_dict = pwd_change.from_dict(pwd_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
