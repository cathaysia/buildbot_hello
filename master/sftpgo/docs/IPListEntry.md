# IPListEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipornet** | **str** | IP address or network in CIDR format, for example &#x60;192.168.1.2/32&#x60;, &#x60;192.168.0.0/24&#x60;, &#x60;2001:db8::/32&#x60; | [optional]
**description** | **str** | optional description | [optional]
**type** | [**IPListType**](IPListType.md) |  | [optional]
**mode** | [**IPListMode**](IPListMode.md) |  | [optional]
**protocols** | **int** | Defines the protocol the entry applies to. &#x60;0&#x60; means all the supported protocols, 1 SSH, 2 FTP, 4 WebDAV, 8 HTTP. Protocols can be combined, for example 3 means SSH and FTP | [optional]
**created_at** | **int** | creation time as unix timestamp in milliseconds | [optional]
**updated_at** | **int** | last update time as unix timestamp in millisecond | [optional]

## Example

```python
from openapi_client.models.ip_list_entry import IPListEntry

# TODO update the JSON string below
json = "{}"
# create an instance of IPListEntry from a JSON string
ip_list_entry_instance = IPListEntry.from_json(json)
# print the JSON string representation of the object
print IPListEntry.to_json()

# convert the object into a dict
ip_list_entry_dict = ip_list_entry_instance.to_dict()
# create an instance of IPListEntry from a dict
ip_list_entry_form_dict = ip_list_entry.from_dict(ip_list_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
