# -*- coding: utf-8 -*-

"""
    SFTPGo

    SFTPGo allows you to securely share your files over SFTP and optionally over HTTP/S, FTP/S and WebDAV as well. Several storage backends are supported and they are configurable per-user, so you can serve a local directory for a user and an S3 bucket (or part of it) for another one. SFTPGo also supports virtual folders, a virtual folder can use any of the supported storage backends. So you can have, for example, a user with the S3 backend mapping a Google Cloud Storage bucket (or part of it) on a specified path and an encrypted local filesystem on another one. Virtual folders can be private or shared among multiple users, for shared virtual folders you can define different quota limits for each user. SFTPGo supports groups to simplify the administration of multiple accounts by letting you assign settings once to a group, instead of multiple times to each individual user. The SFTPGo WebClient allows end users to change their credentials, browse and manage their files in the browser and setup two-factor authentication which works with Authy, Google Authenticator and other compatible apps. From the WebClient each authorized user can also create HTTP/S links to externally share files and folders securely, by setting limits to the number of downloads/uploads, protecting the share with a password, limiting access by source IP address, setting an automatic expiration date.

    The version of the OpenAPI document: 2.5.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import openapi_client
from openapi_client.models.admin import Admin  # noqa: E501
from openapi_client.rest import ApiException


class TestAdmin(unittest.TestCase):
    """Admin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Admin
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Admin`
        """
        model = openapi_client.models.admin.Admin()  # noqa: E501
        if include_optional :
            return Admin(
                id = 1,
                status = 0,
                username = '',
                description = '',
                password = '',
                email = '',
                permissions = [
                    '*'
                    ],
                filters = openapi_client.models.admin_filters.AdminFilters(
                    allow_list = ["192.0.2.0/24","2001:db8::/32"],
                    allow_api_key_auth = True,
                    totp_config = null,
                    recovery_codes = [
                        openapi_client.models.recovery_code.RecoveryCode(
                            secret = openapi_client.models.secret.Secret(
                                status = 'Plain',
                                payload = '',
                                key = '',
                                additional_data = '',
                                mode = 56, ),
                            used = True, )
                        ],
                    preferences = openapi_client.models.admin_preferences.AdminPreferences(
                        hide_user_page_sections = 56,
                        default_users_expiration = 56, ), ),
                additional_info = '',
                groups = [
                    openapi_client.models.admin_group_mapping.AdminGroupMapping(
                        name = '',
                        options = openapi_client.models.admin_group_mapping_options.AdminGroupMappingOptions(
                            add_to_users_as = 0, ), )
                    ],
                created_at = 56,
                updated_at = 56,
                last_login = 56,
                role = ''
            )
        else :
            return Admin(
        )
        """

    def testAdmin(self):
        """Test Admin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()