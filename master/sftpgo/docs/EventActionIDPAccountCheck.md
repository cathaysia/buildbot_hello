# EventActionIDPAccountCheck


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **int** | Account check mode:   * &#x60;0&#x60; Create or update the account   * &#x60;1&#x60; Create the account if it doesn&#39;t exist  | [optional]
**template_user** | **str** | SFTPGo user template in JSON format | [optional]
**template_admin** | **str** | SFTPGo admin template in JSON format | [optional]

## Example

```python
from openapi_client.models.event_action_idp_account_check import EventActionIDPAccountCheck

# TODO update the JSON string below
json = "{}"
# create an instance of EventActionIDPAccountCheck from a JSON string
event_action_idp_account_check_instance = EventActionIDPAccountCheck.from_json(json)
# print the JSON string representation of the object
print EventActionIDPAccountCheck.to_json()

# convert the object into a dict
event_action_idp_account_check_dict = event_action_idp_account_check_instance.to_dict()
# create an instance of EventActionIDPAccountCheck from a dict
event_action_idp_account_check_form_dict = event_action_idp_account_check.from_dict(event_action_idp_account_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
