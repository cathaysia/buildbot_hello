# TransferQuotaUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used_upload_data_transfer** | **int** | The value must be specified as bytes | [optional]
**used_download_data_transfer** | **int** | The value must be specified as bytes | [optional]

## Example

```python
from openapi_client.models.transfer_quota_usage import TransferQuotaUsage

# TODO update the JSON string below
json = "{}"
# create an instance of TransferQuotaUsage from a JSON string
transfer_quota_usage_instance = TransferQuotaUsage.from_json(json)
# print the JSON string representation of the object
print TransferQuotaUsage.to_json()

# convert the object into a dict
transfer_quota_usage_dict = transfer_quota_usage_instance.to_dict()
# create an instance of TransferQuotaUsage from a dict
transfer_quota_usage_form_dict = transfer_quota_usage.from_dict(transfer_quota_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
