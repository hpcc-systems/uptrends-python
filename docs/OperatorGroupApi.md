# uptrends.OperatorGroupApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operator_group_add_duty_schedule_to_all_members**](OperatorGroupApi.md#operator_group_add_duty_schedule_to_all_members) | **POST** /OperatorGroup/{operatorGroupGuid}/DutySchedule/AddDutyScheduleForAllMembers | Adds the provided duty schedule to all operators in the group specified 
[**operator_group_add_operator_to_operator_group**](OperatorGroupApi.md#operator_group_add_operator_to_operator_group) | **POST** /OperatorGroup/{operatorGroupGuid}/Member/{operatorGuid} | Adds the specified operator to the operator group 
[**operator_group_all_operators_in_group_off_duty**](OperatorGroupApi.md#operator_group_all_operators_in_group_off_duty) | **POST** /OperatorGroup/{operatorGroupGuid}/AllOperatorsOffDuty | Set the OnDuty flag to off for all operators that are a member of the operator group specified by the operator group GUID
[**operator_group_all_operators_in_group_on_duty**](OperatorGroupApi.md#operator_group_all_operators_in_group_on_duty) | **POST** /OperatorGroup/{operatorGroupGuid}/AllOperatorsOnDuty | Set the OnDuty flag to on for all operators that are a member of the operator group specified by the operator group GUID
[**operator_group_create_operator_group**](OperatorGroupApi.md#operator_group_create_operator_group) | **POST** /OperatorGroup | Creates a new operator group
[**operator_group_delete_operator_group**](OperatorGroupApi.md#operator_group_delete_operator_group) | **DELETE** /OperatorGroup/{operatorGroupGuid} | Deletes the specified operator group
[**operator_group_get_all_operator_groups**](OperatorGroupApi.md#operator_group_get_all_operator_groups) | **GET** /OperatorGroup | Gets all operator groups
[**operator_group_get_operator_group**](OperatorGroupApi.md#operator_group_get_operator_group) | **GET** /OperatorGroup/{operatorGroupGuid} | Gets the details of a operator group
[**operator_group_get_operator_group_members**](OperatorGroupApi.md#operator_group_get_operator_group_members) | **GET** /OperatorGroup/{operatorGroupGuid}/Member | Gets a list of all members of an operator group
[**operator_group_remove_operator_from_operator_group**](OperatorGroupApi.md#operator_group_remove_operator_from_operator_group) | **DELETE** /OperatorGroup/{operatorGroupGuid}/Member/{operatorGuid} | Removes the specified operator from the operator group
[**operator_group_update_operator_group**](OperatorGroupApi.md#operator_group_update_operator_group) | **PUT** /OperatorGroup/{operatorGroupGuid} | Updates the operator group with the Guid specified


# **operator_group_add_duty_schedule_to_all_members**
> operator_group_add_duty_schedule_to_all_members(operator_group_guid, duty_schedule)

Adds the provided duty schedule to all operators in the group specified 

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
api_instance = uptrends.OperatorGroupApi(uptrends.ApiClient(configuration))
operator_group_guid = 'operator_group_guid_example' # str | 
duty_schedule = uptrends.OperatorDutySchedule() # OperatorDutySchedule | 

try:
    # Adds the provided duty schedule to all operators in the group specified 
    api_instance.operator_group_add_duty_schedule_to_all_members(operator_group_guid, duty_schedule)
except ApiException as e:
    print("Exception when calling OperatorGroupApi->operator_group_add_duty_schedule_to_all_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_group_guid** | **str**|  | 
 **duty_schedule** | [**OperatorDutySchedule**](OperatorDutySchedule.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_group_add_operator_to_operator_group**
> operator_group_add_operator_to_operator_group(operator_group_guid, operator_guid)

Adds the specified operator to the operator group 

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
api_instance = uptrends.OperatorGroupApi(uptrends.ApiClient(configuration))
operator_group_guid = 'operator_group_guid_example' # str | The Guid of the operator group to add the operator to
operator_guid = 'operator_guid_example' # str | The operator Guid

try:
    # Adds the specified operator to the operator group 
    api_instance.operator_group_add_operator_to_operator_group(operator_group_guid, operator_guid)
except ApiException as e:
    print("Exception when calling OperatorGroupApi->operator_group_add_operator_to_operator_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_group_guid** | **str**| The Guid of the operator group to add the operator to | 
 **operator_guid** | **str**| The operator Guid | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_group_all_operators_in_group_off_duty**
> operator_group_all_operators_in_group_off_duty(operator_group_guid)

Set the OnDuty flag to off for all operators that are a member of the operator group specified by the operator group GUID

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
api_instance = uptrends.OperatorGroupApi(uptrends.ApiClient(configuration))
operator_group_guid = 'operator_group_guid_example' # str | The operator group GUID

try:
    # Set the OnDuty flag to off for all operators that are a member of the operator group specified by the operator group GUID
    api_instance.operator_group_all_operators_in_group_off_duty(operator_group_guid)
except ApiException as e:
    print("Exception when calling OperatorGroupApi->operator_group_all_operators_in_group_off_duty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_group_guid** | **str**| The operator group GUID | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_group_all_operators_in_group_on_duty**
> operator_group_all_operators_in_group_on_duty(operator_group_guid)

Set the OnDuty flag to on for all operators that are a member of the operator group specified by the operator group GUID

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
api_instance = uptrends.OperatorGroupApi(uptrends.ApiClient(configuration))
operator_group_guid = 'operator_group_guid_example' # str | The operator group GUID

try:
    # Set the OnDuty flag to on for all operators that are a member of the operator group specified by the operator group GUID
    api_instance.operator_group_all_operators_in_group_on_duty(operator_group_guid)
except ApiException as e:
    print("Exception when calling OperatorGroupApi->operator_group_all_operators_in_group_on_duty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_group_guid** | **str**| The operator group GUID | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_group_create_operator_group**
> OperatorGroup operator_group_create_operator_group(operator_group)

Creates a new operator group

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
api_instance = uptrends.OperatorGroupApi(uptrends.ApiClient(configuration))
operator_group = uptrends.OperatorGroup() # OperatorGroup | The operatorGroup object to be created

try:
    # Creates a new operator group
    api_response = api_instance.operator_group_create_operator_group(operator_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorGroupApi->operator_group_create_operator_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_group** | [**OperatorGroup**](OperatorGroup.md)| The operatorGroup object to be created | 

### Return type

[**OperatorGroup**](OperatorGroup.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_group_delete_operator_group**
> operator_group_delete_operator_group(operator_group_guid)

Deletes the specified operator group

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
api_instance = uptrends.OperatorGroupApi(uptrends.ApiClient(configuration))
operator_group_guid = 'operator_group_guid_example' # str | The Guid of the operator group to be deleted

try:
    # Deletes the specified operator group
    api_instance.operator_group_delete_operator_group(operator_group_guid)
except ApiException as e:
    print("Exception when calling OperatorGroupApi->operator_group_delete_operator_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_group_guid** | **str**| The Guid of the operator group to be deleted | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_group_get_all_operator_groups**
> list[OperatorGroup] operator_group_get_all_operator_groups()

Gets all operator groups

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
api_instance = uptrends.OperatorGroupApi(uptrends.ApiClient(configuration))

try:
    # Gets all operator groups
    api_response = api_instance.operator_group_get_all_operator_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorGroupApi->operator_group_get_all_operator_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OperatorGroup]**](OperatorGroup.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_group_get_operator_group**
> OperatorGroup operator_group_get_operator_group(operator_group_guid)

Gets the details of a operator group

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
api_instance = uptrends.OperatorGroupApi(uptrends.ApiClient(configuration))
operator_group_guid = 'operator_group_guid_example' # str | The Guid of the operator group to be retrieved

try:
    # Gets the details of a operator group
    api_response = api_instance.operator_group_get_operator_group(operator_group_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorGroupApi->operator_group_get_operator_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_group_guid** | **str**| The Guid of the operator group to be retrieved | 

### Return type

[**OperatorGroup**](OperatorGroup.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_group_get_operator_group_members**
> OperatorGroupMember operator_group_get_operator_group_members(operator_group_guid)

Gets a list of all members of an operator group

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
api_instance = uptrends.OperatorGroupApi(uptrends.ApiClient(configuration))
operator_group_guid = 'operator_group_guid_example' # str | The Guid of the operator group to retrieve the members for

try:
    # Gets a list of all members of an operator group
    api_response = api_instance.operator_group_get_operator_group_members(operator_group_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorGroupApi->operator_group_get_operator_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_group_guid** | **str**| The Guid of the operator group to retrieve the members for | 

### Return type

[**OperatorGroupMember**](OperatorGroupMember.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_group_remove_operator_from_operator_group**
> operator_group_remove_operator_from_operator_group(operator_group_guid, operator_guid)

Removes the specified operator from the operator group

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
api_instance = uptrends.OperatorGroupApi(uptrends.ApiClient(configuration))
operator_group_guid = 'operator_group_guid_example' # str | The Guid of the operator group to remove the operator from
operator_guid = 'operator_guid_example' # str | The operator Guid to be removed

try:
    # Removes the specified operator from the operator group
    api_instance.operator_group_remove_operator_from_operator_group(operator_group_guid, operator_guid)
except ApiException as e:
    print("Exception when calling OperatorGroupApi->operator_group_remove_operator_from_operator_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_group_guid** | **str**| The Guid of the operator group to remove the operator from | 
 **operator_guid** | **str**| The operator Guid to be removed | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operator_group_update_operator_group**
> operator_group_update_operator_group(item, operator_group_guid)

Updates the operator group with the Guid specified

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
api_instance = uptrends.OperatorGroupApi(uptrends.ApiClient(configuration))
item = uptrends.OperatorGroup() # OperatorGroup | The operator group to be updated
operator_group_guid = 'operator_group_guid_example' # str | The Guid of the operator group to be updated

try:
    # Updates the operator group with the Guid specified
    api_instance.operator_group_update_operator_group(item, operator_group_guid)
except ApiException as e:
    print("Exception when calling OperatorGroupApi->operator_group_update_operator_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item** | [**OperatorGroup**](OperatorGroup.md)| The operator group to be updated | 
 **operator_group_guid** | **str**| The Guid of the operator group to be updated | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

