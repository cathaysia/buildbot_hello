# ServicesStatusRateLimiters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | [optional]
**protocols** | **List[str]** |  | [optional]

## Example

```python
from openapi_client.models.services_status_rate_limiters import ServicesStatusRateLimiters

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesStatusRateLimiters from a JSON string
services_status_rate_limiters_instance = ServicesStatusRateLimiters.from_json(json)
# print the JSON string representation of the object
print ServicesStatusRateLimiters.to_json()

# convert the object into a dict
services_status_rate_limiters_dict = services_status_rate_limiters_instance.to_dict()
# create an instance of ServicesStatusRateLimiters from a dict
services_status_rate_limiters_form_dict = services_status_rate_limiters.from_dict(services_status_rate_limiters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
