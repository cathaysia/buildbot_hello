# -*- coding: utf-8 -*-

"""
    SFTPGo

    SFTPGo allows you to securely share your files over SFTP and optionally over HTTP/S, FTP/S and WebDAV as well. Several storage backends are supported and they are configurable per-user, so you can serve a local directory for a user and an S3 bucket (or part of it) for another one. SFTPGo also supports virtual folders, a virtual folder can use any of the supported storage backends. So you can have, for example, a user with the S3 backend mapping a Google Cloud Storage bucket (or part of it) on a specified path and an encrypted local filesystem on another one. Virtual folders can be private or shared among multiple users, for shared virtual folders you can define different quota limits for each user. SFTPGo supports groups to simplify the administration of multiple accounts by letting you assign settings once to a group, instead of multiple times to each individual user. The SFTPGo WebClient allows end users to change their credentials, browse and manage their files in the browser and setup two-factor authentication which works with Authy, Google Authenticator and other compatible apps. From the WebClient each authorized user can also create HTTP/S links to externally share files and folders securely, by setting limits to the number of downloads/uploads, protecting the share with a password, limiting access by source IP address, setting an automatic expiration date.

    The version of the OpenAPI document: 2.5.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import openapi_client
from openapi_client.api.admins_api import AdminsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestAdminsApi(unittest.TestCase):
    """AdminsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.admins_api.AdminsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_admin(self):
        """Test case for add_admin

        Add admin  # noqa: E501
        """
        pass

    def test_admin_forgot_password(self):
        """Test case for admin_forgot_password

        Send a password reset code by email  # noqa: E501
        """
        pass

    def test_admin_reset_password(self):
        """Test case for admin_reset_password

        Reset the password  # noqa: E501
        """
        pass

    def test_change_admin_password(self):
        """Test case for change_admin_password

        Change admin password  # noqa: E501
        """
        pass

    def test_delete_admin(self):
        """Test case for delete_admin

        Delete admin  # noqa: E501
        """
        pass

    def test_disable_admin2fa(self):
        """Test case for disable_admin2fa

        Disable second factor authentication  # noqa: E501
        """
        pass

    def test_generate_admin_recovery_codes(self):
        """Test case for generate_admin_recovery_codes

        Generate recovery codes  # noqa: E501
        """
        pass

    def test_generate_admin_totp_secret(self):
        """Test case for generate_admin_totp_secret

        Generate a new TOTP secret  # noqa: E501
        """
        pass

    def test_get_admin_by_username(self):
        """Test case for get_admin_by_username

        Find admins by username  # noqa: E501
        """
        pass

    def test_get_admin_profile(self):
        """Test case for get_admin_profile

        Get admin profile  # noqa: E501
        """
        pass

    def test_get_admin_recovery_codes(self):
        """Test case for get_admin_recovery_codes

        Get recovery codes  # noqa: E501
        """
        pass

    def test_get_admin_totp_configs(self):
        """Test case for get_admin_totp_configs

        Get available TOTP configuration  # noqa: E501
        """
        pass

    def test_get_admins(self):
        """Test case for get_admins

        Get admins  # noqa: E501
        """
        pass

    def test_save_admin_totp_config(self):
        """Test case for save_admin_totp_config

        Save a TOTP config  # noqa: E501
        """
        pass

    def test_update_admin(self):
        """Test case for update_admin

        Update admin  # noqa: E501
        """
        pass

    def test_update_admin_profile(self):
        """Test case for update_admin_profile

        Update admin profile  # noqa: E501
        """
        pass

    def test_validate_admin_totp_secret(self):
        """Test case for validate_admin_totp_secret

        Validate a one time authentication code  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()