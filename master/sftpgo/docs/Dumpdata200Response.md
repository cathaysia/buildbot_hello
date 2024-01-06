# Dumpdata200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | message, can be empty | [optional]
**error** | **str** | error description if any | [optional]
**users** | [**List[User]**](User.md) |  | [optional]
**folders** | [**List[BaseVirtualFolder]**](BaseVirtualFolder.md) |  | [optional]
**groups** | [**List[Group]**](Group.md) |  | [optional]
**admins** | [**List[Admin]**](Admin.md) |  | [optional]
**api_keys** | [**List[APIKey]**](APIKey.md) |  | [optional]
**shares** | [**List[Share]**](Share.md) |  | [optional]
**event_actions** | [**List[EventAction]**](EventAction.md) |  | [optional]
**event_rules** | [**List[EventRule]**](EventRule.md) |  | [optional]
**roles** | [**List[Role]**](Role.md) |  | [optional]
**version** | **int** |  | [optional]

## Example

```python
from openapi_client.models.dumpdata200_response import Dumpdata200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Dumpdata200Response from a JSON string
dumpdata200_response_instance = Dumpdata200Response.from_json(json)
# print the JSON string representation of the object
print Dumpdata200Response.to_json()

# convert the object into a dict
dumpdata200_response_dict = dumpdata200_response_instance.to_dict()
# create an instance of Dumpdata200Response from a dict
dumpdata200_response_form_dict = dumpdata200_response.from_dict(dumpdata200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
