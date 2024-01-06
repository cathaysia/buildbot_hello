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

from pydantic import Field, StrictInt, StrictStr, conint

from typing import List, Optional

from openapi_client.models.api_response import ApiResponse
from openapi_client.models.group import Group

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class GroupsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def add_group(
        self,
        group: Group,
        confidential_data: Annotated[
            Optional[StrictInt],
            Field(
                description="If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted."
            ),
        ] = None,
        **kwargs
    ) -> Group:  # noqa: E501
        """Add group  # noqa: E501

        Adds a new group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_group(group, confidential_data, async_req=True)
        >>> result = thread.get()

        :param group: (required)
        :type group: Group
        :param confidential_data: If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted.
        :type confidential_data: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Group
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the add_group_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        return self.add_group_with_http_info(
            group, confidential_data, **kwargs
        )  # noqa: E501

    @validate_arguments
    def add_group_with_http_info(
        self,
        group: Group,
        confidential_data: Annotated[
            Optional[StrictInt],
            Field(
                description="If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted."
            ),
        ] = None,
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Add group  # noqa: E501

        Adds a new group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_group_with_http_info(group, confidential_data, async_req=True)
        >>> result = thread.get()

        :param group: (required)
        :type group: Group
        :param confidential_data: If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted.
        :type confidential_data: int
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
        :rtype: tuple(Group, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["group", "confidential_data"]
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
                    " to method add_group" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get("confidential_data") is not None:  # noqa: E501
            _query_params.append(("confidential_data", _params["confidential_data"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params["group"] is not None:
            _body_params = _params["group"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings = ["APIKeyAuth", "BearerAuth"]  # noqa: E501

        _response_types_map = {
            "201": "Group",
            "400": "ApiResponse",
            "401": "ApiResponse",
            "403": "ApiResponse",
            "500": "ApiResponse",
        }

        return self.api_client.call_api(
            "/groups",
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

    @validate_arguments
    def delete_group(
        self, name: Annotated[StrictStr, Field(..., description="group name")], **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Delete group  # noqa: E501

        Deletes an existing group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_group(name, async_req=True)
        >>> result = thread.get()

        :param name: group name (required)
        :type name: str
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
                "Error! Please call the delete_group_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        return self.delete_group_with_http_info(name, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_group_with_http_info(
        self, name: Annotated[StrictStr, Field(..., description="group name")], **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Delete group  # noqa: E501

        Deletes an existing group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_group_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param name: group name (required)
        :type name: str
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

        _all_params = ["name"]
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
                    " to method delete_group" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["name"]:
            _path_params["name"] = _params["name"]

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
            "200": "ApiResponse",
            "400": "ApiResponse",
            "401": "ApiResponse",
            "403": "ApiResponse",
            "404": "ApiResponse",
            "500": "ApiResponse",
        }

        return self.api_client.call_api(
            "/groups/{name}",
            "DELETE",
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
    def get_group_by_name(
        self,
        name: Annotated[StrictStr, Field(..., description="group name")],
        confidential_data: Annotated[
            Optional[StrictInt],
            Field(
                description="If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted."
            ),
        ] = None,
        **kwargs
    ) -> Group:  # noqa: E501
        """Find groups by name  # noqa: E501

        Returns the group with the given name if it exists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_group_by_name(name, confidential_data, async_req=True)
        >>> result = thread.get()

        :param name: group name (required)
        :type name: str
        :param confidential_data: If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted.
        :type confidential_data: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Group
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the get_group_by_name_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        return self.get_group_by_name_with_http_info(
            name, confidential_data, **kwargs
        )  # noqa: E501

    @validate_arguments
    def get_group_by_name_with_http_info(
        self,
        name: Annotated[StrictStr, Field(..., description="group name")],
        confidential_data: Annotated[
            Optional[StrictInt],
            Field(
                description="If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted."
            ),
        ] = None,
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Find groups by name  # noqa: E501

        Returns the group with the given name if it exists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_group_by_name_with_http_info(name, confidential_data, async_req=True)
        >>> result = thread.get()

        :param name: group name (required)
        :type name: str
        :param confidential_data: If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the manage_system permission is not granted.
        :type confidential_data: int
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
        :rtype: tuple(Group, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["name", "confidential_data"]
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
                    " to method get_group_by_name" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["name"]:
            _path_params["name"] = _params["name"]

        # process the query parameters
        _query_params = []
        if _params.get("confidential_data") is not None:  # noqa: E501
            _query_params.append(("confidential_data", _params["confidential_data"]))

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
            "200": "Group",
            "400": "ApiResponse",
            "401": "ApiResponse",
            "403": "ApiResponse",
            "404": "ApiResponse",
            "500": "ApiResponse",
        }

        return self.api_client.call_api(
            "/groups/{name}",
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
    def get_groups(
        self,
        offset: Optional[conint(strict=True, ge=0)] = None,
        limit: Annotated[
            Optional[conint(strict=True, le=500, ge=1)],
            Field(
                description="The maximum number of items to return. Max value is 500, default is 100"
            ),
        ] = None,
        order: Annotated[
            Optional[StrictStr],
            Field(description="Ordering groups by name. Default ASC"),
        ] = None,
        **kwargs
    ) -> List[Group]:  # noqa: E501
        """Get groups  # noqa: E501

        Returns an array with one or more groups  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_groups(offset, limit, order, async_req=True)
        >>> result = thread.get()

        :param offset:
        :type offset: int
        :param limit: The maximum number of items to return. Max value is 500, default is 100
        :type limit: int
        :param order: Ordering groups by name. Default ASC
        :type order: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[Group]
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the get_groups_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        return self.get_groups_with_http_info(
            offset, limit, order, **kwargs
        )  # noqa: E501

    @validate_arguments
    def get_groups_with_http_info(
        self,
        offset: Optional[conint(strict=True, ge=0)] = None,
        limit: Annotated[
            Optional[conint(strict=True, le=500, ge=1)],
            Field(
                description="The maximum number of items to return. Max value is 500, default is 100"
            ),
        ] = None,
        order: Annotated[
            Optional[StrictStr],
            Field(description="Ordering groups by name. Default ASC"),
        ] = None,
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Get groups  # noqa: E501

        Returns an array with one or more groups  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_groups_with_http_info(offset, limit, order, async_req=True)
        >>> result = thread.get()

        :param offset:
        :type offset: int
        :param limit: The maximum number of items to return. Max value is 500, default is 100
        :type limit: int
        :param order: Ordering groups by name. Default ASC
        :type order: str
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
        :rtype: tuple(List[Group], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["offset", "limit", "order"]
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
                    " to method get_groups" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get("offset") is not None:  # noqa: E501
            _query_params.append(("offset", _params["offset"]))

        if _params.get("limit") is not None:  # noqa: E501
            _query_params.append(("limit", _params["limit"]))

        if _params.get("order") is not None:  # noqa: E501
            _query_params.append(("order", _params["order"]))

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
            "200": "List[Group]",
            "400": "ApiResponse",
            "401": "ApiResponse",
            "403": "ApiResponse",
            "500": "ApiResponse",
        }

        return self.api_client.call_api(
            "/groups",
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
    def update_group(
        self,
        name: Annotated[StrictStr, Field(..., description="group name")],
        group: Group,
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Update group  # noqa: E501

        Updates an existing group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_group(name, group, async_req=True)
        >>> result = thread.get()

        :param name: group name (required)
        :type name: str
        :param group: (required)
        :type group: Group
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
                "Error! Please call the update_group_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        return self.update_group_with_http_info(name, group, **kwargs)  # noqa: E501

    @validate_arguments
    def update_group_with_http_info(
        self,
        name: Annotated[StrictStr, Field(..., description="group name")],
        group: Group,
        **kwargs
    ) -> ApiResponse:  # noqa: E501
        """Update group  # noqa: E501

        Updates an existing group  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_group_with_http_info(name, group, async_req=True)
        >>> result = thread.get()

        :param name: group name (required)
        :type name: str
        :param group: (required)
        :type group: Group
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

        _all_params = ["name", "group"]
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
                    " to method update_group" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["name"]:
            _path_params["name"] = _params["name"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params["group"] is not None:
            _body_params = _params["group"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings = ["APIKeyAuth", "BearerAuth"]  # noqa: E501

        _response_types_map = {
            "200": "ApiResponse",
            "400": "ApiResponse",
            "401": "ApiResponse",
            "403": "ApiResponse",
            "404": "ApiResponse",
            "500": "ApiResponse",
        }

        return self.api_client.call_api(
            "/groups/{name}",
            "PUT",
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
