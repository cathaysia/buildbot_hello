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


class SSHAuthentications(str, Enum):
    """
    SSHAuthentications
    """

    """
    allowed enum values
    """
    PUBLICKEY = "publickey"
    PASSWORD = "password"
    KEYBOARD_MINUS_INTERACTIVE = "keyboard-interactive"
    PUBLICKEY_PLUS_PASSWORD = "publickey+password"
    PUBLICKEY_PLUS_KEYBOARD_MINUS_INTERACTIVE = "publickey+keyboard-interactive"

    @classmethod
    def from_json(cls, json_str: str) -> SSHAuthentications:
        """Create an instance of SSHAuthentications from a JSON string"""
        return SSHAuthentications(json.loads(json_str))
