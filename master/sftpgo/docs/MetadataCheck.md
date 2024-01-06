# MetadataCheck


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | username to which the check refers | [optional]
**start_time** | **int** | check start time as unix timestamp in milliseconds | [optional]

## Example

```python
from openapi_client.models.metadata_check import MetadataCheck

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataCheck from a JSON string
metadata_check_instance = MetadataCheck.from_json(json)
# print the JSON string representation of the object
print MetadataCheck.to_json()

# convert the object into a dict
metadata_check_dict = metadata_check_instance.to_dict()
# create an instance of MetadataCheck from a dict
metadata_check_form_dict = metadata_check.from_dict(metadata_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
