# uptrends.AlertDefinitionApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alert_definition_add_monitor_group_to_alert_definition**](AlertDefinitionApi.md#alert_definition_add_monitor_group_to_alert_definition) | **POST** /AlertDefinition/{alertDefinitionGuid}/Members/MonitorGroup/{monitorGroupGuid} | Adds a monitor group to the specified alert definition.
[**alert_definition_add_monitor_to_alert_definition**](AlertDefinitionApi.md#alert_definition_add_monitor_to_alert_definition) | **POST** /AlertDefinition/{alertDefinitionGuid}/Members/Monitor/{monitorGuid} | Adds a monitor to the specified alert definition.
[**alert_definition_add_operator_group_to_escalation_level**](AlertDefinitionApi.md#alert_definition_add_operator_group_to_escalation_level) | **POST** /AlertDefinition/{alertDefinitionGuid}/EscalationLevel/{escalationLevelId}/Members/OperatorGroup/{operatorGroupGuid} | Adds an operator group to the specified escalation level.
[**alert_definition_add_operator_to_escalation_level**](AlertDefinitionApi.md#alert_definition_add_operator_to_escalation_level) | **POST** /AlertDefinition/{alertDefinitionGuid}/EscalationLevel/{escalationLevelId}/Members/Operator/{operatorGuid} | Adds an operator to the specified escalation level.
[**alert_definition_create_alert_definition**](AlertDefinitionApi.md#alert_definition_create_alert_definition) | **POST** /AlertDefinition | Creates a new alert definition.
[**alert_definition_delete_alert_definition**](AlertDefinitionApi.md#alert_definition_delete_alert_definition) | **DELETE** /AlertDefinition/{alertDefinitionGuid} | Deletes an existing alert definition.
[**alert_definition_get_all_alert_definitions**](AlertDefinitionApi.md#alert_definition_get_all_alert_definitions) | **GET** /AlertDefinition | Gets a list of all alert definitions.
[**alert_definition_get_all_members**](AlertDefinitionApi.md#alert_definition_get_all_members) | **GET** /AlertDefinition/{alertDefinitionGuid}/Members | Gets a list of all monitor and monitor group guids of the specified alert definition.
[**alert_definition_get_escalation_level**](AlertDefinitionApi.md#alert_definition_get_escalation_level) | **GET** /AlertDefinition/{alertDefinitionGuid}/EscalationLevel/{escalationLevelId} | Gets the escalation level information of the specified alert definition.
[**alert_definition_get_escalation_level_integration**](AlertDefinitionApi.md#alert_definition_get_escalation_level_integration) | **GET** /AlertDefinition/{alertDefinitionGuid}/EscalationLevel/{escalationLevelId}/Integration | Gets the integrations for the specified escalation level.
[**alert_definition_get_escalation_level_operator**](AlertDefinitionApi.md#alert_definition_get_escalation_level_operator) | **GET** /AlertDefinition/{alertDefinitionGuid}/EscalationLevel/{escalationLevelId}/Members | Gets the operator and operator group guids for the specified escalation level.
[**alert_definition_get_specified_alert_definitions**](AlertDefinitionApi.md#alert_definition_get_specified_alert_definitions) | **GET** /AlertDefinition/{alertDefinitionGuid} | Gets the specified alert definition.
[**alert_definition_patch_alert_definition**](AlertDefinitionApi.md#alert_definition_patch_alert_definition) | **PATCH** /AlertDefinition/{alertDefinitionGuid} | Partially updates the definition of the specified alert definition.
[**alert_definition_put_alert_definition**](AlertDefinitionApi.md#alert_definition_put_alert_definition) | **PUT** /AlertDefinition/{alertDefinitionGuid} | Updates the definition of the specified alert definition.
[**alert_definition_remove_monitor_from_alert_definition**](AlertDefinitionApi.md#alert_definition_remove_monitor_from_alert_definition) | **DELETE** /AlertDefinition/{alertDefinitionGuid}/Members/Monitor/{monitorGuid} | Removes a monitor for the specified alert definition.
[**alert_definition_remove_monitor_group_from_alert_definition**](AlertDefinitionApi.md#alert_definition_remove_monitor_group_from_alert_definition) | **DELETE** /AlertDefinition/{alertDefinitionGuid}/Members/MonitorGroup/{monitorGroupGuid} | Removes a monitor group for the specified alert definition.
[**alert_definition_remove_operator_from_escalation_level**](AlertDefinitionApi.md#alert_definition_remove_operator_from_escalation_level) | **DELETE** /AlertDefinition/{alertDefinitionGuid}/EscalationLevel/{escalationLevelId}/Members/Operator/{operatorGuid} | Removes an operator for the specified escalation level.
[**alert_definition_remove_operator_group_from_escalation_level**](AlertDefinitionApi.md#alert_definition_remove_operator_group_from_escalation_level) | **DELETE** /AlertDefinition/{alertDefinitionGuid}/EscalationLevel/{escalationLevelId}/Members/OperatorGroup/{operatorGroupGuid} | Removes an operator group for the specified escalation level.
[**alert_definition_update_integration_for_escalation_with_patch**](AlertDefinitionApi.md#alert_definition_update_integration_for_escalation_with_patch) | **PATCH** /AlertDefinition/{alertDefinitionGuid}/EscalationLevel/{escalationLevelId}/Integration/{integrationGuid} | Partially updates an integration to the specified escalation level.
[**alert_definition_update_integration_for_escalation_with_put**](AlertDefinitionApi.md#alert_definition_update_integration_for_escalation_with_put) | **PUT** /AlertDefinition/{alertDefinitionGuid}/EscalationLevel/{escalationLevelId}/Integration/{integrationGuid} | Updates an integration for the specified escalation level.


# **alert_definition_add_monitor_group_to_alert_definition**
> AlertDefinitionMonitorGroup alert_definition_add_monitor_group_to_alert_definition(alert_definition_guid, monitor_group_guid)

Adds a monitor group to the specified alert definition.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition to modify.
monitor_group_guid = 'monitor_group_guid_example' # str | The Guid of the monitor group to add.

try:
    # Adds a monitor group to the specified alert definition.
    api_response = api_instance.alert_definition_add_monitor_group_to_alert_definition(alert_definition_guid, monitor_group_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_add_monitor_group_to_alert_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition_guid** | **str**| The Guid of the alert definition to modify. | 
 **monitor_group_guid** | **str**| The Guid of the monitor group to add. | 

### Return type

[**AlertDefinitionMonitorGroup**](AlertDefinitionMonitorGroup.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_add_monitor_to_alert_definition**
> AlertDefinitionMonitor alert_definition_add_monitor_to_alert_definition(alert_definition_guid, monitor_guid)

Adds a monitor to the specified alert definition.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition to modify.
monitor_guid = 'monitor_guid_example' # str | The Guid of the monitor to add.

try:
    # Adds a monitor to the specified alert definition.
    api_response = api_instance.alert_definition_add_monitor_to_alert_definition(alert_definition_guid, monitor_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_add_monitor_to_alert_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition_guid** | **str**| The Guid of the alert definition to modify. | 
 **monitor_guid** | **str**| The Guid of the monitor to add. | 

### Return type

[**AlertDefinitionMonitor**](AlertDefinitionMonitor.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_add_operator_group_to_escalation_level**
> AlertDefinitionOperatorGroup alert_definition_add_operator_group_to_escalation_level(alert_definition_guid, escalation_level_id, operator_group_guid)

Adds an operator group to the specified escalation level.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition.
escalation_level_id = 56 # int | The escalation level id.
operator_group_guid = 'operator_group_guid_example' # str | The Guid of the operator group to add.

try:
    # Adds an operator group to the specified escalation level.
    api_response = api_instance.alert_definition_add_operator_group_to_escalation_level(alert_definition_guid, escalation_level_id, operator_group_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_add_operator_group_to_escalation_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition_guid** | **str**| The Guid of the alert definition. | 
 **escalation_level_id** | **int**| The escalation level id. | 
 **operator_group_guid** | **str**| The Guid of the operator group to add. | 

### Return type

[**AlertDefinitionOperatorGroup**](AlertDefinitionOperatorGroup.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_add_operator_to_escalation_level**
> AlertDefinitionOperator alert_definition_add_operator_to_escalation_level(alert_definition_guid, escalation_level_id, operator_guid)

Adds an operator to the specified escalation level.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition.
escalation_level_id = 56 # int | The escalation level id.
operator_guid = 'operator_guid_example' # str | The Guid of the operator to add.

try:
    # Adds an operator to the specified escalation level.
    api_response = api_instance.alert_definition_add_operator_to_escalation_level(alert_definition_guid, escalation_level_id, operator_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_add_operator_to_escalation_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition_guid** | **str**| The Guid of the alert definition. | 
 **escalation_level_id** | **int**| The escalation level id. | 
 **operator_guid** | **str**| The Guid of the operator to add. | 

### Return type

[**AlertDefinitionOperator**](AlertDefinitionOperator.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_create_alert_definition**
> AlertDefinition alert_definition_create_alert_definition(alert_definition)

Creates a new alert definition.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition = uptrends.AlertDefinition() # AlertDefinition | The details of the alert definition to create.

try:
    # Creates a new alert definition.
    api_response = api_instance.alert_definition_create_alert_definition(alert_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_create_alert_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition** | [**AlertDefinition**](AlertDefinition.md)| The details of the alert definition to create. | 

### Return type

[**AlertDefinition**](AlertDefinition.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_delete_alert_definition**
> alert_definition_delete_alert_definition(alert_definition_guid)

Deletes an existing alert definition.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition to remove.

try:
    # Deletes an existing alert definition.
    api_instance.alert_definition_delete_alert_definition(alert_definition_guid)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_delete_alert_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition_guid** | **str**| The Guid of the alert definition to remove. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_get_all_alert_definitions**
> list[AlertDefinition] alert_definition_get_all_alert_definitions()

Gets a list of all alert definitions.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))

try:
    # Gets a list of all alert definitions.
    api_response = api_instance.alert_definition_get_all_alert_definitions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_get_all_alert_definitions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AlertDefinition]**](AlertDefinition.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_get_all_members**
> list[AlertDefinitionMember] alert_definition_get_all_members(alert_definition_guid)

Gets a list of all monitor and monitor group guids of the specified alert definition.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition for which to return the members.

try:
    # Gets a list of all monitor and monitor group guids of the specified alert definition.
    api_response = api_instance.alert_definition_get_all_members(alert_definition_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_get_all_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition_guid** | **str**| The Guid of the alert definition for which to return the members. | 

### Return type

[**list[AlertDefinitionMember]**](AlertDefinitionMember.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_get_escalation_level**
> list[EscalationLevel] alert_definition_get_escalation_level(alert_definition_guid, escalation_level_id)

Gets the escalation level information of the specified alert definition.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition.
escalation_level_id = 56 # int | The escalation level id.

try:
    # Gets the escalation level information of the specified alert definition.
    api_response = api_instance.alert_definition_get_escalation_level(alert_definition_guid, escalation_level_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_get_escalation_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition_guid** | **str**| The Guid of the alert definition. | 
 **escalation_level_id** | **int**| The escalation level id. | 

### Return type

[**list[EscalationLevel]**](EscalationLevel.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_get_escalation_level_integration**
> list[Integration] alert_definition_get_escalation_level_integration(alert_definition_guid, escalation_level_id)

Gets the integrations for the specified escalation level.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition.
escalation_level_id = 56 # int | The escalation level id.

try:
    # Gets the integrations for the specified escalation level.
    api_response = api_instance.alert_definition_get_escalation_level_integration(alert_definition_guid, escalation_level_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_get_escalation_level_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition_guid** | **str**| The Guid of the alert definition. | 
 **escalation_level_id** | **int**| The escalation level id. | 

### Return type

[**list[Integration]**](Integration.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_get_escalation_level_operator**
> list[AlertEscalationLevelMember] alert_definition_get_escalation_level_operator(alert_definition_guid, escalation_level_id)

Gets the operator and operator group guids for the specified escalation level.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition.
escalation_level_id = 56 # int | The escalation level id.

try:
    # Gets the operator and operator group guids for the specified escalation level.
    api_response = api_instance.alert_definition_get_escalation_level_operator(alert_definition_guid, escalation_level_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_get_escalation_level_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition_guid** | **str**| The Guid of the alert definition. | 
 **escalation_level_id** | **int**| The escalation level id. | 

### Return type

[**list[AlertEscalationLevelMember]**](AlertEscalationLevelMember.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_get_specified_alert_definitions**
> AlertDefinition alert_definition_get_specified_alert_definitions(alert_definition_guid)

Gets the specified alert definition.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition.

try:
    # Gets the specified alert definition.
    api_response = api_instance.alert_definition_get_specified_alert_definitions(alert_definition_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_get_specified_alert_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition_guid** | **str**| The Guid of the alert definition. | 

### Return type

[**AlertDefinition**](AlertDefinition.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_patch_alert_definition**
> alert_definition_patch_alert_definition(alert_definition, alert_definition_guid)

Partially updates the definition of the specified alert definition.

This methods accepts parts of an alert definition. Fields that do not require changes can be omitted.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition = uptrends.AlertDefinition() # AlertDefinition | The partial definition for the alert definition that should be updated.
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition that should be updated.

try:
    # Partially updates the definition of the specified alert definition.
    api_instance.alert_definition_patch_alert_definition(alert_definition, alert_definition_guid)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_patch_alert_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition** | [**AlertDefinition**](AlertDefinition.md)| The partial definition for the alert definition that should be updated. | 
 **alert_definition_guid** | **str**| The Guid of the alert definition that should be updated. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_put_alert_definition**
> alert_definition_put_alert_definition(alert_definition, alert_definition_guid)

Updates the definition of the specified alert definition.

This methods only accepts a complete alert definition where all fields are specified.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition = uptrends.AlertDefinition() # AlertDefinition | The partial definition for the alert definition that should be updated.
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition that should be updated.

try:
    # Updates the definition of the specified alert definition.
    api_instance.alert_definition_put_alert_definition(alert_definition, alert_definition_guid)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_put_alert_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition** | [**AlertDefinition**](AlertDefinition.md)| The partial definition for the alert definition that should be updated. | 
 **alert_definition_guid** | **str**| The Guid of the alert definition that should be updated. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_remove_monitor_from_alert_definition**
> alert_definition_remove_monitor_from_alert_definition(alert_definition_guid, monitor_guid)

Removes a monitor for the specified alert definition.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition to modify.
monitor_guid = 'monitor_guid_example' # str | The Guid of the monitor to remove.

try:
    # Removes a monitor for the specified alert definition.
    api_instance.alert_definition_remove_monitor_from_alert_definition(alert_definition_guid, monitor_guid)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_remove_monitor_from_alert_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition_guid** | **str**| The Guid of the alert definition to modify. | 
 **monitor_guid** | **str**| The Guid of the monitor to remove. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_remove_monitor_group_from_alert_definition**
> alert_definition_remove_monitor_group_from_alert_definition(alert_definition_guid, monitor_group_guid)

Removes a monitor group for the specified alert definition.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition to modify.
monitor_group_guid = 'monitor_group_guid_example' # str | The Guid of the monitor group to remove.

try:
    # Removes a monitor group for the specified alert definition.
    api_instance.alert_definition_remove_monitor_group_from_alert_definition(alert_definition_guid, monitor_group_guid)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_remove_monitor_group_from_alert_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition_guid** | **str**| The Guid of the alert definition to modify. | 
 **monitor_group_guid** | **str**| The Guid of the monitor group to remove. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_remove_operator_from_escalation_level**
> alert_definition_remove_operator_from_escalation_level(alert_definition_guid, escalation_level_id, operator_guid)

Removes an operator for the specified escalation level.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition.
escalation_level_id = 56 # int | The escalation level id.
operator_guid = 'operator_guid_example' # str | The Guid of the operator to remove.

try:
    # Removes an operator for the specified escalation level.
    api_instance.alert_definition_remove_operator_from_escalation_level(alert_definition_guid, escalation_level_id, operator_guid)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_remove_operator_from_escalation_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition_guid** | **str**| The Guid of the alert definition. | 
 **escalation_level_id** | **int**| The escalation level id. | 
 **operator_guid** | **str**| The Guid of the operator to remove. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_remove_operator_group_from_escalation_level**
> alert_definition_remove_operator_group_from_escalation_level(alert_definition_guid, escalation_level_id, operator_group_guid)

Removes an operator group for the specified escalation level.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition.
escalation_level_id = 56 # int | The escalation level id.
operator_group_guid = 'operator_group_guid_example' # str | The Guid of the operator group to remove.

try:
    # Removes an operator group for the specified escalation level.
    api_instance.alert_definition_remove_operator_group_from_escalation_level(alert_definition_guid, escalation_level_id, operator_group_guid)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_remove_operator_group_from_escalation_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_definition_guid** | **str**| The Guid of the alert definition. | 
 **escalation_level_id** | **int**| The escalation level id. | 
 **operator_group_guid** | **str**| The Guid of the operator group to remove. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_update_integration_for_escalation_with_patch**
> alert_definition_update_integration_for_escalation_with_patch(escalation_level_integration, alert_definition_guid, escalation_level_id, integration_guid)

Partially updates an integration to the specified escalation level.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
escalation_level_integration = uptrends.EscalationLevelIntegration() # EscalationLevelIntegration | The partial definition for the integration that should be updated.
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition.
escalation_level_id = 56 # int | The escalation level id.
integration_guid = 'integration_guid_example' # str | The Guid of the integration to update.

try:
    # Partially updates an integration to the specified escalation level.
    api_instance.alert_definition_update_integration_for_escalation_with_patch(escalation_level_integration, alert_definition_guid, escalation_level_id, integration_guid)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_update_integration_for_escalation_with_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **escalation_level_integration** | [**EscalationLevelIntegration**](EscalationLevelIntegration.md)| The partial definition for the integration that should be updated. | 
 **alert_definition_guid** | **str**| The Guid of the alert definition. | 
 **escalation_level_id** | **int**| The escalation level id. | 
 **integration_guid** | **str**| The Guid of the integration to update. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_definition_update_integration_for_escalation_with_put**
> alert_definition_update_integration_for_escalation_with_put(escalation_level_integration, alert_definition_guid, escalation_level_id, integration_guid)

Updates an integration for the specified escalation level.

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
api_instance = uptrends.AlertDefinitionApi(uptrends.ApiClient(configuration))
escalation_level_integration = uptrends.EscalationLevelIntegration() # EscalationLevelIntegration | The definition for the integration that should be updated.
alert_definition_guid = 'alert_definition_guid_example' # str | The Guid of the alert definition.
escalation_level_id = 56 # int | The escalation level id.
integration_guid = 'integration_guid_example' # str | The Guid of the integration to update.

try:
    # Updates an integration for the specified escalation level.
    api_instance.alert_definition_update_integration_for_escalation_with_put(escalation_level_integration, alert_definition_guid, escalation_level_id, integration_guid)
except ApiException as e:
    print("Exception when calling AlertDefinitionApi->alert_definition_update_integration_for_escalation_with_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **escalation_level_integration** | [**EscalationLevelIntegration**](EscalationLevelIntegration.md)| The definition for the integration that should be updated. | 
 **alert_definition_guid** | **str**| The Guid of the alert definition. | 
 **escalation_level_id** | **int**| The escalation level id. | 
 **integration_guid** | **str**| The Guid of the integration to update. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

