# uptrends.MonitorApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**monitor_cleanup_maintenance_periods**](MonitorApi.md#monitor_cleanup_maintenance_periods) | **POST** /Monitor/{monitorGuid}/MaintenancePeriod/Cleanup/{beforeDate} | Clears out all one-time maintenance periods for the specified monitor older than the specified date
[**monitor_clone_monitor**](MonitorApi.md#monitor_clone_monitor) | **POST** /Monitor/{monitorGuid}/Clone | Creates a clone (duplicate) of the specified monitor.
[**monitor_create_maintenance_period_for_monitor**](MonitorApi.md#monitor_create_maintenance_period_for_monitor) | **POST** /Monitor/{monitorGuid}/MaintenancePeriod | Saves the new maintenance period provided for the specified monitor
[**monitor_delete_maintenance_period_from_monitor**](MonitorApi.md#monitor_delete_maintenance_period_from_monitor) | **DELETE** /Monitor/{monitorGuid}/MaintenancePeriod/{maintenancePeriodId} | Deletes the specified maintenance period from the specified monitor
[**monitor_delete_monitor**](MonitorApi.md#monitor_delete_monitor) | **DELETE** /Monitor/{monitorGuid} | Deletes the specified monitor.
[**monitor_get_all_maintenance_periods_for_monitor**](MonitorApi.md#monitor_get_all_maintenance_periods_for_monitor) | **GET** /Monitor/{monitorGuid}/MaintenancePeriod | Finds all maintenance periods for a monitor.
[**monitor_get_monitor**](MonitorApi.md#monitor_get_monitor) | **GET** /Monitor/{monitorGuid} | Returns the definition of the specified monitor. 
[**monitor_get_monitors**](MonitorApi.md#monitor_get_monitors) | **GET** /Monitor | Returns the definition of all monitors available in the account.
[**monitor_patch_monitor**](MonitorApi.md#monitor_patch_monitor) | **PATCH** /Monitor/{monitorGuid} | Partially updates the definition of the specified monitor.
[**monitor_post_monitor**](MonitorApi.md#monitor_post_monitor) | **POST** /Monitor | Creates a new monitor.
[**monitor_put_monitor**](MonitorApi.md#monitor_put_monitor) | **PUT** /Monitor/{monitorGuid} | Updates the definition of the specified monitor.
[**monitor_update_maintenance_period_for_monitor**](MonitorApi.md#monitor_update_maintenance_period_for_monitor) | **PUT** /Monitor/{monitorGuid}/MaintenancePeriod/{maintenancePeriodId} | Updates the specified maintenance schedule for the specified monitor


# **monitor_cleanup_maintenance_periods**
> monitor_cleanup_maintenance_periods(monitor_guid, before_date)

Clears out all one-time maintenance periods for the specified monitor older than the specified date

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
api_instance = uptrends.MonitorApi(uptrends.ApiClient(configuration))
monitor_guid = 'monitor_guid_example' # str | 
before_date = '2013-10-20T19:20:30+01:00' # datetime | A string representing the date, formatted as \"yyyy-MM-dd\"

try:
    # Clears out all one-time maintenance periods for the specified monitor older than the specified date
    api_instance.monitor_cleanup_maintenance_periods(monitor_guid, before_date)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_cleanup_maintenance_periods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_guid** | **str**|  | 
 **before_date** | **datetime**| A string representing the date, formatted as \&quot;yyyy-MM-dd\&quot; | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_clone_monitor**
> Monitor monitor_clone_monitor(monitor_guid, include_maintenance_periods=include_maintenance_periods, include_monitor_groups=include_monitor_groups)

Creates a clone (duplicate) of the specified monitor.

Upon creation, the new monitor will be inactive. This allows you to make the necessary changes before you activate it. All other settings will be transferred to the new monitor as-is.

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
api_instance = uptrends.MonitorApi(uptrends.ApiClient(configuration))
monitor_guid = 'monitor_guid_example' # str | The guid of the monitor you want to clone.
include_maintenance_periods = true # bool | Whether or not to also copy the maintenance periods into the clone. (optional) (default to true)
include_monitor_groups = true # bool | Whether or not to also copy the monitor group memberships into the clone. (optional) (default to true)

try:
    # Creates a clone (duplicate) of the specified monitor.
    api_response = api_instance.monitor_clone_monitor(monitor_guid, include_maintenance_periods=include_maintenance_periods, include_monitor_groups=include_monitor_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_clone_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_guid** | **str**| The guid of the monitor you want to clone. | 
 **include_maintenance_periods** | **bool**| Whether or not to also copy the maintenance periods into the clone. | [optional] [default to true]
 **include_monitor_groups** | **bool**| Whether or not to also copy the monitor group memberships into the clone. | [optional] [default to true]

### Return type

[**Monitor**](Monitor.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_create_maintenance_period_for_monitor**
> MaintenancePeriod monitor_create_maintenance_period_for_monitor(maintenance_period, monitor_guid)

Saves the new maintenance period provided for the specified monitor

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
api_instance = uptrends.MonitorApi(uptrends.ApiClient(configuration))
maintenance_period = uptrends.MaintenancePeriod() # MaintenancePeriod | 
monitor_guid = 'monitor_guid_example' # str | 

try:
    # Saves the new maintenance period provided for the specified monitor
    api_response = api_instance.monitor_create_maintenance_period_for_monitor(maintenance_period, monitor_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_create_maintenance_period_for_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintenance_period** | [**MaintenancePeriod**](MaintenancePeriod.md)|  | 
 **monitor_guid** | **str**|  | 

### Return type

[**MaintenancePeriod**](MaintenancePeriod.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_delete_maintenance_period_from_monitor**
> monitor_delete_maintenance_period_from_monitor(monitor_guid, maintenance_period_id)

Deletes the specified maintenance period from the specified monitor

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
api_instance = uptrends.MonitorApi(uptrends.ApiClient(configuration))
monitor_guid = 'monitor_guid_example' # str | 
maintenance_period_id = 56 # int | 

try:
    # Deletes the specified maintenance period from the specified monitor
    api_instance.monitor_delete_maintenance_period_from_monitor(monitor_guid, maintenance_period_id)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_delete_maintenance_period_from_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_guid** | **str**|  | 
 **maintenance_period_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_delete_monitor**
> monitor_delete_monitor(monitor_guid)

Deletes the specified monitor.

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
api_instance = uptrends.MonitorApi(uptrends.ApiClient(configuration))
monitor_guid = 'monitor_guid_example' # str | The guid of the monitor you want to delete.

try:
    # Deletes the specified monitor.
    api_instance.monitor_delete_monitor(monitor_guid)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_delete_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_guid** | **str**| The guid of the monitor you want to delete. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_get_all_maintenance_periods_for_monitor**
> list[MaintenancePeriod] monitor_get_all_maintenance_periods_for_monitor(monitor_guid)

Finds all maintenance periods for a monitor.

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
api_instance = uptrends.MonitorApi(uptrends.ApiClient(configuration))
monitor_guid = 'monitor_guid_example' # str | The guid of the monitor you want to find the maintenance periods of.

try:
    # Finds all maintenance periods for a monitor.
    api_response = api_instance.monitor_get_all_maintenance_periods_for_monitor(monitor_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_get_all_maintenance_periods_for_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_guid** | **str**| The guid of the monitor you want to find the maintenance periods of. | 

### Return type

[**list[MaintenancePeriod]**](MaintenancePeriod.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_get_monitor**
> Monitor monitor_get_monitor(monitor_guid, filter=filter)

Returns the definition of the specified monitor. 

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
api_instance = uptrends.MonitorApi(uptrends.ApiClient(configuration))
monitor_guid = 'monitor_guid_example' # str | The Guid of the requested monitor.
filter = 'filter_example' # str | Provide the option to only retrieve the requested fields. E.g. \"Name,IsActive\". (optional)

try:
    # Returns the definition of the specified monitor. 
    api_response = api_instance.monitor_get_monitor(monitor_guid, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_get_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_guid** | **str**| The Guid of the requested monitor. | 
 **filter** | **str**| Provide the option to only retrieve the requested fields. E.g. \&quot;Name,IsActive\&quot;. | [optional] 

### Return type

[**Monitor**](Monitor.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_get_monitors**
> list[Monitor] monitor_get_monitors(filter=filter)

Returns the definition of all monitors available in the account.

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
api_instance = uptrends.MonitorApi(uptrends.ApiClient(configuration))
filter = 'filter_example' # str | Provide the option to only retrieve the requested fields. E.g. \"Name,IsActive\". (optional)

try:
    # Returns the definition of all monitors available in the account.
    api_response = api_instance.monitor_get_monitors(filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_get_monitors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Provide the option to only retrieve the requested fields. E.g. \&quot;Name,IsActive\&quot;. | [optional] 

### Return type

[**list[Monitor]**](Monitor.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_patch_monitor**
> monitor_patch_monitor(monitor, monitor_guid)

Partially updates the definition of the specified monitor.

This methods accepts parts of a monitor definition. We recommend retrieving the existing definition first (using the GET method). You can then process the changes you want to make and send back these changes only using this PATCH method.

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
api_instance = uptrends.MonitorApi(uptrends.ApiClient(configuration))
monitor = uptrends.Monitor() # Monitor | The partial definition for the monitor that should be updated.
monitor_guid = 'monitor_guid_example' # str | The Guid of the monitor that should be updated.

try:
    # Partially updates the definition of the specified monitor.
    api_instance.monitor_patch_monitor(monitor, monitor_guid)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_patch_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor** | [**Monitor**](Monitor.md)| The partial definition for the monitor that should be updated. | 
 **monitor_guid** | **str**| The Guid of the monitor that should be updated. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_post_monitor**
> Monitor monitor_post_monitor(monitor)

Creates a new monitor.

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
api_instance = uptrends.MonitorApi(uptrends.ApiClient(configuration))
monitor = uptrends.Monitor() # Monitor | The complete definition of the monitor that should be created.

try:
    # Creates a new monitor.
    api_response = api_instance.monitor_post_monitor(monitor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_post_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor** | [**Monitor**](Monitor.md)| The complete definition of the monitor that should be created. | 

### Return type

[**Monitor**](Monitor.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_put_monitor**
> monitor_put_monitor(monitor, monitor_guid)

Updates the definition of the specified monitor.

This methods only accepts a complete monitor definition. We recommend retrieving the existing definition first (using the GET method). You can then process the changes you want to make and send back the updated definition using this PUT method.

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
api_instance = uptrends.MonitorApi(uptrends.ApiClient(configuration))
monitor = uptrends.Monitor() # Monitor | The complete definition for the monitor that should be updated.
monitor_guid = 'monitor_guid_example' # str | The Guid of the monitor that should be updated.

try:
    # Updates the definition of the specified monitor.
    api_instance.monitor_put_monitor(monitor, monitor_guid)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_put_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor** | [**Monitor**](Monitor.md)| The complete definition for the monitor that should be updated. | 
 **monitor_guid** | **str**| The Guid of the monitor that should be updated. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_update_maintenance_period_for_monitor**
> monitor_update_maintenance_period_for_monitor(monitor_guid, maintenance_period_id, maintenance_period)

Updates the specified maintenance schedule for the specified monitor

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
api_instance = uptrends.MonitorApi(uptrends.ApiClient(configuration))
monitor_guid = 'monitor_guid_example' # str | 
maintenance_period_id = 56 # int | 
maintenance_period = uptrends.MaintenancePeriod() # MaintenancePeriod | 

try:
    # Updates the specified maintenance schedule for the specified monitor
    api_instance.monitor_update_maintenance_period_for_monitor(monitor_guid, maintenance_period_id, maintenance_period)
except ApiException as e:
    print("Exception when calling MonitorApi->monitor_update_maintenance_period_for_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_guid** | **str**|  | 
 **maintenance_period_id** | **int**|  | 
 **maintenance_period** | [**MaintenancePeriod**](MaintenancePeriod.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

