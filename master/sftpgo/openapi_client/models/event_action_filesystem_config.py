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
from pydantic import BaseModel, StrictStr, conlist
from openapi_client.models.event_action_fs_compress import EventActionFsCompress
from openapi_client.models.filesystem_action_types import FilesystemActionTypes
from openapi_client.models.key_value import KeyValue


class EventActionFilesystemConfig(BaseModel):
    """
    EventActionFilesystemConfig
    """

    type: Optional[FilesystemActionTypes] = None
    renames: Optional[conlist(KeyValue)] = None
    mkdirs: Optional[conlist(StrictStr)] = None
    deletes: Optional[conlist(StrictStr)] = None
    exist: Optional[conlist(StrictStr)] = None
    copy: Optional[conlist(KeyValue)] = None
    compress: Optional[EventActionFsCompress] = None
    __properties = ["type", "renames", "mkdirs", "deletes", "exist", "copy", "compress"]

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
    def from_json(cls, json_str: str) -> EventActionFilesystemConfig:
        """Create an instance of EventActionFilesystemConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in renames (list)
        _items = []
        if self.renames:
            for _item in self.renames:
                if _item:
                    _items.append(_item.to_dict())
            _dict["renames"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in copy (list)
        _items = []
        if self.copy:
            for _item in self.copy:
                if _item:
                    _items.append(_item.to_dict())
            _dict["copy"] = _items
        # override the default output from pydantic by calling `to_dict()` of compress
        if self.compress:
            _dict["compress"] = self.compress.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventActionFilesystemConfig:
        """Create an instance of EventActionFilesystemConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventActionFilesystemConfig.parse_obj(obj)

        _obj = EventActionFilesystemConfig.parse_obj(
            {
                "type": obj.get("type"),
                "renames": [KeyValue.from_dict(_item) for _item in obj.get("renames")]
                if obj.get("renames") is not None
                else None,
                "mkdirs": obj.get("mkdirs"),
                "deletes": obj.get("deletes"),
                "exist": obj.get("exist"),
                "copy": [KeyValue.from_dict(_item) for _item in obj.get("copy")]
                if obj.get("copy") is not None
                else None,
                "compress": EventActionFsCompress.from_dict(obj.get("compress"))
                if obj.get("compress") is not None
                else None,
            }
        )
        return _obj