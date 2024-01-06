# FTPPassivePortRange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** |  | [optional]
**end** | **int** |  | [optional]

## Example

```python
from openapi_client.models.ftp_passive_port_range import FTPPassivePortRange

# TODO update the JSON string below
json = "{}"
# create an instance of FTPPassivePortRange from a JSON string
ftp_passive_port_range_instance = FTPPassivePortRange.from_json(json)
# print the JSON string representation of the object
print FTPPassivePortRange.to_json()

# convert the object into a dict
ftp_passive_port_range_dict = ftp_passive_port_range_instance.to_dict()
# create an instance of FTPPassivePortRange from a dict
ftp_passive_port_range_form_dict = ftp_passive_port_range.from_dict(ftp_passive_port_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
