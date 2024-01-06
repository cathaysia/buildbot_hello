# QuotaUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used_quota_size** | **int** |  | [optional]
**used_quota_files** | **int** |  | [optional]

## Example

```python
from openapi_client.models.quota_usage import QuotaUsage

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaUsage from a JSON string
quota_usage_instance = QuotaUsage.from_json(json)
# print the JSON string representation of the object
print QuotaUsage.to_json()

# convert the object into a dict
quota_usage_dict = quota_usage_instance.to_dict()
# create an instance of QuotaUsage from a dict
quota_usage_form_dict = quota_usage.from_dict(quota_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
