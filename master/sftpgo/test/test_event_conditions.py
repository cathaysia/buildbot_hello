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
from openapi_client.models.event_conditions import EventConditions  # noqa: E501
from openapi_client.rest import ApiException


class TestEventConditions(unittest.TestCase):
    """EventConditions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EventConditions
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `EventConditions`
        """
        model = openapi_client.models.event_conditions.EventConditions()  # noqa: E501
        if include_optional :
            return EventConditions(
                fs_events = [
                    'upload'
                    ],
                provider_events = [
                    'add'
                    ],
                schedules = [
                    openapi_client.models.schedule.Schedule(
                        hour = '',
                        day_of_week = '',
                        day_of_month = '',
                        month = '', )
                    ],
                idp_login_event = 0,
                options = openapi_client.models.condition_options.ConditionOptions(
                    names = [
                        openapi_client.models.condition_pattern.ConditionPattern(
                            pattern = '',
                            inverse_match = True, )
                        ],
                    group_names = [
                        openapi_client.models.condition_pattern.ConditionPattern(
                            pattern = '',
                            inverse_match = True, )
                        ],
                    role_names = [

                        ],
                    fs_paths = [

                        ],
                    protocols = [
                        'SFTP'
                        ],
                    provider_objects = [
                        'user'
                        ],
                    min_size = 56,
                    max_size = 56,
                    concurrent_execution = True, )
            )
        else :
            return EventConditions(
        )
        """

    def testEventConditions(self):
        """Test EventConditions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
