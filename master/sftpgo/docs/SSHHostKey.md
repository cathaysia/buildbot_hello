# SSHHostKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional]
**fingerprint** | **str** |  | [optional]
**algorithms** | **List[str]** |  | [optional]

## Example

```python
from openapi_client.models.ssh_host_key import SSHHostKey

# TODO update the JSON string below
json = "{}"
# create an instance of SSHHostKey from a JSON string
ssh_host_key_instance = SSHHostKey.from_json(json)
# print the JSON string representation of the object
print SSHHostKey.to_json()

# convert the object into a dict
ssh_host_key_dict = ssh_host_key_instance.to_dict()
# create an instance of SSHHostKey from a dict
ssh_host_key_form_dict = ssh_host_key.from_dict(ssh_host_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
