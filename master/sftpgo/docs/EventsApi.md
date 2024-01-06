# openapi_client.EventsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fs_events**](EventsApi.md#get_fs_events) | **GET** /events/fs | Get filesystem events
[**get_log_events**](EventsApi.md#get_log_events) | **GET** /events/log | Get log events
[**get_provider_events**](EventsApi.md#get_provider_events) | **GET** /events/provider | Get provider events


# **get_fs_events**
> List[FsEvent] get_fs_events(start_timestamp=start_timestamp, end_timestamp=end_timestamp, actions=actions, username=username, ip=ip, ssh_cmd=ssh_cmd, fs_provider=fs_provider, bucket=bucket, endpoint=endpoint, protocols=protocols, statuses=statuses, instance_ids=instance_ids, from_id=from_id, role=role, csv_export=csv_export, limit=limit, order=order)

Get filesystem events

Returns an array with one or more filesystem events applying the specified filters. This API is only available if you configure an \"eventsearcher\" plugin

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.event_protocols import EventProtocols
from openapi_client.models.fs_event import FsEvent
from openapi_client.models.fs_event_action import FsEventAction
from openapi_client.models.fs_event_status import FsEventStatus
from openapi_client.models.fs_providers import FsProviders
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
    api_instance = openapi_client.EventsApi(api_client)
    start_timestamp = 0 # int | the event timestamp, unix timestamp in nanoseconds, must be greater than or equal to the specified one. 0 or missing means omit this filter (optional) (default to 0)
    end_timestamp = 0 # int | the event timestamp, unix timestamp in nanoseconds, must be less than or equal to the specified one. 0 or missing means omit this filter (optional) (default to 0)
    actions = [openapi_client.FsEventAction()] # List[FsEventAction] | the event action must be included among those specified. Empty or missing means omit this filter. Actions must be specified comma separated (optional)
    username = 'username_example' # str | the event username must be the same as the one specified. Empty or missing means omit this filter (optional)
    ip = 'ip_example' # str | the event IP must be the same as the one specified. Empty or missing means omit this filter (optional)
    ssh_cmd = 'ssh_cmd_example' # str | the event SSH command must be the same as the one specified. Empty or missing means omit this filter (optional)
    fs_provider = openapi_client.FsProviders() # FsProviders | the event filesystem provider must be the same as the one specified. Empty or missing means omit this filter (optional)
    bucket = 'bucket_example' # str | the bucket must be the same as the one specified. Empty or missing means omit this filter (optional)
    endpoint = 'endpoint_example' # str | the endpoint must be the same as the one specified. Empty or missing means omit this filter (optional)
    protocols = [openapi_client.EventProtocols()] # List[EventProtocols] | the event protocol must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated (optional)
    statuses = [openapi_client.FsEventStatus()] # List[FsEventStatus] | the event status must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated (optional)
    instance_ids = ['instance_ids_example'] # List[str] | the event instance id must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated (optional)
    from_id = 'from_id_example' # str | the event id to start from. This is useful for cursor based pagination. Empty or missing means omit this filter. (optional)
    role = 'role_example' # str | User role. Empty or missing means omit this filter. Ignored if the admin has a role (optional)
    csv_export = False # bool | If enabled, events are exported as a CSV file (optional) (default to False)
    limit = 100 # int | The maximum number of items to return. Max value is 1000, default is 100 (optional) (default to 100)
    order = 'DESC' # str | Ordering events by timestamp. Default DESC (optional)

    try:
        # Get filesystem events
        api_response = api_instance.get_fs_events(start_timestamp=start_timestamp, end_timestamp=end_timestamp, actions=actions, username=username, ip=ip, ssh_cmd=ssh_cmd, fs_provider=fs_provider, bucket=bucket, endpoint=endpoint, protocols=protocols, statuses=statuses, instance_ids=instance_ids, from_id=from_id, role=role, csv_export=csv_export, limit=limit, order=order)
        print("The response of EventsApi->get_fs_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_fs_events: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_timestamp** | **int**| the event timestamp, unix timestamp in nanoseconds, must be greater than or equal to the specified one. 0 or missing means omit this filter | [optional] [default to 0]
 **end_timestamp** | **int**| the event timestamp, unix timestamp in nanoseconds, must be less than or equal to the specified one. 0 or missing means omit this filter | [optional] [default to 0]
 **actions** | [**List[FsEventAction]**](FsEventAction.md)| the event action must be included among those specified. Empty or missing means omit this filter. Actions must be specified comma separated | [optional]
 **username** | **str**| the event username must be the same as the one specified. Empty or missing means omit this filter | [optional]
 **ip** | **str**| the event IP must be the same as the one specified. Empty or missing means omit this filter | [optional]
 **ssh_cmd** | **str**| the event SSH command must be the same as the one specified. Empty or missing means omit this filter | [optional]
 **fs_provider** | [**FsProviders**](.md)| the event filesystem provider must be the same as the one specified. Empty or missing means omit this filter | [optional]
 **bucket** | **str**| the bucket must be the same as the one specified. Empty or missing means omit this filter | [optional]
 **endpoint** | **str**| the endpoint must be the same as the one specified. Empty or missing means omit this filter | [optional]
 **protocols** | [**List[EventProtocols]**](EventProtocols.md)| the event protocol must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated | [optional]
 **statuses** | [**List[FsEventStatus]**](FsEventStatus.md)| the event status must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated | [optional]
 **instance_ids** | [**List[str]**](str.md)| the event instance id must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated | [optional]
 **from_id** | **str**| the event id to start from. This is useful for cursor based pagination. Empty or missing means omit this filter. | [optional]
 **role** | **str**| User role. Empty or missing means omit this filter. Ignored if the admin has a role | [optional]
 **csv_export** | **bool**| If enabled, events are exported as a CSV file | [optional] [default to False]
 **limit** | **int**| The maximum number of items to return. Max value is 1000, default is 100 | [optional] [default to 100]
 **order** | **str**| Ordering events by timestamp. Default DESC | [optional]

### Return type

[**List[FsEvent]**](FsEvent.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

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

# **get_log_events**
> List[LogEvent] get_log_events(start_timestamp=start_timestamp, end_timestamp=end_timestamp, events=events, username=username, ip=ip, protocols=protocols, instance_ids=instance_ids, from_id=from_id, role=role, csv_export=csv_export, limit=limit, order=order)

Get log events

Returns an array with one or more log events applying the specified filters. This API is only available if you configure an \"eventsearcher\" plugin

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.event_protocols import EventProtocols
from openapi_client.models.log_event import LogEvent
from openapi_client.models.log_event_type import LogEventType
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
    api_instance = openapi_client.EventsApi(api_client)
    start_timestamp = 0 # int | the event timestamp, unix timestamp in nanoseconds, must be greater than or equal to the specified one. 0 or missing means omit this filter (optional) (default to 0)
    end_timestamp = 0 # int | the event timestamp, unix timestamp in nanoseconds, must be less than or equal to the specified one. 0 or missing means omit this filter (optional) (default to 0)
    events = [openapi_client.LogEventType()] # List[LogEventType] | the log events must be included among those specified. Empty or missing means omit this filter. Events must be specified comma separated (optional)
    username = 'username_example' # str | the event username must be the same as the one specified. Empty or missing means omit this filter (optional)
    ip = 'ip_example' # str | the event IP must be the same as the one specified. Empty or missing means omit this filter (optional)
    protocols = [openapi_client.EventProtocols()] # List[EventProtocols] | the event protocol must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated (optional)
    instance_ids = ['instance_ids_example'] # List[str] | the event instance id must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated (optional)
    from_id = 'from_id_example' # str | the event id to start from. This is useful for cursor based pagination. Empty or missing means omit this filter. (optional)
    role = 'role_example' # str | User role. Empty or missing means omit this filter. Ignored if the admin has a role (optional)
    csv_export = False # bool | If enabled, events are exported as a CSV file (optional) (default to False)
    limit = 100 # int | The maximum number of items to return. Max value is 1000, default is 100 (optional) (default to 100)
    order = 'DESC' # str | Ordering events by timestamp. Default DESC (optional)

    try:
        # Get log events
        api_response = api_instance.get_log_events(start_timestamp=start_timestamp, end_timestamp=end_timestamp, events=events, username=username, ip=ip, protocols=protocols, instance_ids=instance_ids, from_id=from_id, role=role, csv_export=csv_export, limit=limit, order=order)
        print("The response of EventsApi->get_log_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_log_events: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_timestamp** | **int**| the event timestamp, unix timestamp in nanoseconds, must be greater than or equal to the specified one. 0 or missing means omit this filter | [optional] [default to 0]
 **end_timestamp** | **int**| the event timestamp, unix timestamp in nanoseconds, must be less than or equal to the specified one. 0 or missing means omit this filter | [optional] [default to 0]
 **events** | [**List[LogEventType]**](LogEventType.md)| the log events must be included among those specified. Empty or missing means omit this filter. Events must be specified comma separated | [optional]
 **username** | **str**| the event username must be the same as the one specified. Empty or missing means omit this filter | [optional]
 **ip** | **str**| the event IP must be the same as the one specified. Empty or missing means omit this filter | [optional]
 **protocols** | [**List[EventProtocols]**](EventProtocols.md)| the event protocol must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated | [optional]
 **instance_ids** | [**List[str]**](str.md)| the event instance id must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated | [optional]
 **from_id** | **str**| the event id to start from. This is useful for cursor based pagination. Empty or missing means omit this filter. | [optional]
 **role** | **str**| User role. Empty or missing means omit this filter. Ignored if the admin has a role | [optional]
 **csv_export** | **bool**| If enabled, events are exported as a CSV file | [optional] [default to False]
 **limit** | **int**| The maximum number of items to return. Max value is 1000, default is 100 | [optional] [default to 100]
 **order** | **str**| Ordering events by timestamp. Default DESC | [optional]

### Return type

[**List[LogEvent]**](LogEvent.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

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

# **get_provider_events**
> List[ProviderEvent] get_provider_events(start_timestamp=start_timestamp, end_timestamp=end_timestamp, actions=actions, username=username, ip=ip, object_name=object_name, object_types=object_types, instance_ids=instance_ids, from_id=from_id, role=role, csv_export=csv_export, omit_object_data=omit_object_data, limit=limit, order=order)

Get provider events

Returns an array with one or more provider events applying the specified filters. This API is only available if you configure an \"eventsearcher\" plugin

### Example

* Api Key Authentication (APIKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.provider_event import ProviderEvent
from openapi_client.models.provider_event_action import ProviderEventAction
from openapi_client.models.provider_event_object_type import ProviderEventObjectType
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
    api_instance = openapi_client.EventsApi(api_client)
    start_timestamp = 0 # int | the event timestamp, unix timestamp in nanoseconds, must be greater than or equal to the specified one. 0 or missing means omit this filter (optional) (default to 0)
    end_timestamp = 0 # int | the event timestamp, unix timestamp in nanoseconds, must be less than or equal to the specified one. 0 or missing means omit this filter (optional) (default to 0)
    actions = [openapi_client.ProviderEventAction()] # List[ProviderEventAction] | the event action must be included among those specified. Empty or missing means omit this filter. Actions must be specified comma separated (optional)
    username = 'username_example' # str | the event username must be the same as the one specified. Empty or missing means omit this filter (optional)
    ip = 'ip_example' # str | the event IP must be the same as the one specified. Empty or missing means omit this filter (optional)
    object_name = 'object_name_example' # str | the event object name must be the same as the one specified. Empty or missing means omit this filter (optional)
    object_types = [openapi_client.ProviderEventObjectType()] # List[ProviderEventObjectType] | the event object type must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated (optional)
    instance_ids = ['instance_ids_example'] # List[str] | the event instance id must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated (optional)
    from_id = 'from_id_example' # str | the event id to start from. This is useful for cursor based pagination. Empty or missing means omit this filter. (optional)
    role = 'role_example' # str | Admin role. Empty or missing means omit this filter. Ignored if the admin has a role (optional)
    csv_export = False # bool | If enabled, events are exported as a CSV file (optional) (default to False)
    omit_object_data = False # bool | If enabled, returned events will not contain the `object_data` field (optional) (default to False)
    limit = 100 # int | The maximum number of items to return. Max value is 1000, default is 100 (optional) (default to 100)
    order = 'DESC' # str | Ordering events by timestamp. Default DESC (optional)

    try:
        # Get provider events
        api_response = api_instance.get_provider_events(start_timestamp=start_timestamp, end_timestamp=end_timestamp, actions=actions, username=username, ip=ip, object_name=object_name, object_types=object_types, instance_ids=instance_ids, from_id=from_id, role=role, csv_export=csv_export, omit_object_data=omit_object_data, limit=limit, order=order)
        print("The response of EventsApi->get_provider_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_provider_events: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_timestamp** | **int**| the event timestamp, unix timestamp in nanoseconds, must be greater than or equal to the specified one. 0 or missing means omit this filter | [optional] [default to 0]
 **end_timestamp** | **int**| the event timestamp, unix timestamp in nanoseconds, must be less than or equal to the specified one. 0 or missing means omit this filter | [optional] [default to 0]
 **actions** | [**List[ProviderEventAction]**](ProviderEventAction.md)| the event action must be included among those specified. Empty or missing means omit this filter. Actions must be specified comma separated | [optional]
 **username** | **str**| the event username must be the same as the one specified. Empty or missing means omit this filter | [optional]
 **ip** | **str**| the event IP must be the same as the one specified. Empty or missing means omit this filter | [optional]
 **object_name** | **str**| the event object name must be the same as the one specified. Empty or missing means omit this filter | [optional]
 **object_types** | [**List[ProviderEventObjectType]**](ProviderEventObjectType.md)| the event object type must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated | [optional]
 **instance_ids** | [**List[str]**](str.md)| the event instance id must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated | [optional]
 **from_id** | **str**| the event id to start from. This is useful for cursor based pagination. Empty or missing means omit this filter. | [optional]
 **role** | **str**| Admin role. Empty or missing means omit this filter. Ignored if the admin has a role | [optional]
 **csv_export** | **bool**| If enabled, events are exported as a CSV file | [optional] [default to False]
 **omit_object_data** | **bool**| If enabled, returned events will not contain the &#x60;object_data&#x60; field | [optional] [default to False]
 **limit** | **int**| The maximum number of items to return. Max value is 1000, default is 100 | [optional] [default to 100]
 **order** | **str**| Ordering events by timestamp. Default DESC | [optional]

### Return type

[**List[ProviderEvent]**](ProviderEvent.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

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
