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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt


class AdminPreferences(BaseModel):
    """
    AdminPreferences
    """

    hide_user_page_sections: Optional[StrictInt] = Field(
        None,
        description='Allow to hide some sections from the user page. These are not security settings and are not enforced server side in any way. They are only intended to simplify the user page in the WebAdmin UI. 1 means hide groups section, 2 means hide filesystem section, "users_base_dir" must be set in the config file otherwise this setting is ignored, 4 means hide virtual folders section, 8 means hide profile section, 16 means hide ACLs section, 32 means hide disk and bandwidth quota limits section, 64 means hide advanced settings section. The settings can be combined',
    )
    default_users_expiration: Optional[StrictInt] = Field(
        None,
        description="Defines the default expiration for newly created users as number of days. 0 means no expiration",
    )
    __properties = ["hide_user_page_sections", "default_users_expiration"]

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
    def from_json(cls, json_str: str) -> AdminPreferences:
        """Create an instance of AdminPreferences from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdminPreferences:
        """Create an instance of AdminPreferences from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdminPreferences.parse_obj(obj)

        _obj = AdminPreferences.parse_obj(
            {
                "hide_user_page_sections": obj.get("hide_user_page_sections"),
                "default_users_expiration": obj.get("default_users_expiration"),
            }
        )
        return _obj
