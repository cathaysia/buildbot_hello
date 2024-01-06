# AddApiKey201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mesage** | **str** |  | [optional]
**key** | **str** | generated API key | [optional]

## Example

```python
from openapi_client.models.add_api_key201_response import AddApiKey201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddApiKey201Response from a JSON string
add_api_key201_response_instance = AddApiKey201Response.from_json(json)
# print the JSON string representation of the object
print AddApiKey201Response.to_json()

# convert the object into a dict
add_api_key201_response_dict = add_api_key201_response_instance.to_dict()
# create an instance of AddApiKey201Response from a dict
add_api_key201_response_form_dict = add_api_key201_response.from_dict(add_api_key201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
