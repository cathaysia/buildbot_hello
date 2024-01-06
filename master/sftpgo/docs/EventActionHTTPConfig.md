# EventActionHTTPConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | HTTP endpoint | [optional]
**username** | **str** |  | [optional]
**password** | [**Secret**](Secret.md) |  | [optional]
**headers** | [**List[KeyValue]**](KeyValue.md) | headers to add | [optional]
**timeout** | **int** | Ignored for multipart requests with files as attachments | [optional]
**skip_tls_verify** | **bool** | if enabled the HTTP client accepts any TLS certificate presented by the server and any host name in that certificate. In this mode, TLS is susceptible to man-in-the-middle attacks. This should be used only for testing. | [optional]
**method** | **str** |  | [optional]
**query_parameters** | [**List[KeyValue]**](KeyValue.md) |  | [optional]
**body** | **str** | HTTP POST/PUT body | [optional]
**parts** | [**List[HTTPPart]**](HTTPPart.md) | Multipart requests allow to combine one or more sets of data into a single body. For each part, you can set a file path or a body as text. Placeholders are supported in file path, body, header values. | [optional]

## Example

```python
from openapi_client.models.event_action_http_config import EventActionHTTPConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EventActionHTTPConfig from a JSON string
event_action_http_config_instance = EventActionHTTPConfig.from_json(json)
# print the JSON string representation of the object
print EventActionHTTPConfig.to_json()

# convert the object into a dict
event_action_http_config_dict = event_action_http_config_instance.to_dict()
# create an instance of EventActionHTTPConfig from a dict
event_action_http_config_form_dict = event_action_http_config.from_dict(event_action_http_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
