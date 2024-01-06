# BandwidthLimit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | **List[str]** | Source networks in CIDR notation as defined in RFC 4632 and RFC 4291 for example &#x60;192.0.2.0/24&#x60; or &#x60;2001:db8::/32&#x60;. The limit applies if the defined networks contain the client IP | [optional]
**upload_bandwidth** | **int** | Maximum upload bandwidth as KB/s, 0 means unlimited | [optional]
**download_bandwidth** | **int** | Maximum download bandwidth as KB/s, 0 means unlimited | [optional]

## Example

```python
from openapi_client.models.bandwidth_limit import BandwidthLimit

# TODO update the JSON string below
json = "{}"
# create an instance of BandwidthLimit from a JSON string
bandwidth_limit_instance = BandwidthLimit.from_json(json)
# print the JSON string representation of the object
print BandwidthLimit.to_json()

# convert the object into a dict
bandwidth_limit_dict = bandwidth_limit_instance.to_dict()
# create an instance of BandwidthLimit from a dict
bandwidth_limit_form_dict = bandwidth_limit.from_dict(bandwidth_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
