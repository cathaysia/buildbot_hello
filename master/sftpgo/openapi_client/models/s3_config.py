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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, constr
from openapi_client.models.secret import Secret


class S3Config(BaseModel):
    """
    S3 Compatible Object Storage configuration details
    """

    bucket: Optional[constr(strict=True, min_length=1)] = None
    region: Optional[constr(strict=True, min_length=1)] = None
    access_key: Optional[StrictStr] = None
    access_secret: Optional[Secret] = None
    role_arn: Optional[StrictStr] = Field(
        None, description="Optional IAM Role ARN to assume"
    )
    endpoint: Optional[StrictStr] = Field(None, description="optional endpoint")
    storage_class: Optional[StrictStr] = None
    acl: Optional[StrictStr] = Field(
        None,
        description="The canned ACL to apply to uploaded objects. Leave empty to use the default ACL. For more information and available ACLs, see here: https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl",
    )
    upload_part_size: Optional[StrictInt] = Field(
        None,
        description="the buffer size (in MB) to use for multipart uploads. The minimum allowed part size is 5MB, and if this value is set to zero, the default value (5MB) for the AWS SDK will be used. The minimum allowed value is 5.",
    )
    upload_concurrency: Optional[StrictInt] = Field(
        None,
        description="the number of parts to upload in parallel. If this value is set to zero, the default value (5) will be used",
    )
    upload_part_max_time: Optional[StrictInt] = Field(
        None,
        description='the maximum time allowed, in seconds, to upload a single chunk (the chunk size is defined via "upload_part_size"). 0 means no timeout',
    )
    download_part_size: Optional[StrictInt] = Field(
        None,
        description="the buffer size (in MB) to use for multipart downloads. The minimum allowed part size is 5MB, and if this value is set to zero, the default value (5MB) for the AWS SDK will be used. The minimum allowed value is 5. Ignored for partial downloads",
    )
    download_concurrency: Optional[StrictInt] = Field(
        None,
        description="the number of parts to download in parallel. If this value is set to zero, the default value (5) will be used. Ignored for partial downloads",
    )
    download_part_max_time: Optional[StrictInt] = Field(
        None,
        description='the maximum time allowed, in seconds, to download a single chunk (the chunk size is defined via "download_part_size"). 0 means no timeout. Ignored for partial downloads.',
    )
    force_path_style: Optional[StrictBool] = Field(
        None,
        description='Set this to "true" to force the request to use path-style addressing, i.e., "http://s3.amazonaws.com/BUCKET/KEY". By default, the S3 client will use virtual hosted bucket addressing when possible ("http://BUCKET.s3.amazonaws.com/KEY")',
    )
    key_prefix: Optional[StrictStr] = Field(
        None,
        description='key_prefix is similar to a chroot directory for a local filesystem. If specified the user will only see contents that starts with this prefix and so you can restrict access to a specific virtual folder. The prefix, if not empty, must not start with "/" and must end with "/". If empty the whole bucket contents will be available',
    )
    __properties = [
        "bucket",
        "region",
        "access_key",
        "access_secret",
        "role_arn",
        "endpoint",
        "storage_class",
        "acl",
        "upload_part_size",
        "upload_concurrency",
        "upload_part_max_time",
        "download_part_size",
        "download_concurrency",
        "download_part_max_time",
        "force_path_style",
        "key_prefix",
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
    def from_json(cls, json_str: str) -> S3Config:
        """Create an instance of S3Config from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of access_secret
        if self.access_secret:
            _dict["access_secret"] = self.access_secret.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> S3Config:
        """Create an instance of S3Config from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return S3Config.parse_obj(obj)

        _obj = S3Config.parse_obj(
            {
                "bucket": obj.get("bucket"),
                "region": obj.get("region"),
                "access_key": obj.get("access_key"),
                "access_secret": Secret.from_dict(obj.get("access_secret"))
                if obj.get("access_secret") is not None
                else None,
                "role_arn": obj.get("role_arn"),
                "endpoint": obj.get("endpoint"),
                "storage_class": obj.get("storage_class"),
                "acl": obj.get("acl"),
                "upload_part_size": obj.get("upload_part_size"),
                "upload_concurrency": obj.get("upload_concurrency"),
                "upload_part_max_time": obj.get("upload_part_max_time"),
                "download_part_size": obj.get("download_part_size"),
                "download_concurrency": obj.get("download_concurrency"),
                "download_part_max_time": obj.get("download_part_max_time"),
                "force_path_style": obj.get("force_path_style"),
                "key_prefix": obj.get("key_prefix"),
            }
        )
        return _obj
