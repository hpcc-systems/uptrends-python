# uptrends.VaultApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vault_create_authorization_for_vault_section**](VaultApi.md#vault_create_authorization_for_vault_section) | **POST** /VaultSection/{vaultSectionGuid}/Authorization | Creates a new authorization for the specified vault section. 
[**vault_create_new_vault_item**](VaultApi.md#vault_create_new_vault_item) | **POST** /VaultItem | Creates a new vault item.
[**vault_create_new_vault_section**](VaultApi.md#vault_create_new_vault_section) | **POST** /VaultSection | Creates a new vault section.
[**vault_delete_authorization_for_vault_section**](VaultApi.md#vault_delete_authorization_for_vault_section) | **DELETE** /VaultSection/{vaultSectionGuid}/Authorization/{authorizationGuid} | Deletes the specified authorization for the specified vault section. 
[**vault_delete_vault_item**](VaultApi.md#vault_delete_vault_item) | **DELETE** /VaultItem/{vaultItemGuid} | Deletes the specified vault item.
[**vault_delete_vault_section**](VaultApi.md#vault_delete_vault_section) | **DELETE** /VaultSection/{vaultSectionGuid} | Deletes the specified vault section.
[**vault_get_all_vault_items**](VaultApi.md#vault_get_all_vault_items) | **GET** /VaultItem | Returns all vault items.
[**vault_get_all_vault_sections**](VaultApi.md#vault_get_all_vault_sections) | **GET** /VaultSection | Returns all vault sections.
[**vault_get_authorizations_for_vault_section**](VaultApi.md#vault_get_authorizations_for_vault_section) | **GET** /VaultSection/{vaultSectionGuid}/Authorization | Returns all authorizations for the specified vault section.
[**vault_get_vault_item**](VaultApi.md#vault_get_vault_item) | **GET** /VaultItem/{vaultItemGuid} | Returns the specified vault item.
[**vault_get_vault_section**](VaultApi.md#vault_get_vault_section) | **GET** /VaultSection/{vaultSectionGuid} | Returns the specified vault section.
[**vault_update_vault_item**](VaultApi.md#vault_update_vault_item) | **PUT** /VaultItem/{vaultItemGuid} | Updates the specified vault item.
[**vault_update_vault_section**](VaultApi.md#vault_update_vault_section) | **PUT** /VaultSection/{vaultSectionGuid} | Updates the specified vault section.


# **vault_create_authorization_for_vault_section**
> VaultSectionAuthorization vault_create_authorization_for_vault_section(authorization, vault_section_guid)

Creates a new authorization for the specified vault section. 

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
api_instance = uptrends.VaultApi(uptrends.ApiClient(configuration))
authorization = uptrends.VaultSectionAuthorization() # VaultSectionAuthorization | 
vault_section_guid = 'vault_section_guid_example' # str | The Guid of the vault section for which to create the new authorization.

try:
    # Creates a new authorization for the specified vault section. 
    api_response = api_instance.vault_create_authorization_for_vault_section(authorization, vault_section_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaultApi->vault_create_authorization_for_vault_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | [**VaultSectionAuthorization**](VaultSectionAuthorization.md)|  | 
 **vault_section_guid** | **str**| The Guid of the vault section for which to create the new authorization. | 

### Return type

[**VaultSectionAuthorization**](VaultSectionAuthorization.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vault_create_new_vault_item**
> VaultItem vault_create_new_vault_item(item)

Creates a new vault item.

The VaultItemGuid field should be omitted

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
api_instance = uptrends.VaultApi(uptrends.ApiClient(configuration))
item = uptrends.VaultItem() # VaultItem | The item to create

try:
    # Creates a new vault item.
    api_response = api_instance.vault_create_new_vault_item(item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaultApi->vault_create_new_vault_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item** | [**VaultItem**](VaultItem.md)| The item to create | 

### Return type

[**VaultItem**](VaultItem.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vault_create_new_vault_section**
> VaultSection vault_create_new_vault_section(section)

Creates a new vault section.

When a new vault section is created, the user that created the section is granted View and Edit authorizations to that section. The VaultSectionGuid attribute should be omitted in the request body. The Guid of the newly created section will be returned in the response.

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
api_instance = uptrends.VaultApi(uptrends.ApiClient(configuration))
section = uptrends.VaultSection() # VaultSection | The attributes of the vault section that should be created.

try:
    # Creates a new vault section.
    api_response = api_instance.vault_create_new_vault_section(section)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaultApi->vault_create_new_vault_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section** | [**VaultSection**](VaultSection.md)| The attributes of the vault section that should be created. | 

### Return type

[**VaultSection**](VaultSection.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vault_delete_authorization_for_vault_section**
> vault_delete_authorization_for_vault_section(vault_section_guid, authorization_guid)

Deletes the specified authorization for the specified vault section. 

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
api_instance = uptrends.VaultApi(uptrends.ApiClient(configuration))
vault_section_guid = 'vault_section_guid_example' # str | The Guid of the vault section for which the authorization should be deleted.
authorization_guid = 'authorization_guid_example' # str | The Guid of the authorization that should be deleted.

try:
    # Deletes the specified authorization for the specified vault section. 
    api_instance.vault_delete_authorization_for_vault_section(vault_section_guid, authorization_guid)
except ApiException as e:
    print("Exception when calling VaultApi->vault_delete_authorization_for_vault_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_section_guid** | **str**| The Guid of the vault section for which the authorization should be deleted. | 
 **authorization_guid** | **str**| The Guid of the authorization that should be deleted. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vault_delete_vault_item**
> vault_delete_vault_item(vault_item_guid)

Deletes the specified vault item.

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
api_instance = uptrends.VaultApi(uptrends.ApiClient(configuration))
vault_item_guid = 'vault_item_guid_example' # str | The Guid of the vault item that should be deleted.

try:
    # Deletes the specified vault item.
    api_instance.vault_delete_vault_item(vault_item_guid)
except ApiException as e:
    print("Exception when calling VaultApi->vault_delete_vault_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_item_guid** | **str**| The Guid of the vault item that should be deleted. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vault_delete_vault_section**
> vault_delete_vault_section(vault_section_guid)

Deletes the specified vault section.

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
api_instance = uptrends.VaultApi(uptrends.ApiClient(configuration))
vault_section_guid = 'vault_section_guid_example' # str | The Guid of the vault section that should be deleted.

try:
    # Deletes the specified vault section.
    api_instance.vault_delete_vault_section(vault_section_guid)
except ApiException as e:
    print("Exception when calling VaultApi->vault_delete_vault_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_section_guid** | **str**| The Guid of the vault section that should be deleted. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vault_get_all_vault_items**
> list[VaultItem] vault_get_all_vault_items()

Returns all vault items.

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
api_instance = uptrends.VaultApi(uptrends.ApiClient(configuration))

try:
    # Returns all vault items.
    api_response = api_instance.vault_get_all_vault_items()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaultApi->vault_get_all_vault_items: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VaultItem]**](VaultItem.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vault_get_all_vault_sections**
> list[VaultSection] vault_get_all_vault_sections()

Returns all vault sections.

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
api_instance = uptrends.VaultApi(uptrends.ApiClient(configuration))

try:
    # Returns all vault sections.
    api_response = api_instance.vault_get_all_vault_sections()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaultApi->vault_get_all_vault_sections: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VaultSection]**](VaultSection.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vault_get_authorizations_for_vault_section**
> VaultSectionAuthorization vault_get_authorizations_for_vault_section(vault_section_guid)

Returns all authorizations for the specified vault section.

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
api_instance = uptrends.VaultApi(uptrends.ApiClient(configuration))
vault_section_guid = 'vault_section_guid_example' # str | The Guid of the vault section for which to return authorizations.

try:
    # Returns all authorizations for the specified vault section.
    api_response = api_instance.vault_get_authorizations_for_vault_section(vault_section_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaultApi->vault_get_authorizations_for_vault_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_section_guid** | **str**| The Guid of the vault section for which to return authorizations. | 

### Return type

[**VaultSectionAuthorization**](VaultSectionAuthorization.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vault_get_vault_item**
> VaultItem vault_get_vault_item(vault_item_guid)

Returns the specified vault item.

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
api_instance = uptrends.VaultApi(uptrends.ApiClient(configuration))
vault_item_guid = 'vault_item_guid_example' # str | The Guid of the requested vault item.

try:
    # Returns the specified vault item.
    api_response = api_instance.vault_get_vault_item(vault_item_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaultApi->vault_get_vault_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_item_guid** | **str**| The Guid of the requested vault item. | 

### Return type

[**VaultItem**](VaultItem.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vault_get_vault_section**
> VaultSection vault_get_vault_section(vault_section_guid)

Returns the specified vault section.

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
api_instance = uptrends.VaultApi(uptrends.ApiClient(configuration))
vault_section_guid = 'vault_section_guid_example' # str | The Guid of the requested vault section.

try:
    # Returns the specified vault section.
    api_response = api_instance.vault_get_vault_section(vault_section_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaultApi->vault_get_vault_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_section_guid** | **str**| The Guid of the requested vault section. | 

### Return type

[**VaultSection**](VaultSection.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vault_update_vault_item**
> vault_update_vault_item(item, vault_item_guid)

Updates the specified vault item.

Only complete definitions are accepted. Fields not specified will be NULLed.

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
api_instance = uptrends.VaultApi(uptrends.ApiClient(configuration))
item = uptrends.VaultItem() # VaultItem | The complete definition of the vault item that should be updated.
vault_item_guid = 'vault_item_guid_example' # str | The Guid of the vault item that should be updated.

try:
    # Updates the specified vault item.
    api_instance.vault_update_vault_item(item, vault_item_guid)
except ApiException as e:
    print("Exception when calling VaultApi->vault_update_vault_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item** | [**VaultItem**](VaultItem.md)| The complete definition of the vault item that should be updated. | 
 **vault_item_guid** | **str**| The Guid of the vault item that should be updated. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vault_update_vault_section**
> vault_update_vault_section(item, vault_section_guid)

Updates the specified vault section.

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
api_instance = uptrends.VaultApi(uptrends.ApiClient(configuration))
item = uptrends.VaultSection() # VaultSection | 
vault_section_guid = 'vault_section_guid_example' # str | The Guid of the vault section that should be updated.

try:
    # Updates the specified vault section.
    api_instance.vault_update_vault_section(item, vault_section_guid)
except ApiException as e:
    print("Exception when calling VaultApi->vault_update_vault_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item** | [**VaultSection**](VaultSection.md)|  | 
 **vault_section_guid** | **str**| The Guid of the vault section that should be updated. | 

### Return type

void (empty response body)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

