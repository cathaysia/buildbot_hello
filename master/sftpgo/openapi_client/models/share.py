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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from openapi_client.models.share_scope import ShareScope


class Share(BaseModel):
    """
    Share
    """

    id: Optional[StrictStr] = Field(
        None, description="auto-generated unique share identifier"
    )
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = Field(None, description="optional description")
    scope: Optional[ShareScope] = None
    paths: Optional[conlist(StrictStr)] = Field(
        None,
        description="paths to files or directories, for share scope write this array must contain exactly one directory. Paths will not be validated on save so you can also create them after creating the share",
    )
    username: Optional[StrictStr] = None
    created_at: Optional[StrictInt] = Field(
        None, description="creation time as unix timestamp in milliseconds"
    )
    updated_at: Optional[StrictInt] = Field(
        None, description="last update time as unix timestamp in milliseconds"
    )
    last_use_at: Optional[StrictInt] = Field(
        None, description="last use time as unix timestamp in milliseconds"
    )
    expires_at: Optional[StrictInt] = Field(
        None,
        description="optional share expiration, as unix timestamp in milliseconds. 0 means no expiration",
    )
    password: Optional[StrictStr] = Field(
        None,
        description='optional password to protect the share. The special value "[**redacted**]" means that a password has been set, you can use this value if you want to preserve the current password when you update a share',
    )
    max_tokens: Optional[StrictInt] = Field(
        None, description="maximum allowed access tokens. 0 means no limit"
    )
    used_tokens: Optional[StrictInt] = None
    allow_from: Optional[conlist(StrictStr)] = Field(
        None,
        description='Limit the share availability to these IP/Mask. IP/Mask must be in CIDR notation as defined in RFC 4632 and RFC 4291, for example "192.0.2.0/24" or "2001:db8::/32". An empty list means no restrictions',
    )
    __properties = [
        "id",
        "name",
        "description",
        "scope",
        "paths",
        "username",
        "created_at",
        "updated_at",
        "last_use_at",
        "expires_at",
        "password",
        "max_tokens",
        "used_tokens",
        "allow_from",
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
    def from_json(cls, json_str: str) -> Share:
        """Create an instance of Share from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Share:
        """Create an instance of Share from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Share.parse_obj(obj)

        _obj = Share.parse_obj(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "description": obj.get("description"),
                "scope": obj.get("scope"),
                "paths": obj.get("paths"),
                "username": obj.get("username"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "last_use_at": obj.get("last_use_at"),
                "expires_at": obj.get("expires_at"),
                "password": obj.get("password"),
                "max_tokens": obj.get("max_tokens"),
                "used_tokens": obj.get("used_tokens"),
                "allow_from": obj.get("allow_from"),
            }
        )
        return _obj