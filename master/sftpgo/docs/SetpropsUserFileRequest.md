# SetpropsUserFileRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modification_time** | **int** | File modification time as unix timestamp in milliseconds | [optional]

## Example

```python
from openapi_client.models.setprops_user_file_request import SetpropsUserFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetpropsUserFileRequest from a JSON string
setprops_user_file_request_instance = SetpropsUserFileRequest.from_json(json)
# print the JSON string representation of the object
print SetpropsUserFileRequest.to_json()

# convert the object into a dict
setprops_user_file_request_dict = setprops_user_file_request_instance.to_dict()
# create an instance of SetpropsUserFileRequest from a dict
setprops_user_file_request_form_dict = setprops_user_file_request.from_dict(setprops_user_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
