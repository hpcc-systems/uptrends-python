# VaultItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_item_guid** | **str** | The unique key of this vault item | 
**hash** | **str** | The hash of this vault item | [optional] 
**name** | **str** | The name of this vault item | [optional] 
**value** | **str** | The value that is stored in this vault item. Not used for Certificate Archives | [optional] 
**vault_section_guid** | **str** | The unique identifier of the vault section that this vault item belongs to | 
**vault_item_type** | **object** | The vault item type | 
**is_sensitive** | **bool** | Whether or not the vault item is considered sensitive.  | 
**notes** | **str** | Notes about this vault item | [optional] 
**user_name** | **str** | The UserName of a credentialset | [optional] 
**password** | **str** | The password associated with a credentialset | [optional] 
**certificate_archive** | **object** | The certificate archive that is stored in this vault item, if applicable | [optional] 
**file_info** | **object** | The file info that is stored in this vault item, if applicable | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


