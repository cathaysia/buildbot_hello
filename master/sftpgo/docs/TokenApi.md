# openapi_client.TokenApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_logout**](TokenApi.md#client_logout) | **GET** /user/logout | Invalidate a user access token
[**get_token**](TokenApi.md#get_token) | **GET** /token | Get a new admin access token
[**get_user_token**](TokenApi.md#get_user_token) | **GET** /user/token | Get a new user access token
[**logout**](TokenApi.md#logout) | **GET** /logout | Invalidate an admin access token


# **client_logout**
> ApiResponse client_logout()

Invalidate a user access token

Allows to invalidate a client token before its expiration

### Example

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TokenApi(api_client)

    try:
        # Invalidate a user access token
        api_response = api_instance.client_logout()
        print("The response of TokenApi->client_logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenApi->client_logout: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_token**
> Token get_token(x_sftpgo_otp=x_sftpgo_otp)

Get a new admin access token

Returns an access token and its expiration

### Example

* Basic Authentication (BasicAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.token import Token
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

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TokenApi(api_client)
    x_sftpgo_otp = 'x_sftpgo_otp_example' # str | If you have 2FA configured for the admin attempting to log in you need to set the authentication code using this header parameter (optional)

    try:
        # Get a new admin access token
        api_response = api_instance.get_token(x_sftpgo_otp=x_sftpgo_otp)
        print("The response of TokenApi->get_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenApi->get_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sftpgo_otp** | **str**| If you have 2FA configured for the admin attempting to log in you need to set the authentication code using this header parameter | [optional]

### Return type

[**Token**](Token.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

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

# **get_user_token**
> Token get_user_token(x_sftpgo_otp=x_sftpgo_otp)

Get a new user access token

Returns an access token and its expiration

### Example

* Basic Authentication (BasicAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.token import Token
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

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TokenApi(api_client)
    x_sftpgo_otp = 'x_sftpgo_otp_example' # str | If you have 2FA configured, for the HTTP protocol, for the user attempting to log in you need to set the authentication code using this header parameter (optional)

    try:
        # Get a new user access token
        api_response = api_instance.get_user_token(x_sftpgo_otp=x_sftpgo_otp)
        print("The response of TokenApi->get_user_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenApi->get_user_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sftpgo_otp** | **str**| If you have 2FA configured, for the HTTP protocol, for the user attempting to log in you need to set the authentication code using this header parameter | [optional]

### Return type

[**Token**](Token.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

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

# **logout**
> ApiResponse logout()

Invalidate an admin access token

Allows to invalidate an admin token before its expiration

### Example

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

# Configure Bearer authorization (JWT): BearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TokenApi(api_client)

    try:
        # Invalidate an admin access token
        api_response = api_instance.logout()
        print("The response of TokenApi->logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenApi->logout: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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
