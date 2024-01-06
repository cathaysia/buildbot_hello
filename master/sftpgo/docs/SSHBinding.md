# SSHBinding


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | TCP address the server listen on | [optional]
**port** | **int** | the port used for serving requests | [optional]
**apply_proxy_config** | **bool** | apply the proxy configuration, if any | [optional]

## Example

```python
from openapi_client.models.ssh_binding import SSHBinding

# TODO update the JSON string below
json = "{}"
# create an instance of SSHBinding from a JSON string
ssh_binding_instance = SSHBinding.from_json(json)
# print the JSON string representation of the object
print SSHBinding.to_json()

# convert the object into a dict
ssh_binding_dict = ssh_binding_instance.to_dict()
# create an instance of SSHBinding from a dict
ssh_binding_form_dict = ssh_binding.from_dict(ssh_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
