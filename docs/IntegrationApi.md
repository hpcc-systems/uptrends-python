# uptrends.IntegrationApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integration_get_all_integrations**](IntegrationApi.md#integration_get_all_integrations) | **GET** /Integration | Gets a list of all integrations.


# **integration_get_all_integrations**
> list[Integration] integration_get_all_integrations()

Gets a list of all integrations.

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
api_instance = uptrends.IntegrationApi(uptrends.ApiClient(configuration))

try:
    # Gets a list of all integrations.
    api_response = api_instance.integration_get_all_integrations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationApi->integration_get_all_integrations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Integration]**](Integration.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

