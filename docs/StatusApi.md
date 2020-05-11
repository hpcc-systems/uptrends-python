# uptrends.StatusApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_get_monitor_group_status**](StatusApi.md#status_get_monitor_group_status) | **GET** /Status/MonitorGroup/{monitorGroupGuid} | Gets a list of all monitor group status data.
[**status_get_monitor_status**](StatusApi.md#status_get_monitor_status) | **GET** /Status/Monitor/{monitorGuid} | Gets all monitor status data.


# **status_get_monitor_group_status**
> MonitorStatusListResponse status_get_monitor_group_status(monitor_group_guid)

Gets a list of all monitor group status data.

### Example
```python
from __future__ import print_function
import time
import uptrends
from uptrends.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicauth
configuration = uptrends.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = uptrends.StatusApi(uptrends.ApiClient(configuration))
monitor_group_guid = 'monitor_group_guid_example' # str | The Guid of the monitor group.

try:
    # Gets a list of all monitor group status data.
    api_response = api_instance.status_get_monitor_group_status(monitor_group_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->status_get_monitor_group_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_group_guid** | **str**| The Guid of the monitor group. | 

### Return type

[**MonitorStatusListResponse**](MonitorStatusListResponse.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_get_monitor_status**
> MonitorStatusResponse status_get_monitor_status(monitor_guid)

Gets all monitor status data.

### Example
```python
from __future__ import print_function
import time
import uptrends
from uptrends.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicauth
configuration = uptrends.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = uptrends.StatusApi(uptrends.ApiClient(configuration))
monitor_guid = 'monitor_guid_example' # str | The Guid of the monitor.

try:
    # Gets all monitor status data.
    api_response = api_instance.status_get_monitor_status(monitor_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->status_get_monitor_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_guid** | **str**| The Guid of the monitor. | 

### Return type

[**MonitorStatusResponse**](MonitorStatusResponse.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

