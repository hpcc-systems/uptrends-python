# uptrends.ScheduledReportApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scheduled_report_create_scheduled_report**](ScheduledReportApi.md#scheduled_report_create_scheduled_report) | **POST** /ScheduledReport | Creates a new scheduled report.
[**scheduled_report_delete_specified_scheduled_report**](ScheduledReportApi.md#scheduled_report_delete_specified_scheduled_report) | **DELETE** /ScheduledReport/{scheduledReportGuid} | Delete the specified scheduled report.
[**scheduled_report_get_all_scheduled_reports**](ScheduledReportApi.md#scheduled_report_get_all_scheduled_reports) | **GET** /ScheduledReport | Returns data for all scheduled reports.
[**scheduled_report_get_specified_scheduled_report**](ScheduledReportApi.md#scheduled_report_get_specified_scheduled_report) | **GET** /ScheduledReport/{scheduledReportGuid} | Returns data for the specified scheduled report.
[**scheduled_report_partially_update_scheduled_report**](ScheduledReportApi.md#scheduled_report_partially_update_scheduled_report) | **PATCH** /ScheduledReport/{scheduledReportGuid} | Partially update the specified scheduled report.
[**scheduled_report_update_scheduled_report**](ScheduledReportApi.md#scheduled_report_update_scheduled_report) | **PUT** /ScheduledReport/{scheduledReportGuid} | Update the specified scheduled report.


# **scheduled_report_create_scheduled_report**
> ScheduledReport scheduled_report_create_scheduled_report(scheduled_report)

Creates a new scheduled report.

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
api_instance = uptrends.ScheduledReportApi(uptrends.ApiClient(configuration))
scheduled_report = uptrends.ScheduledReport() # ScheduledReport | The details for the scheduled report.

try:
    # Creates a new scheduled report.
    api_response = api_instance.scheduled_report_create_scheduled_report(scheduled_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledReportApi->scheduled_report_create_scheduled_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_report** | [**ScheduledReport**](ScheduledReport.md)| The details for the scheduled report. | 

### Return type

[**ScheduledReport**](ScheduledReport.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_report_delete_specified_scheduled_report**
> scheduled_report_delete_specified_scheduled_report(scheduled_report_guid)

Delete the specified scheduled report.

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
api_instance = uptrends.ScheduledReportApi(uptrends.ApiClient(configuration))
scheduled_report_guid = 'scheduled_report_guid_example' # str | The guid of the specified scheduled report.

try:
    # Delete the specified scheduled report.
    api_instance.scheduled_report_delete_specified_scheduled_report(scheduled_report_guid)
except ApiException as e:
    print("Exception when calling ScheduledReportApi->scheduled_report_delete_specified_scheduled_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_report_guid** | **str**| The guid of the specified scheduled report. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_report_get_all_scheduled_reports**
> list[ScheduledReport] scheduled_report_get_all_scheduled_reports()

Returns data for all scheduled reports.

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
api_instance = uptrends.ScheduledReportApi(uptrends.ApiClient(configuration))

try:
    # Returns data for all scheduled reports.
    api_response = api_instance.scheduled_report_get_all_scheduled_reports()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledReportApi->scheduled_report_get_all_scheduled_reports: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ScheduledReport]**](ScheduledReport.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_report_get_specified_scheduled_report**
> ScheduledReport scheduled_report_get_specified_scheduled_report(scheduled_report_guid)

Returns data for the specified scheduled report.

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
api_instance = uptrends.ScheduledReportApi(uptrends.ApiClient(configuration))
scheduled_report_guid = 'scheduled_report_guid_example' # str | The guid of the specified scheduled report.

try:
    # Returns data for the specified scheduled report.
    api_response = api_instance.scheduled_report_get_specified_scheduled_report(scheduled_report_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledReportApi->scheduled_report_get_specified_scheduled_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_report_guid** | **str**| The guid of the specified scheduled report. | 

### Return type

[**ScheduledReport**](ScheduledReport.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_report_partially_update_scheduled_report**
> ScheduledReport scheduled_report_partially_update_scheduled_report(scheduled_report_guid, scheduled_report)

Partially update the specified scheduled report.

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
api_instance = uptrends.ScheduledReportApi(uptrends.ApiClient(configuration))
scheduled_report_guid = 'scheduled_report_guid_example' # str | The guid of the specified scheduled report.
scheduled_report = uptrends.ScheduledReport() # ScheduledReport | The details for the scheduled report.

try:
    # Partially update the specified scheduled report.
    api_response = api_instance.scheduled_report_partially_update_scheduled_report(scheduled_report_guid, scheduled_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledReportApi->scheduled_report_partially_update_scheduled_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_report_guid** | **str**| The guid of the specified scheduled report. | 
 **scheduled_report** | [**ScheduledReport**](ScheduledReport.md)| The details for the scheduled report. | 

### Return type

[**ScheduledReport**](ScheduledReport.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduled_report_update_scheduled_report**
> ScheduledReport scheduled_report_update_scheduled_report(scheduled_report_guid, scheduled_report)

Update the specified scheduled report.

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
api_instance = uptrends.ScheduledReportApi(uptrends.ApiClient(configuration))
scheduled_report_guid = 'scheduled_report_guid_example' # str | The guid of the specified scheduled report.
scheduled_report = uptrends.ScheduledReport() # ScheduledReport | The details for the scheduled report.

try:
    # Update the specified scheduled report.
    api_response = api_instance.scheduled_report_update_scheduled_report(scheduled_report_guid, scheduled_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduledReportApi->scheduled_report_update_scheduled_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_report_guid** | **str**| The guid of the specified scheduled report. | 
 **scheduled_report** | [**ScheduledReport**](ScheduledReport.md)| The details for the scheduled report. | 

### Return type

[**ScheduledReport**](ScheduledReport.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

