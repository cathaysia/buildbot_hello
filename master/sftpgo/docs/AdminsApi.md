# openapi_client.AdminsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_admin**](AdminsApi.md#add_admin) | **POST** /admins | Add admin
[**admin_forgot_password**](AdminsApi.md#admin_forgot_password) | **POST** /admins/{username}/forgot-password | Send a password reset code by email
[**admin_reset_password**](AdminsApi.md#admin_reset_password) | **POST** /admins/{username}/reset-password | Reset the password
[**change_admin_password**](AdminsApi.md#change_admin_password) | **PUT** /admin/changepwd | Change admin password
[**delete_admin**](AdminsApi.md#delete_admin) | **DELETE** /admins/{username} | Delete admin
[**disable_admin2fa**](AdminsApi.md#disable_admin2fa) | **PUT** /admins/{username}/2fa/disable | Disable second factor authentication
[**generate_admin_recovery_codes**](AdminsApi.md#generate_admin_recovery_codes) | **POST** /admin/2fa/recoverycodes | Generate recovery codes
[**generate_admin_totp_secret**](AdminsApi.md#generate_admin_totp_secret) | **POST** /admin/totp/generate | Generate a new TOTP secret
[**get_admin_by_username**](AdminsApi.md#get_admin_by_username) | **GET** /admins/{username} | Find admins by username
[**get_admin_profile**](AdminsApi.md#get_admin_profile) | **GET** /admin/profile | Get admin profile
[**get_admin_recovery_codes**](AdminsApi.md#get_admin_recovery_codes) | **GET** /admin/2fa/recoverycodes | Get recovery codes
[**get_admin_totp_configs**](AdminsApi.md#get_admin_totp_configs) | **GET** /admin/totp/configs | Get available TOTP configuration
[**get_admins**](AdminsApi.md#get_admins) | **GET** /admins | Get admins
[**save_admin_totp_config**](AdminsApi.md#save_admin_totp_config) | **POST** /admin/totp/save | Save a TOTP config
[**update_admin**](AdminsApi.md#update_admin) | **PUT** /admins/{username} | Update admin
[**update_admin_profile**](AdminsApi.md#update_admin_profile) | **PUT** /admin/profile | Update admin profile
[**validate_admin_totp_secret**](AdminsApi.md#validate_admin_totp_secret) | **POST** /admin/totp/validate | Validate a one time authentication code


# **add_admin**
> Admin add_admin(admin)

Add admin

Adds a new admin. Recovery codes and TOTP configuration cannot be set using this API: each admin must use the specific APIs

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.admin import Admin
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
    api_instance = openapi_client.AdminsApi(api_client)
    admin = openapi_client.Admin() # Admin |

    try:
        # Add admin
        api_response = api_instance.add_admin(admin)
        print("The response of AdminsApi->add_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->add_admin: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin** | [**Admin**](Admin.md)|  |

### Return type

[**Admin**](Admin.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | successful operation |  * Location - URI to retrieve the details for the new created share <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_forgot_password**
> ApiResponse admin_forgot_password(username)

Send a password reset code by email

You must set up an SMTP server and the account must have a valid email address, in which case SFTPGo will send a code via email to reset the password. If the specified admin does not exist, the request will be silently ignored (a success response will be returned) to avoid disclosing existing admins

### Example

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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AdminsApi(api_client)
    username = 'username_example' # str | the admin username

    try:
        # Send a password reset code by email
        api_response = api_instance.admin_forgot_password(username)
        print("The response of AdminsApi->admin_forgot_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->admin_forgot_password: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the admin username |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_reset_password**
> ApiResponse admin_reset_password(username, admin_reset_password_request)

Reset the password

Set a new password using the code received via email

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.admin_reset_password_request import AdminResetPasswordRequest
from openapi_client.models.api_response import ApiResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AdminsApi(api_client)
    username = 'username_example' # str | the admin username
    admin_reset_password_request = openapi_client.AdminResetPasswordRequest() # AdminResetPasswordRequest |

    try:
        # Reset the password
        api_response = api_instance.admin_reset_password(username, admin_reset_password_request)
        print("The response of AdminsApi->admin_reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->admin_reset_password: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the admin username |
 **admin_reset_password_request** | [**AdminResetPasswordRequest**](AdminResetPasswordRequest.md)|  |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

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
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_admin_password**
> ApiResponse change_admin_password(pwd_change)

Change admin password

Changes the password for the logged in admin

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.pwd_change import PwdChange
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
    api_instance = openapi_client.AdminsApi(api_client)
    pwd_change = openapi_client.PwdChange() # PwdChange |

    try:
        # Change admin password
        api_response = api_instance.change_admin_password(pwd_change)
        print("The response of AdminsApi->change_admin_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->change_admin_password: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pwd_change** | [**PwdChange**](PwdChange.md)|  |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **delete_admin**
> ApiResponse delete_admin(username)

Delete admin

Deletes an existing admin

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
    api_instance = openapi_client.AdminsApi(api_client)
    username = 'username_example' # str | the admin username

    try:
        # Delete admin
        api_response = api_instance.delete_admin(username)
        print("The response of AdminsApi->delete_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->delete_admin: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the admin username |

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_admin2fa**
> ApiResponse disable_admin2fa(username)

Disable second factor authentication

Disables second factor authentication for the given admin. This API must be used if the admin loses access to their second factor auth device and has no recovery codes

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
    api_instance = openapi_client.AdminsApi(api_client)
    username = 'username_example' # str | the admin username

    try:
        # Disable second factor authentication
        api_response = api_instance.disable_admin2fa(username)
        print("The response of AdminsApi->disable_admin2fa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->disable_admin2fa: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the admin username |

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_admin_recovery_codes**
> List[str] generate_admin_recovery_codes()

Generate recovery codes

Generates new recovery codes for the logged in admin. Generating new recovery codes you automatically invalidate old ones

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.AdminsApi(api_client)

    try:
        # Generate recovery codes
        api_response = api_instance.generate_admin_recovery_codes()
        print("The response of AdminsApi->generate_admin_recovery_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->generate_admin_recovery_codes: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **generate_admin_totp_secret**
> GenerateAdminTotpSecret200Response generate_admin_totp_secret(generate_admin_totp_secret_request)

Generate a new TOTP secret

Generates a new TOTP secret, including the QR code as png, using the specified configuration for the logged in admin

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.generate_admin_totp_secret200_response import GenerateAdminTotpSecret200Response
from openapi_client.models.generate_admin_totp_secret_request import GenerateAdminTotpSecretRequest
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
    api_instance = openapi_client.AdminsApi(api_client)
    generate_admin_totp_secret_request = openapi_client.GenerateAdminTotpSecretRequest() # GenerateAdminTotpSecretRequest |

    try:
        # Generate a new TOTP secret
        api_response = api_instance.generate_admin_totp_secret(generate_admin_totp_secret_request)
        print("The response of AdminsApi->generate_admin_totp_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->generate_admin_totp_secret: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_admin_totp_secret_request** | [**GenerateAdminTotpSecretRequest**](GenerateAdminTotpSecretRequest.md)|  |

### Return type

[**GenerateAdminTotpSecret200Response**](GenerateAdminTotpSecret200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_admin_by_username**
> Admin get_admin_by_username(username)

Find admins by username

Returns the admin with the given username, if it exists. For security reasons the hashed password is omitted in the response

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.admin import Admin
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
    api_instance = openapi_client.AdminsApi(api_client)
    username = 'username_example' # str | the admin username

    try:
        # Find admins by username
        api_response = api_instance.get_admin_by_username(username)
        print("The response of AdminsApi->get_admin_by_username:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->get_admin_by_username: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the admin username |

### Return type

[**Admin**](Admin.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_profile**
> AdminProfile get_admin_profile()

Get admin profile

Returns the profile for the logged in admin

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.admin_profile import AdminProfile
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
    api_instance = openapi_client.AdminsApi(api_client)

    try:
        # Get admin profile
        api_response = api_instance.get_admin_profile()
        print("The response of AdminsApi->get_admin_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->get_admin_profile: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminProfile**](AdminProfile.md)

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

# **get_admin_recovery_codes**
> List[RecoveryCode] get_admin_recovery_codes()

Get recovery codes

Returns the recovery codes for the logged in admin. Recovery codes can be used if the admin loses access to their second factor auth device. Recovery codes are returned unencrypted

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.recovery_code import RecoveryCode
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
    api_instance = openapi_client.AdminsApi(api_client)

    try:
        # Get recovery codes
        api_response = api_instance.get_admin_recovery_codes()
        print("The response of AdminsApi->get_admin_recovery_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->get_admin_recovery_codes: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[RecoveryCode]**](RecoveryCode.md)

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

# **get_admin_totp_configs**
> List[TOTPConfig] get_admin_totp_configs()

Get available TOTP configuration

Returns the available TOTP configurations for the logged in admin

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.totp_config import TOTPConfig
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
    api_instance = openapi_client.AdminsApi(api_client)

    try:
        # Get available TOTP configuration
        api_response = api_instance.get_admin_totp_configs()
        print("The response of AdminsApi->get_admin_totp_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->get_admin_totp_configs: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[TOTPConfig]**](TOTPConfig.md)

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

# **get_admins**
> List[Admin] get_admins(offset=offset, limit=limit, order=order)

Get admins

Returns an array with one or more admins. For security reasons hashed passwords are omitted in the response

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.admin import Admin
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
    api_instance = openapi_client.AdminsApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int | The maximum number of items to return. Max value is 500, default is 100 (optional) (default to 100)
    order = 'ASC' # str | Ordering admins by username. Default ASC (optional)

    try:
        # Get admins
        api_response = api_instance.get_admins(offset=offset, limit=limit, order=order)
        print("The response of AdminsApi->get_admins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->get_admins: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**| The maximum number of items to return. Max value is 500, default is 100 | [optional] [default to 100]
 **order** | **str**| Ordering admins by username. Default ASC | [optional]

### Return type

[**List[Admin]**](Admin.md)

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

# **save_admin_totp_config**
> ApiResponse save_admin_totp_config(admin_totp_config)

Save a TOTP config

Saves the specified TOTP config for the logged in admin

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.admin_totp_config import AdminTOTPConfig
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
    api_instance = openapi_client.AdminsApi(api_client)
    admin_totp_config = openapi_client.AdminTOTPConfig() # AdminTOTPConfig |

    try:
        # Save a TOTP config
        api_response = api_instance.save_admin_totp_config(admin_totp_config)
        print("The response of AdminsApi->save_admin_totp_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->save_admin_totp_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_totp_config** | [**AdminTOTPConfig**](AdminTOTPConfig.md)|  |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **update_admin**
> ApiResponse update_admin(username, admin)

Update admin

Updates an existing admin. Recovery codes and TOTP configuration cannot be set/updated using this API: each admin must use the specific APIs. You are not allowed to update the admin impersonated using an API key

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.admin import Admin
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
    api_instance = openapi_client.AdminsApi(api_client)
    username = 'username_example' # str | the admin username
    admin = openapi_client.Admin() # Admin |

    try:
        # Update admin
        api_response = api_instance.update_admin(username, admin)
        print("The response of AdminsApi->update_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->update_admin: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the admin username |
 **admin** | [**Admin**](Admin.md)|  |

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
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_admin_profile**
> ApiResponse update_admin_profile(admin_profile)

Update admin profile

Allows to update the profile for the logged in admin

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.admin_profile import AdminProfile
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
    api_instance = openapi_client.AdminsApi(api_client)
    admin_profile = openapi_client.AdminProfile() # AdminProfile |

    try:
        # Update admin profile
        api_response = api_instance.update_admin_profile(admin_profile)
        print("The response of AdminsApi->update_admin_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->update_admin_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_profile** | [**AdminProfile**](AdminProfile.md)|  |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **validate_admin_totp_secret**
> ApiResponse validate_admin_totp_secret(validate_admin_totp_secret_request)

Validate a one time authentication code

Checks if the given authentication code can be validated using the specified secret and config name

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.validate_admin_totp_secret_request import ValidateAdminTotpSecretRequest
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
    api_instance = openapi_client.AdminsApi(api_client)
    validate_admin_totp_secret_request = openapi_client.ValidateAdminTotpSecretRequest() # ValidateAdminTotpSecretRequest |

    try:
        # Validate a one time authentication code
        api_response = api_instance.validate_admin_totp_secret(validate_admin_totp_secret_request)
        print("The response of AdminsApi->validate_admin_totp_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->validate_admin_totp_secret: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_admin_totp_secret_request** | [**ValidateAdminTotpSecretRequest**](ValidateAdminTotpSecretRequest.md)|  |

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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
