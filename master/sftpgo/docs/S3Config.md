# S3Config

S3 Compatible Object Storage configuration details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | [optional]
**region** | **str** |  | [optional]
**access_key** | **str** |  | [optional]
**access_secret** | [**Secret**](Secret.md) |  | [optional]
**role_arn** | **str** | Optional IAM Role ARN to assume | [optional]
**endpoint** | **str** | optional endpoint | [optional]
**storage_class** | **str** |  | [optional]
**acl** | **str** | The canned ACL to apply to uploaded objects. Leave empty to use the default ACL. For more information and available ACLs, see here: https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl | [optional]
**upload_part_size** | **int** | the buffer size (in MB) to use for multipart uploads. The minimum allowed part size is 5MB, and if this value is set to zero, the default value (5MB) for the AWS SDK will be used. The minimum allowed value is 5. | [optional]
**upload_concurrency** | **int** | the number of parts to upload in parallel. If this value is set to zero, the default value (5) will be used | [optional]
**upload_part_max_time** | **int** | the maximum time allowed, in seconds, to upload a single chunk (the chunk size is defined via \&quot;upload_part_size\&quot;). 0 means no timeout | [optional]
**download_part_size** | **int** | the buffer size (in MB) to use for multipart downloads. The minimum allowed part size is 5MB, and if this value is set to zero, the default value (5MB) for the AWS SDK will be used. The minimum allowed value is 5. Ignored for partial downloads | [optional]
**download_concurrency** | **int** | the number of parts to download in parallel. If this value is set to zero, the default value (5) will be used. Ignored for partial downloads | [optional]
**download_part_max_time** | **int** | the maximum time allowed, in seconds, to download a single chunk (the chunk size is defined via \&quot;download_part_size\&quot;). 0 means no timeout. Ignored for partial downloads. | [optional]
**force_path_style** | **bool** | Set this to \&quot;true\&quot; to force the request to use path-style addressing, i.e., \&quot;http://s3.amazonaws.com/BUCKET/KEY\&quot;. By default, the S3 client will use virtual hosted bucket addressing when possible (\&quot;http://BUCKET.s3.amazonaws.com/KEY\&quot;) | [optional]
**key_prefix** | **str** | key_prefix is similar to a chroot directory for a local filesystem. If specified the user will only see contents that starts with this prefix and so you can restrict access to a specific virtual folder. The prefix, if not empty, must not start with \&quot;/\&quot; and must end with \&quot;/\&quot;. If empty the whole bucket contents will be available | [optional]

## Example

```python
from openapi_client.models.s3_config import S3Config

# TODO update the JSON string below
json = "{}"
# create an instance of S3Config from a JSON string
s3_config_instance = S3Config.from_json(json)
# print the JSON string representation of the object
print S3Config.to_json()

# convert the object into a dict
s3_config_dict = s3_config_instance.to_dict()
# create an instance of S3Config from a dict
s3_config_form_dict = s3_config.from_dict(s3_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
