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


class PatternsFilter(BaseModel):
    """
    PatternsFilter
    """

    path: Optional[StrictStr] = Field(
        None,
        description='virtual path as seen by users, if no other specific filter is defined, the filter applies for sub directories too. For example if filters are defined for the paths "/" and "/sub" then the filters for "/" are applied for any file outside the "/sub" directory',
    )
    allowed_patterns: Optional[conlist(StrictStr)] = Field(
        None,
        description="list of, case insensitive, allowed shell like patterns. Allowed patterns are evaluated before the denied ones",
    )
    denied_patterns: Optional[conlist(StrictStr)] = Field(
        None, description="list of, case insensitive, denied shell like patterns"
    )
    deny_policy: Optional[StrictInt] = Field(
        None,
        description="Policies for denied patterns   * `0` - default policy. Denied files/directories matching the filters are visible in directory listing but cannot be uploaded/downloaded/overwritten/renamed   * `1` - deny policy hide. This policy applies the same restrictions as the default one and denied files/directories matching the filters will also be hidden in directory listing. This mode may cause performance issues for large directories ",
    )
    __properties = ["path", "allowed_patterns", "denied_patterns", "deny_policy"]

    @validator("deny_policy")
    def deny_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (0, 1):
            raise ValueError("must be one of enum values (0, 1)")
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
    def from_json(cls, json_str: str) -> PatternsFilter:
        """Create an instance of PatternsFilter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PatternsFilter:
        """Create an instance of PatternsFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PatternsFilter.parse_obj(obj)

        _obj = PatternsFilter.parse_obj(
            {
                "path": obj.get("path"),
                "allowed_patterns": obj.get("allowed_patterns"),
                "denied_patterns": obj.get("denied_patterns"),
                "deny_policy": obj.get("deny_policy"),
            }
        )
        return _obj
