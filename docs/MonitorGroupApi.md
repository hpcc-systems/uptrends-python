# uptrends.MonitorGroupApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**monitor_group_add_maintenance_period_to_all_members**](MonitorGroupApi.md#monitor_group_add_maintenance_period_to_all_members) | **POST** /MonitorGroup/{monitorGroupGuid}/AddMaintenancePeriodToAllMembers | Adds the provided maintenance period to all monitors in the group specified 
[**monitor_group_add_monitor_to_monitor_group**](MonitorGroupApi.md#monitor_group_add_monitor_to_monitor_group) | **POST** /MonitorGroup/{monitorGroupGuid}/Members/{monitorGuid} | Adds the specified monitor to the monitor group 
[**monitor_group_create_monitor_group**](MonitorGroupApi.md#monitor_group_create_monitor_group) | **POST** /MonitorGroup | Creates a new monitor group
[**monitor_group_delete_monitor_group**](MonitorGroupApi.md#monitor_group_delete_monitor_group) | **DELETE** /MonitorGroup/{monitorGroupGuid} | Deletes the specified monitor group
[**monitor_group_get_all_monitor_groups**](MonitorGroupApi.md#monitor_group_get_all_monitor_groups) | **GET** /MonitorGroup | Gets all monitor groups
[**monitor_group_get_monitor_group**](MonitorGroupApi.md#monitor_group_get_monitor_group) | **GET** /MonitorGroup/{monitorGroupGuid} | Gets the details of a monitor group
[**monitor_group_get_monitor_group_members**](MonitorGroupApi.md#monitor_group_get_monitor_group_members) | **GET** /MonitorGroup/{monitorGroupGuid}/Members | Gets a list of all members of a monitor group
[**monitor_group_remove_monitor_from_monitor_group**](MonitorGroupApi.md#monitor_group_remove_monitor_from_monitor_group) | **DELETE** /MonitorGroup/{monitorGroupGuid}/Members/{monitorGuid} | Removes the specified monitor from the monitor group
[**monitor_group_start_all_monitor_alerts_in_group**](MonitorGroupApi.md#monitor_group_start_all_monitor_alerts_in_group) | **POST** /MonitorGroup/{monitorGroupGuid}/StartAllMonitorAlerts | Starts alerting for all monitors that are a member of the monitor group specified by the monitor group GUID
[**monitor_group_start_all_monitors_in_group**](MonitorGroupApi.md#monitor_group_start_all_monitors_in_group) | **POST** /MonitorGroup/{monitorGroupGuid}/StartAllMonitors | Starts all monitors that are a member of the monitor group specified by the monitor group GUID
[**monitor_group_stop_all_monitor_alerts_in_group**](MonitorGroupApi.md#monitor_group_stop_all_monitor_alerts_in_group) | **POST** /MonitorGroup/{monitorGroupGuid}/StopAllMonitorAlerts | Stops alerting for all monitors that are a member of the monitor group specified by the monitor group GUID
[**monitor_group_stop_all_monitors_in_group**](MonitorGroupApi.md#monitor_group_stop_all_monitors_in_group) | **POST** /MonitorGroup/{monitorGroupGuid}/StopAllMonitors | Stops all monitors that are a member of the monitor group specified by the monitor group GUID
[**monitor_group_update_monitor_group**](MonitorGroupApi.md#monitor_group_update_monitor_group) | **PUT** /MonitorGroup/{monitorGroupGuid} | Updates the monitor group with the Guid specified


# **monitor_group_add_maintenance_period_to_all_members**
> monitor_group_add_maintenance_period_to_all_members(monitor_group_guid, maintenance_period)

Adds the provided maintenance period to all monitors in the group specified 

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
api_instance = uptrends.MonitorGroupApi(uptrends.ApiClient(configuration))
monitor_group_guid = 'monitor_group_guid_example' # str | 
maintenance_period = uptrends.MaintenancePeriod() # MaintenancePeriod | 

try:
    # Adds the provided maintenance period to all monitors in the group specified 
    api_instance.monitor_group_add_maintenance_period_to_all_members(monitor_group_guid, maintenance_period)
except ApiException as e:
    print("Exception when calling MonitorGroupApi->monitor_group_add_maintenance_period_to_all_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_group_guid** | **str**|  | 
 **maintenance_period** | [**MaintenancePeriod**](MaintenancePeriod.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_group_add_monitor_to_monitor_group**
> monitor_group_add_monitor_to_monitor_group(monitor_group_guid, monitor_guid)

Adds the specified monitor to the monitor group 

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
api_instance = uptrends.MonitorGroupApi(uptrends.ApiClient(configuration))
monitor_group_guid = 'monitor_group_guid_example' # str | The Guid of the monitor group to add the monitor to
monitor_guid = 'monitor_guid_example' # str | The monitor Guid

try:
    # Adds the specified monitor to the monitor group 
    api_instance.monitor_group_add_monitor_to_monitor_group(monitor_group_guid, monitor_guid)
except ApiException as e:
    print("Exception when calling MonitorGroupApi->monitor_group_add_monitor_to_monitor_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_group_guid** | **str**| The Guid of the monitor group to add the monitor to | 
 **monitor_guid** | **str**| The monitor Guid | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_group_create_monitor_group**
> MonitorGroup monitor_group_create_monitor_group(monitor_group)

Creates a new monitor group

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
api_instance = uptrends.MonitorGroupApi(uptrends.ApiClient(configuration))
monitor_group = uptrends.MonitorGroup() # MonitorGroup | The MonitorGroup object to be created

try:
    # Creates a new monitor group
    api_response = api_instance.monitor_group_create_monitor_group(monitor_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorGroupApi->monitor_group_create_monitor_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_group** | [**MonitorGroup**](MonitorGroup.md)| The MonitorGroup object to be created | 

### Return type

[**MonitorGroup**](MonitorGroup.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_group_delete_monitor_group**
> monitor_group_delete_monitor_group(monitor_group_guid)

Deletes the specified monitor group

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
api_instance = uptrends.MonitorGroupApi(uptrends.ApiClient(configuration))
monitor_group_guid = 'monitor_group_guid_example' # str | The Guid of the monitor group to be deleted

try:
    # Deletes the specified monitor group
    api_instance.monitor_group_delete_monitor_group(monitor_group_guid)
except ApiException as e:
    print("Exception when calling MonitorGroupApi->monitor_group_delete_monitor_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_group_guid** | **str**| The Guid of the monitor group to be deleted | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_group_get_all_monitor_groups**
> list[MonitorGroup] monitor_group_get_all_monitor_groups()

Gets all monitor groups

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
api_instance = uptrends.MonitorGroupApi(uptrends.ApiClient(configuration))

try:
    # Gets all monitor groups
    api_response = api_instance.monitor_group_get_all_monitor_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorGroupApi->monitor_group_get_all_monitor_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MonitorGroup]**](MonitorGroup.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_group_get_monitor_group**
> MonitorGroup monitor_group_get_monitor_group(monitor_group_guid)

Gets the details of a monitor group

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
api_instance = uptrends.MonitorGroupApi(uptrends.ApiClient(configuration))
monitor_group_guid = 'monitor_group_guid_example' # str | The Guid of the monitor group to be retrieved

try:
    # Gets the details of a monitor group
    api_response = api_instance.monitor_group_get_monitor_group(monitor_group_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorGroupApi->monitor_group_get_monitor_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_group_guid** | **str**| The Guid of the monitor group to be retrieved | 

### Return type

[**MonitorGroup**](MonitorGroup.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_group_get_monitor_group_members**
> MonitorGroupMember monitor_group_get_monitor_group_members(monitor_group_guid)

Gets a list of all members of a monitor group

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
api_instance = uptrends.MonitorGroupApi(uptrends.ApiClient(configuration))
monitor_group_guid = 'monitor_group_guid_example' # str | The Guid of the monitor group to retrieve the members for

try:
    # Gets a list of all members of a monitor group
    api_response = api_instance.monitor_group_get_monitor_group_members(monitor_group_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitorGroupApi->monitor_group_get_monitor_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_group_guid** | **str**| The Guid of the monitor group to retrieve the members for | 

### Return type

[**MonitorGroupMember**](MonitorGroupMember.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_group_remove_monitor_from_monitor_group**
> monitor_group_remove_monitor_from_monitor_group(monitor_group_guid, monitor_guid)

Removes the specified monitor from the monitor group

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
api_instance = uptrends.MonitorGroupApi(uptrends.ApiClient(configuration))
monitor_group_guid = 'monitor_group_guid_example' # str | The Guid of the monitor group to remove the monitor from
monitor_guid = 'monitor_guid_example' # str | The monitor Guid to be removed

try:
    # Removes the specified monitor from the monitor group
    api_instance.monitor_group_remove_monitor_from_monitor_group(monitor_group_guid, monitor_guid)
except ApiException as e:
    print("Exception when calling MonitorGroupApi->monitor_group_remove_monitor_from_monitor_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_group_guid** | **str**| The Guid of the monitor group to remove the monitor from | 
 **monitor_guid** | **str**| The monitor Guid to be removed | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_group_start_all_monitor_alerts_in_group**
> monitor_group_start_all_monitor_alerts_in_group(monitor_group_guid)

Starts alerting for all monitors that are a member of the monitor group specified by the monitor group GUID

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
api_instance = uptrends.MonitorGroupApi(uptrends.ApiClient(configuration))
monitor_group_guid = 'monitor_group_guid_example' # str | The monitor group GUID

try:
    # Starts alerting for all monitors that are a member of the monitor group specified by the monitor group GUID
    api_instance.monitor_group_start_all_monitor_alerts_in_group(monitor_group_guid)
except ApiException as e:
    print("Exception when calling MonitorGroupApi->monitor_group_start_all_monitor_alerts_in_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_group_guid** | **str**| The monitor group GUID | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_group_start_all_monitors_in_group**
> monitor_group_start_all_monitors_in_group(monitor_group_guid)

Starts all monitors that are a member of the monitor group specified by the monitor group GUID

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
api_instance = uptrends.MonitorGroupApi(uptrends.ApiClient(configuration))
monitor_group_guid = 'monitor_group_guid_example' # str | The monitor group GUID

try:
    # Starts all monitors that are a member of the monitor group specified by the monitor group GUID
    api_instance.monitor_group_start_all_monitors_in_group(monitor_group_guid)
except ApiException as e:
    print("Exception when calling MonitorGroupApi->monitor_group_start_all_monitors_in_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_group_guid** | **str**| The monitor group GUID | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_group_stop_all_monitor_alerts_in_group**
> monitor_group_stop_all_monitor_alerts_in_group(monitor_group_guid)

Stops alerting for all monitors that are a member of the monitor group specified by the monitor group GUID

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
api_instance = uptrends.MonitorGroupApi(uptrends.ApiClient(configuration))
monitor_group_guid = 'monitor_group_guid_example' # str | The monitor group GUID

try:
    # Stops alerting for all monitors that are a member of the monitor group specified by the monitor group GUID
    api_instance.monitor_group_stop_all_monitor_alerts_in_group(monitor_group_guid)
except ApiException as e:
    print("Exception when calling MonitorGroupApi->monitor_group_stop_all_monitor_alerts_in_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_group_guid** | **str**| The monitor group GUID | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_group_stop_all_monitors_in_group**
> monitor_group_stop_all_monitors_in_group(monitor_group_guid)

Stops all monitors that are a member of the monitor group specified by the monitor group GUID

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
api_instance = uptrends.MonitorGroupApi(uptrends.ApiClient(configuration))
monitor_group_guid = 'monitor_group_guid_example' # str | The monitor group GUID

try:
    # Stops all monitors that are a member of the monitor group specified by the monitor group GUID
    api_instance.monitor_group_stop_all_monitors_in_group(monitor_group_guid)
except ApiException as e:
    print("Exception when calling MonitorGroupApi->monitor_group_stop_all_monitors_in_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_group_guid** | **str**| The monitor group GUID | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_group_update_monitor_group**
> monitor_group_update_monitor_group(item, monitor_group_guid)

Updates the monitor group with the Guid specified

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
api_instance = uptrends.MonitorGroupApi(uptrends.ApiClient(configuration))
item = uptrends.MonitorGroup() # MonitorGroup | The monitor group to be updated
monitor_group_guid = 'monitor_group_guid_example' # str | The Guid of the monitor group to be updated

try:
    # Updates the monitor group with the Guid specified
    api_instance.monitor_group_update_monitor_group(item, monitor_group_guid)
except ApiException as e:
    print("Exception when calling MonitorGroupApi->monitor_group_update_monitor_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item** | [**MonitorGroup**](MonitorGroup.md)| The monitor group to be updated | 
 **monitor_group_guid** | **str**| The Guid of the monitor group to be updated | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

