# BackupData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from openapi_client.models.backup_data import BackupData

# TODO update the JSON string below
json = "{}"
# create an instance of BackupData from a JSON string
backup_data_instance = BackupData.from_json(json)
# print the JSON string representation of the object
print BackupData.to_json()

# convert the object into a dict
backup_data_dict = backup_data_instance.to_dict()
# create an instance of BackupData from a dict
backup_data_form_dict = backup_data.from_dict(backup_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
