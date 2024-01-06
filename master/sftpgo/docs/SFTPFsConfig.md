# SFTPFsConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | remote SFTP endpoint as host:port | [optional]
**username** | **str** | you can specify a password or private key or both. In the latter case the private key will be tried first. | [optional]
**password** | [**Secret**](Secret.md) |  | [optional]
**private_key** | [**Secret**](Secret.md) |  | [optional]
**key_passphrase** | [**Secret**](Secret.md) |  | [optional]
**fingerprints** | **List[str]** | SHA256 fingerprints to use for host key verification. If you don&#39;t provide any fingerprint the remote host key will not be verified, this is a security risk | [optional]
**prefix** | **str** | Specifying a prefix you can restrict all operations to a given path within the remote SFTP server. | [optional]
**disable_concurrent_reads** | **bool** | Concurrent reads are safe to use and disabling them will degrade performance. Some servers automatically delete files once they are downloaded. Using concurrent reads is problematic with such servers. | [optional]
**buffer_size** | **int** | The size of the buffer (in MB) to use for transfers. By enabling buffering, the reads and writes, from/to the remote SFTP server, are split in multiple concurrent requests and this allows data to be transferred at a faster rate, over high latency networks, by overlapping round-trip times. With buffering enabled, resuming uploads is not supported and a file cannot be opened for both reading and writing at the same time. 0 means disabled. | [optional]
**equality_check_mode** | **int** | Defines how to check if this config points to the same server as another config. If different configs point to the same server the renaming between the fs configs is allowed:  * &#x60;0&#x60; username and endpoint must match. This is the default  * &#x60;1&#x60; only the endpoint must match  | [optional]

## Example

```python
from openapi_client.models.sftpfs_config import SFTPFsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SFTPFsConfig from a JSON string
sftpfs_config_instance = SFTPFsConfig.from_json(json)
# print the JSON string representation of the object
print SFTPFsConfig.to_json()

# convert the object into a dict
sftpfs_config_dict = sftpfs_config_instance.to_dict()
# create an instance of SFTPFsConfig from a dict
sftpfs_config_form_dict = sftpfs_config.from_dict(sftpfs_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
