# StepTimingInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**start_utc** | **datetime** |  | 
**end_utc** | **datetime** |  | 
**elapsed_milliseconds** | **int** |  | 
**delay_milliseconds** | **int** |  | 
**sub_timing_infos** | [**list[StepTimingInfo]**](StepTimingInfo.md) |  | [optional] 
**is_valid** | **bool** | If true, this TimingInfo should be counted as part of the sum of its siblings. If false, the TimingInfo should be discarded (e.g. for PreDelays we don&#39;t want to count). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


