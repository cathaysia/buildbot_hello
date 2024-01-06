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
from openapi_client.models.transfer import Transfer


class ConnectionStatus(BaseModel):
    """
    ConnectionStatus
    """

    username: Optional[StrictStr] = Field(None, description="connected username")
    connection_id: Optional[StrictStr] = Field(
        None, description="unique connection identifier"
    )
    client_version: Optional[StrictStr] = Field(None, description="client version")
    remote_address: Optional[StrictStr] = Field(
        None, description="Remote address for the connected client"
    )
    connection_time: Optional[StrictInt] = Field(
        None, description="connection time as unix timestamp in milliseconds"
    )
    command: Optional[StrictStr] = Field(
        None, description="Last SSH/FTP command or WebDAV method"
    )
    last_activity: Optional[StrictInt] = Field(
        None, description="last client activity as unix timestamp in milliseconds"
    )
    protocol: Optional[StrictStr] = None
    active_transfers: Optional[conlist(Transfer)] = None
    node: Optional[StrictStr] = Field(
        None, description="Node identifier, omitted for single node installations"
    )
    __properties = [
        "username",
        "connection_id",
        "client_version",
        "remote_address",
        "connection_time",
        "command",
        "last_activity",
        "protocol",
        "active_transfers",
        "node",
    ]

    @validator("protocol")
    def protocol_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("SFTP", "SCP", "SSH", "FTP", "DAV"):
            raise ValueError(
                "must be one of enum values ('SFTP', 'SCP', 'SSH', 'FTP', 'DAV')"
            )
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
    def from_json(cls, json_str: str) -> ConnectionStatus:
        """Create an instance of ConnectionStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in active_transfers (list)
        _items = []
        if self.active_transfers:
            for _item in self.active_transfers:
                if _item:
                    _items.append(_item.to_dict())
            _dict["active_transfers"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConnectionStatus:
        """Create an instance of ConnectionStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConnectionStatus.parse_obj(obj)

        _obj = ConnectionStatus.parse_obj(
            {
                "username": obj.get("username"),
                "connection_id": obj.get("connection_id"),
                "client_version": obj.get("client_version"),
                "remote_address": obj.get("remote_address"),
                "connection_time": obj.get("connection_time"),
                "command": obj.get("command"),
                "last_activity": obj.get("last_activity"),
                "protocol": obj.get("protocol"),
                "active_transfers": [
                    Transfer.from_dict(_item) for _item in obj.get("active_transfers")
                ]
                if obj.get("active_transfers") is not None
                else None,
                "node": obj.get("node"),
            }
        )
        return _obj
