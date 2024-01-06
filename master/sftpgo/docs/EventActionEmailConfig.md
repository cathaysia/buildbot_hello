# EventActionEmailConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | **List[str]** |  | [optional]
**bcc** | **List[str]** |  | [optional]
**subject** | **str** |  | [optional]
**body** | **str** |  | [optional]
**content_type** | **int** | Content type:   * &#x60;0&#x60; text/plain   * &#x60;1&#x60; text/html  | [optional]
**attachments** | **List[str]** | list of file paths to attach. The total size is limited to 10 MB | [optional]

## Example

```python
from openapi_client.models.event_action_email_config import EventActionEmailConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EventActionEmailConfig from a JSON string
event_action_email_config_instance = EventActionEmailConfig.from_json(json)
# print the JSON string representation of the object
print EventActionEmailConfig.to_json()

# convert the object into a dict
event_action_email_config_dict = event_action_email_config_instance.to_dict()
# create an instance of EventActionEmailConfig from a dict
event_action_email_config_form_dict = event_action_email_config.from_dict(event_action_email_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
