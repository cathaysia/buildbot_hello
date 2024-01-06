# -*- coding: utf-8 -*-

"""
    SFTPGo

    SFTPGo allows you to securely share your files over SFTP and optionally over HTTP/S, FTP/S and WebDAV as well. Several storage backends are supported and they are configurable per-user, so you can serve a local directory for a user and an S3 bucket (or part of it) for another one. SFTPGo also supports virtual folders, a virtual folder can use any of the supported storage backends. So you can have, for example, a user with the S3 backend mapping a Google Cloud Storage bucket (or part of it) on a specified path and an encrypted local filesystem on another one. Virtual folders can be private or shared among multiple users, for shared virtual folders you can define different quota limits for each user. SFTPGo supports groups to simplify the administration of multiple accounts by letting you assign settings once to a group, instead of multiple times to each individual user. The SFTPGo WebClient allows end users to change their credentials, browse and manage their files in the browser and setup two-factor authentication which works with Authy, Google Authenticator and other compatible apps. From the WebClient each authorized user can also create HTTP/S links to externally share files and folders securely, by setting limits to the number of downloads/uploads, protecting the share with a password, limiting access by source IP address, setting an automatic expiration date.

    The version of the OpenAPI document: 2.5.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from openapi_client.models.condition_options import ConditionOptions
from openapi_client.models.schedule import Schedule


class EventConditions(BaseModel):
    """
    EventConditions
    """

    fs_events: Optional[conlist(StrictStr)] = None
    provider_events: Optional[conlist(StrictStr)] = None
    schedules: Optional[conlist(Schedule)] = None
    idp_login_event: Optional[StrictInt] = Field(
        None,
        description="IDP login events:   - `0` any login event   - `1` user login event   - `2` admin login event ",
    )
    options: Optional[ConditionOptions] = None
    __properties = [
        "fs_events",
        "provider_events",
        "schedules",
        "idp_login_event",
        "options",
    ]

    @validator("fs_events")
    def fs_events_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in (
                "upload",
                "download",
                "delete",
                "rename",
                "mkdir",
                "rmdir",
                "copy",
                "ssh_cmd",
                "pre-upload",
                "pre-download",
                "pre-delete",
                "first-upload",
                "first-download",
            ):
                raise ValueError(
                    "each list item must be one of ('upload', 'download', 'delete', 'rename', 'mkdir', 'rmdir', 'copy', 'ssh_cmd', 'pre-upload', 'pre-download', 'pre-delete', 'first-upload', 'first-download')"
                )
        return value

    @validator("provider_events")
    def provider_events_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ("add", "update", "delete"):
                raise ValueError(
                    "each list item must be one of ('add', 'update', 'delete')"
                )
        return value

    @validator("idp_login_event")
    def idp_login_event_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (0, 1, 2):
            raise ValueError("must be one of enum values (0, 1, 2)")
        return value

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> EventConditions:
        """Create an instance of EventConditions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in schedules (list)
        _items = []
        if self.schedules:
            for _item in self.schedules:
                if _item:
                    _items.append(_item.to_dict())
            _dict["schedules"] = _items
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict["options"] = self.options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventConditions:
        """Create an instance of EventConditions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventConditions.parse_obj(obj)

        _obj = EventConditions.parse_obj(
            {
                "fs_events": obj.get("fs_events"),
                "provider_events": obj.get("provider_events"),
                "schedules": [
                    Schedule.from_dict(_item) for _item in obj.get("schedules")
                ]
                if obj.get("schedules") is not None
                else None,
                "idp_login_event": obj.get("idp_login_event"),
                "options": ConditionOptions.from_dict(obj.get("options"))
                if obj.get("options") is not None
                else None,
            }
        )
        return _obj
