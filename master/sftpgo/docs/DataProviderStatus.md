# DataProviderStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | [optional]
**driver** | **str** |  | [optional]
**error** | **str** |  | [optional]

## Example

```python
from openapi_client.models.data_provider_status import DataProviderStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DataProviderStatus from a JSON string
data_provider_status_instance = DataProviderStatus.from_json(json)
# print the JSON string representation of the object
print DataProviderStatus.to_json()

# convert the object into a dict
data_provider_status_dict = data_provider_status_instance.to_dict()
# create an instance of DataProviderStatus from a dict
data_provider_status_form_dict = data_provider_status.from_dict(data_provider_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
