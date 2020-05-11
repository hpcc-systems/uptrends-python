# MonitorCheckAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_guid** | **str** | Monitor identifier | 
**timestamp** | **datetime** | Date/time stamp of the check | 
**error_code** | **int** | The numeric Uptrends error code in case of an error result, or 0 in case of an OK result. | 
**total_time** | **float** | The number of milliseconds needed to complete the monitor check. | 
**resolve_time** | **float** | The number of milliseconds needed to perform the DNS query for this check, when appropriate. | 
**connection_time** | **float** | The number of milliseconds needed to establish a connection. | 
**download_time** | **float** | The number of milliseconds needed to download the response data. | 
**total_bytes** | **int** | The number of downloaded bytes for this check. | [optional] 
**resolved_ip_address** | **str** | The IP address that was found for the specified domain name as part of this monitor check. | [optional] 
**error_level** | **object** | A value that represents the OK/Error state for this check: NoError if the result was OK, Unconfirmed if an error was found, Confirmed if an error was found as a double check, right after an Unconfirmed error. | 
**error_description** | **str** | A text value that describes the error that was found, or OK if no error was found. | [optional] 
**error_message** | **str** | Any additional error information, if available. | [optional] 
**staging_mode** | **bool** | Did the check come from a staging monitor? | 
**server_id** | **int** | The Id of the Uptrends checkpoint server that performed this check. | 
**http_status_code** | **int** | The HTTP status code returned (if applicable) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


