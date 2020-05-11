# uptrends.StatisticsApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistics_get_monitor_group_statistics**](StatisticsApi.md#statistics_get_monitor_group_statistics) | **GET** /Statistics/MonitorGroup/{monitorGroupGuid} | Gets the monitor group statistics.
[**statistics_get_monitor_statistics**](StatisticsApi.md#statistics_get_monitor_statistics) | **GET** /Statistics/Monitor/{monitorGuid} | Gets the monitor statistics.


# **statistics_get_monitor_group_statistics**
> StatisticsResponse statistics_get_monitor_group_statistics(monitor_group_guid, filter=filter, start=start, end=end, preset_period=preset_period)

Gets the monitor group statistics.

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
api_instance = uptrends.StatisticsApi(uptrends.ApiClient(configuration))
monitor_group_guid = 'monitor_group_guid_example' # str | The Guid of the monitor group.
filter = 'filter_example' # str | The filter for the requested response fields. E.g. \"Alerts,SlaTarget\". (optional)
start = '2013-10-20T19:20:30+01:00' # datetime | The start of a custom period (can't be used together with the PresetPeriod parameter) (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | The end of a custom period (optional)
preset_period = 'Last24Hours' # str | The requested time period. (optional) (default to Last24Hours)

try:
    # Gets the monitor group statistics.
    api_response = api_instance.statistics_get_monitor_group_statistics(monitor_group_guid, filter=filter, start=start, end=end, preset_period=preset_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->statistics_get_monitor_group_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_group_guid** | **str**| The Guid of the monitor group. | 
 **filter** | **str**| The filter for the requested response fields. E.g. \&quot;Alerts,SlaTarget\&quot;. | [optional] 
 **start** | **datetime**| The start of a custom period (can&#39;t be used together with the PresetPeriod parameter) | [optional] 
 **end** | **datetime**| The end of a custom period | [optional] 
 **preset_period** | **str**| The requested time period. | [optional] [default to Last24Hours]

### Return type

[**StatisticsResponse**](StatisticsResponse.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_get_monitor_statistics**
> StatisticsResponse statistics_get_monitor_statistics(monitor_guid, filter=filter, start=start, end=end, preset_period=preset_period)

Gets the monitor statistics.

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
api_instance = uptrends.StatisticsApi(uptrends.ApiClient(configuration))
monitor_guid = 'monitor_guid_example' # str | The Guid of the monitor.
filter = 'filter_example' # str | The filter for the requested response fields. E.g. \"Alerts,SlaTarget\". (optional)
start = '2013-10-20T19:20:30+01:00' # datetime | The start of a custom period (can't be used together with the PresetPeriod parameter) (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | The end of a custom period (optional)
preset_period = 'Last24Hours' # str | The requested time period. (optional) (default to Last24Hours)

try:
    # Gets the monitor statistics.
    api_response = api_instance.statistics_get_monitor_statistics(monitor_guid, filter=filter, start=start, end=end, preset_period=preset_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->statistics_get_monitor_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_guid** | **str**| The Guid of the monitor. | 
 **filter** | **str**| The filter for the requested response fields. E.g. \&quot;Alerts,SlaTarget\&quot;. | [optional] 
 **start** | **datetime**| The start of a custom period (can&#39;t be used together with the PresetPeriod parameter) | [optional] 
 **end** | **datetime**| The end of a custom period | [optional] 
 **preset_period** | **str**| The requested time period. | [optional] [default to Last24Hours]

### Return type

[**StatisticsResponse**](StatisticsResponse.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

