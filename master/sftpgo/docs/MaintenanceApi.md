# openapi_client.MaintenanceApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dumpdata**](MaintenanceApi.md#dumpdata) | **GET** /dumpdata | Dump data
[**get_status**](MaintenanceApi.md#get_status) | **GET** /status | Get status
[**get_version**](MaintenanceApi.md#get_version) | **GET** /version | Get version details
[**loaddata_from_file**](MaintenanceApi.md#loaddata_from_file) | **GET** /loaddata | Load data from path
[**loaddata_from_request_body**](MaintenanceApi.md#loaddata_from_request_body) | **POST** /loaddata | Load data


# **dumpdata**
> Dumpdata200Response dumpdata(output_file=output_file, output_data=output_data, indent=indent, scopes=scopes)

Dump data

Backups data as data provider independent JSON. The backup can be saved in a local file on the server, to avoid exposing sensitive data over the network, or returned as response body. The output of dumpdata can be used as input for loaddata

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.dump_data_scopes import DumpDataScopes
from openapi_client.models.dumpdata200_response import Dumpdata200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MaintenanceApi(api_client)
    output_file = 'output_file_example' # str | Path for the file to write the JSON serialized data to. This path is relative to the configured \"backups_path\". If this file already exists it will be overwritten. To return the backup as response body set `output_data` to true instead. (optional)
    output_data = 56 # int | output data:   * `0` or any other value != 1, the backup will be saved to a file on the server, `output_file` is required   * `1` the backup will be returned as response body  (optional)
    indent = 56 # int | indent:   * `0` no indentation. This is the default   * `1` format the output JSON  (optional)
    scopes = [openapi_client.DumpDataScopes()] # List[DumpDataScopes] | You can limit the dump contents to the specified scopes. Empty or missing means any supported scope. Scopes must be specified comma separated (optional)

    try:
        # Dump data
        api_response = api_instance.dumpdata(output_file=output_file, output_data=output_data, indent=indent, scopes=scopes)
        print("The response of MaintenanceApi->dumpdata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceApi->dumpdata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_file** | **str**| Path for the file to write the JSON serialized data to. This path is relative to the configured \&quot;backups_path\&quot;. If this file already exists it will be overwritten. To return the backup as response body set &#x60;output_data&#x60; to true instead. | [optional]
 **output_data** | **int**| output data:   * &#x60;0&#x60; or any other value !&#x3D; 1, the backup will be saved to a file on the server, &#x60;output_file&#x60; is required   * &#x60;1&#x60; the backup will be returned as response body  | [optional]
 **indent** | **int**| indent:   * &#x60;0&#x60; no indentation. This is the default   * &#x60;1&#x60; format the output JSON  | [optional]
 **scopes** | [**List[DumpDataScopes]**](DumpDataScopes.md)| You can limit the dump contents to the specified scopes. Empty or missing means any supported scope. Scopes must be specified comma separated | [optional]

### Return type

[**Dumpdata200Response**](Dumpdata200Response.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> ServicesStatus get_status()

Get status

Retrieves the status of the active services

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.services_status import ServicesStatus
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MaintenanceApi(api_client)

    try:
        # Get status
        api_response = api_instance.get_status()
        print("The response of MaintenanceApi->get_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceApi->get_status: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ServicesStatus**](ServicesStatus.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> VersionInfo get_version()

Get version details

Returns version details such as the version number, build date, commit hash and enabled features

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.version_info import VersionInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MaintenanceApi(api_client)

    try:
        # Get version details
        api_response = api_instance.get_version()
        print("The response of MaintenanceApi->get_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceApi->get_version: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionInfo**](VersionInfo.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loaddata_from_file**
> ApiResponse loaddata_from_file(input_file, scan_quota=scan_quota, mode=mode)

Load data from path

Restores SFTPGo data from a JSON backup file on the server. Objects will be restored one by one and the restore is stopped if a object cannot be added or updated, so it could happen a partial restore

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MaintenanceApi(api_client)
    input_file = 'input_file_example' # str | Path for the file to read the JSON serialized data from. This can be an absolute path or a path relative to the configured \"backups_path\". The max allowed file size is 10MB
    scan_quota = 56 # int | Quota scan:   * `0` no quota scan is done, the imported users/folders will have used_quota_size and used_quota_files = 0 or the existing values if they already exists. This is the default   * `1` scan quota   * `2` scan quota if the user has quota restrictions required: false  (optional)
    mode = 56 # int | Mode:   * `0` New objects are added, existing ones are updated. This is the default   * `1` New objects are added, existing ones are not modified   * `2` New objects are added, existing ones are updated and connected users are disconnected and so forced to use the new configuration  (optional)

    try:
        # Load data from path
        api_response = api_instance.loaddata_from_file(input_file, scan_quota=scan_quota, mode=mode)
        print("The response of MaintenanceApi->loaddata_from_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceApi->loaddata_from_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **str**| Path for the file to read the JSON serialized data from. This can be an absolute path or a path relative to the configured \&quot;backups_path\&quot;. The max allowed file size is 10MB |
 **scan_quota** | **int**| Quota scan:   * &#x60;0&#x60; no quota scan is done, the imported users/folders will have used_quota_size and used_quota_files &#x3D; 0 or the existing values if they already exists. This is the default   * &#x60;1&#x60; scan quota   * &#x60;2&#x60; scan quota if the user has quota restrictions required: false  | [optional]
 **mode** | **int**| Mode:   * &#x60;0&#x60; New objects are added, existing ones are updated. This is the default   * &#x60;1&#x60; New objects are added, existing ones are not modified   * &#x60;2&#x60; New objects are added, existing ones are updated and connected users are disconnected and so forced to use the new configuration  | [optional]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loaddata_from_request_body**
> ApiResponse loaddata_from_request_body(backup_data, scan_quota=scan_quota, mode=mode)

Load data

Restores SFTPGo data from a JSON backup. Objects will be restored one by one and the restore is stopped if a object cannot be added or updated, so it could happen a partial restore

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.backup_data import BackupData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyAuth
configuration.api_key['APIKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MaintenanceApi(api_client)
    backup_data = openapi_client.BackupData() # BackupData |
    scan_quota = 56 # int | Quota scan:   * `0` no quota scan is done, the imported users/folders will have used_quota_size and used_quota_files = 0 or the existing values if they already exists. This is the default   * `1` scan quota   * `2` scan quota if the user has quota restrictions required: false  (optional)
    mode = 56 # int | Mode:   * `0` New objects are added, existing ones are updated. This is the default   * `1` New objects are added, existing ones are not modified   * `2` New objects are added, existing ones are updated and connected users are disconnected and so forced to use the new configuration  (optional)

    try:
        # Load data
        api_response = api_instance.loaddata_from_request_body(backup_data, scan_quota=scan_quota, mode=mode)
        print("The response of MaintenanceApi->loaddata_from_request_body:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceApi->loaddata_from_request_body: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_data** | [**BackupData**](BackupData.md)|  |
 **scan_quota** | **int**| Quota scan:   * &#x60;0&#x60; no quota scan is done, the imported users/folders will have used_quota_size and used_quota_files &#x3D; 0 or the existing values if they already exists. This is the default   * &#x60;1&#x60; scan quota   * &#x60;2&#x60; scan quota if the user has quota restrictions required: false  | [optional]
 **mode** | **int**| Mode:   * &#x60;0&#x60; New objects are added, existing ones are updated. This is the default   * &#x60;1&#x60; New objects are added, existing ones are not modified   * &#x60;2&#x60; New objects are added, existing ones are updated and connected users are disconnected and so forced to use the new configuration  | [optional]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
