# uptrends.OperatorApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operator_add_duty_period_for_operator**](OperatorApi.md#operator_add_duty_period_for_operator) | **POST** /Operator/{operatorGuid}/DutySchedule | Adds a duty schedule to the specified operator.
[**operator_create_operator**](OperatorApi.md#operator_create_operator) | **POST** /Operator | Creates a new operator.
[**operator_delete_authorization_for_operator**](OperatorApi.md#operator_delete_authorization_for_operator) | **DELETE** /Operator/{operatorGuid}/Authorization/{authorizationType} | Removes the specified authorization of this operator.
[**operator_delete_duty_schedule_from_operator**](OperatorApi.md#operator_delete_duty_schedule_from_operator) | **DELETE** /Operator/{operatorGuid}/DutySchedule/{dutyScheduleId} | Deletes the specified duty schedule of the specified operator.
[**operator_delete_operator**](OperatorApi.md#operator_delete_operator) | **DELETE** /Operator/{operatorGuid} | Deletes an existing operator.
[**operator_get_all_operators**](OperatorApi.md#operator_get_all_operators) | **GET** /Operator | Gets a list of all operators.
[**operator_get_authorizations_for_operator**](OperatorApi.md#operator_get_authorizations_for_operator) | **GET** /Operator/{operatorGuid}/Authorization | Gets all authorizations for the specified operator.
[**operator_get_duty_schedule_for_operator**](OperatorApi.md#operator_get_duty_schedule_for_operator) | **GET** /Operator/{operatorGuid}/DutySchedule | Gets the duty schedules for an specified operator.
[**operator_get_operator**](OperatorApi.md#operator_get_operator) | **GET** /Operator/{operatorGuid} | Gets the details of the operator with the provided OperatorGuid.
[**operator_get_operator_groups_for_operator**](OperatorApi.md#operator_get_operator_groups_for_operator) | **GET** /Operator/{operatorGuid}/OperatorGroups | Gets a list of all operator groups for the specified operator.
[**operator_post_authorization_for_operator**](OperatorApi.md#operator_post_authorization_for_operator) | **POST** /Operator/{operatorGuid}/Authorization/{authorizationType} | Assigns the specified authorization to this operator.
[**operator_update_duty_period_for_operator**](OperatorApi.md#operator_update_duty_period_for_operator) | **PUT** /Operator/{operatorGuid}/DutySchedule/{dutyScheduleId} | Updates the specified duty schedule of the specified operator.
[**operator_update_operator**](OperatorApi.md#operator_update_operator) | **PUT** /Operator/{operatorGuid} | Updates an existing operator.
[**operator_update_operator_with_patch**](OperatorApi.md#operator_update_operator_with_patch) | **PATCH** /Operator/{operatorGuid} | Updates an existing operator.


# **operator_add_duty_period_for_operator**
> operator_add_duty_period_for_operator(schedule, operator_guid)

Adds a duty schedule to the specified operator.

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
api_instance = uptrends.OperatorApi(uptrends.ApiClient(configuration))
schedule = uptrends.OperatorDutySchedule() # OperatorDutySchedule | The duty schedule to add
operator_guid = 'operator_guid_example' # str | The Guid of the operator to add the duty schedule to

try:
    # Adds a duty schedule to the specified operator.
    api_instance.operator_add_duty_period_for_operator(schedule, operator_guid)
except ApiException as e:
    print("Exception when calling OperatorApi->operator_add_duty_period_for_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule** | [**OperatorDutySchedule**](OperatorDutySchedule.md)| The duty schedule to add | 
 **operator_guid** | **str**| The Guid of the operator to add the duty schedule to | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_create_operator**
> Operator operator_create_operator(uptrends_operator)

Creates a new operator.

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
api_instance = uptrends.OperatorApi(uptrends.ApiClient(configuration))
uptrends_operator = uptrends.Operator() # Operator | The details of the operator to create

try:
    # Creates a new operator.
    api_response = api_instance.operator_create_operator(uptrends_operator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorApi->operator_create_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uptrends_operator** | [**Operator**](Operator.md)| The details of the operator to create | 

### Return type

[**Operator**](Operator.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_delete_authorization_for_operator**
> operator_delete_authorization_for_operator(operator_guid, authorization_type)

Removes the specified authorization of this operator.

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
api_instance = uptrends.OperatorApi(uptrends.ApiClient(configuration))
operator_guid = 'operator_guid_example' # str | The Guid of the operator
authorization_type = 'authorization_type_example' # str | The type of authorization

try:
    # Removes the specified authorization of this operator.
    api_instance.operator_delete_authorization_for_operator(operator_guid, authorization_type)
except ApiException as e:
    print("Exception when calling OperatorApi->operator_delete_authorization_for_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_guid** | **str**| The Guid of the operator | 
 **authorization_type** | **str**| The type of authorization | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_delete_duty_schedule_from_operator**
> operator_delete_duty_schedule_from_operator(operator_guid, duty_schedule_id)

Deletes the specified duty schedule of the specified operator.

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
api_instance = uptrends.OperatorApi(uptrends.ApiClient(configuration))
operator_guid = 'operator_guid_example' # str | 
duty_schedule_id = 56 # int | 

try:
    # Deletes the specified duty schedule of the specified operator.
    api_instance.operator_delete_duty_schedule_from_operator(operator_guid, duty_schedule_id)
except ApiException as e:
    print("Exception when calling OperatorApi->operator_delete_duty_schedule_from_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_guid** | **str**|  | 
 **duty_schedule_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_delete_operator**
> operator_delete_operator(operator_guid)

Deletes an existing operator.

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
api_instance = uptrends.OperatorApi(uptrends.ApiClient(configuration))
operator_guid = 'operator_guid_example' # str | The Guid of the operator to delete

try:
    # Deletes an existing operator.
    api_instance.operator_delete_operator(operator_guid)
except ApiException as e:
    print("Exception when calling OperatorApi->operator_delete_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_guid** | **str**| The Guid of the operator to delete | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_get_all_operators**
> list[Operator] operator_get_all_operators()

Gets a list of all operators.

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
api_instance = uptrends.OperatorApi(uptrends.ApiClient(configuration))

try:
    # Gets a list of all operators.
    api_response = api_instance.operator_get_all_operators()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorApi->operator_get_all_operators: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Operator]**](Operator.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_get_authorizations_for_operator**
> list[AuthorizationTypeWithoutContext] operator_get_authorizations_for_operator(operator_guid)

Gets all authorizations for the specified operator.

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
api_instance = uptrends.OperatorApi(uptrends.ApiClient(configuration))
operator_guid = 'operator_guid_example' # str | The Guid of the operator

try:
    # Gets all authorizations for the specified operator.
    api_response = api_instance.operator_get_authorizations_for_operator(operator_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorApi->operator_get_authorizations_for_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_guid** | **str**| The Guid of the operator | 

### Return type

[**list[AuthorizationTypeWithoutContext]**](AuthorizationTypeWithoutContext.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_get_duty_schedule_for_operator**
> list[OperatorDutySchedule] operator_get_duty_schedule_for_operator(operator_guid)

Gets the duty schedules for an specified operator.

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
api_instance = uptrends.OperatorApi(uptrends.ApiClient(configuration))
operator_guid = 'operator_guid_example' # str | The Guid of the operator to get the duty schedule for

try:
    # Gets the duty schedules for an specified operator.
    api_response = api_instance.operator_get_duty_schedule_for_operator(operator_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorApi->operator_get_duty_schedule_for_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_guid** | **str**| The Guid of the operator to get the duty schedule for | 

### Return type

[**list[OperatorDutySchedule]**](OperatorDutySchedule.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_get_operator**
> Operator operator_get_operator(operator_guid)

Gets the details of the operator with the provided OperatorGuid.

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
api_instance = uptrends.OperatorApi(uptrends.ApiClient(configuration))
operator_guid = 'operator_guid_example' # str | The Guid of the operator for which to retrieve the details

try:
    # Gets the details of the operator with the provided OperatorGuid.
    api_response = api_instance.operator_get_operator(operator_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorApi->operator_get_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_guid** | **str**| The Guid of the operator for which to retrieve the details | 

### Return type

[**Operator**](Operator.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_get_operator_groups_for_operator**
> list[OperatorMember] operator_get_operator_groups_for_operator(operator_guid)

Gets a list of all operator groups for the specified operator.

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
api_instance = uptrends.OperatorApi(uptrends.ApiClient(configuration))
operator_guid = 'operator_guid_example' # str | The Guid of the operator for which to retrieve the operator group guids

try:
    # Gets a list of all operator groups for the specified operator.
    api_response = api_instance.operator_get_operator_groups_for_operator(operator_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorApi->operator_get_operator_groups_for_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_guid** | **str**| The Guid of the operator for which to retrieve the operator group guids | 

### Return type

[**list[OperatorMember]**](OperatorMember.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_post_authorization_for_operator**
> operator_post_authorization_for_operator(operator_guid, authorization_type)

Assigns the specified authorization to this operator.

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
api_instance = uptrends.OperatorApi(uptrends.ApiClient(configuration))
operator_guid = 'operator_guid_example' # str | The Guid of the operator
authorization_type = 'authorization_type_example' # str | The type of authorization

try:
    # Assigns the specified authorization to this operator.
    api_instance.operator_post_authorization_for_operator(operator_guid, authorization_type)
except ApiException as e:
    print("Exception when calling OperatorApi->operator_post_authorization_for_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_guid** | **str**| The Guid of the operator | 
 **authorization_type** | **str**| The type of authorization | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_update_duty_period_for_operator**
> operator_update_duty_period_for_operator(operator_guid, duty_schedule_id, schedule)

Updates the specified duty schedule of the specified operator.

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
api_instance = uptrends.OperatorApi(uptrends.ApiClient(configuration))
operator_guid = 'operator_guid_example' # str | 
duty_schedule_id = 56 # int | 
schedule = uptrends.OperatorDutySchedule() # OperatorDutySchedule | 

try:
    # Updates the specified duty schedule of the specified operator.
    api_instance.operator_update_duty_period_for_operator(operator_guid, duty_schedule_id, schedule)
except ApiException as e:
    print("Exception when calling OperatorApi->operator_update_duty_period_for_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_guid** | **str**|  | 
 **duty_schedule_id** | **int**|  | 
 **schedule** | [**OperatorDutySchedule**](OperatorDutySchedule.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_update_operator**
> operator_update_operator(uptrends_operator, operator_guid)

Updates an existing operator.

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
api_instance = uptrends.OperatorApi(uptrends.ApiClient(configuration))
uptrends_operator = uptrends.Operator() # Operator | The updated details of the operator
operator_guid = 'operator_guid_example' # str | The Guid of the operator to update

try:
    # Updates an existing operator.
    api_instance.operator_update_operator(uptrends_operator, operator_guid)
except ApiException as e:
    print("Exception when calling OperatorApi->operator_update_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uptrends_operator** | [**Operator**](Operator.md)| The updated details of the operator | 
 **operator_guid** | **str**| The Guid of the operator to update | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_update_operator_with_patch**
> operator_update_operator_with_patch(uptrends_operator, operator_guid)

Updates an existing operator.

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
api_instance = uptrends.OperatorApi(uptrends.ApiClient(configuration))
uptrends_operator = uptrends.Operator() # Operator | The updated details of the operator
operator_guid = 'operator_guid_example' # str | The Guid of the operator to update

try:
    # Updates an existing operator.
    api_instance.operator_update_operator_with_patch(uptrends_operator, operator_guid)
except ApiException as e:
    print("Exception when calling OperatorApi->operator_update_operator_with_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uptrends_operator** | [**Operator**](Operator.md)| The updated details of the operator | 
 **operator_guid** | **str**| The Guid of the operator to update | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

