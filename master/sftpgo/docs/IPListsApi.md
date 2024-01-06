# openapi_client.IPListsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ip_list_entry**](IPListsApi.md#add_ip_list_entry) | **POST** /iplists/{type} | Add a new IP list entry
[**delete_ip_list_entry**](IPListsApi.md#delete_ip_list_entry) | **DELETE** /iplists/{type}/{ipornet} | Delete IP list entry
[**get_ip_list_by_ipornet**](IPListsApi.md#get_ip_list_by_ipornet) | **GET** /iplists/{type}/{ipornet} | Find entry by ipornet
[**get_ip_list_entries**](IPListsApi.md#get_ip_list_entries) | **GET** /iplists/{type} | Get IP list entries
[**update_ip_list_entry**](IPListsApi.md#update_ip_list_entry) | **PUT** /iplists/{type}/{ipornet} | Update IP list entry


# **add_ip_list_entry**
> ApiResponse add_ip_list_entry(type, ip_list_entry)

Add a new IP list entry

Add an IP address or a CIDR network to a supported list

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.ip_list_entry import IPListEntry
from openapi_client.models.ip_list_type import IPListType
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
    api_instance = openapi_client.IPListsApi(api_client)
    type = openapi_client.IPListType() # IPListType | IP list type
    ip_list_entry = openapi_client.IPListEntry() # IPListEntry |

    try:
        # Add a new IP list entry
        api_response = api_instance.add_ip_list_entry(type, ip_list_entry)
        print("The response of IPListsApi->add_ip_list_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPListsApi->add_ip_list_entry: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**IPListType**](.md)| IP list type |
 **ip_list_entry** | [**IPListEntry**](IPListEntry.md)|  |

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
**201** | successful operation |  * Location - URI to retrieve the details for the new created share <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_list_entry**
> ApiResponse delete_ip_list_entry(type, ipornet)

Delete IP list entry

Deletes an existing IP list entry

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.ip_list_type import IPListType
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
    api_instance = openapi_client.IPListsApi(api_client)
    type = openapi_client.IPListType() # IPListType | IP list type
    ipornet = 'ipornet_example' # str |

    try:
        # Delete IP list entry
        api_response = api_instance.delete_ip_list_entry(type, ipornet)
        print("The response of IPListsApi->delete_ip_list_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPListsApi->delete_ip_list_entry: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**IPListType**](.md)| IP list type |
 **ipornet** | **str**|  |

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

# **get_ip_list_by_ipornet**
> IPListEntry get_ip_list_by_ipornet(type, ipornet)

Find entry by ipornet

Returns the entry with the given ipornet if it exists.

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.ip_list_entry import IPListEntry
from openapi_client.models.ip_list_type import IPListType
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
    api_instance = openapi_client.IPListsApi(api_client)
    type = openapi_client.IPListType() # IPListType | IP list type
    ipornet = 'ipornet_example' # str |

    try:
        # Find entry by ipornet
        api_response = api_instance.get_ip_list_by_ipornet(type, ipornet)
        print("The response of IPListsApi->get_ip_list_by_ipornet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPListsApi->get_ip_list_by_ipornet: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**IPListType**](.md)| IP list type |
 **ipornet** | **str**|  |

### Return type

[**IPListEntry**](IPListEntry.md)

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

# **get_ip_list_entries**
> List[IPListEntry] get_ip_list_entries(type, filter=filter, var_from=var_from, limit=limit, order=order)

Get IP list entries

Returns an array with one or more IP list entry

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.ip_list_entry import IPListEntry
from openapi_client.models.ip_list_type import IPListType
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
    api_instance = openapi_client.IPListsApi(api_client)
    type = openapi_client.IPListType() # IPListType | IP list type
    filter = 'filter_example' # str | restrict results to ipornet matching or starting with this filter (optional)
    var_from = 'var_from_example' # str | ipornet to start from (optional)
    limit = 100 # int | The maximum number of items to return. Max value is 500, default is 100 (optional) (default to 100)
    order = 'ASC' # str | Ordering entries by ipornet field. Default ASC (optional)

    try:
        # Get IP list entries
        api_response = api_instance.get_ip_list_entries(type, filter=filter, var_from=var_from, limit=limit, order=order)
        print("The response of IPListsApi->get_ip_list_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPListsApi->get_ip_list_entries: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**IPListType**](.md)| IP list type |
 **filter** | **str**| restrict results to ipornet matching or starting with this filter | [optional]
 **var_from** | **str**| ipornet to start from | [optional]
 **limit** | **int**| The maximum number of items to return. Max value is 500, default is 100 | [optional] [default to 100]
 **order** | **str**| Ordering entries by ipornet field. Default ASC | [optional]

### Return type

[**List[IPListEntry]**](IPListEntry.md)

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

# **update_ip_list_entry**
> ApiResponse update_ip_list_entry(type, ipornet, ip_list_entry)

Update IP list entry

Updates an existing IP list entry

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.ip_list_entry import IPListEntry
from openapi_client.models.ip_list_type import IPListType
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
    api_instance = openapi_client.IPListsApi(api_client)
    type = openapi_client.IPListType() # IPListType | IP list type
    ipornet = 'ipornet_example' # str |
    ip_list_entry = openapi_client.IPListEntry() # IPListEntry |

    try:
        # Update IP list entry
        api_response = api_instance.update_ip_list_entry(type, ipornet, ip_list_entry)
        print("The response of IPListsApi->update_ip_list_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPListsApi->update_ip_list_entry: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**IPListType**](.md)| IP list type |
 **ipornet** | **str**|  |
 **ip_list_entry** | [**IPListEntry**](IPListEntry.md)|  |

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
