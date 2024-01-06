# BaseUserFilters

Additional user options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_ip** | **List[str]** | only clients connecting from these IP/Mask are allowed. IP/Mask must be in CIDR notation as defined in RFC 4632 and RFC 4291, for example \&quot;192.0.2.0/24\&quot; or \&quot;2001:db8::/32\&quot; | [optional]
**denied_ip** | **List[str]** | clients connecting from these IP/Mask are not allowed. Denied rules are evaluated before allowed ones | [optional]
**denied_login_methods** | [**List[LoginMethods]**](LoginMethods.md) | if null or empty any available login method is allowed | [optional]
**denied_protocols** | [**List[SupportedProtocols]**](SupportedProtocols.md) | if null or empty any available protocol is allowed | [optional]
**file_patterns** | [**List[PatternsFilter]**](PatternsFilter.md) | filters based on shell like file patterns. These restrictions do not apply to files listing for performance reasons, so a denied file cannot be downloaded/overwritten/renamed but it will still be in the list of files. Please note that these restrictions can be easily bypassed | [optional]
**max_upload_file_size** | **int** | maximum allowed size, as bytes, for a single file upload. The upload will be aborted if/when the size of the file being sent exceeds this limit. 0 means unlimited. This restriction does not apply for SSH system commands such as &#x60;git&#x60; and &#x60;rsync&#x60; | [optional]
**tls_username** | **str** | defines the TLS certificate field to use as username. For FTP clients it must match the name provided using the \&quot;USER\&quot; command. For WebDAV, if no username is provided, the CN will be used as username. For WebDAV clients it must match the implicit or provided username. Ignored if mutual TLS is disabled. Currently the only supported value is &#x60;CommonName&#x60; | [optional]
**hooks** | [**HooksFilter**](HooksFilter.md) |  | [optional]
**disable_fs_checks** | **bool** | Disable checks for existence and automatic creation of home directory and virtual folders. SFTPGo requires that the user&#39;s home directory, virtual folder root, and intermediate paths to virtual folders exist to work properly. If you already know that the required directories exist, disabling these checks will speed up login. You could, for example, disable these checks after the first login | [optional]
**web_client** | [**List[WebClientOptions]**](WebClientOptions.md) | WebClient/user REST API related configuration options | [optional]
**allow_api_key_auth** | **bool** | API key authentication allows to impersonate this user with an API key | [optional]
**user_type** | [**UserType**](UserType.md) |  | [optional]
**bandwidth_limits** | [**List[BandwidthLimit]**](BandwidthLimit.md) |  | [optional]
**external_auth_cache_time** | **int** | Defines the cache time, in seconds, for users authenticated using an external auth hook. 0 means no cache | [optional]
**start_directory** | **str** | Specifies an alternate starting directory. If not set, the default is \&quot;/\&quot;. This option is supported for SFTP/SCP, FTP and HTTP (WebClient/REST API) protocols. Relative paths will use this directory as base. | [optional]
**two_factor_protocols** | [**List[MFAProtocols]**](MFAProtocols.md) | Defines protocols that require two factor authentication | [optional]
**ftp_security** | **int** | Set to &#x60;1&#x60; to require TLS for both data and control connection. his setting is useful if you want to allow both encrypted and plain text FTP sessions globally and then you want to require encrypted sessions on a per-user basis. It has no effect if TLS is already required for all users in the configuration file. | [optional]
**is_anonymous** | **bool** | If enabled the user can login with any password or no password at all. Anonymous users are supported for FTP and WebDAV protocols and permissions will be automatically set to \&quot;list\&quot; and \&quot;download\&quot; (read only) | [optional]
**default_shares_expiration** | **int** | Defines the default expiration for newly created shares as number of days. 0 means no expiration | [optional]
**password_expiration** | **int** | The password expires after the defined number of days. 0 means no expiration | [optional]

## Example

```python
from openapi_client.models.base_user_filters import BaseUserFilters

# TODO update the JSON string below
json = "{}"
# create an instance of BaseUserFilters from a JSON string
base_user_filters_instance = BaseUserFilters.from_json(json)
# print the JSON string representation of the object
print BaseUserFilters.to_json()

# convert the object into a dict
base_user_filters_dict = base_user_filters_instance.to_dict()
# create an instance of BaseUserFilters from a dict
base_user_filters_form_dict = base_user_filters.from_dict(base_user_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
