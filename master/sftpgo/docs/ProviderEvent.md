# ProviderEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional]
**timestamp** | **int** | unix timestamp in nanoseconds | [optional]
**action** | [**ProviderEventAction**](ProviderEventAction.md) |  | [optional]
**username** | **str** |  | [optional]
**ip** | **str** |  | [optional]
**object_type** | [**ProviderEventObjectType**](ProviderEventObjectType.md) |  | [optional]
**object_name** | **str** |  | [optional]
**object_data** | **bytearray** | base64 of the JSON serialized object with sensitive fields removed | [optional]
**role** | **str** |  | [optional]
**instance_id** | **str** |  | [optional]

## Example

```python
from openapi_client.models.provider_event import ProviderEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderEvent from a JSON string
provider_event_instance = ProviderEvent.from_json(json)
# print the JSON string representation of the object
print ProviderEvent.to_json()

# convert the object into a dict
provider_event_dict = provider_event_instance.to_dict()
# create an instance of ProviderEvent from a dict
provider_event_form_dict = provider_event.from_dict(provider_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
