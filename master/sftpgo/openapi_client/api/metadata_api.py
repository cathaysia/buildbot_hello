# -*- coding: utf-8 -*-

"""
    SFTPGo

    SFTPGo allows you to securely share your files over SFTP and optionally over HTTP/S, FTP/S and WebDAV as well. Several storage backends are supported and they are configurable per-user, so you can serve a local directory for a user and an S3 bucket (or part of it) for another one. SFTPGo also supports virtual folders, a virtual folder can use any of the supported storage backends. So you can have, for example, a user with the S3 backend mapping a Google Cloud Storage bucket (or part of it) on a specified path and an encrypted local filesystem on another one. Virtual folders can be private or shared among multiple users, for shared virtual folders you can define different quota limits for each user. SFTPGo supports groups to simplify the administration of multiple accounts by letting you assign settings once to a group, instead of multiple times to each individual user. The SFTPGo WebClient allows end users to change their credentials, browse and manage their files in the browser and setup two-factor authentication which works with Authy, Google Authenticator and other compatible apps. From the WebClient each authorized user can also create HTTP/S links to externally share files and folders securely, by setting limits to the number of downloads/uploads, protecting the share with a password, limiting access by source IP address, setting an automatic expiration date.

    The version of the OpenAPI document: 2.5.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr

from typing import List

from openapi_client.models.api_response import ApiResponse
from openapi_client.models.metadata_check import MetadataCheck

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class MetadataApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_users_metadata_checks(self, **kwargs) -> List[MetadataCheck]:  # noqa: E501
        """Get metadata checks  # noqa: E501

        Returns the active metadata checks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_users_metadata_checks(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[MetadataCheck]
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the get_users_metadata_checks_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        return self.get_users_metadata_checks_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_users_metadata_checks_with_http_info(
        self, **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Get metadata checks  # noqa: E501

        Returns the active metadata checks  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_users_metadata_checks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[MetadataCheck], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = []
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_users_metadata_checks" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["APIKeyAuth", "BearerAuth"]  # noqa: E501

        _response_types_map = {
            "200": "List[MetadataCheck]",
            "401": "ApiResponse",
            "403": "ApiResponse",
            "500": "ApiResponse",
        }

        return self.api_client.call_api(
            "/metadata/users/checks",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def start_user_metadata_check(
        self,
        username: Annotated[StrictStr, Field(..., description="the username")],
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Start a metadata check  # noqa: E501

        Starts a new metadata check for the given user. A metadata check requires a metadata plugin and removes the metadata associated to missing items (for example objects deleted outside SFTPGo). If a metadata check for this user is already active a 409 status code is returned. Metadata are stored for cloud storage backends. This API does nothing for other backends or if no metadata plugin is configured  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.start_user_metadata_check(username, async_req=True)
        >>> result = thread.get()

        :param username: the username (required)
        :type username: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiResponse
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the start_user_metadata_check_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        return self.start_user_metadata_check_with_http_info(
            username, **kwargs
        )  # noqa: E501

    @validate_arguments
    def start_user_metadata_check_with_http_info(
        self,
        username: Annotated[StrictStr, Field(..., description="the username")],
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Start a metadata check  # noqa: E501

        Starts a new metadata check for the given user. A metadata check requires a metadata plugin and removes the metadata associated to missing items (for example objects deleted outside SFTPGo). If a metadata check for this user is already active a 409 status code is returned. Metadata are stored for cloud storage backends. This API does nothing for other backends or if no metadata plugin is configured  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.start_user_metadata_check_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param username: the username (required)
        :type username: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ApiResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["username"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_user_metadata_check" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["username"]:
            _path_params["username"] = _params["username"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["APIKeyAuth", "BearerAuth"]  # noqa: E501

        _response_types_map = {
            "202": "ApiResponse",
            "400": "ApiResponse",
            "401": "ApiResponse",
            "403": "ApiResponse",
            "404": "ApiResponse",
            "409": "ApiResponse",
            "500": "ApiResponse",
        }

        return self.api_client.call_api(
            "/metadata/users/{username}/check",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )
