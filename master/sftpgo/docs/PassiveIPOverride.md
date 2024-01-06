# PassiveIPOverride


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**networks** | **List[str]** |  | [optional]
**ip** | **str** |  | [optional]

## Example

```python
from openapi_client.models.passive_ip_override import PassiveIPOverride

# TODO update the JSON string below
json = "{}"
# create an instance of PassiveIPOverride from a JSON string
passive_ip_override_instance = PassiveIPOverride.from_json(json)
# print the JSON string representation of the object
print PassiveIPOverride.to_json()

# convert the object into a dict
passive_ip_override_dict = passive_ip_override_instance.to_dict()
# create an instance of PassiveIPOverride from a dict
passive_ip_override_form_dict = passive_ip_override.from_dict(passive_ip_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
