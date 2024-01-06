# GCSConfig

Google Cloud Storage configuration details. The \"credentials\" field must be populated only when adding/updating a user. It will be always omitted, since there are sensitive data, when you search/get users

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | [optional]
**credentials** | [**Secret**](Secret.md) |  | [optional]
**automatic_credentials** | **int** | Automatic credentials:   * &#x60;0&#x60; - disabled, explicit credentials, using a JSON credentials file, must be provided. This is the default value if the field is null   * &#x60;1&#x60; - enabled, we try to use the Application Default Credentials (ADC) strategy to find your application&#39;s credentials  | [optional]
**storage_class** | **str** |  | [optional]
**acl** | **str** | The ACL to apply to uploaded objects. Leave empty to use the default ACL. For more information and available ACLs, refer to the JSON API here: https://cloud.google.com/storage/docs/access-control/lists#predefined-acl | [optional]
**key_prefix** | **str** | key_prefix is similar to a chroot directory for a local filesystem. If specified the user will only see contents that starts with this prefix and so you can restrict access to a specific virtual folder. The prefix, if not empty, must not start with \&quot;/\&quot; and must end with \&quot;/\&quot;. If empty the whole bucket contents will be available | [optional]
**upload_part_size** | **int** | The buffer size (in MB) to use for multipart uploads. The default value is 16MB. 0 means use the default | [optional]
**upload_part_max_time** | **int** | The maximum time allowed, in seconds, to upload a single chunk. The default value is 32. 0 means use the default | [optional]

## Example

```python
from openapi_client.models.gcs_config import GCSConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GCSConfig from a JSON string
gcs_config_instance = GCSConfig.from_json(json)
# print the JSON string representation of the object
print GCSConfig.to_json()

# convert the object into a dict
gcs_config_dict = gcs_config_instance.to_dict()
# create an instance of GCSConfig from a dict
gcs_config_form_dict = gcs_config.from_dict(gcs_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
