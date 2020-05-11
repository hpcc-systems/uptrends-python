# PageElement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the element in the waterfall context | 
**start_time** | **int** | Starting time in milliseconds | 
**resolve_time** | **int** | Number of milliseconds needed to perform the DNS query for this element, when appropriate. | 
**connect_time** | **int** | Number of milliseconds needed to establish a connection. | 
**stale_time** | **int** | Number of milliseconds the connection was stale | 
**https_handshake_time** | **int** | Number of milliseconds needed for the HTTPS handshake | 
**send_time** | **int** | Number of milliseconds it took to send data | 
**wait_time** | **int** | Number of milliseconds the connection was in waiting state | 
**receive_time** | **int** | Number of milliseconds it took to retrieve the data | 
**timeout_time** | **int** | Number of milliseconds the connection was timed-out  | 
**total_time** | **int** | Total number of milliseconds it took for the connection to complete | 
**http_status_code** | **int** | The Http status code | 
**url** | **str** | The requested resource url | [optional] 
**total_bytes** | **int** | Total number of downloaded bytes | 
**element_type** | **str** | Requested resource element type, can be HTML, scripts, CSS, images, frames, objects, data and other | [optional] 
**request_headers** | **str** | The HTTP request headers used | [optional] 
**response_headers** | **str** | The HTTP response headers retrieved | [optional] 
**resolved_ip_address** | **object** | The IP address that was found for the specified domain name as part of this monitor check. | [optional] 
**group_ids** | **list[int]** |  | [optional] 
**url_is_blocked** | **bool** | Was the Url excluded from waterfall (timing) data by the user? | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


