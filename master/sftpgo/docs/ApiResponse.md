# ApiResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | message, can be empty | [optional]
**error** | **str** | error description if any | [optional]

## Example

```python
from openapi_client.models.api_response import ApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResponse from a JSON string
api_response_instance = ApiResponse.from_json(json)
# print the JSON string representation of the object
print ApiResponse.to_json()

# convert the object into a dict
api_response_dict = api_response_instance.to_dict()
# create an instance of ApiResponse from a dict
api_response_form_dict = api_response.from_dict(api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
