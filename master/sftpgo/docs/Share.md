# Share


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | auto-generated unique share identifier | [optional]
**name** | **str** |  | [optional]
**description** | **str** | optional description | [optional]
**scope** | [**ShareScope**](ShareScope.md) |  | [optional]
**paths** | **List[str]** | paths to files or directories, for share scope write this array must contain exactly one directory. Paths will not be validated on save so you can also create them after creating the share | [optional]
**username** | **str** |  | [optional]
**created_at** | **int** | creation time as unix timestamp in milliseconds | [optional]
**updated_at** | **int** | last update time as unix timestamp in milliseconds | [optional]
**last_use_at** | **int** | last use time as unix timestamp in milliseconds | [optional]
**expires_at** | **int** | optional share expiration, as unix timestamp in milliseconds. 0 means no expiration | [optional]
**password** | **str** | optional password to protect the share. The special value \&quot;[**redacted**]\&quot; means that a password has been set, you can use this value if you want to preserve the current password when you update a share | [optional]
**max_tokens** | **int** | maximum allowed access tokens. 0 means no limit | [optional]
**used_tokens** | **int** |  | [optional]
**allow_from** | **List[str]** | Limit the share availability to these IP/Mask. IP/Mask must be in CIDR notation as defined in RFC 4632 and RFC 4291, for example \&quot;192.0.2.0/24\&quot; or \&quot;2001:db8::/32\&quot;. An empty list means no restrictions | [optional]

## Example

```python
from openapi_client.models.share import Share

# TODO update the JSON string below
json = "{}"
# create an instance of Share from a JSON string
share_instance = Share.from_json(json)
# print the JSON string representation of the object
print Share.to_json()

# convert the object into a dict
share_dict = share_instance.to_dict()
# create an instance of Share from a dict
share_form_dict = share.from_dict(share_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
