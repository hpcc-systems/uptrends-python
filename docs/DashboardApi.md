# uptrends.DashboardApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboard_clone_dashboard**](DashboardApi.md#dashboard_clone_dashboard) | **POST** /Dashboard/{dashboardGuid}/Clone | Clone the specified dashboard.
[**dashboard_delete_dashboard**](DashboardApi.md#dashboard_delete_dashboard) | **DELETE** /Dashboard/{dashboardGuid} | Delete the specified dashboard.
[**dashboard_get_all_dashboards**](DashboardApi.md#dashboard_get_all_dashboards) | **GET** /Dashboard | Returns data for all dashboards.
[**dashboard_get_one_dashboard**](DashboardApi.md#dashboard_get_one_dashboard) | **GET** /Dashboard/{dashboardGuid} | Returns data for the specified dashboard.
[**dashboard_partially_update_dashboard**](DashboardApi.md#dashboard_partially_update_dashboard) | **PATCH** /Dashboard/{dashboardGuid} | Partially update the specified dashboard.
[**dashboard_update_dashboard**](DashboardApi.md#dashboard_update_dashboard) | **PUT** /Dashboard/{dashboardGuid} | Update the specified dashboard.


# **dashboard_clone_dashboard**
> Dashboard dashboard_clone_dashboard(dashboard_guid)

Clone the specified dashboard.

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
api_instance = uptrends.DashboardApi(uptrends.ApiClient(configuration))
dashboard_guid = 'dashboard_guid_example' # str | The guid of the specified dashboard.

try:
    # Clone the specified dashboard.
    api_response = api_instance.dashboard_clone_dashboard(dashboard_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_clone_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_guid** | **str**| The guid of the specified dashboard. | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_delete_dashboard**
> dashboard_delete_dashboard(dashboard_guid)

Delete the specified dashboard.

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
api_instance = uptrends.DashboardApi(uptrends.ApiClient(configuration))
dashboard_guid = 'dashboard_guid_example' # str | The guid of the specified dashboard.

try:
    # Delete the specified dashboard.
    api_instance.dashboard_delete_dashboard(dashboard_guid)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_delete_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_guid** | **str**| The guid of the specified dashboard. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_get_all_dashboards**
> list[Dashboard] dashboard_get_all_dashboards()

Returns data for all dashboards.

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
api_instance = uptrends.DashboardApi(uptrends.ApiClient(configuration))

try:
    # Returns data for all dashboards.
    api_response = api_instance.dashboard_get_all_dashboards()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_get_all_dashboards: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Dashboard]**](Dashboard.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_get_one_dashboard**
> Dashboard dashboard_get_one_dashboard(dashboard_guid)

Returns data for the specified dashboard.

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
api_instance = uptrends.DashboardApi(uptrends.ApiClient(configuration))
dashboard_guid = 'dashboard_guid_example' # str | The guid of the specified dashboard.

try:
    # Returns data for the specified dashboard.
    api_response = api_instance.dashboard_get_one_dashboard(dashboard_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_get_one_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_guid** | **str**| The guid of the specified dashboard. | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_partially_update_dashboard**
> dashboard_partially_update_dashboard(dashboard_guid, dashboard)

Partially update the specified dashboard.

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
api_instance = uptrends.DashboardApi(uptrends.ApiClient(configuration))
dashboard_guid = 'dashboard_guid_example' # str | The guid of the specified dashboard.
dashboard = uptrends.Dashboard() # Dashboard | The details for the dashboard.

try:
    # Partially update the specified dashboard.
    api_instance.dashboard_partially_update_dashboard(dashboard_guid, dashboard)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_partially_update_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_guid** | **str**| The guid of the specified dashboard. | 
 **dashboard** | [**Dashboard**](Dashboard.md)| The details for the dashboard. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_update_dashboard**
> dashboard_update_dashboard(dashboard_guid, dashboard)

Update the specified dashboard.

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
api_instance = uptrends.DashboardApi(uptrends.ApiClient(configuration))
dashboard_guid = 'dashboard_guid_example' # str | The guid of the specified dashboard.
dashboard = uptrends.Dashboard() # Dashboard | The details for the dashboard.

try:
    # Update the specified dashboard.
    api_instance.dashboard_update_dashboard(dashboard_guid, dashboard)
except ApiException as e:
    print("Exception when calling DashboardApi->dashboard_update_dashboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_guid** | **str**| The guid of the specified dashboard. | 
 **dashboard** | [**Dashboard**](Dashboard.md)| The details for the dashboard. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

