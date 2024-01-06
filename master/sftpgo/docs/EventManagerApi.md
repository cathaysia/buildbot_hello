# openapi_client.EventManagerApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_event_action**](EventManagerApi.md#add_event_action) | **POST** /eventactions | Add event action
[**add_event_rule**](EventManagerApi.md#add_event_rule) | **POST** /eventrules | Add event rule
[**delete_event_action**](EventManagerApi.md#delete_event_action) | **DELETE** /eventactions/{name} | Delete event action
[**delete_event_rule**](EventManagerApi.md#delete_event_rule) | **DELETE** /eventrules/{name} | Delete event rule
[**get_event_action_by_name**](EventManagerApi.md#get_event_action_by_name) | **GET** /eventactions/{name} | Find event actions by name
[**get_event_actons**](EventManagerApi.md#get_event_actons) | **GET** /eventactions | Get event actions
[**get_event_rile_by_name**](EventManagerApi.md#get_event_rile_by_name) | **GET** /eventrules/{name} | Find event rules by name
[**get_event_rules**](EventManagerApi.md#get_event_rules) | **GET** /eventrules | Get event rules
[**run_event_rule**](EventManagerApi.md#run_event_rule) | **POST** /eventrules/run/{name} | Run an on-demand event rule
[**update_event_action**](EventManagerApi.md#update_event_action) | **PUT** /eventactions/{name} | Update event action
[**update_event_rule**](EventManagerApi.md#update_event_rule) | **PUT** /eventrules/{name} | Update event rule


# **add_event_action**
> BaseEventAction add_event_action(base_event_action, confidential_data=confidential_data)

Add event action

Adds a new event actions

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.base_event_action import BaseEventAction
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
    api_instance = openapi_client.EventManagerApi(api_client)
    base_event_action = openapi_client.BaseEventAction() # BaseEventAction |
    confidential_data = 56 # int | If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted. (optional)

    try:
        # Add event action
        api_response = api_instance.add_event_action(base_event_action, confidential_data=confidential_data)
        print("The response of EventManagerApi->add_event_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->add_event_action: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_event_action** | [**BaseEventAction**](BaseEventAction.md)|  |
 **confidential_data** | **int**| If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted. | [optional]

### Return type

[**BaseEventAction**](BaseEventAction.md)

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

# **add_event_rule**
> EventRule add_event_rule(event_rule_minimal, confidential_data=confidential_data)

Add event rule

Adds a new event rule

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.event_rule import EventRule
from openapi_client.models.event_rule_minimal import EventRuleMinimal
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
    api_instance = openapi_client.EventManagerApi(api_client)
    event_rule_minimal = openapi_client.EventRuleMinimal() # EventRuleMinimal |
    confidential_data = 56 # int | If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted. (optional)

    try:
        # Add event rule
        api_response = api_instance.add_event_rule(event_rule_minimal, confidential_data=confidential_data)
        print("The response of EventManagerApi->add_event_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->add_event_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_rule_minimal** | [**EventRuleMinimal**](EventRuleMinimal.md)|  |
 **confidential_data** | **int**| If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted. | [optional]

### Return type

[**EventRule**](EventRule.md)

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

# **delete_event_action**
> ApiResponse delete_event_action(name)

Delete event action

Deletes an existing event action

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
    api_instance = openapi_client.EventManagerApi(api_client)
    name = 'name_example' # str | action name

    try:
        # Delete event action
        api_response = api_instance.delete_event_action(name)
        print("The response of EventManagerApi->delete_event_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->delete_event_action: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| action name |

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

# **delete_event_rule**
> ApiResponse delete_event_rule(name)

Delete event rule

Deletes an existing event rule

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
    api_instance = openapi_client.EventManagerApi(api_client)
    name = 'name_example' # str | rule name

    try:
        # Delete event rule
        api_response = api_instance.delete_event_rule(name)
        print("The response of EventManagerApi->delete_event_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->delete_event_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| rule name |

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

# **get_event_action_by_name**
> BaseEventAction get_event_action_by_name(name, confidential_data=confidential_data)

Find event actions by name

Returns the event action with the given name if it exists.

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.base_event_action import BaseEventAction
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
    api_instance = openapi_client.EventManagerApi(api_client)
    name = 'name_example' # str | action name
    confidential_data = 56 # int | If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted. (optional)

    try:
        # Find event actions by name
        api_response = api_instance.get_event_action_by_name(name, confidential_data=confidential_data)
        print("The response of EventManagerApi->get_event_action_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->get_event_action_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| action name |
 **confidential_data** | **int**| If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted. | [optional]

### Return type

[**BaseEventAction**](BaseEventAction.md)

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

# **get_event_actons**
> List[BaseEventAction] get_event_actons(offset=offset, limit=limit, order=order)

Get event actions

Returns an array with one or more event actions

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.base_event_action import BaseEventAction
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
    api_instance = openapi_client.EventManagerApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int | The maximum number of items to return. Max value is 500, default is 100 (optional) (default to 100)
    order = 'ASC' # str | Ordering actions by name. Default ASC (optional)

    try:
        # Get event actions
        api_response = api_instance.get_event_actons(offset=offset, limit=limit, order=order)
        print("The response of EventManagerApi->get_event_actons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->get_event_actons: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**| The maximum number of items to return. Max value is 500, default is 100 | [optional] [default to 100]
 **order** | **str**| Ordering actions by name. Default ASC | [optional]

### Return type

[**List[BaseEventAction]**](BaseEventAction.md)

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

# **get_event_rile_by_name**
> EventRule get_event_rile_by_name(name, confidential_data=confidential_data)

Find event rules by name

Returns the event rule with the given name if it exists.

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.event_rule import EventRule
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
    api_instance = openapi_client.EventManagerApi(api_client)
    name = 'name_example' # str | rule name
    confidential_data = 56 # int | If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted. (optional)

    try:
        # Find event rules by name
        api_response = api_instance.get_event_rile_by_name(name, confidential_data=confidential_data)
        print("The response of EventManagerApi->get_event_rile_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->get_event_rile_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| rule name |
 **confidential_data** | **int**| If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted. | [optional]

### Return type

[**EventRule**](EventRule.md)

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

# **get_event_rules**
> List[EventRule] get_event_rules(offset=offset, limit=limit, order=order)

Get event rules

Returns an array with one or more event rules

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.event_rule import EventRule
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
    api_instance = openapi_client.EventManagerApi(api_client)
    offset = 0 # int |  (optional) (default to 0)
    limit = 100 # int | The maximum number of items to return. Max value is 500, default is 100 (optional) (default to 100)
    order = 'ASC' # str | Ordering rules by name. Default ASC (optional)

    try:
        # Get event rules
        api_response = api_instance.get_event_rules(offset=offset, limit=limit, order=order)
        print("The response of EventManagerApi->get_event_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->get_event_rules: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**| The maximum number of items to return. Max value is 500, default is 100 | [optional] [default to 100]
 **order** | **str**| Ordering rules by name. Default ASC | [optional]

### Return type

[**List[EventRule]**](EventRule.md)

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

# **run_event_rule**
> ApiResponse run_event_rule(name)

Run an on-demand event rule

The rule's actions will run in background. SFTPGo will not monitor any concurrency and such. If you want to be notified at the end of the execution please add an appropriate action

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
    api_instance = openapi_client.EventManagerApi(api_client)
    name = 'name_example' # str | on-demand rule name

    try:
        # Run an on-demand event rule
        api_response = api_instance.run_event_rule(name)
        print("The response of EventManagerApi->run_event_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->run_event_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| on-demand rule name |

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
**500** | Internal Server Error |  -  |
**0** | Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_action**
> ApiResponse update_event_action(name, base_event_action)

Update event action

Updates an existing event action

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.base_event_action import BaseEventAction
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
    api_instance = openapi_client.EventManagerApi(api_client)
    name = 'name_example' # str | action name
    base_event_action = openapi_client.BaseEventAction() # BaseEventAction |

    try:
        # Update event action
        api_response = api_instance.update_event_action(name, base_event_action)
        print("The response of EventManagerApi->update_event_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->update_event_action: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| action name |
 **base_event_action** | [**BaseEventAction**](BaseEventAction.md)|  |

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

# **update_event_rule**
> ApiResponse update_event_rule(name, event_rule_minimal)

Update event rule

Updates an existing event rule

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.api_response import ApiResponse
from openapi_client.models.event_rule_minimal import EventRuleMinimal
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
    api_instance = openapi_client.EventManagerApi(api_client)
    name = 'name_example' # str | rule name
    event_rule_minimal = openapi_client.EventRuleMinimal() # EventRuleMinimal |

    try:
        # Update event rule
        api_response = api_instance.update_event_rule(name, event_rule_minimal)
        print("The response of EventManagerApi->update_event_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventManagerApi->update_event_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| rule name |
 **event_rule_minimal** | [**EventRuleMinimal**](EventRuleMinimal.md)|  |

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
