# uptrends.MiscellaneousApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**miscellaneous_get_all_outgoing_phone_numbers**](MiscellaneousApi.md#miscellaneous_get_all_outgoing_phone_numbers) | **GET** /OutgoingPhoneNumber | Gets a list of all outgoing phone numbers available.
[**miscellaneous_get_all_timezones**](MiscellaneousApi.md#miscellaneous_get_all_timezones) | **GET** /Timezone | Gets all timezones available.
[**miscellaneous_get_timezone_by_id**](MiscellaneousApi.md#miscellaneous_get_timezone_by_id) | **GET** /Timezone/{timezoneId} | Gets the timezone with the specified Id.


# **miscellaneous_get_all_outgoing_phone_numbers**
> list[OutgoingPhoneNumberDetails] miscellaneous_get_all_outgoing_phone_numbers()

Gets a list of all outgoing phone numbers available.

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
api_instance = uptrends.MiscellaneousApi(uptrends.ApiClient(configuration))

try:
    # Gets a list of all outgoing phone numbers available.
    api_response = api_instance.miscellaneous_get_all_outgoing_phone_numbers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->miscellaneous_get_all_outgoing_phone_numbers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OutgoingPhoneNumberDetails]**](OutgoingPhoneNumberDetails.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **miscellaneous_get_all_timezones**
> list[Timezone] miscellaneous_get_all_timezones()

Gets all timezones available.

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
api_instance = uptrends.MiscellaneousApi(uptrends.ApiClient(configuration))

try:
    # Gets all timezones available.
    api_response = api_instance.miscellaneous_get_all_timezones()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->miscellaneous_get_all_timezones: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Timezone]**](Timezone.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **miscellaneous_get_timezone_by_id**
> Timezone miscellaneous_get_timezone_by_id(timezone_id)

Gets the timezone with the specified Id.

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
api_instance = uptrends.MiscellaneousApi(uptrends.ApiClient(configuration))
timezone_id = 56 # int | 

try:
    # Gets the timezone with the specified Id.
    api_response = api_instance.miscellaneous_get_timezone_by_id(timezone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscellaneousApi->miscellaneous_get_timezone_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timezone_id** | **int**|  | 

### Return type

[**Timezone**](Timezone.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

