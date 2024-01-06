# openapi_client.UserAPIsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_share**](UserAPIsApi.md#add_share) | **POST** /user/shares | Add a share
[**change_user_password**](UserAPIsApi.md#change_user_password) | **PUT** /user/changepwd | Change user password
[**create_user_dir**](UserAPIsApi.md#create_user_dir) | **POST** /user/dirs | Create a directory
[**create_user_file**](UserAPIsApi.md#create_user_file) | **POST** /user/files/upload | Upload a single file
[**create_user_files**](UserAPIsApi.md#create_user_files) | **POST** /user/files | Upload files
[**delete_user_dir**](UserAPIsApi.md#delete_user_dir) | **DELETE** /user/dirs | Delete a directory
[**delete_user_file**](UserAPIsApi.md#delete_user_file) | **DELETE** /user/files | Delete a file
[**delete_user_share**](UserAPIsApi.md#delete_user_share) | **DELETE** /user/shares/{id} | Delete share
[**download_user_file**](UserAPIsApi.md#download_user_file) | **GET** /user/files | Download a single file
[**generate_user_recovery_codes**](UserAPIsApi.md#generate_user_recovery_codes) | **POST** /user/2fa/recoverycodes | Generate recovery codes
[**generate_user_totp_secret**](UserAPIsApi.md#generate_user_totp_secret) | **POST** /user/totp/generate | Generate a new TOTP secret
[**get_user_dir_contents**](UserAPIsApi.md#get_user_dir_contents) | **GET** /user/dirs | Read directory contents
[**get_user_profile**](UserAPIsApi.md#get_user_profile) | **GET** /user/profile | Get user profile
[**get_user_recovery_codes**](UserAPIsApi.md#get_user_recovery_codes) | **GET** /user/2fa/recoverycodes | Get recovery codes
[**get_user_share_by_id**](UserAPIsApi.md#get_user_share_by_id) | **GET** /user/shares/{id} | Get share by id
[**get_user_shares**](UserAPIsApi.md#get_user_shares) | **GET** /user/shares | List user shares
[**get_user_totp_configs**](UserAPIsApi.md#get_user_totp_configs) | **GET** /user/totp/configs | Get available TOTP configuration
[**rename_user_dir**](UserAPIsApi.md#rename_user_dir) | **PATCH** /user/dirs | Rename a directory. Deprecated, use \&quot;file-actions/move\&quot;
[**rename_user_file**](UserAPIsApi.md#rename_user_file) | **PATCH** /user/files | Rename a file
[**save_user_totp_config**](UserAPIsApi.md#save_user_totp_config) | **POST** /user/totp/save | Save a TOTP config
[**setprops_user_file**](UserAPIsApi.md#setprops_user_file) | **PATCH** /user/files/metadata | Set metadata for a file/directory
[**streamzip**](UserAPIsApi.md#streamzip) | **POST** /user/streamzip | Download multiple files and folders as a single zip file
[**update_user_profile**](UserAPIsApi.md#update_user_profile) | **PUT** /user/profile | Update user profile
[**update_user_share**](UserAPIsApi.md#update_user_share) | **PUT** /user/shares/{id} | Update share
[**user_file_actions_copy_post**](UserAPIsApi.md#user_file_actions_copy_post) | **POST** /user/file-actions/copy | Copy a file or a directory
[**user_file_actions_move_post**](UserAPIsApi.md#user_file_actions_move_post) | **POST** /user/file-actions/move | Move (rename) a file or a directory
[**validate_user_totp_secret**](UserAPIsApi.md#validate_user_totp_secret) | **POST** /user/totp/validate | Validate a one time authentication code


# **add_share**
> ApiResponse add_share(share)

Add a share

Adds a new share. The share id will be auto-generated

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.share import Share
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
    api_instance = openapi_client.UserAPIsApi(api_client)
    share = openapi_client.Share() # Share |

    try:
        # Add a share
        api_response = api_instance.add_share(share)
        print("The response of UserAPIsApi->add_share:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->add_share: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share** | [**Share**](Share.md)|  |

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
**201** | successful operation |  * X-Object-ID - ID for the new created share <br>  * Location - URI to retrieve the details for the new created share <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_password**
> ApiResponse change_user_password(pwd_change)

Change user password

Changes the password for the logged in user

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
    api_instance = openapi_client.UserAPIsApi(api_client)
    pwd_change = openapi_client.PwdChange() # PwdChange |

    try:
        # Change user password
        api_response = api_instance.change_user_password(pwd_change)
        print("The response of UserAPIsApi->change_user_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->change_user_password: %s\n" % e)
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

# **create_user_dir**
> ApiResponse create_user_dir(path, mkdir_parents=mkdir_parents)

Create a directory

Create a directory for the logged in user

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
    api_instance = openapi_client.UserAPIsApi(api_client)
    path = 'path_example' # str | Path to the folder to create. It must be URL encoded, for example the path \"my dir/àdir\" must be sent as \"my%20dir%2F%C3%A0dir\"
    mkdir_parents = True # bool | Create parent directories if they do not exist? (optional)

    try:
        # Create a directory
        api_response = api_instance.create_user_dir(path, mkdir_parents=mkdir_parents)
        print("The response of UserAPIsApi->create_user_dir:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->create_user_dir: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path to the folder to create. It must be URL encoded, for example the path \&quot;my dir/àdir\&quot; must be sent as \&quot;my%20dir%2F%C3%A0dir\&quot; |
 **mkdir_parents** | **bool**| Create parent directories if they do not exist? | [optional]

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
**201** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_file**
> ApiResponse create_user_file(path, body, mkdir_parents=mkdir_parents, x_sftpgo_mtime=x_sftpgo_mtime)

Upload a single file

Upload a single file for the logged in user to an existing directory. This API does not use multipart/form-data and so no temporary files are created server side but only a single file can be uploaded as POST body

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
    api_instance = openapi_client.UserAPIsApi(api_client)
    path = 'path_example' # str | Full file path. It must be path encoded, for example the path \"my dir/àdir/file.txt\" must be sent as \"my%20dir%2F%C3%A0dir%2Ffile.txt\". The parent directory must exist. If a file with the same name already exists, it will be overwritten
    body = None # bytearray |
    mkdir_parents = True # bool | Create parent directories if they do not exist? (optional)
    x_sftpgo_mtime = 56 # int | File modification time as unix timestamp in milliseconds (optional)

    try:
        # Upload a single file
        api_response = api_instance.create_user_file(path, body, mkdir_parents=mkdir_parents, x_sftpgo_mtime=x_sftpgo_mtime)
        print("The response of UserAPIsApi->create_user_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->create_user_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Full file path. It must be path encoded, for example the path \&quot;my dir/àdir/file.txt\&quot; must be sent as \&quot;my%20dir%2F%C3%A0dir%2Ffile.txt\&quot;. The parent directory must exist. If a file with the same name already exists, it will be overwritten |
 **body** | **bytearray**|  |
 **mkdir_parents** | **bool**| Create parent directories if they do not exist? | [optional]
 **x_sftpgo_mtime** | **int**| File modification time as unix timestamp in milliseconds | [optional]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/*, text/*, image/*, audio/*, video/*
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**413** | Request Entity Too Large, max allowed size exceeded |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_files**
> ApiResponse create_user_files(path=path, mkdir_parents=mkdir_parents, filenames=filenames)

Upload files

Upload one or more files for the logged in user

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
    api_instance = openapi_client.UserAPIsApi(api_client)
    path = 'path_example' # str | Parent directory for the uploaded files. It must be URL encoded, for example the path \"my dir/àdir\" must be sent as \"my%20dir%2F%C3%A0dir\". If empty or missing the root path is assumed. If a file with the same name already exists, it will be overwritten (optional)
    mkdir_parents = True # bool | Create parent directories if they do not exist? (optional)
    filenames = None # List[bytearray] |  (optional)

    try:
        # Upload files
        api_response = api_instance.create_user_files(path=path, mkdir_parents=mkdir_parents, filenames=filenames)
        print("The response of UserAPIsApi->create_user_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->create_user_files: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Parent directory for the uploaded files. It must be URL encoded, for example the path \&quot;my dir/àdir\&quot; must be sent as \&quot;my%20dir%2F%C3%A0dir\&quot;. If empty or missing the root path is assumed. If a file with the same name already exists, it will be overwritten | [optional]
 **mkdir_parents** | **bool**| Create parent directories if they do not exist? | [optional]
 **filenames** | **List[bytearray]**|  | [optional]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**413** | Request Entity Too Large, max allowed size exceeded |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_dir**
> ApiResponse delete_user_dir(path)

Delete a directory

Delete a directory and any children it contains for the logged in user

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
    api_instance = openapi_client.UserAPIsApi(api_client)
    path = 'path_example' # str | Path to the folder to delete. It must be URL encoded, for example the path \"my dir/àdir\" must be sent as \"my%20dir%2F%C3%A0dir\"

    try:
        # Delete a directory
        api_response = api_instance.delete_user_dir(path)
        print("The response of UserAPIsApi->delete_user_dir:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->delete_user_dir: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path to the folder to delete. It must be URL encoded, for example the path \&quot;my dir/àdir\&quot; must be sent as \&quot;my%20dir%2F%C3%A0dir\&quot; |

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

# **delete_user_file**
> ApiResponse delete_user_file(path)

Delete a file

Delete a file for the logged in user.

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
    api_instance = openapi_client.UserAPIsApi(api_client)
    path = 'path_example' # str | Path to the file to delete. It must be URL encoded

    try:
        # Delete a file
        api_response = api_instance.delete_user_file(path)
        print("The response of UserAPIsApi->delete_user_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->delete_user_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path to the file to delete. It must be URL encoded |

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

# **delete_user_share**
> ApiResponse delete_user_share(id)

Delete share

Deletes an existing share belonging to the logged in user

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
    api_instance = openapi_client.UserAPIsApi(api_client)
    id = 'id_example' # str | the share id

    try:
        # Delete share
        api_response = api_instance.delete_user_share(id)
        print("The response of UserAPIsApi->delete_user_share:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->delete_user_share: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the share id |

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

# **download_user_file**
> bytearray download_user_file(path, inline=inline)

Download a single file

Returns the file contents as response body

### Example

* Api Key Authentication (APIKeyAuth):
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
    api_instance = openapi_client.UserAPIsApi(api_client)
    path = 'path_example' # str | Path to the file to download. It must be URL encoded, for example the path \"my dir/àdir/file.txt\" must be sent as \"my%20dir%2F%C3%A0dir%2Ffile.txt\"
    inline = 'inline_example' # str | If set, the response will not have the Content-Disposition header set to `attachment` (optional)

    try:
        # Download a single file
        api_response = api_instance.download_user_file(path, inline=inline)
        print("The response of UserAPIsApi->download_user_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->download_user_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path to the file to download. It must be URL encoded, for example the path \&quot;my dir/àdir/file.txt\&quot; must be sent as \&quot;my%20dir%2F%C3%A0dir%2Ffile.txt\&quot; |
 **inline** | **str**| If set, the response will not have the Content-Disposition header set to &#x60;attachment&#x60; | [optional]

### Return type

**bytearray**

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**206** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_user_recovery_codes**
> List[str] generate_user_recovery_codes()

Generate recovery codes

Generates new recovery codes for the logged in user. Generating new recovery codes you automatically invalidate old ones

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
    api_instance = openapi_client.UserAPIsApi(api_client)

    try:
        # Generate recovery codes
        api_response = api_instance.generate_user_recovery_codes()
        print("The response of UserAPIsApi->generate_user_recovery_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->generate_user_recovery_codes: %s\n" % e)
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

# **generate_user_totp_secret**
> GenerateAdminTotpSecret200Response generate_user_totp_secret(generate_admin_totp_secret_request)

Generate a new TOTP secret

Generates a new TOTP secret, including the QR code as png, using the specified configuration for the logged in user

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
    api_instance = openapi_client.UserAPIsApi(api_client)
    generate_admin_totp_secret_request = openapi_client.GenerateAdminTotpSecretRequest() # GenerateAdminTotpSecretRequest |

    try:
        # Generate a new TOTP secret
        api_response = api_instance.generate_user_totp_secret(generate_admin_totp_secret_request)
        print("The response of UserAPIsApi->generate_user_totp_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->generate_user_totp_secret: %s\n" % e)
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

# **get_user_dir_contents**
> List[DirEntry] get_user_dir_contents(path=path)

Read directory contents

Returns the contents of the specified directory for the logged in user

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.dir_entry import DirEntry
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
    api_instance = openapi_client.UserAPIsApi(api_client)
    path = 'path_example' # str | Path to the folder to read. It must be URL encoded, for example the path \"my dir/àdir\" must be sent as \"my%20dir%2F%C3%A0dir\". If empty or missing the user's start directory is assumed. If relative, the user's start directory is used as the base (optional)

    try:
        # Read directory contents
        api_response = api_instance.get_user_dir_contents(path=path)
        print("The response of UserAPIsApi->get_user_dir_contents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->get_user_dir_contents: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path to the folder to read. It must be URL encoded, for example the path \&quot;my dir/àdir\&quot; must be sent as \&quot;my%20dir%2F%C3%A0dir\&quot;. If empty or missing the user&#39;s start directory is assumed. If relative, the user&#39;s start directory is used as the base | [optional]

### Return type

[**List[DirEntry]**](DirEntry.md)

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

# **get_user_profile**
> UserProfile get_user_profile()

Get user profile

Returns the profile for the logged in user

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.user_profile import UserProfile
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
    api_instance = openapi_client.UserAPIsApi(api_client)

    try:
        # Get user profile
        api_response = api_instance.get_user_profile()
        print("The response of UserAPIsApi->get_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->get_user_profile: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**UserProfile**](UserProfile.md)

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

# **get_user_recovery_codes**
> List[RecoveryCode] get_user_recovery_codes()

Get recovery codes

Returns the recovery codes for the logged in user. Recovery codes can be used if the user loses access to their second factor auth device. Recovery codes are returned unencrypted

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
    api_instance = openapi_client.UserAPIsApi(api_client)

    try:
        # Get recovery codes
        api_response = api_instance.get_user_recovery_codes()
        print("The response of UserAPIsApi->get_user_recovery_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->get_user_recovery_codes: %s\n" % e)
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

# **get_user_share_by_id**
> Share get_user_share_by_id(id)

Get share by id

Returns a share by id for the logged in user

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.share import Share
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
    api_instance = openapi_client.UserAPIsApi(api_client)
    id = 'id_example' # str | the share id

    try:
        # Get share by id
        api_response = api_instance.get_user_share_by_id(id)
        print("The response of UserAPIsApi->get_user_share_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->get_user_share_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the share id |

### Return type

[**Share**](Share.md)

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

# **get_user_shares**
> List[Share] get_user_shares(offset=offset, limit=limit, order=order)

List user shares

Returns the share for the logged in user

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.share import Share
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
    api_instance = openapi_client.UserAPIsApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int | The maximum number of items to return. Max value is 500, default is 100 (optional) (default to 100)
    order = 'ASC' # str | Ordering shares by ID. Default ASC (optional)

    try:
        # List user shares
        api_response = api_instance.get_user_shares(offset=offset, limit=limit, order=order)
        print("The response of UserAPIsApi->get_user_shares:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->get_user_shares: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**| The maximum number of items to return. Max value is 500, default is 100 | [optional] [default to 100]
 **order** | **str**| Ordering shares by ID. Default ASC | [optional]

### Return type

[**List[Share]**](Share.md)

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

# **get_user_totp_configs**
> List[TOTPConfig] get_user_totp_configs()

Get available TOTP configuration

Returns the available TOTP configurations for the logged in user

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
    api_instance = openapi_client.UserAPIsApi(api_client)

    try:
        # Get available TOTP configuration
        api_response = api_instance.get_user_totp_configs()
        print("The response of UserAPIsApi->get_user_totp_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->get_user_totp_configs: %s\n" % e)
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

# **rename_user_dir**
> ApiResponse rename_user_dir(path, target)

Rename a directory. Deprecated, use \"file-actions/move\"

Rename a directory for the logged in user. The rename is allowed for empty directory or for non empty local directories, with no virtual folders inside

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
    api_instance = openapi_client.UserAPIsApi(api_client)
    path = 'path_example' # str | Path to the folder to rename. It must be URL encoded, for example the path \"my dir/àdir\" must be sent as \"my%20dir%2F%C3%A0dir\"
    target = 'target_example' # str | New name. It must be URL encoded, for example the path \"my dir/àdir\" must be sent as \"my%20dir%2F%C3%A0dir\"

    try:
        # Rename a directory. Deprecated, use \"file-actions/move\"
        api_response = api_instance.rename_user_dir(path, target)
        print("The response of UserAPIsApi->rename_user_dir:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->rename_user_dir: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path to the folder to rename. It must be URL encoded, for example the path \&quot;my dir/àdir\&quot; must be sent as \&quot;my%20dir%2F%C3%A0dir\&quot; |
 **target** | **str**| New name. It must be URL encoded, for example the path \&quot;my dir/àdir\&quot; must be sent as \&quot;my%20dir%2F%C3%A0dir\&quot; |

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

# **rename_user_file**
> ApiResponse rename_user_file(path, target)

Rename a file

Rename a file for the logged in user. Deprecated, use \"file-actions/move\"

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
    api_instance = openapi_client.UserAPIsApi(api_client)
    path = 'path_example' # str | Path to the file to rename. It must be URL encoded
    target = 'target_example' # str | New name. It must be URL encoded

    try:
        # Rename a file
        api_response = api_instance.rename_user_file(path, target)
        print("The response of UserAPIsApi->rename_user_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->rename_user_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path to the file to rename. It must be URL encoded |
 **target** | **str**| New name. It must be URL encoded |

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

# **save_user_totp_config**
> ApiResponse save_user_totp_config(user_totp_config)

Save a TOTP config

Saves the specified TOTP config for the logged in user

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.user_totp_config import UserTOTPConfig
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
    api_instance = openapi_client.UserAPIsApi(api_client)
    user_totp_config = openapi_client.UserTOTPConfig() # UserTOTPConfig |

    try:
        # Save a TOTP config
        api_response = api_instance.save_user_totp_config(user_totp_config)
        print("The response of UserAPIsApi->save_user_totp_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->save_user_totp_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_totp_config** | [**UserTOTPConfig**](UserTOTPConfig.md)|  |

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

# **setprops_user_file**
> ApiResponse setprops_user_file(path, setprops_user_file_request)

Set metadata for a file/directory

Set supported metadata attributes for the specified file or directory

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.setprops_user_file_request import SetpropsUserFileRequest
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
    api_instance = openapi_client.UserAPIsApi(api_client)
    path = 'path_example' # str | Full file/directory path. It must be URL encoded, for example the path \"my dir/àdir/file.txt\" must be sent as \"my%20dir%2F%C3%A0dir%2Ffile.txt\"
    setprops_user_file_request = openapi_client.SetpropsUserFileRequest() # SetpropsUserFileRequest |

    try:
        # Set metadata for a file/directory
        api_response = api_instance.setprops_user_file(path, setprops_user_file_request)
        print("The response of UserAPIsApi->setprops_user_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->setprops_user_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Full file/directory path. It must be URL encoded, for example the path \&quot;my dir/àdir/file.txt\&quot; must be sent as \&quot;my%20dir%2F%C3%A0dir%2Ffile.txt\&quot; |
 **setprops_user_file_request** | [**SetpropsUserFileRequest**](SetpropsUserFileRequest.md)|  |

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
**413** | Request Entity Too Large, max allowed size exceeded |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **streamzip**
> bytearray streamzip(request_body)

Download multiple files and folders as a single zip file

A zip file, containing the specified files and folders, will be generated on the fly and returned as response body. Only folders and regular files will be included in the zip

### Example

* Api Key Authentication (APIKeyAuth):
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
    api_instance = openapi_client.UserAPIsApi(api_client)
    request_body = ['request_body_example'] # List[str] |

    try:
        # Download multiple files and folders as a single zip file
        api_response = api_instance.streamzip(request_body)
        print("The response of UserAPIsApi->streamzip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->streamzip: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  |

### Return type

**bytearray**

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip, application/json

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

# **update_user_profile**
> ApiResponse update_user_profile(user_profile)

Update user profile

Allows to update the profile for the logged in user

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.user_profile import UserProfile
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
    api_instance = openapi_client.UserAPIsApi(api_client)
    user_profile = openapi_client.UserProfile() # UserProfile |

    try:
        # Update user profile
        api_response = api_instance.update_user_profile(user_profile)
        print("The response of UserAPIsApi->update_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->update_user_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_profile** | [**UserProfile**](UserProfile.md)|  |

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

# **update_user_share**
> ApiResponse update_user_share(id, share)

Update share

Updates an existing share belonging to the logged in user

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.share import Share
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
    api_instance = openapi_client.UserAPIsApi(api_client)
    id = 'id_example' # str | the share id
    share = openapi_client.Share() # Share |

    try:
        # Update share
        api_response = api_instance.update_user_share(id, share)
        print("The response of UserAPIsApi->update_user_share:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->update_user_share: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the share id |
 **share** | [**Share**](Share.md)|  |

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

# **user_file_actions_copy_post**
> ApiResponse user_file_actions_copy_post(path, target)

Copy a file or a directory

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
    api_instance = openapi_client.UserAPIsApi(api_client)
    path = 'path_example' # str | Path to the file/folder to copy. It must be URL encoded, for example the path \"my dir/àdir\" must be sent as \"my%20dir%2F%C3%A0dir\"
    target = 'target_example' # str | New name. It must be URL encoded, for example the path \"my dir/àdir\" must be sent as \"my%20dir%2F%C3%A0dir\"

    try:
        # Copy a file or a directory
        api_response = api_instance.user_file_actions_copy_post(path, target)
        print("The response of UserAPIsApi->user_file_actions_copy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->user_file_actions_copy_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path to the file/folder to copy. It must be URL encoded, for example the path \&quot;my dir/àdir\&quot; must be sent as \&quot;my%20dir%2F%C3%A0dir\&quot; |
 **target** | **str**| New name. It must be URL encoded, for example the path \&quot;my dir/àdir\&quot; must be sent as \&quot;my%20dir%2F%C3%A0dir\&quot; |

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

# **user_file_actions_move_post**
> ApiResponse user_file_actions_move_post(path, target)

Move (rename) a file or a directory

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
    api_instance = openapi_client.UserAPIsApi(api_client)
    path = 'path_example' # str | Path to the file/folder to rename. It must be URL encoded, for example the path \"my dir/àdir\" must be sent as \"my%20dir%2F%C3%A0dir\"
    target = 'target_example' # str | New name. It must be URL encoded, for example the path \"my dir/àdir\" must be sent as \"my%20dir%2F%C3%A0dir\"

    try:
        # Move (rename) a file or a directory
        api_response = api_instance.user_file_actions_move_post(path, target)
        print("The response of UserAPIsApi->user_file_actions_move_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->user_file_actions_move_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path to the file/folder to rename. It must be URL encoded, for example the path \&quot;my dir/àdir\&quot; must be sent as \&quot;my%20dir%2F%C3%A0dir\&quot; |
 **target** | **str**| New name. It must be URL encoded, for example the path \&quot;my dir/àdir\&quot; must be sent as \&quot;my%20dir%2F%C3%A0dir\&quot; |

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

# **validate_user_totp_secret**
> ApiResponse validate_user_totp_secret(validate_admin_totp_secret_request)

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
    api_instance = openapi_client.UserAPIsApi(api_client)
    validate_admin_totp_secret_request = openapi_client.ValidateAdminTotpSecretRequest() # ValidateAdminTotpSecretRequest |

    try:
        # Validate a one time authentication code
        api_response = api_instance.validate_user_totp_secret(validate_admin_totp_secret_request)
        print("The response of UserAPIsApi->validate_user_totp_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAPIsApi->validate_user_totp_secret: %s\n" % e)
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
