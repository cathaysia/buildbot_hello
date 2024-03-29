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
from openapi_client.models.group_user_settings import GroupUserSettings
from openapi_client.models.virtual_folder import VirtualFolder


class Group(BaseModel):
    """
    Group
    """

    id: Optional[conint(strict=True, ge=1)] = None
    name: Optional[StrictStr] = Field(None, description="name is unique")
    description: Optional[StrictStr] = Field(None, description="optional description")
    created_at: Optional[StrictInt] = Field(
        None, description="creation time as unix timestamp in milliseconds"
    )
    updated_at: Optional[StrictInt] = Field(
        None, description="last update time as unix timestamp in milliseconds"
    )
    user_settings: Optional[GroupUserSettings] = None
    virtual_folders: Optional[conlist(VirtualFolder)] = Field(
        None, description="mapping between virtual SFTPGo paths and folders"
    )
    users: Optional[conlist(StrictStr)] = Field(
        None, description="list of usernames associated with this group"
    )
    admins: Optional[conlist(StrictStr)] = Field(
        None, description="list of admins usernames associated with this group"
    )
    __properties = [
        "id",
        "name",
        "description",
        "created_at",
        "updated_at",
        "user_settings",
        "virtual_folders",
        "users",
        "admins",
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
    def from_json(cls, json_str: str) -> Group:
        """Create an instance of Group from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of user_settings
        if self.user_settings:
            _dict["user_settings"] = self.user_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in virtual_folders (list)
        _items = []
        if self.virtual_folders:
            for _item in self.virtual_folders:
                if _item:
                    _items.append(_item.to_dict())
            _dict["virtual_folders"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Group:
        """Create an instance of Group from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Group.parse_obj(obj)

        _obj = Group.parse_obj(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "description": obj.get("description"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "user_settings": GroupUserSettings.from_dict(obj.get("user_settings"))
                if obj.get("user_settings") is not None
                else None,
                "virtual_folders": [
                    VirtualFolder.from_dict(_item)
                    for _item in obj.get("virtual_folders")
                ]
                if obj.get("virtual_folders") is not None
                else None,
                "users": obj.get("users"),
                "admins": obj.get("admins"),
            }
        )
        return _obj
