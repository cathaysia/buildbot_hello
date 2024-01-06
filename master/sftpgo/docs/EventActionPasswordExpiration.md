# EventActionPasswordExpiration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold** | **int** | An email notification will be generated for users whose password expires in a number of days less than or equal to this threshold | [optional]

## Example

```python
from openapi_client.models.event_action_password_expiration import EventActionPasswordExpiration

# TODO update the JSON string below
json = "{}"
# create an instance of EventActionPasswordExpiration from a JSON string
event_action_password_expiration_instance = EventActionPasswordExpiration.from_json(json)
# print the JSON string representation of the object
print EventActionPasswordExpiration.to_json()

# convert the object into a dict
event_action_password_expiration_dict = event_action_password_expiration_instance.to_dict()
# create an instance of EventActionPasswordExpiration from a dict
event_action_password_expiration_form_dict = event_action_password_expiration.from_dict(event_action_password_expiration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
