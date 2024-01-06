# WebDAVBinding


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | TCP address the server listen on | [optional]
**port** | **int** | the port used for serving requests | [optional]
**enable_https** | **bool** |  | [optional]
**min_tls_version** | [**TLSVersions**](TLSVersions.md) |  | [optional]
**client_auth_type** | **int** | 1 means that client certificate authentication is required in addition to HTTP basic authentication | [optional]
**tls_cipher_suites** | **List[str]** | List of supported cipher suites for TLS version 1.2. If empty  a default list of secure cipher suites is used, with a preference order based on hardware performance | [optional]
**prefix** | **str** | Prefix for WebDAV resources, if empty WebDAV resources will be available at the &#x60;/&#x60; URI | [optional]
**proxy_allowed** | **List[str]** | List of IP addresses and IP ranges allowed to set proxy headers | [optional]

## Example

```python
from openapi_client.models.web_dav_binding import WebDAVBinding

# TODO update the JSON string below
json = "{}"
# create an instance of WebDAVBinding from a JSON string
web_dav_binding_instance = WebDAVBinding.from_json(json)
# print the JSON string representation of the object
print WebDAVBinding.to_json()

# convert the object into a dict
web_dav_binding_dict = web_dav_binding_instance.to_dict()
# create an instance of WebDAVBinding from a dict
web_dav_binding_form_dict = web_dav_binding.from_dict(web_dav_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
