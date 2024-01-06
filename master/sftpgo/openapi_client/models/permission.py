# -*- coding: utf-8 -*-

"""
    SFTPGo

    SFTPGo allows you to securely share your files over SFTP and optionally over HTTP/S, FTP/S and WebDAV as well. Several storage backends are supported and they are configurable per-user, so you can serve a local directory for a user and an S3 bucket (or part of it) for another one. SFTPGo also supports virtual folders, a virtual folder can use any of the supported storage backends. So you can have, for example, a user with the S3 backend mapping a Google Cloud Storage bucket (or part of it) on a specified path and an encrypted local filesystem on another one. Virtual folders can be private or shared among multiple users, for shared virtual folders you can define different quota limits for each user. SFTPGo supports groups to simplify the administration of multiple accounts by letting you assign settings once to a group, instead of multiple times to each individual user. The SFTPGo WebClient allows end users to change their credentials, browse and manage their files in the browser and setup two-factor authentication which works with Authy, Google Authenticator and other compatible apps. From the WebClient each authorized user can also create HTTP/S links to externally share files and folders securely, by setting limits to the number of downloads/uploads, protecting the share with a password, limiting access by source IP address, setting an automatic expiration date.

    The version of the OpenAPI document: 2.5.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg


class Permission(str, Enum):
    """
    Permissions:   * `*` - all permissions are granted   * `list` - list items is allowed   * `download` - download files is allowed   * `upload` - upload files is allowed   * `overwrite` - overwrite an existing file, while uploading, is allowed. upload permission is required to allow file overwrite   * `delete` - delete files or directories is allowed   * `delete_files` - delete files is allowed   * `delete_dirs` - delete directories is allowed   * `rename` - rename files or directories is allowed   * `rename_files` - rename files is allowed   * `rename_dirs` - rename directories is allowed   * `create_dirs` - create directories is allowed   * `create_symlinks` - create links is allowed   * `chmod` changing file or directory permissions is allowed   * `chown` changing file or directory owner and group is allowed   * `chtimes` changing file or directory access and modification time is allowed
    """

    """
    allowed enum values
    """
    STAR = "*"
    LIST = "list"
    DOWNLOAD = "download"
    UPLOAD = "upload"
    OVERWRITE = "overwrite"
    DELETE = "delete"
    DELETE_FILES = "delete_files"
    DELETE_DIRS = "delete_dirs"
    RENAME = "rename"
    RENAME_FILES = "rename_files"
    RENAME_DIRS = "rename_dirs"
    CREATE_DIRS = "create_dirs"
    CREATE_SYMLINKS = "create_symlinks"
    CHMOD = "chmod"
    CHOWN = "chown"
    CHTIMES = "chtimes"

    @classmethod
    def from_json(cls, json_str: str) -> Permission:
        """Create an instance of Permission from a JSON string"""
        return Permission(json.loads(json_str))