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
from pydantic import BaseModel
from openapi_client.models.azure_blob_fs_config import AzureBlobFsConfig
from openapi_client.models.crypt_fs_config import CryptFsConfig
from openapi_client.models.fs_providers import FsProviders
from openapi_client.models.gcs_config import GCSConfig
from openapi_client.models.httpfs_config import HTTPFsConfig
from openapi_client.models.osfs_config import OSFsConfig
from openapi_client.models.s3_config import S3Config
from openapi_client.models.sftpfs_config import SFTPFsConfig


class FilesystemConfig(BaseModel):
    """
    Storage filesystem details
    """

    provider: Optional[FsProviders] = None
    osconfig: Optional[OSFsConfig] = None
    s3config: Optional[S3Config] = None
    gcsconfig: Optional[GCSConfig] = None
    azblobconfig: Optional[AzureBlobFsConfig] = None
    cryptconfig: Optional[CryptFsConfig] = None
    sftpconfig: Optional[SFTPFsConfig] = None
    httpconfig: Optional[HTTPFsConfig] = None
    __properties = [
        "provider",
        "osconfig",
        "s3config",
        "gcsconfig",
        "azblobconfig",
        "cryptconfig",
        "sftpconfig",
        "httpconfig",
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
    def from_json(cls, json_str: str) -> FilesystemConfig:
        """Create an instance of FilesystemConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of osconfig
        if self.osconfig:
            _dict["osconfig"] = self.osconfig.to_dict()
        # override the default output from pydantic by calling `to_dict()` of s3config
        if self.s3config:
            _dict["s3config"] = self.s3config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gcsconfig
        if self.gcsconfig:
            _dict["gcsconfig"] = self.gcsconfig.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azblobconfig
        if self.azblobconfig:
            _dict["azblobconfig"] = self.azblobconfig.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cryptconfig
        if self.cryptconfig:
            _dict["cryptconfig"] = self.cryptconfig.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sftpconfig
        if self.sftpconfig:
            _dict["sftpconfig"] = self.sftpconfig.to_dict()
        # override the default output from pydantic by calling `to_dict()` of httpconfig
        if self.httpconfig:
            _dict["httpconfig"] = self.httpconfig.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FilesystemConfig:
        """Create an instance of FilesystemConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FilesystemConfig.parse_obj(obj)

        _obj = FilesystemConfig.parse_obj(
            {
                "provider": obj.get("provider"),
                "osconfig": OSFsConfig.from_dict(obj.get("osconfig"))
                if obj.get("osconfig") is not None
                else None,
                "s3config": S3Config.from_dict(obj.get("s3config"))
                if obj.get("s3config") is not None
                else None,
                "gcsconfig": GCSConfig.from_dict(obj.get("gcsconfig"))
                if obj.get("gcsconfig") is not None
                else None,
                "azblobconfig": AzureBlobFsConfig.from_dict(obj.get("azblobconfig"))
                if obj.get("azblobconfig") is not None
                else None,
                "cryptconfig": CryptFsConfig.from_dict(obj.get("cryptconfig"))
                if obj.get("cryptconfig") is not None
                else None,
                "sftpconfig": SFTPFsConfig.from_dict(obj.get("sftpconfig"))
                if obj.get("sftpconfig") is not None
                else None,
                "httpconfig": HTTPFsConfig.from_dict(obj.get("httpconfig"))
                if obj.get("httpconfig") is not None
                else None,
            }
        )
        return _obj