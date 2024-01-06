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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint, conlist
from openapi_client.models.filesystem_config import FilesystemConfig


class BaseVirtualFolder(BaseModel):
    """
    Defines the filesystem for the virtual folder and the used quota limits. The same folder can be shared among multiple users and each user can have different quota limits or a different virtual path.
    """

    id: Optional[conint(strict=True, ge=1)] = None
    name: Optional[StrictStr] = Field(
        None, description="unique name for this virtual folder"
    )
    mapped_path: Optional[StrictStr] = Field(
        None, description="absolute filesystem path to use as virtual folder"
    )
    description: Optional[StrictStr] = Field(None, description="optional description")
    used_quota_size: Optional[StrictInt] = None
    used_quota_files: Optional[StrictInt] = None
    last_quota_update: Optional[StrictInt] = Field(
        None, description="Last quota update as unix timestamp in milliseconds"
    )
    users: Optional[conlist(StrictStr)] = Field(
        None, description="list of usernames associated with this virtual folder"
    )
    filesystem: Optional[FilesystemConfig] = None
    __properties = [
        "id",
        "name",
        "mapped_path",
        "description",
        "used_quota_size",
        "used_quota_files",
        "last_quota_update",
        "users",
        "filesystem",
    ]

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
    def from_json(cls, json_str: str) -> BaseVirtualFolder:
        """Create an instance of BaseVirtualFolder from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of filesystem
        if self.filesystem:
            _dict["filesystem"] = self.filesystem.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BaseVirtualFolder:
        """Create an instance of BaseVirtualFolder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BaseVirtualFolder.parse_obj(obj)

        _obj = BaseVirtualFolder.parse_obj(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "mapped_path": obj.get("mapped_path"),
                "description": obj.get("description"),
                "used_quota_size": obj.get("used_quota_size"),
                "used_quota_files": obj.get("used_quota_files"),
                "last_quota_update": obj.get("last_quota_update"),
                "users": obj.get("users"),
                "filesystem": FilesystemConfig.from_dict(obj.get("filesystem"))
                if obj.get("filesystem") is not None
                else None,
            }
        )
        return _obj