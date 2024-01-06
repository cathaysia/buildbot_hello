# VersionInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional]
**build_date** | **str** |  | [optional]
**commit_hash** | **str** |  | [optional]
**features** | **List[str]** | Features for the current build. Available features are &#x60;portable&#x60;, &#x60;bolt&#x60;, &#x60;mysql&#x60;, &#x60;sqlite&#x60;, &#x60;pgsql&#x60;, &#x60;s3&#x60;, &#x60;gcs&#x60;, &#x60;azblob&#x60;, &#x60;metrics&#x60;, &#x60;unixcrypt&#x60;. If a feature is available it has a &#x60;+&#x60; prefix, otherwise a &#x60;-&#x60; prefix | [optional]

## Example

```python
from openapi_client.models.version_info import VersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VersionInfo from a JSON string
version_info_instance = VersionInfo.from_json(json)
# print the JSON string representation of the object
print VersionInfo.to_json()

# convert the object into a dict
version_info_dict = version_info_instance.to_dict()
# create an instance of VersionInfo from a dict
version_info_form_dict = version_info.from_dict(version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
