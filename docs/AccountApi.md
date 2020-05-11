# uptrends.AccountApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_get_account_statistics**](AccountApi.md#account_get_account_statistics) | **GET** /Account | Returns the account statistics.


# **account_get_account_statistics**
> AccountStatistics account_get_account_statistics()

Returns the account statistics.

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
api_instance = uptrends.AccountApi(uptrends.ApiClient(configuration))

try:
    # Returns the account statistics.
    api_response = api_instance.account_get_account_statistics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get_account_statistics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountStatistics**](AccountStatistics.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

