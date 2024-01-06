# QuotaScan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | username to which the quota scan refers | [optional]
**start_time** | **int** | scan start time as unix timestamp in milliseconds | [optional]

## Example

```python
from openapi_client.models.quota_scan import QuotaScan

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaScan from a JSON string
quota_scan_instance = QuotaScan.from_json(json)
# print the JSON string representation of the object
print QuotaScan.to_json()

# convert the object into a dict
quota_scan_dict = quota_scan_instance.to_dict()
# create an instance of QuotaScan from a dict
quota_scan_form_dict = quota_scan.from_dict(quota_scan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
