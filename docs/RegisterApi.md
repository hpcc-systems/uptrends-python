# uptrends.RegisterApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_post**](RegisterApi.md#register_post) | **POST** /Register | Creates a new API account.


# **register_post**
> RegistrationResponse register_post()

Creates a new API account.

This method requires that you specify the username and password of an Uptrends operator login as authentication. When registration is successful, please save the UserName and Password fields from the response; these are your new API credentials.

### Example
```python
from __future__ import print_function
import time
import uptrends
from uptrends.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: user-basicauth
configuration = uptrends.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = uptrends.RegisterApi(uptrends.ApiClient(configuration))

try:
    # Creates a new API account.
    api_response = api_instance.register_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisterApi->register_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RegistrationResponse**](RegistrationResponse.md)

### Authorization

[user-basicauth](../README.md#user-basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

