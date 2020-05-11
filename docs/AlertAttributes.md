# AlertAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_type** | **object** | Alert type indicating if this was an Error or Ok alert. | 
**monitor_guid** | **str** | The monitor identifier. | 
**timestamp** | **datetime** | Date/time stamp of the alert. | 
**first_error** | **datetime** | Date/time stamp of the first monitor check. | 
**monitor_check_id** | **int** | The Id of the monitor check that triggered this alert. | 
**first_error_monitor_check_id** | **int** | The Id of the first monitor check error that led to this alert. | 
**error_description** | **str** | A text value that describes the error that was found, or OK if no error was found. | [optional] 
**error_message** | **str** | Any additional error information, if available. | [optional] 
**incident_key** | **str** | The incident key of this alert. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


