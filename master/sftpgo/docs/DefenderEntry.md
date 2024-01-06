# DefenderEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional]
**ip** | **str** |  | [optional]
**score** | **int** | the score increases whenever a violation is detected, such as an attempt to log in using an incorrect password or invalid username. If the score exceeds the configured threshold, the IP is banned. Omitted for banned IPs | [optional]
**ban_time** | **datetime** | date time until the IP is banned. For already banned hosts, the ban time is increased each time a new violation is detected. Omitted if the IP is not banned | [optional]

## Example

```python
from openapi_client.models.defender_entry import DefenderEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DefenderEntry from a JSON string
defender_entry_instance = DefenderEntry.from_json(json)
# print the JSON string representation of the object
print DefenderEntry.to_json()

# convert the object into a dict
defender_entry_dict = defender_entry_instance.to_dict()
# create an instance of DefenderEntry from a dict
defender_entry_form_dict = defender_entry.from_dict(defender_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
