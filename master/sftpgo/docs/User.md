# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional]
**status** | **int** | status:   * &#x60;0&#x60; user is disabled, login is not allowed   * &#x60;1&#x60; user is enabled  | [optional]
**username** | **str** | username is unique | [optional]
**email** | **str** |  | [optional]
**description** | **str** | optional description, for example the user full name | [optional]
**expiration_date** | **int** | expiration date as unix timestamp in milliseconds. An expired account cannot login. 0 means no expiration | [optional]
**password** | **str** | If the password has no known hashing algo prefix it will be stored, by default, using bcrypt, argon2id is supported too. You can send a password hashed as bcrypt ($2a$ prefix), argon2id, pbkdf2 or unix crypt and it will be stored as is. For security reasons this field is omitted when you search/get users | [optional]
**public_keys** | **List[str]** | Public keys in OpenSSH format. | [optional]
**has_password** | **bool** | Indicates whether the password is set | [optional]
**home_dir** | **str** | path to the user home directory. The user cannot upload or download files outside this directory. SFTPGo tries to automatically create this folder if missing. Must be an absolute path | [optional]
**virtual_folders** | [**List[VirtualFolder]**](VirtualFolder.md) | mapping between virtual SFTPGo paths and virtual folders. If one or more of the specified folders are not inside the dataprovider they will be automatically created. You have to create the folder on the filesystem yourself | [optional]
**uid** | **int** | if you run SFTPGo as root user, the created files and directories will be assigned to this uid. 0 means no change, the owner will be the user that runs SFTPGo. Ignored on windows | [optional]
**gid** | **int** | if you run SFTPGo as root user, the created files and directories will be assigned to this gid. 0 means no change, the group will be the one of the user that runs SFTPGo. Ignored on windows | [optional]
**max_sessions** | **int** | Limit the sessions that a user can open. 0 means unlimited | [optional]
**quota_size** | **int** | Quota as size in bytes. 0 means unlimited. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed | [optional]
**quota_files** | **int** | Quota as number of files. 0 means unlimited. Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed | [optional]
**permissions** | **Dict[str, List[Permission]]** | hash map with directory as key and an array of permissions as value. Directories must be absolute paths, permissions for root directory (\&quot;/\&quot;) are required | [optional]
**used_quota_size** | **int** |  | [optional]
**used_quota_files** | **int** |  | [optional]
**last_quota_update** | **int** | Last quota update as unix timestamp in milliseconds | [optional]
**upload_bandwidth** | **int** | Maximum upload bandwidth as KB/s, 0 means unlimited | [optional]
**download_bandwidth** | **int** | Maximum download bandwidth as KB/s, 0 means unlimited | [optional]
**upload_data_transfer** | **int** | Maximum data transfer allowed for uploads as MB. 0 means no limit | [optional]
**download_data_transfer** | **int** | Maximum data transfer allowed for downloads as MB. 0 means no limit | [optional]
**total_data_transfer** | **int** | Maximum total data transfer as MB. 0 means unlimited. You can set a total data transfer instead of the individual values for uploads and downloads | [optional]
**used_upload_data_transfer** | **int** | Uploaded size, as bytes, since the last reset | [optional]
**used_download_data_transfer** | **int** | Downloaded size, as bytes, since the last reset | [optional]
**created_at** | **int** | creation time as unix timestamp in milliseconds. It will be 0 for users created before v2.2.0 | [optional]
**updated_at** | **int** | last update time as unix timestamp in milliseconds | [optional]
**last_login** | **int** | Last user login as unix timestamp in milliseconds. It is saved at most once every 10 minutes | [optional]
**first_download** | **int** | first download time as unix timestamp in milliseconds | [optional]
**first_upload** | **int** | first upload time as unix timestamp in milliseconds | [optional]
**last_password_change** | **int** | last password change time as unix timestamp in milliseconds | [optional]
**filters** | [**UserFilters**](UserFilters.md) |  | [optional]
**filesystem** | [**FilesystemConfig**](FilesystemConfig.md) |  | [optional]
**additional_info** | **str** | Free form text field for external systems | [optional]
**groups** | [**List[GroupMapping]**](GroupMapping.md) |  | [optional]
**oidc_custom_fields** | **Dict[str, object]** | This field is passed to the pre-login hook if custom OIDC token fields have been configured. Field values can be of any type (this is a free form object) and depend on the type of the configured OIDC token fields | [optional]
**role** | **str** |  | [optional]

## Example

```python
from openapi_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
