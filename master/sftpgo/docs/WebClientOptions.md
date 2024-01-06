# WebClientOptions

Options:   * `publickey-change-disabled` - changing SSH public keys is not allowed   * `write-disabled` - upload, rename, delete are not allowed even if the user has permissions for these actions   * `mfa-disabled` - enabling multi-factor authentication is not allowed. This option cannot be set if the user has MFA already enabled   * `password-change-disabled` - changing password is not allowed   * `api-key-auth-change-disabled` - enabling/disabling API key authentication is not allowed   * `info-change-disabled` - changing info such as email and description is not allowed   * `shares-disabled` - sharing files and directories with external users is not allowed   * `password-reset-disabled` - resetting the password is not allowed   * `shares-without-password-disabled` - creating shares without password protection is not allowed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
