# FolderQuotaScan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | folder name to which the quota scan refers | [optional]
**start_time** | **int** | scan start time as unix timestamp in milliseconds | [optional]

## Example

```python
from openapi_client.models.folder_quota_scan import FolderQuotaScan

# TODO update the JSON string below
json = "{}"
# create an instance of FolderQuotaScan from a JSON string
folder_quota_scan_instance = FolderQuotaScan.from_json(json)
# print the JSON string representation of the object
print FolderQuotaScan.to_json()

# convert the object into a dict
folder_quota_scan_dict = folder_quota_scan_instance.to_dict()
# create an instance of FolderQuotaScan from a dict
folder_quota_scan_form_dict = folder_quota_scan.from_dict(folder_quota_scan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
