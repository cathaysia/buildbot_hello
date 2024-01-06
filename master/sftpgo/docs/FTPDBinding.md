# FTPDBinding


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | TCP address the server listen on | [optional]
**port** | **int** | the port used for serving requests | [optional]
**apply_proxy_config** | **bool** | apply the proxy configuration, if any | [optional]
**tls_mode** | **int** | TLS mode:   * &#x60;0&#x60; - clear or explicit TLS   * &#x60;1&#x60; - explicit TLS required   * &#x60;2&#x60; - implicit TLS  | [optional]
**min_tls_version** | [**TLSVersions**](TLSVersions.md) |  | [optional]
**force_passive_ip** | **str** | External IP address for passive connections | [optional]
**passive_ip_overrides** | [**List[PassiveIPOverride]**](PassiveIPOverride.md) |  | [optional]
**client_auth_type** | **int** | 1 means that client certificate authentication is required in addition to FTP authentication | [optional]
**tls_cipher_suites** | **List[str]** | List of supported cipher suites for TLS version 1.2. If empty  a default list of secure cipher suites is used, with a preference order based on hardware performance | [optional]
**passive_connections_security** | **int** | Active connections security:   * &#x60;0&#x60; - require matching peer IP addresses of control and data connection   * &#x60;1&#x60; - disable any checks  | [optional]
**active_connections_security** | **int** | Active connections security:   * &#x60;0&#x60; - require matching peer IP addresses of control and data connection   * &#x60;1&#x60; - disable any checks  | [optional]
**debug** | **bool** | If enabled any FTP command will be logged | [optional]

## Example

```python
from openapi_client.models.ftpd_binding import FTPDBinding

# TODO update the JSON string below
json = "{}"
# create an instance of FTPDBinding from a JSON string
ftpd_binding_instance = FTPDBinding.from_json(json)
# print the JSON string representation of the object
print FTPDBinding.to_json()

# convert the object into a dict
ftpd_binding_dict = ftpd_binding_instance.to_dict()
# create an instance of FTPDBinding from a dict
ftpd_binding_form_dict = ftpd_binding.from_dict(ftpd_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
