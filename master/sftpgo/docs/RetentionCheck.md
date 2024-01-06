# RetentionCheck


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | username to which the retention check refers | [optional]
**folders** | [**List[FolderRetention]**](FolderRetention.md) |  | [optional]
**start_time** | **int** | check start time as unix timestamp in milliseconds | [optional]
**notifications** | [**List[RetentionCheckNotification]**](RetentionCheckNotification.md) |  | [optional]
**email** | **str** | if the notification method is set to \&quot;Email\&quot;, this is the e-mail address that receives the retention check report. This field is automatically set to the email address associated with the administrator starting the check | [optional]

## Example

```python
from openapi_client.models.retention_check import RetentionCheck

# TODO update the JSON string below
json = "{}"
# create an instance of RetentionCheck from a JSON string
retention_check_instance = RetentionCheck.from_json(json)
# print the JSON string representation of the object
print RetentionCheck.to_json()

# convert the object into a dict
retention_check_dict = retention_check_instance.to_dict()
# create an instance of RetentionCheck from a dict
retention_check_form_dict = retention_check.from_dict(retention_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
