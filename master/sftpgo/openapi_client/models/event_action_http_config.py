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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, conlist, validator
from openapi_client.models.http_part import HTTPPart
from openapi_client.models.key_value import KeyValue
from openapi_client.models.secret import Secret


class EventActionHTTPConfig(BaseModel):
    """
    EventActionHTTPConfig
    """

    endpoint: Optional[StrictStr] = Field(None, description="HTTP endpoint")
    username: Optional[StrictStr] = None
    password: Optional[Secret] = None
    headers: Optional[conlist(KeyValue)] = Field(None, description="headers to add")
    timeout: Optional[conint(strict=True, le=180, ge=1)] = Field(
        None, description="Ignored for multipart requests with files as attachments"
    )
    skip_tls_verify: Optional[StrictBool] = Field(
        None,
        description="if enabled the HTTP client accepts any TLS certificate presented by the server and any host name in that certificate. In this mode, TLS is susceptible to man-in-the-middle attacks. This should be used only for testing.",
    )
    method: Optional[StrictStr] = None
    query_parameters: Optional[conlist(KeyValue)] = None
    body: Optional[StrictStr] = Field(None, description="HTTP POST/PUT body")
    parts: Optional[conlist(HTTPPart)] = Field(
        None,
        description="Multipart requests allow to combine one or more sets of data into a single body. For each part, you can set a file path or a body as text. Placeholders are supported in file path, body, header values.",
    )
    __properties = [
        "endpoint",
        "username",
        "password",
        "headers",
        "timeout",
        "skip_tls_verify",
        "method",
        "query_parameters",
        "body",
        "parts",
    ]

    @validator("method")
    def method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("GET", "POST", "PUT"):
            raise ValueError("must be one of enum values ('GET', 'POST', 'PUT')")
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
    def from_json(cls, json_str: str) -> EventActionHTTPConfig:
        """Create an instance of EventActionHTTPConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of password
        if self.password:
            _dict["password"] = self.password.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in headers (list)
        _items = []
        if self.headers:
            for _item in self.headers:
                if _item:
                    _items.append(_item.to_dict())
            _dict["headers"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in query_parameters (list)
        _items = []
        if self.query_parameters:
            for _item in self.query_parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict["query_parameters"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in parts (list)
        _items = []
        if self.parts:
            for _item in self.parts:
                if _item:
                    _items.append(_item.to_dict())
            _dict["parts"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventActionHTTPConfig:
        """Create an instance of EventActionHTTPConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventActionHTTPConfig.parse_obj(obj)

        _obj = EventActionHTTPConfig.parse_obj(
            {
                "endpoint": obj.get("endpoint"),
                "username": obj.get("username"),
                "password": Secret.from_dict(obj.get("password"))
                if obj.get("password") is not None
                else None,
                "headers": [KeyValue.from_dict(_item) for _item in obj.get("headers")]
                if obj.get("headers") is not None
                else None,
                "timeout": obj.get("timeout"),
                "skip_tls_verify": obj.get("skip_tls_verify"),
                "method": obj.get("method"),
                "query_parameters": [
                    KeyValue.from_dict(_item) for _item in obj.get("query_parameters")
                ]
                if obj.get("query_parameters") is not None
                else None,
                "body": obj.get("body"),
                "parts": [HTTPPart.from_dict(_item) for _item in obj.get("parts")]
                if obj.get("parts") is not None
                else None,
            }
        )
        return _obj