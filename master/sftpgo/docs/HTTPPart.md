# HTTPPart


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional]
**headers** | [**List[KeyValue]**](KeyValue.md) | Additional headers. Content-Disposition header is automatically set. Content-Type header is automatically detect for files to attach | [optional]
**filepath** | **str** | path to the file to be sent as an attachment | [optional]
**body** | **str** |  | [optional]

## Example

```python
from openapi_client.models.http_part import HTTPPart

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPPart from a JSON string
http_part_instance = HTTPPart.from_json(json)
# print the JSON string representation of the object
print HTTPPart.to_json()

# convert the object into a dict
http_part_dict = http_part_instance.to_dict()
# create an instance of HTTPPart from a dict
http_part_form_dict = http_part.from_dict(http_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
