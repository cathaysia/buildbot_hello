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


class AdminPermissions(str, Enum):
    """
    Admin permissions:   * `*` - all permissions are granted   * `add_users` - add new users is allowed   * `edit_users` - change existing users is allowed   * `del_users` - remove users is allowed   * `view_users` - list users is allowed   * `view_conns` - list active connections is allowed   * `close_conns` - close active connections is allowed   * `view_status` - view the server status is allowed   * `manage_admins` - manage other admins is allowed   * `manage_groups` - manage groups is allowed   * `manage_apikeys` - manage API keys is allowed   * `quota_scans` - view and start quota scans is allowed   * `manage_system` - backups and restores are allowed   * `manage_defender` - remove ip from the dynamic blocklist is allowed   * `view_defender` - list the dynamic blocklist is allowed   * `retention_checks` - view and start retention checks is allowed   * `metadata_checks` - view and start metadata checks is allowed   * `view_events` - view and search filesystem and provider events is allowed   * `manage_event_rules` - manage event actions and rules is allowed   * `manage_roles` - manage roles is allowed   * `manage_ip_lists` - manage global and ratelimter allow lists and defender block and safe lists is allowed
    """

    """
    allowed enum values
    """
    STAR = "*"
    ADD_USERS = "add_users"
    EDIT_USERS = "edit_users"
    DEL_USERS = "del_users"
    VIEW_USERS = "view_users"
    VIEW_CONNS = "view_conns"
    CLOSE_CONNS = "close_conns"
    VIEW_STATUS = "view_status"
    MANAGE_ADMINS = "manage_admins"
    MANAGE_GROUPS = "manage_groups"
    MANAGE_APIKEYS = "manage_apikeys"
    QUOTA_SCANS = "quota_scans"
    MANAGE_SYSTEM = "manage_system"
    MANAGE_DEFENDER = "manage_defender"
    VIEW_DEFENDER = "view_defender"
    RETENTION_CHECKS = "retention_checks"
    METADATA_CHECKS = "metadata_checks"
    VIEW_EVENTS = "view_events"
    MANAGE_EVENT_RULES = "manage_event_rules"
    MANAGE_ROLES = "manage_roles"
    MANAGE_IP_LISTS = "manage_ip_lists"

    @classmethod
    def from_json(cls, json_str: str) -> AdminPermissions:
        """Create an instance of AdminPermissions from a JSON string"""
        return AdminPermissions(json.loads(json_str))
