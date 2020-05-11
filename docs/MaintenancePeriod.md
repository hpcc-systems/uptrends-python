# MaintenancePeriod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique ID of this maintenance period | 
**schedule_mode** | **object** | The schedule mode (one time, daily, weekly, monthly) | 
**start_date_time** | **datetime** | The start date/time for this schedule (for one-time schedules only) | [optional] 
**end_date_time** | **datetime** | The end date/time for this maintenance period (for one-time maintenance periods only) | [optional] 
**week_day** | **object** | The weekday for this maintenance period (for weekly maintenance periods only) | [optional] 
**month_day** | **int** | the month day for this maintenance period (for montly maintenance periods only) | [optional] 
**start_time** | **str** | The start time of this maintenance period | [optional] 
**end_time** | **str** | The end time of this maintenance period | [optional] 
**maintenance_type** | **object** | Indicates whether, during the maintenance periods, only alerting will be disabled, or if the entire monitor will be stopped | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


