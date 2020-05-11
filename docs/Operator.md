# Operator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator_guid** | **str** | The unique identifier of this operator | [optional] 
**hash** | **str** | The hash of this operator. | [optional] 
**password** | **str** | The password is a required field if AllowNativeLogin is set to True | [optional] 
**full_name** | **str** | The full name of this operator | [optional] 
**email** | **str** | The email address of this operator. This also serves as the username | [optional] 
**mobile_phone** | **str** | The phone number of this operator to which SMS and phone alerts can be sent. Start with a plus (+) sign and your country code | [optional] 
**outgoing_phone_number_id** | **int** | The id of the phone number that will be used to send phone alerts (See /OutgoingPhoneNumber API under Miscellaneous for available ids) | [optional] 
**outgoing_phone_number_id_specified** | **bool** |  | [optional] 
**is_account_administrator** | **bool** | This indicates if the operator is the account administrator. | [optional] 
**backup_email** | **str** | The backup email address of this operator | [optional] 
**is_on_duty** | **bool** | Indicates whether the operator is currently active | [optional] 
**culture_name** | **str** | If ommitted the operator will use the account culture. If set it will override the account default | [optional] 
**culture_name_specified** | **bool** |  | [optional] 
**time_zone_id** | **int** | The id of the timezone of this operator (See /Timezone API under Miscellaneous for available timezones) | [optional] 
**time_zone_id_specified** | **bool** |  | [optional] 
**sms_provider** | **object** | The SMS provider used to send out SMS alerts | [optional] 
**use_numeric_sender** | **bool** | Set to True to override the default behavior of sending SMS alerts with textual sender ID | [optional] 
**use_numeric_sender_specified** | **bool** |  | [optional] 
**allow_native_login** | **bool** | This can only be set to false if the account has SSO enabled. Ommitting or providing null will use the account default | [optional] 
**allow_native_login_specified** | **bool** |  | [optional] 
**allow_single_signon** | **bool** | This can only be set to true if the account has SSO enabled. Ommitting or providing null will use the account default | [optional] 
**allow_single_signon_specified** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


