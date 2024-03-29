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
from openapi_client.models.bandwidth_limit import BandwidthLimit
from openapi_client.models.hooks_filter import HooksFilter
from openapi_client.models.login_methods import LoginMethods
from openapi_client.models.mfa_protocols import MFAProtocols
from openapi_client.models.patterns_filter import PatternsFilter
from openapi_client.models.recovery_code import RecoveryCode
from openapi_client.models.supported_protocols import SupportedProtocols
from openapi_client.models.user_totp_config import UserTOTPConfig
from openapi_client.models.user_type import UserType
from openapi_client.models.web_client_options import WebClientOptions


class UserFilters(BaseModel):
    """
    UserFilters
    """

    allowed_ip: Optional[conlist(StrictStr)] = Field(
        None,
        description='only clients connecting from these IP/Mask are allowed. IP/Mask must be in CIDR notation as defined in RFC 4632 and RFC 4291, for example "192.0.2.0/24" or "2001:db8::/32"',
    )
    denied_ip: Optional[conlist(StrictStr)] = Field(
        None,
        description="clients connecting from these IP/Mask are not allowed. Denied rules are evaluated before allowed ones",
    )
    denied_login_methods: Optional[conlist(LoginMethods)] = Field(
        None, description="if null or empty any available login method is allowed"
    )
    denied_protocols: Optional[conlist(SupportedProtocols)] = Field(
        None, description="if null or empty any available protocol is allowed"
    )
    file_patterns: Optional[conlist(PatternsFilter)] = Field(
        None,
        description="filters based on shell like file patterns. These restrictions do not apply to files listing for performance reasons, so a denied file cannot be downloaded/overwritten/renamed but it will still be in the list of files. Please note that these restrictions can be easily bypassed",
    )
    max_upload_file_size: Optional[StrictInt] = Field(
        None,
        description="maximum allowed size, as bytes, for a single file upload. The upload will be aborted if/when the size of the file being sent exceeds this limit. 0 means unlimited. This restriction does not apply for SSH system commands such as `git` and `rsync`",
    )
    tls_username: Optional[StrictStr] = Field(
        None,
        description='defines the TLS certificate field to use as username. For FTP clients it must match the name provided using the "USER" command. For WebDAV, if no username is provided, the CN will be used as username. For WebDAV clients it must match the implicit or provided username. Ignored if mutual TLS is disabled. Currently the only supported value is `CommonName`',
    )
    hooks: Optional[HooksFilter] = None
    disable_fs_checks: Optional[StrictBool] = Field(
        None,
        description="Disable checks for existence and automatic creation of home directory and virtual folders. SFTPGo requires that the user's home directory, virtual folder root, and intermediate paths to virtual folders exist to work properly. If you already know that the required directories exist, disabling these checks will speed up login. You could, for example, disable these checks after the first login",
    )
    web_client: Optional[conlist(WebClientOptions)] = Field(
        None, description="WebClient/user REST API related configuration options"
    )
    allow_api_key_auth: Optional[StrictBool] = Field(
        None,
        description="API key authentication allows to impersonate this user with an API key",
    )
    user_type: Optional[UserType] = None
    bandwidth_limits: Optional[conlist(BandwidthLimit)] = None
    external_auth_cache_time: Optional[StrictInt] = Field(
        None,
        description="Defines the cache time, in seconds, for users authenticated using an external auth hook. 0 means no cache",
    )
    start_directory: Optional[StrictStr] = Field(
        None,
        description='Specifies an alternate starting directory. If not set, the default is "/". This option is supported for SFTP/SCP, FTP and HTTP (WebClient/REST API) protocols. Relative paths will use this directory as base.',
    )
    two_factor_protocols: Optional[conlist(MFAProtocols)] = Field(
        None, description="Defines protocols that require two factor authentication"
    )
    ftp_security: Optional[StrictInt] = Field(
        None,
        description="Set to `1` to require TLS for both data and control connection. his setting is useful if you want to allow both encrypted and plain text FTP sessions globally and then you want to require encrypted sessions on a per-user basis. It has no effect if TLS is already required for all users in the configuration file.",
    )
    is_anonymous: Optional[StrictBool] = Field(
        None,
        description='If enabled the user can login with any password or no password at all. Anonymous users are supported for FTP and WebDAV protocols and permissions will be automatically set to "list" and "download" (read only)',
    )
    default_shares_expiration: Optional[StrictInt] = Field(
        None,
        description="Defines the default expiration for newly created shares as number of days. 0 means no expiration",
    )
    password_expiration: Optional[StrictInt] = Field(
        None,
        description="The password expires after the defined number of days. 0 means no expiration",
    )
    require_password_change: Optional[StrictBool] = Field(
        None,
        description="User must change password from WebClient/REST API at next login",
    )
    totp_config: Optional[UserTOTPConfig] = None
    recovery_codes: Optional[conlist(RecoveryCode)] = None
    __properties = [
        "allowed_ip",
        "denied_ip",
        "denied_login_methods",
        "denied_protocols",
        "file_patterns",
        "max_upload_file_size",
        "tls_username",
        "hooks",
        "disable_fs_checks",
        "web_client",
        "allow_api_key_auth",
        "user_type",
        "bandwidth_limits",
        "external_auth_cache_time",
        "start_directory",
        "two_factor_protocols",
        "ftp_security",
        "is_anonymous",
        "default_shares_expiration",
        "password_expiration",
        "require_password_change",
        "totp_config",
        "recovery_codes",
    ]

    @validator("ftp_security")
    def ftp_security_validate_enum(cls, value):
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
    def from_json(cls, json_str: str) -> UserFilters:
        """Create an instance of UserFilters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in file_patterns (list)
        _items = []
        if self.file_patterns:
            for _item in self.file_patterns:
                if _item:
                    _items.append(_item.to_dict())
            _dict["file_patterns"] = _items
        # override the default output from pydantic by calling `to_dict()` of hooks
        if self.hooks:
            _dict["hooks"] = self.hooks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in bandwidth_limits (list)
        _items = []
        if self.bandwidth_limits:
            for _item in self.bandwidth_limits:
                if _item:
                    _items.append(_item.to_dict())
            _dict["bandwidth_limits"] = _items
        # override the default output from pydantic by calling `to_dict()` of totp_config
        if self.totp_config:
            _dict["totp_config"] = self.totp_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in recovery_codes (list)
        _items = []
        if self.recovery_codes:
            for _item in self.recovery_codes:
                if _item:
                    _items.append(_item.to_dict())
            _dict["recovery_codes"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserFilters:
        """Create an instance of UserFilters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserFilters.parse_obj(obj)

        _obj = UserFilters.parse_obj(
            {
                "allowed_ip": obj.get("allowed_ip"),
                "denied_ip": obj.get("denied_ip"),
                "denied_login_methods": obj.get("denied_login_methods"),
                "denied_protocols": obj.get("denied_protocols"),
                "file_patterns": [
                    PatternsFilter.from_dict(_item)
                    for _item in obj.get("file_patterns")
                ]
                if obj.get("file_patterns") is not None
                else None,
                "max_upload_file_size": obj.get("max_upload_file_size"),
                "tls_username": obj.get("tls_username"),
                "hooks": HooksFilter.from_dict(obj.get("hooks"))
                if obj.get("hooks") is not None
                else None,
                "disable_fs_checks": obj.get("disable_fs_checks"),
                "web_client": obj.get("web_client"),
                "allow_api_key_auth": obj.get("allow_api_key_auth"),
                "user_type": obj.get("user_type"),
                "bandwidth_limits": [
                    BandwidthLimit.from_dict(_item)
                    for _item in obj.get("bandwidth_limits")
                ]
                if obj.get("bandwidth_limits") is not None
                else None,
                "external_auth_cache_time": obj.get("external_auth_cache_time"),
                "start_directory": obj.get("start_directory"),
                "two_factor_protocols": obj.get("two_factor_protocols"),
                "ftp_security": obj.get("ftp_security"),
                "is_anonymous": obj.get("is_anonymous"),
                "default_shares_expiration": obj.get("default_shares_expiration"),
                "password_expiration": obj.get("password_expiration"),
                "require_password_change": obj.get("require_password_change"),
                "totp_config": UserTOTPConfig.from_dict(obj.get("totp_config"))
                if obj.get("totp_config") is not None
                else None,
                "recovery_codes": [
                    RecoveryCode.from_dict(_item) for _item in obj.get("recovery_codes")
                ]
                if obj.get("recovery_codes") is not None
                else None,
            }
        )
        return _obj
