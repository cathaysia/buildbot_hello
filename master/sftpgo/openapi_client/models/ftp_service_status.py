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
from pydantic import BaseModel, StrictBool, conlist
from openapi_client.models.ftp_passive_port_range import FTPPassivePortRange
from openapi_client.models.ftpd_binding import FTPDBinding


class FTPServiceStatus(BaseModel):
    """
    FTPServiceStatus
    """

    is_active: Optional[StrictBool] = None
    bindings: Optional[conlist(FTPDBinding)] = None
    passive_port_range: Optional[FTPPassivePortRange] = None
    __properties = ["is_active", "bindings", "passive_port_range"]

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
    def from_json(cls, json_str: str) -> FTPServiceStatus:
        """Create an instance of FTPServiceStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in bindings (list)
        _items = []
        if self.bindings:
            for _item in self.bindings:
                if _item:
                    _items.append(_item.to_dict())
            _dict["bindings"] = _items
        # override the default output from pydantic by calling `to_dict()` of passive_port_range
        if self.passive_port_range:
            _dict["passive_port_range"] = self.passive_port_range.to_dict()
        # set to None if bindings (nullable) is None
        # and __fields_set__ contains the field
        if self.bindings is None and "bindings" in self.__fields_set__:
            _dict["bindings"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FTPServiceStatus:
        """Create an instance of FTPServiceStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FTPServiceStatus.parse_obj(obj)

        _obj = FTPServiceStatus.parse_obj(
            {
                "is_active": obj.get("is_active"),
                "bindings": [
                    FTPDBinding.from_dict(_item) for _item in obj.get("bindings")
                ]
                if obj.get("bindings") is not None
                else None,
                "passive_port_range": FTPPassivePortRange.from_dict(
                    obj.get("passive_port_range")
                )
                if obj.get("passive_port_range") is not None
                else None,
            }
        )
        return _obj