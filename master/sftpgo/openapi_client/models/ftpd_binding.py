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
from pydantic import (
    BaseModel,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    conlist,
    validator,
)
from openapi_client.models.passive_ip_override import PassiveIPOverride
from openapi_client.models.tls_versions import TLSVersions


class FTPDBinding(BaseModel):
    """
    FTPDBinding
    """

    address: Optional[StrictStr] = Field(
        None, description="TCP address the server listen on"
    )
    port: Optional[StrictInt] = Field(
        None, description="the port used for serving requests"
    )
    apply_proxy_config: Optional[StrictBool] = Field(
        None, description="apply the proxy configuration, if any"
    )
    tls_mode: Optional[StrictInt] = Field(
        None,
        description="TLS mode:   * `0` - clear or explicit TLS   * `1` - explicit TLS required   * `2` - implicit TLS ",
    )
    min_tls_version: Optional[TLSVersions] = None
    force_passive_ip: Optional[StrictStr] = Field(
        None, description="External IP address for passive connections"
    )
    passive_ip_overrides: Optional[conlist(PassiveIPOverride)] = None
    client_auth_type: Optional[StrictInt] = Field(
        None,
        description="1 means that client certificate authentication is required in addition to FTP authentication",
    )
    tls_cipher_suites: Optional[conlist(StrictStr)] = Field(
        None,
        description="List of supported cipher suites for TLS version 1.2. If empty  a default list of secure cipher suites is used, with a preference order based on hardware performance",
    )
    passive_connections_security: Optional[StrictInt] = Field(
        None,
        description="Active connections security:   * `0` - require matching peer IP addresses of control and data connection   * `1` - disable any checks ",
    )
    active_connections_security: Optional[StrictInt] = Field(
        None,
        description="Active connections security:   * `0` - require matching peer IP addresses of control and data connection   * `1` - disable any checks ",
    )
    debug: Optional[StrictBool] = Field(
        None, description="If enabled any FTP command will be logged"
    )
    __properties = [
        "address",
        "port",
        "apply_proxy_config",
        "tls_mode",
        "min_tls_version",
        "force_passive_ip",
        "passive_ip_overrides",
        "client_auth_type",
        "tls_cipher_suites",
        "passive_connections_security",
        "active_connections_security",
        "debug",
    ]

    @validator("tls_mode")
    def tls_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (0, 1, 2):
            raise ValueError("must be one of enum values (0, 1, 2)")
        return value

    @validator("passive_connections_security")
    def passive_connections_security_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (0, 1):
            raise ValueError("must be one of enum values (0, 1)")
        return value

    @validator("active_connections_security")
    def active_connections_security_validate_enum(cls, value):
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
    def from_json(cls, json_str: str) -> FTPDBinding:
        """Create an instance of FTPDBinding from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in passive_ip_overrides (list)
        _items = []
        if self.passive_ip_overrides:
            for _item in self.passive_ip_overrides:
                if _item:
                    _items.append(_item.to_dict())
            _dict["passive_ip_overrides"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FTPDBinding:
        """Create an instance of FTPDBinding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FTPDBinding.parse_obj(obj)

        _obj = FTPDBinding.parse_obj(
            {
                "address": obj.get("address"),
                "port": obj.get("port"),
                "apply_proxy_config": obj.get("apply_proxy_config"),
                "tls_mode": obj.get("tls_mode"),
                "min_tls_version": obj.get("min_tls_version"),
                "force_passive_ip": obj.get("force_passive_ip"),
                "passive_ip_overrides": [
                    PassiveIPOverride.from_dict(_item)
                    for _item in obj.get("passive_ip_overrides")
                ]
                if obj.get("passive_ip_overrides") is not None
                else None,
                "client_auth_type": obj.get("client_auth_type"),
                "tls_cipher_suites": obj.get("tls_cipher_suites"),
                "passive_connections_security": obj.get("passive_connections_security"),
                "active_connections_security": obj.get("active_connections_security"),
                "debug": obj.get("debug"),
            }
        )
        return _obj
