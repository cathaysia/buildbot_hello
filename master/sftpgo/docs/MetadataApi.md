# openapi_client.MetadataApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_users_metadata_checks**](MetadataApi.md#get_users_metadata_checks) | **GET** /metadata/users/checks | Get metadata checks
[**start_user_metadata_check**](MetadataApi.md#start_user_metadata_check) | **POST** /metadata/users/{username}/check | Start a metadata check


# **get_users_metadata_checks**
> List[MetadataCheck] get_users_metadata_checks()

Get metadata checks

Returns the active metadata checks

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.metadata_check import MetadataCheck
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
    api_instance = openapi_client.MetadataApi(api_client)

    try:
        # Get metadata checks
        api_response = api_instance.get_users_metadata_checks()
        print("The response of MetadataApi->get_users_metadata_checks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->get_users_metadata_checks: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[MetadataCheck]**](MetadataCheck.md)

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

# **start_user_metadata_check**
> ApiResponse start_user_metadata_check(username)

Start a metadata check

Starts a new metadata check for the given user. A metadata check requires a metadata plugin and removes the metadata associated to missing items (for example objects deleted outside SFTPGo). If a metadata check for this user is already active a 409 status code is returned. Metadata are stored for cloud storage backends. This API does nothing for other backends or if no metadata plugin is configured

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
    api_instance = openapi_client.MetadataApi(api_client)
    username = 'username_example' # str | the username

    try:
        # Start a metadata check
        api_response = api_instance.start_user_metadata_check(username)
        print("The response of MetadataApi->start_user_metadata_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataApi->start_user_metadata_check: %s\n" % e)
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
