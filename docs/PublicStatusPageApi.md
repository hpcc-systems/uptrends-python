# uptrends.PublicStatusPageApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_status_page_add_authorization_to_public_status_page**](PublicStatusPageApi.md#public_status_page_add_authorization_to_public_status_page) | **POST** /PublicStatusPage/{publicStatusPageGuid}/Authorization | Creates a new authorization for the specified public status page.
[**public_status_page_delete_public_status_page**](PublicStatusPageApi.md#public_status_page_delete_public_status_page) | **DELETE** /PublicStatusPage/{publicStatusPageGuid} | Deletes the definition of the specified public status page.
[**public_status_page_get_authorizations_for_public_status_page**](PublicStatusPageApi.md#public_status_page_get_authorizations_for_public_status_page) | **GET** /PublicStatusPage/{publicStatusPageGuid}/Authorization | Returns all authorizations for the specified public status page.
[**public_status_page_get_public_status_page**](PublicStatusPageApi.md#public_status_page_get_public_status_page) | **GET** /PublicStatusPage/{publicStatusPageGuid} | Returns the definition of the specified public status page.
[**public_status_page_get_public_status_pages**](PublicStatusPageApi.md#public_status_page_get_public_status_pages) | **GET** /PublicStatusPage | Returns the definition of all public status pages available in the account.
[**public_status_page_patch_public_status_page**](PublicStatusPageApi.md#public_status_page_patch_public_status_page) | **PATCH** /PublicStatusPage/{publicStatusPageGuid} | Partially updates the definition of the specified public status page.
[**public_status_page_post_public_status_page**](PublicStatusPageApi.md#public_status_page_post_public_status_page) | **POST** /PublicStatusPage | Creates a new public status page.
[**public_status_page_put_public_status_page**](PublicStatusPageApi.md#public_status_page_put_public_status_page) | **PUT** /PublicStatusPage/{publicStatusPageGuid} | Updates the definition of the specified public status page.
[**public_status_page_remove_authorization_from_public_status_page**](PublicStatusPageApi.md#public_status_page_remove_authorization_from_public_status_page) | **DELETE** /PublicStatusPage/{publicStatusPageGuid}/Authorization/{authorizationGuid} | Removes an authorization from a public status page.


# **public_status_page_add_authorization_to_public_status_page**
> PSPAuthorization public_status_page_add_authorization_to_public_status_page(public_status_page_guid, authorization)

Creates a new authorization for the specified public status page.

The AuthorizationId attribute should be omitted in the request body. The newly created authorization will be returned in the response. An authorization should be granted to either an individual operator, or an operator group. Therefore, either specify the OperatorGuid attribute or the OperatorGroupGuid attribute.

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
api_instance = uptrends.PublicStatusPageApi(uptrends.ApiClient(configuration))
public_status_page_guid = 'public_status_page_guid_example' # str | The Guid of the public status page.
authorization = uptrends.PSPAuthorization() # PSPAuthorization | The complete definition of the authorization that should be created.

try:
    # Creates a new authorization for the specified public status page.
    api_response = api_instance.public_status_page_add_authorization_to_public_status_page(public_status_page_guid, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicStatusPageApi->public_status_page_add_authorization_to_public_status_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_status_page_guid** | **str**| The Guid of the public status page. | 
 **authorization** | [**PSPAuthorization**](PSPAuthorization.md)| The complete definition of the authorization that should be created. | 

### Return type

[**PSPAuthorization**](PSPAuthorization.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_status_page_delete_public_status_page**
> public_status_page_delete_public_status_page(public_status_page_guid)

Deletes the definition of the specified public status page.

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
api_instance = uptrends.PublicStatusPageApi(uptrends.ApiClient(configuration))
public_status_page_guid = 'public_status_page_guid_example' # str | The Guid of the public status page that should be updated.

try:
    # Deletes the definition of the specified public status page.
    api_instance.public_status_page_delete_public_status_page(public_status_page_guid)
except ApiException as e:
    print("Exception when calling PublicStatusPageApi->public_status_page_delete_public_status_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_status_page_guid** | **str**| The Guid of the public status page that should be updated. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_status_page_get_authorizations_for_public_status_page**
> list[PSPAuthorization] public_status_page_get_authorizations_for_public_status_page(public_status_page_guid)

Returns all authorizations for the specified public status page.

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
api_instance = uptrends.PublicStatusPageApi(uptrends.ApiClient(configuration))
public_status_page_guid = 'public_status_page_guid_example' # str | The Guid of the public status page.

try:
    # Returns all authorizations for the specified public status page.
    api_response = api_instance.public_status_page_get_authorizations_for_public_status_page(public_status_page_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicStatusPageApi->public_status_page_get_authorizations_for_public_status_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_status_page_guid** | **str**| The Guid of the public status page. | 

### Return type

[**list[PSPAuthorization]**](PSPAuthorization.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_status_page_get_public_status_page**
> PublicStatusPage public_status_page_get_public_status_page(public_status_page_guid)

Returns the definition of the specified public status page.

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
api_instance = uptrends.PublicStatusPageApi(uptrends.ApiClient(configuration))
public_status_page_guid = 'public_status_page_guid_example' # str | The Guid of the requested public status page.

try:
    # Returns the definition of the specified public status page.
    api_response = api_instance.public_status_page_get_public_status_page(public_status_page_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicStatusPageApi->public_status_page_get_public_status_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_status_page_guid** | **str**| The Guid of the requested public status page. | 

### Return type

[**PublicStatusPage**](PublicStatusPage.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_status_page_get_public_status_pages**
> list[PublicStatusPage] public_status_page_get_public_status_pages()

Returns the definition of all public status pages available in the account.

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
api_instance = uptrends.PublicStatusPageApi(uptrends.ApiClient(configuration))

try:
    # Returns the definition of all public status pages available in the account.
    api_response = api_instance.public_status_page_get_public_status_pages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicStatusPageApi->public_status_page_get_public_status_pages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PublicStatusPage]**](PublicStatusPage.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_status_page_patch_public_status_page**
> public_status_page_patch_public_status_page(public_status_page, public_status_page_guid)

Partially updates the definition of the specified public status page.

This methods accepts parts of a public status page definition. We recommend retrieving the existing definition first (using the GET method). You can then process the changes you want to make and send back these changes only using this PATCH method.

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
api_instance = uptrends.PublicStatusPageApi(uptrends.ApiClient(configuration))
public_status_page = uptrends.PublicStatusPage() # PublicStatusPage | The partial definition for the public status page that should be updated.
public_status_page_guid = 'public_status_page_guid_example' # str | The Guid of the public status page that should be updated.

try:
    # Partially updates the definition of the specified public status page.
    api_instance.public_status_page_patch_public_status_page(public_status_page, public_status_page_guid)
except ApiException as e:
    print("Exception when calling PublicStatusPageApi->public_status_page_patch_public_status_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_status_page** | [**PublicStatusPage**](PublicStatusPage.md)| The partial definition for the public status page that should be updated. | 
 **public_status_page_guid** | **str**| The Guid of the public status page that should be updated. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_status_page_post_public_status_page**
> PublicStatusPage public_status_page_post_public_status_page(public_status_page)

Creates a new public status page.

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
api_instance = uptrends.PublicStatusPageApi(uptrends.ApiClient(configuration))
public_status_page = uptrends.PublicStatusPage() # PublicStatusPage | The complete definition for the public status page that should be updated.

try:
    # Creates a new public status page.
    api_response = api_instance.public_status_page_post_public_status_page(public_status_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicStatusPageApi->public_status_page_post_public_status_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_status_page** | [**PublicStatusPage**](PublicStatusPage.md)| The complete definition for the public status page that should be updated. | 

### Return type

[**PublicStatusPage**](PublicStatusPage.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_status_page_put_public_status_page**
> public_status_page_put_public_status_page(public_status_page, public_status_page_guid)

Updates the definition of the specified public status page.

This methods only accepts a complete public status page definition. We recommend retrieving the existing definition first (using the GET method). You can then process the changes you want to make and send back the updated definition using this PUT method.

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
api_instance = uptrends.PublicStatusPageApi(uptrends.ApiClient(configuration))
public_status_page = uptrends.PublicStatusPage() # PublicStatusPage | The complete definition for the public status page that should be updated.
public_status_page_guid = 'public_status_page_guid_example' # str | The Guid of the public status page that should be updated.

try:
    # Updates the definition of the specified public status page.
    api_instance.public_status_page_put_public_status_page(public_status_page, public_status_page_guid)
except ApiException as e:
    print("Exception when calling PublicStatusPageApi->public_status_page_put_public_status_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_status_page** | [**PublicStatusPage**](PublicStatusPage.md)| The complete definition for the public status page that should be updated. | 
 **public_status_page_guid** | **str**| The Guid of the public status page that should be updated. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_status_page_remove_authorization_from_public_status_page**
> public_status_page_remove_authorization_from_public_status_page(public_status_page_guid, authorization_guid)

Removes an authorization from a public status page.

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
api_instance = uptrends.PublicStatusPageApi(uptrends.ApiClient(configuration))
public_status_page_guid = 'public_status_page_guid_example' # str | The Guid of the public status page.
authorization_guid = 'authorization_guid_example' # str | The Guid of the authorization.

try:
    # Removes an authorization from a public status page.
    api_instance.public_status_page_remove_authorization_from_public_status_page(public_status_page_guid, authorization_guid)
except ApiException as e:
    print("Exception when calling PublicStatusPageApi->public_status_page_remove_authorization_from_public_status_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_status_page_guid** | **str**| The Guid of the public status page. | 
 **authorization_guid** | **str**| The Guid of the authorization. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

