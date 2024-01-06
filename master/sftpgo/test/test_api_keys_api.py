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
from openapi_client.api.api_keys_api import APIKeysApi  # noqa: E501
from openapi_client.rest import ApiException


class TestAPIKeysApi(unittest.TestCase):
    """APIKeysApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.api_keys_api.APIKeysApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_api_key(self):
        """Test case for add_api_key

        Add API key  # noqa: E501
        """
        pass

    def test_delete_api_key(self):
        """Test case for delete_api_key

        Delete API key  # noqa: E501
        """
        pass

    def test_get_api_key_by_id(self):
        """Test case for get_api_key_by_id

        Find API key by id  # noqa: E501
        """
        pass

    def test_get_api_keys(self):
        """Test case for get_api_keys

        Get API keys  # noqa: E501
        """
        pass

    def test_update_api_key(self):
        """Test case for update_api_key

        Update API key  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
