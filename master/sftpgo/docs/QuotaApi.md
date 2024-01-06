# openapi_client.QuotaApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**folder_quota_update_usage**](QuotaApi.md#folder_quota_update_usage) | **PUT** /quotas/folders/{name}/usage | Update folder quota usage limits
[**get_folders_quota_scans**](QuotaApi.md#get_folders_quota_scans) | **GET** /quotas/folders/scans | Get active folder quota scans
[**get_users_quota_scans**](QuotaApi.md#get_users_quota_scans) | **GET** /quotas/users/scans | Get active user quota scans
[**start_folder_quota_scan**](QuotaApi.md#start_folder_quota_scan) | **POST** /quotas/folders/{name}/scan | Start a folder quota scan
[**start_user_quota_scan**](QuotaApi.md#start_user_quota_scan) | **POST** /quotas/users/{username}/scan | Start a user quota scan
[**user_quota_update_usage**](QuotaApi.md#user_quota_update_usage) | **PUT** /quotas/users/{username}/usage | Update disk quota usage limits
[**user_transfer_quota_update_usage**](QuotaApi.md#user_transfer_quota_update_usage) | **PUT** /quotas/users/{username}/transfer-usage | Update transfer quota usage limits


# **folder_quota_update_usage**
> ApiResponse folder_quota_update_usage(name, quota_usage, mode=mode)

Update folder quota usage limits

Sets the current used quota limits for the given folder

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.quota_usage import QuotaUsage
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
    api_instance = openapi_client.QuotaApi(api_client)
    name = 'name_example' # str | folder name
    quota_usage = openapi_client.QuotaUsage() # QuotaUsage | If used_quota_size and used_quota_files are missing they will default to 0, this means that if mode is \"add\" the current value, for the missing field, will remain unchanged, if mode is \"reset\" the missing field is set to 0
    mode = 'reset' # str | the update mode specifies if the given quota usage values should be added or replace the current ones (optional)

    try:
        # Update folder quota usage limits
        api_response = api_instance.folder_quota_update_usage(name, quota_usage, mode=mode)
        print("The response of QuotaApi->folder_quota_update_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->folder_quota_update_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| folder name |
 **quota_usage** | [**QuotaUsage**](QuotaUsage.md)| If used_quota_size and used_quota_files are missing they will default to 0, this means that if mode is \&quot;add\&quot; the current value, for the missing field, will remain unchanged, if mode is \&quot;reset\&quot; the missing field is set to 0 |
 **mode** | **str**| the update mode specifies if the given quota usage values should be added or replace the current ones | [optional]

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folders_quota_scans**
> List[FolderQuotaScan] get_folders_quota_scans()

Get active folder quota scans

Returns the active folder quota scans

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.folder_quota_scan import FolderQuotaScan
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
    api_instance = openapi_client.QuotaApi(api_client)

    try:
        # Get active folder quota scans
        api_response = api_instance.get_folders_quota_scans()
        print("The response of QuotaApi->get_folders_quota_scans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->get_folders_quota_scans: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[FolderQuotaScan]**](FolderQuotaScan.md)

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

# **get_users_quota_scans**
> List[QuotaScan] get_users_quota_scans()

Get active user quota scans

Returns the active user quota scans

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.quota_scan import QuotaScan
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
    api_instance = openapi_client.QuotaApi(api_client)

    try:
        # Get active user quota scans
        api_response = api_instance.get_users_quota_scans()
        print("The response of QuotaApi->get_users_quota_scans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->get_users_quota_scans: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[QuotaScan]**](QuotaScan.md)

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

# **start_folder_quota_scan**
> ApiResponse start_folder_quota_scan(name)

Start a folder quota scan

Starts a new quota scan for the given folder. A quota scan update the number of files and their total size for the specified folder

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
    api_instance = openapi_client.QuotaApi(api_client)
    name = 'name_example' # str | folder name

    try:
        # Start a folder quota scan
        api_response = api_instance.start_folder_quota_scan(name)
        print("The response of QuotaApi->start_folder_quota_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->start_folder_quota_scan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| folder name |

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
**202** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_user_quota_scan**
> ApiResponse start_user_quota_scan(username)

Start a user quota scan

Starts a new quota scan for the given user. A quota scan updates the number of files and their total size for the specified user and the virtual folders, if any, included in his quota

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
    api_instance = openapi_client.QuotaApi(api_client)
    username = 'username_example' # str | the username

    try:
        # Start a user quota scan
        api_response = api_instance.start_user_quota_scan(username)
        print("The response of QuotaApi->start_user_quota_scan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->start_user_quota_scan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username |

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
**202** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_quota_update_usage**
> ApiResponse user_quota_update_usage(username, quota_usage, mode=mode)

Update disk quota usage limits

Sets the current used quota limits for the given user

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.quota_usage import QuotaUsage
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
    api_instance = openapi_client.QuotaApi(api_client)
    username = 'username_example' # str | the username
    quota_usage = openapi_client.QuotaUsage() # QuotaUsage | If used_quota_size and used_quota_files are missing they will default to 0, this means that if mode is \"add\" the current value, for the missing field, will remain unchanged, if mode is \"reset\" the missing field is set to 0
    mode = 'reset' # str | the update mode specifies if the given quota usage values should be added or replace the current ones (optional)

    try:
        # Update disk quota usage limits
        api_response = api_instance.user_quota_update_usage(username, quota_usage, mode=mode)
        print("The response of QuotaApi->user_quota_update_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->user_quota_update_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username |
 **quota_usage** | [**QuotaUsage**](QuotaUsage.md)| If used_quota_size and used_quota_files are missing they will default to 0, this means that if mode is \&quot;add\&quot; the current value, for the missing field, will remain unchanged, if mode is \&quot;reset\&quot; the missing field is set to 0 |
 **mode** | **str**| the update mode specifies if the given quota usage values should be added or replace the current ones | [optional]

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_transfer_quota_update_usage**
> ApiResponse user_transfer_quota_update_usage(username, transfer_quota_usage, mode=mode)

Update transfer quota usage limits

Sets the current used transfer quota limits for the given user

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.transfer_quota_usage import TransferQuotaUsage
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
    api_instance = openapi_client.QuotaApi(api_client)
    username = 'username_example' # str | the username
    transfer_quota_usage = openapi_client.TransferQuotaUsage() # TransferQuotaUsage | If used_upload_data_transfer and used_download_data_transfer are missing they will default to 0, this means that if mode is \"add\" the current value, for the missing field, will remain unchanged, if mode is \"reset\" the missing field is set to 0
    mode = 'reset' # str | the update mode specifies if the given quota usage values should be added or replace the current ones (optional)

    try:
        # Update transfer quota usage limits
        api_response = api_instance.user_transfer_quota_update_usage(username, transfer_quota_usage, mode=mode)
        print("The response of QuotaApi->user_transfer_quota_update_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->user_transfer_quota_update_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username |
 **transfer_quota_usage** | [**TransferQuotaUsage**](TransferQuotaUsage.md)| If used_upload_data_transfer and used_download_data_transfer are missing they will default to 0, this means that if mode is \&quot;add\&quot; the current value, for the missing field, will remain unchanged, if mode is \&quot;reset\&quot; the missing field is set to 0 |
 **mode** | **str**| the update mode specifies if the given quota usage values should be added or replace the current ones | [optional]

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
