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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from openapi_client.models.base_user_filters import BaseUserFilters
from openapi_client.models.filesystem_config import FilesystemConfig
from openapi_client.models.permission import Permission


class GroupUserSettings(BaseModel):
    """
    GroupUserSettings
    """

    home_dir: Optional[StrictStr] = None
    max_sessions: Optional[StrictInt] = None
    quota_size: Optional[StrictInt] = None
    quota_files: Optional[StrictInt] = None
    permissions: Optional[Dict[str, conlist(Permission, min_items=1)]] = Field(
        None,
        description='hash map with directory as key and an array of permissions as value. Directories must be absolute paths, permissions for root directory ("/") are required',
    )
    upload_bandwidth: Optional[StrictInt] = Field(
        None, description="Maximum upload bandwidth as KB/s"
    )
    download_bandwidth: Optional[StrictInt] = Field(
        None, description="Maximum download bandwidth as KB/s"
    )
    upload_data_transfer: Optional[StrictInt] = Field(
        None, description="Maximum data transfer allowed for uploads as MB"
    )
    download_data_transfer: Optional[StrictInt] = Field(
        None, description="Maximum data transfer allowed for downloads as MB"
    )
    total_data_transfer: Optional[StrictInt] = Field(
        None, description="Maximum total data transfer as MB"
    )
    expires_in: Optional[StrictInt] = Field(
        None,
        description="Account expiration in number of days from creation. 0 means no expiration",
    )
    filters: Optional[BaseUserFilters] = None
    filesystem: Optional[FilesystemConfig] = None
    __properties = [
        "home_dir",
        "max_sessions",
        "quota_size",
        "quota_files",
        "permissions",
        "upload_bandwidth",
        "download_bandwidth",
        "upload_data_transfer",
        "download_data_transfer",
        "total_data_transfer",
        "expires_in",
        "filters",
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
    def from_json(cls, json_str: str) -> GroupUserSettings:
        """Create an instance of GroupUserSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in permissions (dict of array)
        _field_dict_of_array = {}
        if self.permissions:
            for _key in self.permissions:
                if self.permissions[_key]:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.permissions[_key]
                    ]
            _dict["permissions"] = _field_dict_of_array
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict["filters"] = self.filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filesystem
        if self.filesystem:
            _dict["filesystem"] = self.filesystem.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GroupUserSettings:
        """Create an instance of GroupUserSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GroupUserSettings.parse_obj(obj)

        _obj = GroupUserSettings.parse_obj(
            {
                "home_dir": obj.get("home_dir"),
                "max_sessions": obj.get("max_sessions"),
                "quota_size": obj.get("quota_size"),
                "quota_files": obj.get("quota_files"),
                "permissions": dict(
                    (
                        _k,
                        [Permission.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None,
                    )
                    for _k, _v in obj.get("permissions").items()
                ),
                "upload_bandwidth": obj.get("upload_bandwidth"),
                "download_bandwidth": obj.get("download_bandwidth"),
                "upload_data_transfer": obj.get("upload_data_transfer"),
                "download_data_transfer": obj.get("download_data_transfer"),
                "total_data_transfer": obj.get("total_data_transfer"),
                "expires_in": obj.get("expires_in"),
                "filters": BaseUserFilters.from_dict(obj.get("filters"))
                if obj.get("filters") is not None
                else None,
                "filesystem": FilesystemConfig.from_dict(obj.get("filesystem"))
                if obj.get("filesystem") is not None
                else None,
            }
        )
        return _obj