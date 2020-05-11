# uptrends.CheckpointApi

All URIs are relative to *https://api.uptrends.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkpoint_get_all_checkpoints**](CheckpointApi.md#checkpoint_get_all_checkpoints) | **GET** /Checkpoint | Returns all the checkpoints. 
[**checkpoint_get_checkpoint**](CheckpointApi.md#checkpoint_get_checkpoint) | **GET** /Checkpoint/{checkpointId} | Returns the specified checkpoint. 
[**checkpoint_region_get_all_checkpoint_regions**](CheckpointApi.md#checkpoint_region_get_all_checkpoint_regions) | **GET** /CheckpointRegion | Returns all the checkpoint regions. 
[**checkpoint_region_get_checkpoint_region_checkpoints**](CheckpointApi.md#checkpoint_region_get_checkpoint_region_checkpoints) | **GET** /CheckpointRegion/{checkpointRegionId}/Checkpoint | Returns the checkpoints for the specified checkpoint region. 
[**checkpoint_region_get_specified_checkpoint_region**](CheckpointApi.md#checkpoint_region_get_specified_checkpoint_region) | **GET** /CheckpointRegion/{checkpointRegionId} | Returns the specified checkpoint region. 
[**checkpoint_server_get_all_server_ipv4_addresses**](CheckpointApi.md#checkpoint_server_get_all_server_ipv4_addresses) | **GET** /Checkpoint/Server/Ipv4 | Anonymous call that returns all the IPv4 addresses of all the checkpoint servers. 
[**checkpoint_server_get_all_server_ipv6_addresses**](CheckpointApi.md#checkpoint_server_get_all_server_ipv6_addresses) | **GET** /Checkpoint/Server/Ipv6 | Anonymous call that returns all the IPv6 addresses of all the checkpoint servers. 
[**checkpoint_server_get_server**](CheckpointApi.md#checkpoint_server_get_server) | **GET** /Checkpoint/Server/{serverId} | Returns the requested checkpoint server.


# **checkpoint_get_all_checkpoints**
> list[Checkpoint] checkpoint_get_all_checkpoints()

Returns all the checkpoints. 

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
api_instance = uptrends.CheckpointApi(uptrends.ApiClient(configuration))

try:
    # Returns all the checkpoints. 
    api_response = api_instance.checkpoint_get_all_checkpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckpointApi->checkpoint_get_all_checkpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Checkpoint]**](Checkpoint.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkpoint_get_checkpoint**
> Checkpoint checkpoint_get_checkpoint(checkpoint_id)

Returns the specified checkpoint. 

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
api_instance = uptrends.CheckpointApi(uptrends.ApiClient(configuration))
checkpoint_id = 56 # int | The Id of the requested checkpoint.

try:
    # Returns the specified checkpoint. 
    api_response = api_instance.checkpoint_get_checkpoint(checkpoint_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckpointApi->checkpoint_get_checkpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkpoint_id** | **int**| The Id of the requested checkpoint. | 

### Return type

[**Checkpoint**](Checkpoint.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkpoint_region_get_all_checkpoint_regions**
> list[CheckpointRegion] checkpoint_region_get_all_checkpoint_regions()

Returns all the checkpoint regions. 

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
api_instance = uptrends.CheckpointApi(uptrends.ApiClient(configuration))

try:
    # Returns all the checkpoint regions. 
    api_response = api_instance.checkpoint_region_get_all_checkpoint_regions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckpointApi->checkpoint_region_get_all_checkpoint_regions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CheckpointRegion]**](CheckpointRegion.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkpoint_region_get_checkpoint_region_checkpoints**
> list[Checkpoint] checkpoint_region_get_checkpoint_region_checkpoints(checkpoint_region_id)

Returns the checkpoints for the specified checkpoint region. 

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
api_instance = uptrends.CheckpointApi(uptrends.ApiClient(configuration))
checkpoint_region_id = 56 # int | The id for the specified checkpoint region.

try:
    # Returns the checkpoints for the specified checkpoint region. 
    api_response = api_instance.checkpoint_region_get_checkpoint_region_checkpoints(checkpoint_region_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckpointApi->checkpoint_region_get_checkpoint_region_checkpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkpoint_region_id** | **int**| The id for the specified checkpoint region. | 

### Return type

[**list[Checkpoint]**](Checkpoint.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkpoint_region_get_specified_checkpoint_region**
> CheckpointRegion checkpoint_region_get_specified_checkpoint_region(checkpoint_region_id)

Returns the specified checkpoint region. 

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
api_instance = uptrends.CheckpointApi(uptrends.ApiClient(configuration))
checkpoint_region_id = 56 # int | The id for the specified checkpoint region.

try:
    # Returns the specified checkpoint region. 
    api_response = api_instance.checkpoint_region_get_specified_checkpoint_region(checkpoint_region_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckpointApi->checkpoint_region_get_specified_checkpoint_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkpoint_region_id** | **int**| The id for the specified checkpoint region. | 

### Return type

[**CheckpointRegion**](CheckpointRegion.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkpoint_server_get_all_server_ipv4_addresses**
> list[str] checkpoint_server_get_all_server_ipv4_addresses()

Anonymous call that returns all the IPv4 addresses of all the checkpoint servers. 

### Example
```python
from __future__ import print_function
import time
import uptrends
from uptrends.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uptrends.CheckpointApi()

try:
    # Anonymous call that returns all the IPv4 addresses of all the checkpoint servers. 
    api_response = api_instance.checkpoint_server_get_all_server_ipv4_addresses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckpointApi->checkpoint_server_get_all_server_ipv4_addresses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkpoint_server_get_all_server_ipv6_addresses**
> list[str] checkpoint_server_get_all_server_ipv6_addresses()

Anonymous call that returns all the IPv6 addresses of all the checkpoint servers. 

### Example
```python
from __future__ import print_function
import time
import uptrends
from uptrends.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = uptrends.CheckpointApi()

try:
    # Anonymous call that returns all the IPv6 addresses of all the checkpoint servers. 
    api_response = api_instance.checkpoint_server_get_all_server_ipv6_addresses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckpointApi->checkpoint_server_get_all_server_ipv6_addresses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkpoint_server_get_server**
> CheckpointServer checkpoint_server_get_server(server_id)

Returns the requested checkpoint server.

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
api_instance = uptrends.CheckpointApi(uptrends.ApiClient(configuration))
server_id = 56 # int | The Id of the requested server.

try:
    # Returns the requested checkpoint server.
    api_response = api_instance.checkpoint_server_get_server(server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckpointApi->checkpoint_server_get_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **int**| The Id of the requested server. | 

### Return type

[**CheckpointServer**](CheckpointServer.md)

### Authorization

[basicauth](../README.md#basicauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

