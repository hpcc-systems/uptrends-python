# uptrends.AlertApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alert_get_monitor_alerts**](AlertApi.md#alert_get_monitor_alerts) | **GET** /Alert/Monitor/{monitorGuid} | Returns alerts for a specific monitor.
[**alert_get_monitor_group_alerts**](AlertApi.md#alert_get_monitor_group_alerts) | **GET** /Alert/MonitorGroup/{monitorGroupGuid} | Returns alerts for a specific monitor group.


# **alert_get_monitor_alerts**
> AlertResponse alert_get_monitor_alerts(monitor_guid, include_reminders=include_reminders, cursor=cursor, sorting=sorting, take=take, start=start, end=end, preset_period=preset_period)

Returns alerts for a specific monitor.

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
api_instance = uptrends.AlertApi(uptrends.ApiClient(configuration))
monitor_guid = 'monitor_guid_example' # str | The Guid of the monitor to get alerts for.
include_reminders = false # bool | When true reminder alerts will be included in the results (optional) (default to false)
cursor = 'cursor_example' # str | A cursor value that should be used for traversing the dataset. (optional)
sorting = 'Descending' # str | Sorting direction based on timestamp. (optional) (default to Descending)
take = 100 # int | The number of records to return (Max value = 100) (optional) (default to 100)
start = '2013-10-20T19:20:30+01:00' # datetime | The start of a custom period (can't be used together with the PresetPeriod parameter) (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | The end of a custom period (optional)
preset_period = 'Last24Hours' # str | The requested time period. (optional) (default to Last24Hours)

try:
    # Returns alerts for a specific monitor.
    api_response = api_instance.alert_get_monitor_alerts(monitor_guid, include_reminders=include_reminders, cursor=cursor, sorting=sorting, take=take, start=start, end=end, preset_period=preset_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->alert_get_monitor_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_guid** | **str**| The Guid of the monitor to get alerts for. | 
 **include_reminders** | **bool**| When true reminder alerts will be included in the results | [optional] [default to false]
 **cursor** | **str**| A cursor value that should be used for traversing the dataset. | [optional] 
 **sorting** | **str**| Sorting direction based on timestamp. | [optional] [default to Descending]
 **take** | **int**| The number of records to return (Max value &#x3D; 100) | [optional] [default to 100]
 **start** | **datetime**| The start of a custom period (can&#39;t be used together with the PresetPeriod parameter) | [optional] 
 **end** | **datetime**| The end of a custom period | [optional] 
 **preset_period** | **str**| The requested time period. | [optional] [default to Last24Hours]

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_get_monitor_group_alerts**
> AlertResponse alert_get_monitor_group_alerts(monitor_group_guid, include_reminders=include_reminders, cursor=cursor, sorting=sorting, take=take, start=start, end=end, preset_period=preset_period)

Returns alerts for a specific monitor group.

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
api_instance = uptrends.AlertApi(uptrends.ApiClient(configuration))
monitor_group_guid = 'monitor_group_guid_example' # str | The Guid of the monitor group to get alerts for.
include_reminders = false # bool | When true reminder alerts will be included in the results (optional) (default to false)
cursor = 'cursor_example' # str | A cursor value that should be used for traversing the dataset. (optional)
sorting = 'Descending' # str | Sorting direction based on timestamp. (optional) (default to Descending)
take = 100 # int | The number of records to return (Max value = 100) (optional) (default to 100)
start = '2013-10-20T19:20:30+01:00' # datetime | The start of a custom period (can't be used together with the PresetPeriod parameter) (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | The end of a custom period (optional)
preset_period = 'Last24Hours' # str | The requested time period. (optional) (default to Last24Hours)

try:
    # Returns alerts for a specific monitor group.
    api_response = api_instance.alert_get_monitor_group_alerts(monitor_group_guid, include_reminders=include_reminders, cursor=cursor, sorting=sorting, take=take, start=start, end=end, preset_period=preset_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->alert_get_monitor_group_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_group_guid** | **str**| The Guid of the monitor group to get alerts for. | 
 **include_reminders** | **bool**| When true reminder alerts will be included in the results | [optional] [default to false]
 **cursor** | **str**| A cursor value that should be used for traversing the dataset. | [optional] 
 **sorting** | **str**| Sorting direction based on timestamp. | [optional] [default to Descending]
 **take** | **int**| The number of records to return (Max value &#x3D; 100) | [optional] [default to 100]
 **start** | **datetime**| The start of a custom period (can&#39;t be used together with the PresetPeriod parameter) | [optional] 
 **end** | **datetime**| The end of a custom period | [optional] 
 **preset_period** | **str**| The requested time period. | [optional] [default to Last24Hours]

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

