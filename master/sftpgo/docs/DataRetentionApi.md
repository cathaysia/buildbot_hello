# openapi_client.DataRetentionApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_users_retention_checks**](DataRetentionApi.md#get_users_retention_checks) | **GET** /retention/users/checks | Get retention checks
[**start_user_retention_check**](DataRetentionApi.md#start_user_retention_check) | **POST** /retention/users/{username}/check | Start a retention check


# **get_users_retention_checks**
> List[RetentionCheck] get_users_retention_checks()

Get retention checks

Returns the active retention checks

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.retention_check import RetentionCheck
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
    api_instance = openapi_client.DataRetentionApi(api_client)

    try:
        # Get retention checks
        api_response = api_instance.get_users_retention_checks()
        print("The response of DataRetentionApi->get_users_retention_checks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataRetentionApi->get_users_retention_checks: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[RetentionCheck]**](RetentionCheck.md)

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

# **start_user_retention_check**
> ApiResponse start_user_retention_check(username, folder_retention, notifications=notifications)

Start a retention check

Starts a new retention check for the given user. If a retention check for this user is already active a 409 status code is returned

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.folder_retention import FolderRetention
from openapi_client.models.retention_check_notification import RetentionCheckNotification
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
    api_instance = openapi_client.DataRetentionApi(api_client)
    username = 'username_example' # str | the username
    folder_retention = [openapi_client.FolderRetention()] # List[FolderRetention] | Defines virtual paths to check and their retention time in hours
    notifications = [openapi_client.RetentionCheckNotification()] # List[RetentionCheckNotification] | specify how to notify results (optional)

    try:
        # Start a retention check
        api_response = api_instance.start_user_retention_check(username, folder_retention, notifications=notifications)
        print("The response of DataRetentionApi->start_user_retention_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataRetentionApi->start_user_retention_check: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the username |
 **folder_retention** | [**List[FolderRetention]**](FolderRetention.md)| Defines virtual paths to check and their retention time in hours |
 **notifications** | [**List[RetentionCheckNotification]**](RetentionCheckNotification.md)| specify how to notify results | [optional]

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
**202** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
