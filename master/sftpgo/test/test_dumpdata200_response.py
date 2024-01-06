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
from openapi_client.models.dumpdata200_response import Dumpdata200Response  # noqa: E501
from openapi_client.rest import ApiException


class TestDumpdata200Response(unittest.TestCase):
    """Dumpdata200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Dumpdata200Response
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Dumpdata200Response`
        """
        model = openapi_client.models.dumpdata200_response.Dumpdata200Response()  # noqa: E501
        if include_optional :
            return Dumpdata200Response(
                message = '',
                error = '',
                users = [
                    openapi_client.models.user.User(
                        id = 1,
                        status = 0,
                        username = '',
                        email = '',
                        description = '',
                        expiration_date = 56,
                        password = '',
                        public_keys = [
                            'ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEUWwDwEWhTbF0MqAsp/oXK1HR2cElhM8oo1uVmL3ZeDKDiTm4ljMr92wfTgIGDqIoxmVqgYIkAOAhuykAVWBzc= user@host'
                            ],
                        has_password = True,
                        home_dir = '',
                        virtual_folders = [
                            null
                            ],
                        uid = 0,
                        gid = 0,
                        max_sessions = 56,
                        quota_size = 56,
                        quota_files = 56,
                        permissions = {"/":["*"],"/somedir":["list","download"]},
                        used_quota_size = 56,
                        used_quota_files = 56,
                        last_quota_update = 56,
                        upload_bandwidth = 56,
                        download_bandwidth = 56,
                        upload_data_transfer = 56,
                        download_data_transfer = 56,
                        total_data_transfer = 56,
                        used_upload_data_transfer = 56,
                        used_download_data_transfer = 56,
                        created_at = 56,
                        updated_at = 56,
                        last_login = 56,
                        first_download = 56,
                        first_upload = 56,
                        last_password_change = 56,
                        filters = null,
                        filesystem = openapi_client.models.filesystem_config.FilesystemConfig(
                            provider = 0,
                            osconfig = openapi_client.models.osfs_config.OSFsConfig(
                                read_buffer_size = 0,
                                write_buffer_size = 0, ),
                            s3config = openapi_client.models.s3_config.S3Config(
                                bucket = '0',
                                region = '0',
                                access_key = '',
                                access_secret = openapi_client.models.secret.Secret(
                                    status = 'Plain',
                                    payload = '',
                                    key = '',
                                    additional_data = '',
                                    mode = 56, ),
                                role_arn = '',
                                endpoint = '',
                                storage_class = '',
                                acl = '',
                                upload_part_size = 56,
                                upload_concurrency = 56,
                                upload_part_max_time = 56,
                                download_part_size = 56,
                                download_concurrency = 56,
                                download_part_max_time = 56,
                                force_path_style = True,
                                key_prefix = 'folder/subfolder/', ),
                            gcsconfig = openapi_client.models.gcs_config.GCSConfig(
                                bucket = '0',
                                credentials = openapi_client.models.secret.Secret(
                                    status = 'Plain',
                                    payload = '',
                                    key = '',
                                    additional_data = '',
                                    mode = 56, ),
                                automatic_credentials = 0,
                                storage_class = '',
                                acl = '',
                                key_prefix = 'folder/subfolder/',
                                upload_part_size = 56,
                                upload_part_max_time = 56, ),
                            azblobconfig = openapi_client.models.azure_blob_fs_config.AzureBlobFsConfig(
                                container = '',
                                account_name = '',
                                account_key = ,
                                sas_url = ,
                                endpoint = '',
                                upload_part_size = 56,
                                upload_concurrency = 56,
                                download_part_size = 56,
                                download_concurrency = 56,
                                access_tier = '',
                                key_prefix = 'folder/subfolder/',
                                use_emulator = True, ),
                            cryptconfig = openapi_client.models.crypt_fs_config.CryptFsConfig(
                                passphrase = ,
                                read_buffer_size = 0,
                                write_buffer_size = 0, ),
                            sftpconfig = openapi_client.models.sftpfs_config.SFTPFsConfig(
                                endpoint = '',
                                username = '',
                                password = ,
                                private_key = ,
                                key_passphrase = ,
                                fingerprints = [
                                    ''
                                    ],
                                prefix = '',
                                disable_concurrent_reads = True,
                                buffer_size = 2,
                                equality_check_mode = 0, ),
                            httpconfig = openapi_client.models.httpfs_config.HTTPFsConfig(
                                endpoint = '',
                                username = '',
                                api_key = ,
                                skip_tls_verify = True,
                                equality_check_mode = 0, ), ),
                        additional_info = '',
                        groups = [
                            openapi_client.models.group_mapping.GroupMapping(
                                name = '',
                                type = 1, )
                            ],
                        oidc_custom_fields = { },
                        role = '', )
                    ],
                folders = [
                    openapi_client.models.base_virtual_folder.BaseVirtualFolder(
                        id = 1,
                        name = '',
                        mapped_path = '',
                        description = '',
                        used_quota_size = 56,
                        used_quota_files = 56,
                        last_quota_update = 56,
                        users = [
                            ''
                            ],
                        filesystem = openapi_client.models.filesystem_config.FilesystemConfig(
                            provider = 0,
                            osconfig = openapi_client.models.osfs_config.OSFsConfig(
                                read_buffer_size = 0,
                                write_buffer_size = 0, ),
                            s3config = openapi_client.models.s3_config.S3Config(
                                bucket = '0',
                                region = '0',
                                access_key = '',
                                access_secret = openapi_client.models.secret.Secret(
                                    status = 'Plain',
                                    payload = '',
                                    key = '',
                                    additional_data = '',
                                    mode = 56, ),
                                role_arn = '',
                                endpoint = '',
                                storage_class = '',
                                acl = '',
                                upload_part_size = 56,
                                upload_concurrency = 56,
                                upload_part_max_time = 56,
                                download_part_size = 56,
                                download_concurrency = 56,
                                download_part_max_time = 56,
                                force_path_style = True,
                                key_prefix = 'folder/subfolder/', ),
                            gcsconfig = openapi_client.models.gcs_config.GCSConfig(
                                bucket = '0',
                                credentials = openapi_client.models.secret.Secret(
                                    status = 'Plain',
                                    payload = '',
                                    key = '',
                                    additional_data = '',
                                    mode = 56, ),
                                automatic_credentials = 0,
                                storage_class = '',
                                acl = '',
                                key_prefix = 'folder/subfolder/',
                                upload_part_size = 56,
                                upload_part_max_time = 56, ),
                            azblobconfig = openapi_client.models.azure_blob_fs_config.AzureBlobFsConfig(
                                container = '',
                                account_name = '',
                                account_key = ,
                                sas_url = ,
                                endpoint = '',
                                upload_part_size = 56,
                                upload_concurrency = 56,
                                download_part_size = 56,
                                download_concurrency = 56,
                                access_tier = '',
                                key_prefix = 'folder/subfolder/',
                                use_emulator = True, ),
                            cryptconfig = openapi_client.models.crypt_fs_config.CryptFsConfig(
                                passphrase = ,
                                read_buffer_size = 0,
                                write_buffer_size = 0, ),
                            sftpconfig = openapi_client.models.sftpfs_config.SFTPFsConfig(
                                endpoint = '',
                                username = '',
                                password = ,
                                private_key = ,
                                key_passphrase = ,
                                fingerprints = [
                                    ''
                                    ],
                                prefix = '',
                                disable_concurrent_reads = True,
                                buffer_size = 2,
                                equality_check_mode = 0, ),
                            httpconfig = openapi_client.models.httpfs_config.HTTPFsConfig(
                                endpoint = '',
                                username = '',
                                api_key = ,
                                skip_tls_verify = True,
                                equality_check_mode = 0, ), ), )
                    ],
                groups = [
                    openapi_client.models.group.Group(
                        id = 1,
                        name = '',
                        description = '',
                        created_at = 56,
                        updated_at = 56,
                        user_settings = openapi_client.models.group_user_settings.GroupUserSettings(
                            home_dir = '',
                            max_sessions = 56,
                            quota_size = 56,
                            quota_files = 56,
                            permissions = {"/":["*"],"/somedir":["list","download"]},
                            upload_bandwidth = 56,
                            download_bandwidth = 56,
                            upload_data_transfer = 56,
                            download_data_transfer = 56,
                            total_data_transfer = 56,
                            expires_in = 56,
                            filters = openapi_client.models.base_user_filters.BaseUserFilters(
                                allowed_ip = ["192.0.2.0/24","2001:db8::/32"],
                                denied_ip = ["172.16.0.0/16"],
                                denied_login_methods = [
                                    'publickey'
                                    ],
                                denied_protocols = [
                                    'SSH'
                                    ],
                                file_patterns = [
                                    openapi_client.models.patterns_filter.PatternsFilter(
                                        path = '',
                                        allowed_patterns = ["*.jpg","a*b?.png"],
                                        denied_patterns = ["*.zip"],
                                        deny_policy = 0, )
                                    ],
                                max_upload_file_size = 56,
                                tls_username = '',
                                hooks = openapi_client.models.hooks_filter.HooksFilter(
                                    external_auth_disabled = False,
                                    pre_login_disabled = False,
                                    check_password_disabled = False, ),
                                disable_fs_checks = False,
                                web_client = [
                                    'publickey-change-disabled'
                                    ],
                                allow_api_key_auth = True,
                                user_type = '',
                                bandwidth_limits = [
                                    openapi_client.models.bandwidth_limit.BandwidthLimit(
                                        sources = [
                                            ''
                                            ],
                                        upload_bandwidth = 56,
                                        download_bandwidth = 56, )
                                    ],
                                external_auth_cache_time = 56,
                                start_directory = '',
                                two_factor_protocols = [
                                    'SSH'
                                    ],
                                ftp_security = 0,
                                is_anonymous = True,
                                default_shares_expiration = 56,
                                password_expiration = 56, ),
                            filesystem = openapi_client.models.filesystem_config.FilesystemConfig(
                                provider = 0,
                                osconfig = openapi_client.models.osfs_config.OSFsConfig(
                                    read_buffer_size = 0,
                                    write_buffer_size = 0, ),
                                s3config = openapi_client.models.s3_config.S3Config(
                                    bucket = '0',
                                    region = '0',
                                    access_key = '',
                                    access_secret = openapi_client.models.secret.Secret(
                                        status = 'Plain',
                                        payload = '',
                                        key = '',
                                        additional_data = '',
                                        mode = 56, ),
                                    role_arn = '',
                                    endpoint = '',
                                    storage_class = '',
                                    acl = '',
                                    upload_part_size = 56,
                                    upload_concurrency = 56,
                                    upload_part_max_time = 56,
                                    download_part_size = 56,
                                    download_concurrency = 56,
                                    download_part_max_time = 56,
                                    force_path_style = True,
                                    key_prefix = 'folder/subfolder/', ),
                                gcsconfig = openapi_client.models.gcs_config.GCSConfig(
                                    bucket = '0',
                                    credentials = openapi_client.models.secret.Secret(
                                        status = 'Plain',
                                        payload = '',
                                        key = '',
                                        additional_data = '',
                                        mode = 56, ),
                                    automatic_credentials = 0,
                                    storage_class = '',
                                    acl = '',
                                    key_prefix = 'folder/subfolder/',
                                    upload_part_size = 56,
                                    upload_part_max_time = 56, ),
                                azblobconfig = openapi_client.models.azure_blob_fs_config.AzureBlobFsConfig(
                                    container = '',
                                    account_name = '',
                                    account_key = ,
                                    sas_url = ,
                                    endpoint = '',
                                    upload_part_size = 56,
                                    upload_concurrency = 56,
                                    download_part_size = 56,
                                    download_concurrency = 56,
                                    access_tier = '',
                                    key_prefix = 'folder/subfolder/',
                                    use_emulator = True, ),
                                cryptconfig = openapi_client.models.crypt_fs_config.CryptFsConfig(
                                    passphrase = ,
                                    read_buffer_size = 0,
                                    write_buffer_size = 0, ),
                                sftpconfig = openapi_client.models.sftpfs_config.SFTPFsConfig(
                                    endpoint = '',
                                    username = '',
                                    password = ,
                                    private_key = ,
                                    key_passphrase = ,
                                    fingerprints = [
                                        ''
                                        ],
                                    prefix = '',
                                    disable_concurrent_reads = True,
                                    buffer_size = 2,
                                    equality_check_mode = 0, ),
                                httpconfig = openapi_client.models.httpfs_config.HTTPFsConfig(
                                    endpoint = '',
                                    username = '',
                                    api_key = ,
                                    skip_tls_verify = True,
                                    equality_check_mode = 0, ), ), ),
                        virtual_folders = [
                            null
                            ],
                        users = [
                            ''
                            ],
                        admins = [
                            ''
                            ], )
                    ],
                admins = [
                    openapi_client.models.admin.Admin(
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
                        role = '', )
                    ],
                api_keys = [
                    openapi_client.models.api_key.APIKey(
                        id = '',
                        name = '',
                        key = '',
                        scope = 1,
                        created_at = 56,
                        updated_at = 56,
                        last_use_at = 56,
                        expires_at = 56,
                        description = '',
                        user = '',
                        admin = '', )
                    ],
                shares = [
                    openapi_client.models.share.Share(
                        id = '',
                        name = '',
                        description = '',
                        scope = 1,
                        paths = ["/dir1","/dir2/file.txt","/dir3/subdir"],
                        username = '',
                        created_at = 56,
                        updated_at = 56,
                        last_use_at = 56,
                        expires_at = 56,
                        password = '',
                        max_tokens = 56,
                        used_tokens = 56,
                        allow_from = ["192.0.2.0/24","2001:db8::/32"], )
                    ],
                event_actions = [
                    null
                    ],
                event_rules = [
                    null
                    ],
                roles = [
                    openapi_client.models.role.Role(
                        id = 1,
                        name = '',
                        description = '',
                        created_at = 56,
                        updated_at = 56,
                        users = [
                            ''
                            ],
                        admins = [
                            ''
                            ], )
                    ],
                version = 56
            )
        else :
            return Dumpdata200Response(
        )
        """

    def testDumpdata200Response(self):
        """Test Dumpdata200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
