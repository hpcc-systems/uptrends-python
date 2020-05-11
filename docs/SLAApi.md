# uptrends.SLAApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sla_create_sla**](SLAApi.md#sla_create_sla) | **POST** /Sla | Creates a new SLA.
[**sla_delete_exclusion_period**](SLAApi.md#sla_delete_exclusion_period) | **DELETE** /Sla/{slaGuid}/ExclusionPeriod/{exclusionPeriodId} | Deletes the specified exclusion period for the specified SLA.
[**sla_delete_sla**](SLAApi.md#sla_delete_sla) | **DELETE** /Sla/{slaGuid} | Deletes the specified SLA.
[**sla_get_exclusion_period**](SLAApi.md#sla_get_exclusion_period) | **GET** /Sla/{slaGuid}/ExclusionPeriod/{exclusionPeriodId} | Gets the specified exclusion period for the specified SLA.
[**sla_get_exclusion_periods**](SLAApi.md#sla_get_exclusion_periods) | **GET** /Sla/{slaGuid}/ExclusionPeriod | Gets a list of all exclusion periods for the specified SLA.
[**sla_get_sla**](SLAApi.md#sla_get_sla) | **GET** /Sla/{slaGuid} | Gets the specified SLA definition.
[**sla_get_slas**](SLAApi.md#sla_get_slas) | **GET** /Sla | Gets a list of all SLA definitions.
[**sla_patch_exclusion_period**](SLAApi.md#sla_patch_exclusion_period) | **PATCH** /Sla/{slaGuid}/ExclusionPeriod/{exclusionPeriodId} | Partially updates the specified exclusion period for the specified SLA.
[**sla_patch_sla**](SLAApi.md#sla_patch_sla) | **PATCH** /Sla/{slaGuid} | Partially updates the definition of the specified SLA.
[**sla_post_exclusion_period**](SLAApi.md#sla_post_exclusion_period) | **POST** /Sla/{slaGuid}/ExclusionPeriod | Creates a new exclusion period for the specified SLA.
[**sla_put_exclusion_period**](SLAApi.md#sla_put_exclusion_period) | **PUT** /Sla/{slaGuid}/ExclusionPeriod/{exclusionPeriodId} | Updates the specified exclusion period for the specified SLA.
[**sla_put_sla**](SLAApi.md#sla_put_sla) | **PUT** /Sla/{slaGuid} | Updates the definition of the specified SLA.


# **sla_create_sla**
> Sla sla_create_sla(sla)

Creates a new SLA.

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
api_instance = uptrends.SLAApi(uptrends.ApiClient(configuration))
sla = uptrends.Sla() # Sla | The complete SLA definition that should be created.

try:
    # Creates a new SLA.
    api_response = api_instance.sla_create_sla(sla)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SLAApi->sla_create_sla: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla** | [**Sla**](Sla.md)| The complete SLA definition that should be created. | 

### Return type

[**Sla**](Sla.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sla_delete_exclusion_period**
> sla_delete_exclusion_period(sla_guid, exclusion_period_id)

Deletes the specified exclusion period for the specified SLA.

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
api_instance = uptrends.SLAApi(uptrends.ApiClient(configuration))
sla_guid = 'sla_guid_example' # str | The Guid of the sla definition.
exclusion_period_id = 56 # int | The id of the exclusion period.

try:
    # Deletes the specified exclusion period for the specified SLA.
    api_instance.sla_delete_exclusion_period(sla_guid, exclusion_period_id)
except ApiException as e:
    print("Exception when calling SLAApi->sla_delete_exclusion_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_guid** | **str**| The Guid of the sla definition. | 
 **exclusion_period_id** | **int**| The id of the exclusion period. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sla_delete_sla**
> sla_delete_sla(sla_guid)

Deletes the specified SLA.

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
api_instance = uptrends.SLAApi(uptrends.ApiClient(configuration))
sla_guid = 'sla_guid_example' # str | The Guid of the SLA definition that should be deleted.

try:
    # Deletes the specified SLA.
    api_instance.sla_delete_sla(sla_guid)
except ApiException as e:
    print("Exception when calling SLAApi->sla_delete_sla: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_guid** | **str**| The Guid of the SLA definition that should be deleted. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sla_get_exclusion_period**
> ExclusionPeriod sla_get_exclusion_period(sla_guid, exclusion_period_id)

Gets the specified exclusion period for the specified SLA.

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
api_instance = uptrends.SLAApi(uptrends.ApiClient(configuration))
sla_guid = 'sla_guid_example' # str | The Guid of the SLA definition.
exclusion_period_id = 56 # int | The id of the exclusion period.

try:
    # Gets the specified exclusion period for the specified SLA.
    api_response = api_instance.sla_get_exclusion_period(sla_guid, exclusion_period_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SLAApi->sla_get_exclusion_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_guid** | **str**| The Guid of the SLA definition. | 
 **exclusion_period_id** | **int**| The id of the exclusion period. | 

### Return type

[**ExclusionPeriod**](ExclusionPeriod.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sla_get_exclusion_periods**
> list[ExclusionPeriod] sla_get_exclusion_periods(sla_guid)

Gets a list of all exclusion periods for the specified SLA.

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
api_instance = uptrends.SLAApi(uptrends.ApiClient(configuration))
sla_guid = 'sla_guid_example' # str | The Guid of the SLA definition.

try:
    # Gets a list of all exclusion periods for the specified SLA.
    api_response = api_instance.sla_get_exclusion_periods(sla_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SLAApi->sla_get_exclusion_periods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_guid** | **str**| The Guid of the SLA definition. | 

### Return type

[**list[ExclusionPeriod]**](ExclusionPeriod.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sla_get_sla**
> Sla sla_get_sla(sla_guid)

Gets the specified SLA definition.

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
api_instance = uptrends.SLAApi(uptrends.ApiClient(configuration))
sla_guid = 'sla_guid_example' # str | The Guid of the SLA definition.

try:
    # Gets the specified SLA definition.
    api_response = api_instance.sla_get_sla(sla_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SLAApi->sla_get_sla: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_guid** | **str**| The Guid of the SLA definition. | 

### Return type

[**Sla**](Sla.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sla_get_slas**
> list[Sla] sla_get_slas()

Gets a list of all SLA definitions.

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
api_instance = uptrends.SLAApi(uptrends.ApiClient(configuration))

try:
    # Gets a list of all SLA definitions.
    api_response = api_instance.sla_get_slas()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SLAApi->sla_get_slas: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Sla]**](Sla.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sla_patch_exclusion_period**
> sla_patch_exclusion_period(sla_guid, exclusion_period_id, exclusion_period)

Partially updates the specified exclusion period for the specified SLA.

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
api_instance = uptrends.SLAApi(uptrends.ApiClient(configuration))
sla_guid = 'sla_guid_example' # str | The Guid of the SLA definition.
exclusion_period_id = 56 # int | The id of the exclusion period.
exclusion_period = uptrends.ExclusionPeriod() # ExclusionPeriod | The complete definition of the exclusion period.

try:
    # Partially updates the specified exclusion period for the specified SLA.
    api_instance.sla_patch_exclusion_period(sla_guid, exclusion_period_id, exclusion_period)
except ApiException as e:
    print("Exception when calling SLAApi->sla_patch_exclusion_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_guid** | **str**| The Guid of the SLA definition. | 
 **exclusion_period_id** | **int**| The id of the exclusion period. | 
 **exclusion_period** | [**ExclusionPeriod**](ExclusionPeriod.md)| The complete definition of the exclusion period. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sla_patch_sla**
> sla_patch_sla(sla, sla_guid)

Partially updates the definition of the specified SLA.

This methods accepts parts of a SLA definition. We recommend retrieving the existing definition first (using the GET method). You can then process the changes you want to make and send back these changes only using this PATCH method.

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
api_instance = uptrends.SLAApi(uptrends.ApiClient(configuration))
sla = uptrends.Sla() # Sla | The partial definition for the SLA that should be updated.
sla_guid = 'sla_guid_example' # str | The Guid of the SLA that should be updated.

try:
    # Partially updates the definition of the specified SLA.
    api_instance.sla_patch_sla(sla, sla_guid)
except ApiException as e:
    print("Exception when calling SLAApi->sla_patch_sla: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla** | [**Sla**](Sla.md)| The partial definition for the SLA that should be updated. | 
 **sla_guid** | **str**| The Guid of the SLA that should be updated. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sla_post_exclusion_period**
> ExclusionPeriod sla_post_exclusion_period(exclusion_period, sla_guid)

Creates a new exclusion period for the specified SLA.

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
api_instance = uptrends.SLAApi(uptrends.ApiClient(configuration))
exclusion_period = uptrends.ExclusionPeriod() # ExclusionPeriod | The complete definition of the exclusion period.
sla_guid = 'sla_guid_example' # str | The Guid of the SLA definition.

try:
    # Creates a new exclusion period for the specified SLA.
    api_response = api_instance.sla_post_exclusion_period(exclusion_period, sla_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SLAApi->sla_post_exclusion_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclusion_period** | [**ExclusionPeriod**](ExclusionPeriod.md)| The complete definition of the exclusion period. | 
 **sla_guid** | **str**| The Guid of the SLA definition. | 

### Return type

[**ExclusionPeriod**](ExclusionPeriod.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sla_put_exclusion_period**
> sla_put_exclusion_period(sla_guid, exclusion_period_id, exclusion_period)

Updates the specified exclusion period for the specified SLA.

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
api_instance = uptrends.SLAApi(uptrends.ApiClient(configuration))
sla_guid = 'sla_guid_example' # str | The Guid of the SLA definition.
exclusion_period_id = 56 # int | The id of the exclusion period.
exclusion_period = uptrends.ExclusionPeriod() # ExclusionPeriod | The complete definition of the exclusion period.

try:
    # Updates the specified exclusion period for the specified SLA.
    api_instance.sla_put_exclusion_period(sla_guid, exclusion_period_id, exclusion_period)
except ApiException as e:
    print("Exception when calling SLAApi->sla_put_exclusion_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla_guid** | **str**| The Guid of the SLA definition. | 
 **exclusion_period_id** | **int**| The id of the exclusion period. | 
 **exclusion_period** | [**ExclusionPeriod**](ExclusionPeriod.md)| The complete definition of the exclusion period. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sla_put_sla**
> sla_put_sla(sla, sla_guid)

Updates the definition of the specified SLA.

This methods only accepts a complete SLA definition. We recommend retrieving the existing definition first (using the GET method). You can then process the changes you want to make and send back the updated definition using this PUT method.

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
api_instance = uptrends.SLAApi(uptrends.ApiClient(configuration))
sla = uptrends.Sla() # Sla | The complete definition for the SLA that should be updated.
sla_guid = 'sla_guid_example' # str | The Guid of the SLA that should be updated.

try:
    # Updates the definition of the specified SLA.
    api_instance.sla_put_sla(sla, sla_guid)
except ApiException as e:
    print("Exception when calling SLAApi->sla_put_sla: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sla** | [**Sla**](Sla.md)| The complete definition for the SLA that should be updated. | 
 **sla_guid** | **str**| The Guid of the SLA that should be updated. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

