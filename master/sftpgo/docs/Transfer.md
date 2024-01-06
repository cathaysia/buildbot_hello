# Transfer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_type** | **str** | Operations:   * &#x60;upload&#x60;   * &#x60;download&#x60;  | [optional]
**path** | **str** | file path for the upload/download | [optional]
**start_time** | **int** | start time as unix timestamp in milliseconds | [optional]
**size** | **int** | bytes transferred | [optional]

## Example

```python
from openapi_client.models.transfer import Transfer

# TODO update the JSON string below
json = "{}"
# create an instance of Transfer from a JSON string
transfer_instance = Transfer.from_json(json)
# print the JSON string representation of the object
print Transfer.to_json()

# convert the object into a dict
transfer_dict = transfer_instance.to_dict()
# create an instance of Transfer from a dict
transfer_form_dict = transfer.from_dict(transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
