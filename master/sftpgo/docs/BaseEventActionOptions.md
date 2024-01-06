# BaseEventActionOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_config** | [**EventActionHTTPConfig**](EventActionHTTPConfig.md) |  | [optional]
**cmd_config** | [**EventActionCommandConfig**](EventActionCommandConfig.md) |  | [optional]
**email_config** | [**EventActionEmailConfig**](EventActionEmailConfig.md) |  | [optional]
**retention_config** | [**EventActionDataRetentionConfig**](EventActionDataRetentionConfig.md) |  | [optional]
**fs_config** | [**EventActionFilesystemConfig**](EventActionFilesystemConfig.md) |  | [optional]
**pwd_expiration_config** | [**EventActionPasswordExpiration**](EventActionPasswordExpiration.md) |  | [optional]
**idp_config** | [**EventActionIDPAccountCheck**](EventActionIDPAccountCheck.md) |  | [optional]

## Example

```python
from openapi_client.models.base_event_action_options import BaseEventActionOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BaseEventActionOptions from a JSON string
base_event_action_options_instance = BaseEventActionOptions.from_json(json)
# print the JSON string representation of the object
print BaseEventActionOptions.to_json()

# convert the object into a dict
base_event_action_options_dict = base_event_action_options_instance.to_dict()
# create an instance of BaseEventActionOptions from a dict
base_event_action_options_form_dict = base_event_action_options.from_dict(base_event_action_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
