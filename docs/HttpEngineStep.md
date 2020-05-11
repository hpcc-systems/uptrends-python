# HttpEngineStep

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_name** | **str** | The name of the step | [optional] 
**url** | **str** | Url the step was executed on | [optional] 
**http_status_code** | **str** | The HTTP status code returned | [optional] 
**http_method** | **str** | Http method used in this step | [optional] 
**http_status_description** | **str** | Step description | [optional] 
**response_completed** | **bool** | Did the response complete? | 
**step_executed** | **bool** | Was this step executed? | 
**assertion_results_info** | **object** | Results of the assertions in this step | [optional] 
**total_time** | **int** | Number of milliseconds it took for this step to succeed | 
**response_headers** | **str** | Response headers | [optional] 
**response_body** | **str** | Response body | [optional] 
**request_headers** | **str** | Request headers send | [optional] 
**request_body** | **str** | Request body send | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


