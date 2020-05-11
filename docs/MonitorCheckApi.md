# uptrends.MonitorCheckApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**monitor_check_get_account_monitor_checks**](MonitorCheckApi.md#monitor_check_get_account_monitor_checks) | **GET** /MonitorCheck | Returns all monitor check data.
[**monitor_check_get_http_details**](MonitorCheckApi.md#monitor_check_get_http_details) | **GET** /MonitorCheck/{monitorCheckId}/Http | Returns HTTP details for a monitor check.
[**monitor_check_get_monitor_check**](MonitorCheckApi.md#monitor_check_get_monitor_check) | **GET** /MonitorCheck/Monitor/{monitorGuid} | Returns monitor check data for a specific monitor.
[**monitor_check_get_monitor_group_data**](MonitorCheckApi.md#monitor_check_get_monitor_group_data) | **GET** /MonitorCheck/MonitorGroup/{monitorGroupGuid} | Returns monitor check data for a specific monitor group.
[**monitor_check_get_multistep_details**](MonitorCheckApi.md#monitor_check_get_multistep_details) | **GET** /MonitorCheck/{monitorCheckId}/MultiStepAPI | Returns Multi-Step API details for a monitor check.
[**monitor_check_get_screenshots**](MonitorCheckApi.md#monitor_check_get_screenshots) | **GET** /MonitorCheck/{monitorCheckId}/Screenshot/{screenshotId} | Gets a specific screenshot for a specified monitor check
[**monitor_check_get_single_monitor_check**](MonitorCheckApi.md#monitor_check_get_single_monitor_check) | **GET** /MonitorCheck/{monitorCheckId} | Returns a single monitor check.
[**monitor_check_get_transaction_details**](MonitorCheckApi.md#monitor_check_get_transaction_details) | **GET** /MonitorCheck/{monitorCheckId}/Transaction | Returns transaction step details for a monitor check.
[**monitor_check_get_waterfall_info**](MonitorCheckApi.md#monitor_check_get_waterfall_info) | **GET** /MonitorCheck/{monitorCheckId}/Waterfall | Returns waterfall information for a monitor check.


# **monitor_check_get_account_monitor_checks**
> MonitorCheckResponse monitor_check_get_account_monitor_checks(error_level=error_level, cursor=cursor, sorting=sorting, take=take, start=start, end=end, preset_period=preset_period)

Returns all monitor check data.

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
api_instance = uptrends.MonitorCheckApi(uptrends.ApiClient(configuration))
error_level = 'error_level_example' # str | Error level filter that should be applied. (default = NoError and above) (optional)
cursor = 'cursor_example' # str | A cursor value that should be used for traversing the dataset. (optional)
sorting = 'Descending' # str | Sorting direction based on timestamp. (optional) (default to Descending)
take = 100 # int | The number of records to return (Max value = 100) (optional) (default to 100)
start = '2013-10-20T19:20:30+01:00' # datetime | The start of a custom period (can't be used together with the PresetPeriod parameter) (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | The end of a custom period (optional)
preset_period = 'Last24Hours' # str | The requested time period. (optional) (default to Last24Hours)

try:
    # Returns all monitor check data.
    api_response = api_instance.monitor_check_get_account_monitor_checks(error_level=error_level, cursor=cursor, sorting=sorting, take=take, start=start, end=end, preset_period=preset_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorCheckApi->monitor_check_get_account_monitor_checks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error_level** | **str**| Error level filter that should be applied. (default &#x3D; NoError and above) | [optional] 
 **cursor** | **str**| A cursor value that should be used for traversing the dataset. | [optional] 
 **sorting** | **str**| Sorting direction based on timestamp. | [optional] [default to Descending]
 **take** | **int**| The number of records to return (Max value &#x3D; 100) | [optional] [default to 100]
 **start** | **datetime**| The start of a custom period (can&#39;t be used together with the PresetPeriod parameter) | [optional] 
 **end** | **datetime**| The end of a custom period | [optional] 
 **preset_period** | **str**| The requested time period. | [optional] [default to Last24Hours]

### Return type

[**MonitorCheckResponse**](MonitorCheckResponse.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_check_get_http_details**
> HttpDetailsResponse monitor_check_get_http_details(monitor_check_id)

Returns HTTP details for a monitor check.

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
api_instance = uptrends.MonitorCheckApi(uptrends.ApiClient(configuration))
monitor_check_id = 789 # int | The monitor check Id to get the detailed data for.

try:
    # Returns HTTP details for a monitor check.
    api_response = api_instance.monitor_check_get_http_details(monitor_check_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorCheckApi->monitor_check_get_http_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_check_id** | **int**| The monitor check Id to get the detailed data for. | 

### Return type

[**HttpDetailsResponse**](HttpDetailsResponse.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_check_get_monitor_check**
> MonitorCheckResponse monitor_check_get_monitor_check(monitor_guid, error_level=error_level, cursor=cursor, sorting=sorting, take=take, start=start, end=end, preset_period=preset_period)

Returns monitor check data for a specific monitor.

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
api_instance = uptrends.MonitorCheckApi(uptrends.ApiClient(configuration))
monitor_guid = 'monitor_guid_example' # str | The Guid of the monitor to get monitor checks for.
error_level = 'error_level_example' # str | Error level filter that should be applied. (default = NoError and above) (optional)
cursor = 'cursor_example' # str | A cursor value that should be used for traversing the dataset. (optional)
sorting = 'Descending' # str | Sorting direction based on timestamp. (optional) (default to Descending)
take = 100 # int | The number of records to return (Max value = 100) (optional) (default to 100)
start = '2013-10-20T19:20:30+01:00' # datetime | The start of a custom period (can't be used together with the PresetPeriod parameter) (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | The end of a custom period (optional)
preset_period = 'Last24Hours' # str | The requested time period. (optional) (default to Last24Hours)

try:
    # Returns monitor check data for a specific monitor.
    api_response = api_instance.monitor_check_get_monitor_check(monitor_guid, error_level=error_level, cursor=cursor, sorting=sorting, take=take, start=start, end=end, preset_period=preset_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorCheckApi->monitor_check_get_monitor_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_guid** | **str**| The Guid of the monitor to get monitor checks for. | 
 **error_level** | **str**| Error level filter that should be applied. (default &#x3D; NoError and above) | [optional] 
 **cursor** | **str**| A cursor value that should be used for traversing the dataset. | [optional] 
 **sorting** | **str**| Sorting direction based on timestamp. | [optional] [default to Descending]
 **take** | **int**| The number of records to return (Max value &#x3D; 100) | [optional] [default to 100]
 **start** | **datetime**| The start of a custom period (can&#39;t be used together with the PresetPeriod parameter) | [optional] 
 **end** | **datetime**| The end of a custom period | [optional] 
 **preset_period** | **str**| The requested time period. | [optional] [default to Last24Hours]

### Return type

[**MonitorCheckResponse**](MonitorCheckResponse.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_check_get_monitor_group_data**
> MonitorCheckResponse monitor_check_get_monitor_group_data(monitor_group_guid, error_level=error_level, cursor=cursor, sorting=sorting, take=take, start=start, end=end, preset_period=preset_period)

Returns monitor check data for a specific monitor group.

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
api_instance = uptrends.MonitorCheckApi(uptrends.ApiClient(configuration))
monitor_group_guid = 'monitor_group_guid_example' # str | The Guid of the monitor group to get monitor checks for.
error_level = 'error_level_example' # str | Error level filter that should be applied. (default = NoError and above) (optional)
cursor = 'cursor_example' # str | A cursor value that should be used for traversing the dataset. (optional)
sorting = 'Descending' # str | Sorting direction based on timestamp. (optional) (default to Descending)
take = 100 # int | The number of records to return (Max value = 100) (optional) (default to 100)
start = '2013-10-20T19:20:30+01:00' # datetime | The start of a custom period (can't be used together with the PresetPeriod parameter) (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | The end of a custom period (optional)
preset_period = 'Last24Hours' # str | The requested time period. (optional) (default to Last24Hours)

try:
    # Returns monitor check data for a specific monitor group.
    api_response = api_instance.monitor_check_get_monitor_group_data(monitor_group_guid, error_level=error_level, cursor=cursor, sorting=sorting, take=take, start=start, end=end, preset_period=preset_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorCheckApi->monitor_check_get_monitor_group_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_group_guid** | **str**| The Guid of the monitor group to get monitor checks for. | 
 **error_level** | **str**| Error level filter that should be applied. (default &#x3D; NoError and above) | [optional] 
 **cursor** | **str**| A cursor value that should be used for traversing the dataset. | [optional] 
 **sorting** | **str**| Sorting direction based on timestamp. | [optional] [default to Descending]
 **take** | **int**| The number of records to return (Max value &#x3D; 100) | [optional] [default to 100]
 **start** | **datetime**| The start of a custom period (can&#39;t be used together with the PresetPeriod parameter) | [optional] 
 **end** | **datetime**| The end of a custom period | [optional] 
 **preset_period** | **str**| The requested time period. | [optional] [default to Last24Hours]

### Return type

[**MonitorCheckResponse**](MonitorCheckResponse.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_check_get_multistep_details**
> MsaDetailsResponse monitor_check_get_multistep_details(monitor_check_id)

Returns Multi-Step API details for a monitor check.

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
api_instance = uptrends.MonitorCheckApi(uptrends.ApiClient(configuration))
monitor_check_id = 789 # int | The monitor check Id to get the detailed data for.

try:
    # Returns Multi-Step API details for a monitor check.
    api_response = api_instance.monitor_check_get_multistep_details(monitor_check_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorCheckApi->monitor_check_get_multistep_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_check_id** | **int**| The monitor check Id to get the detailed data for. | 

### Return type

[**MsaDetailsResponse**](MsaDetailsResponse.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_check_get_screenshots**
> ScreenshotResponse monitor_check_get_screenshots(monitor_check_id, screenshot_id)

Gets a specific screenshot for a specified monitor check

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
api_instance = uptrends.MonitorCheckApi(uptrends.ApiClient(configuration))
monitor_check_id = 789 # int | The monitor check Id to get the screenshot data for.
screenshot_id = 'screenshot_id_example' # str | The screenshot Id of the screenshot to get.

try:
    # Gets a specific screenshot for a specified monitor check
    api_response = api_instance.monitor_check_get_screenshots(monitor_check_id, screenshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorCheckApi->monitor_check_get_screenshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_check_id** | **int**| The monitor check Id to get the screenshot data for. | 
 **screenshot_id** | **str**| The screenshot Id of the screenshot to get. | 

### Return type

[**ScreenshotResponse**](ScreenshotResponse.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_check_get_single_monitor_check**
> SingleMonitorCheckResponse monitor_check_get_single_monitor_check(monitor_check_id)

Returns a single monitor check.

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
api_instance = uptrends.MonitorCheckApi(uptrends.ApiClient(configuration))
monitor_check_id = 789 # int | The Id of the monitor check to get the data for.

try:
    # Returns a single monitor check.
    api_response = api_instance.monitor_check_get_single_monitor_check(monitor_check_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorCheckApi->monitor_check_get_single_monitor_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_check_id** | **int**| The Id of the monitor check to get the data for. | 

### Return type

[**SingleMonitorCheckResponse**](SingleMonitorCheckResponse.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_check_get_transaction_details**
> TransactionDetailsResponse monitor_check_get_transaction_details(monitor_check_id)

Returns transaction step details for a monitor check.

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
api_instance = uptrends.MonitorCheckApi(uptrends.ApiClient(configuration))
monitor_check_id = 789 # int | The monitor check Id to get the detailed data for.

try:
    # Returns transaction step details for a monitor check.
    api_response = api_instance.monitor_check_get_transaction_details(monitor_check_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorCheckApi->monitor_check_get_transaction_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_check_id** | **int**| The monitor check Id to get the detailed data for. | 

### Return type

[**TransactionDetailsResponse**](TransactionDetailsResponse.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_check_get_waterfall_info**
> WaterfallResponse monitor_check_get_waterfall_info(monitor_check_id, step=step)

Returns waterfall information for a monitor check.

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
api_instance = uptrends.MonitorCheckApi(uptrends.ApiClient(configuration))
monitor_check_id = 789 # int | The monitor check Id to get the detailed data for.
step = 56 # int | For transaction waterfalls only: the transaction step to get the waterfall for. (optional)

try:
    # Returns waterfall information for a monitor check.
    api_response = api_instance.monitor_check_get_waterfall_info(monitor_check_id, step=step)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorCheckApi->monitor_check_get_waterfall_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_check_id** | **int**| The monitor check Id to get the detailed data for. | 
 **step** | **int**| For transaction waterfalls only: the transaction step to get the waterfall for. | [optional] 

### Return type

[**WaterfallResponse**](WaterfallResponse.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

