# openapi_client.PublicSharesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_share_file**](PublicSharesApi.md#download_share_file) | **GET** /shares/{id}/files | Download a single file
[**get_share**](PublicSharesApi.md#get_share) | **GET** /shares/{id} | Download shared files and folders as a single zip file
[**get_share_dir_contents**](PublicSharesApi.md#get_share_dir_contents) | **GET** /shares/{id}/dirs | Read directory contents
[**upload_single_to_share**](PublicSharesApi.md#upload_single_to_share) | **POST** /shares/{id}/{fileName} | Upload a single file to the shared path
[**upload_to_share**](PublicSharesApi.md#upload_to_share) | **POST** /shares/{id} | Upload one or more files to the shared path


# **download_share_file**
> bytearray download_share_file(id, path, inline=inline)

Download a single file

Returns the file contents as response body. The share must have exactly one path defined and it must be a directory for this to work

### Example

* Basic Authentication (BasicAuth):
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

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicSharesApi(api_client)
    id = 'id_example' # str | the share id
    path = 'path_example' # str | Path to the file to download. It must be URL encoded, for example the path \"my dir/àdir/file.txt\" must be sent as \"my%20dir%2F%C3%A0dir%2Ffile.txt\"
    inline = 'inline_example' # str | If set, the response will not have the Content-Disposition header set to `attachment` (optional)

    try:
        # Download a single file
        api_response = api_instance.download_share_file(id, path, inline=inline)
        print("The response of PublicSharesApi->download_share_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSharesApi->download_share_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the share id |
 **path** | **str**| Path to the file to download. It must be URL encoded, for example the path \&quot;my dir/àdir/file.txt\&quot; must be sent as \&quot;my%20dir%2F%C3%A0dir%2Ffile.txt\&quot; |
 **inline** | **str**| If set, the response will not have the Content-Disposition header set to &#x60;attachment&#x60; | [optional]

### Return type

**bytearray**

### Authorization

[BasicAuth](../README.md#BasicAuth)

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

# **get_share**
> bytearray get_share(id, compress=compress)

Download shared files and folders as a single zip file

A zip file, containing the shared files and folders, will be generated on the fly and returned as response body. Only folders and regular files will be included in the zip. The share must be defined with the read scope and the associated user must have list and download permissions

### Example

* Basic Authentication (BasicAuth):
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

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicSharesApi(api_client)
    id = 'id_example' # str | the share id
    compress = True # bool |  (optional) (default to True)

    try:
        # Download shared files and folders as a single zip file
        api_response = api_instance.get_share(id, compress=compress)
        print("The response of PublicSharesApi->get_share:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSharesApi->get_share: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the share id |
 **compress** | **bool**|  | [optional] [default to True]

### Return type

**bytearray**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

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

# **get_share_dir_contents**
> List[DirEntry] get_share_dir_contents(id, path=path)

Read directory contents

Returns the contents of the specified directory for the specified share. The share must have exactly one path defined and it must be a directory for this to work

### Example

* Basic Authentication (BasicAuth):
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

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicSharesApi(api_client)
    id = 'id_example' # str | the share id
    path = 'path_example' # str | Path to the folder to read. It must be URL encoded, for example the path \"my dir/àdir\" must be sent as \"my%20dir%2F%C3%A0dir\". If empty or missing the user's start directory is assumed. If relative, the user's start directory is used as the base (optional)

    try:
        # Read directory contents
        api_response = api_instance.get_share_dir_contents(id, path=path)
        print("The response of PublicSharesApi->get_share_dir_contents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSharesApi->get_share_dir_contents: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the share id |
 **path** | **str**| Path to the folder to read. It must be URL encoded, for example the path \&quot;my dir/àdir\&quot; must be sent as \&quot;my%20dir%2F%C3%A0dir\&quot;. If empty or missing the user&#39;s start directory is assumed. If relative, the user&#39;s start directory is used as the base | [optional]

### Return type

[**List[DirEntry]**](DirEntry.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

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

# **upload_single_to_share**
> ApiResponse upload_single_to_share(id, file_name, body, x_sftpgo_mtime=x_sftpgo_mtime)

Upload a single file to the shared path

The share must be defined with the write scope and the associated user must have the upload/overwrite permissions

### Example

* Basic Authentication (BasicAuth):
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

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicSharesApi(api_client)
    id = 'id_example' # str | the share id
    file_name = 'file_name_example' # str | the name of the new file. It must be path encoded. Sub directories are not accepted
    body = None # bytearray |
    x_sftpgo_mtime = 56 # int | File modification time as unix timestamp in milliseconds (optional)

    try:
        # Upload a single file to the shared path
        api_response = api_instance.upload_single_to_share(id, file_name, body, x_sftpgo_mtime=x_sftpgo_mtime)
        print("The response of PublicSharesApi->upload_single_to_share:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSharesApi->upload_single_to_share: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the share id |
 **file_name** | **str**| the name of the new file. It must be path encoded. Sub directories are not accepted |
 **body** | **bytearray**|  |
 **x_sftpgo_mtime** | **int**| File modification time as unix timestamp in milliseconds | [optional]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

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

# **upload_to_share**
> ApiResponse upload_to_share(id, filenames=filenames)

Upload one or more files to the shared path

The share must be defined with the write scope and the associated user must have the upload permission

### Example

* Basic Authentication (BasicAuth):
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

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicSharesApi(api_client)
    id = 'id_example' # str | the share id
    filenames = None # List[bytearray] |  (optional)

    try:
        # Upload one or more files to the shared path
        api_response = api_instance.upload_to_share(id, filenames=filenames)
        print("The response of PublicSharesApi->upload_to_share:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSharesApi->upload_to_share: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the share id |
 **filenames** | **List[bytearray]**|  | [optional]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

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
