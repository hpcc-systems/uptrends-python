# coding: utf-8

"""
    Uptrends API v4

    This document describes Uptrends API version 4. This Swagger environment also lets you execute API methods directly.  Please note that this is not a sandbox environment: these API methods operate directly on your actual Uptrends account.  For more information, please visit https://www.uptrends.com/api.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from uptrends.api_client import ApiClient


class CheckpointApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def checkpoint_get_all_checkpoints(self, **kwargs):  # noqa: E501
        """Returns all the checkpoints.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_get_all_checkpoints(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Checkpoint]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.checkpoint_get_all_checkpoints_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.checkpoint_get_all_checkpoints_with_http_info(**kwargs)  # noqa: E501
            return data

    def checkpoint_get_all_checkpoints_with_http_info(self, **kwargs):  # noqa: E501
        """Returns all the checkpoints.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_get_all_checkpoints_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Checkpoint]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method checkpoint_get_all_checkpoints" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicauth']  # noqa: E501

        return self.api_client.call_api(
            '/Checkpoint', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Checkpoint]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def checkpoint_get_checkpoint(self, checkpoint_id, **kwargs):  # noqa: E501
        """Returns the specified checkpoint.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_get_checkpoint(checkpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int checkpoint_id: The Id of the requested checkpoint. (required)
        :return: Checkpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.checkpoint_get_checkpoint_with_http_info(checkpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.checkpoint_get_checkpoint_with_http_info(checkpoint_id, **kwargs)  # noqa: E501
            return data

    def checkpoint_get_checkpoint_with_http_info(self, checkpoint_id, **kwargs):  # noqa: E501
        """Returns the specified checkpoint.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_get_checkpoint_with_http_info(checkpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int checkpoint_id: The Id of the requested checkpoint. (required)
        :return: Checkpoint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['checkpoint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method checkpoint_get_checkpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'checkpoint_id' is set
        if ('checkpoint_id' not in params or
                params['checkpoint_id'] is None):
            raise ValueError("Missing the required parameter `checkpoint_id` when calling `checkpoint_get_checkpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'checkpoint_id' in params:
            path_params['checkpointId'] = params['checkpoint_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicauth']  # noqa: E501

        return self.api_client.call_api(
            '/Checkpoint/{checkpointId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Checkpoint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def checkpoint_region_get_all_checkpoint_regions(self, **kwargs):  # noqa: E501
        """Returns all the checkpoint regions.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_region_get_all_checkpoint_regions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CheckpointRegion]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.checkpoint_region_get_all_checkpoint_regions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.checkpoint_region_get_all_checkpoint_regions_with_http_info(**kwargs)  # noqa: E501
            return data

    def checkpoint_region_get_all_checkpoint_regions_with_http_info(self, **kwargs):  # noqa: E501
        """Returns all the checkpoint regions.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_region_get_all_checkpoint_regions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CheckpointRegion]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method checkpoint_region_get_all_checkpoint_regions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicauth']  # noqa: E501

        return self.api_client.call_api(
            '/CheckpointRegion', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CheckpointRegion]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def checkpoint_region_get_checkpoint_region_checkpoints(self, checkpoint_region_id, **kwargs):  # noqa: E501
        """Returns the checkpoints for the specified checkpoint region.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_region_get_checkpoint_region_checkpoints(checkpoint_region_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int checkpoint_region_id: The id for the specified checkpoint region. (required)
        :return: list[Checkpoint]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.checkpoint_region_get_checkpoint_region_checkpoints_with_http_info(checkpoint_region_id, **kwargs)  # noqa: E501
        else:
            (data) = self.checkpoint_region_get_checkpoint_region_checkpoints_with_http_info(checkpoint_region_id, **kwargs)  # noqa: E501
            return data

    def checkpoint_region_get_checkpoint_region_checkpoints_with_http_info(self, checkpoint_region_id, **kwargs):  # noqa: E501
        """Returns the checkpoints for the specified checkpoint region.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_region_get_checkpoint_region_checkpoints_with_http_info(checkpoint_region_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int checkpoint_region_id: The id for the specified checkpoint region. (required)
        :return: list[Checkpoint]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['checkpoint_region_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method checkpoint_region_get_checkpoint_region_checkpoints" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'checkpoint_region_id' is set
        if ('checkpoint_region_id' not in params or
                params['checkpoint_region_id'] is None):
            raise ValueError("Missing the required parameter `checkpoint_region_id` when calling `checkpoint_region_get_checkpoint_region_checkpoints`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'checkpoint_region_id' in params:
            path_params['checkpointRegionId'] = params['checkpoint_region_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicauth']  # noqa: E501

        return self.api_client.call_api(
            '/CheckpointRegion/{checkpointRegionId}/Checkpoint', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Checkpoint]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def checkpoint_region_get_specified_checkpoint_region(self, checkpoint_region_id, **kwargs):  # noqa: E501
        """Returns the specified checkpoint region.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_region_get_specified_checkpoint_region(checkpoint_region_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int checkpoint_region_id: The id for the specified checkpoint region. (required)
        :return: CheckpointRegion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.checkpoint_region_get_specified_checkpoint_region_with_http_info(checkpoint_region_id, **kwargs)  # noqa: E501
        else:
            (data) = self.checkpoint_region_get_specified_checkpoint_region_with_http_info(checkpoint_region_id, **kwargs)  # noqa: E501
            return data

    def checkpoint_region_get_specified_checkpoint_region_with_http_info(self, checkpoint_region_id, **kwargs):  # noqa: E501
        """Returns the specified checkpoint region.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_region_get_specified_checkpoint_region_with_http_info(checkpoint_region_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int checkpoint_region_id: The id for the specified checkpoint region. (required)
        :return: CheckpointRegion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['checkpoint_region_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method checkpoint_region_get_specified_checkpoint_region" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'checkpoint_region_id' is set
        if ('checkpoint_region_id' not in params or
                params['checkpoint_region_id'] is None):
            raise ValueError("Missing the required parameter `checkpoint_region_id` when calling `checkpoint_region_get_specified_checkpoint_region`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'checkpoint_region_id' in params:
            path_params['checkpointRegionId'] = params['checkpoint_region_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicauth']  # noqa: E501

        return self.api_client.call_api(
            '/CheckpointRegion/{checkpointRegionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CheckpointRegion',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def checkpoint_server_get_all_server_ipv4_addresses(self, **kwargs):  # noqa: E501
        """Anonymous call that returns all the IPv4 addresses of all the checkpoint servers.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_server_get_all_server_ipv4_addresses(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.checkpoint_server_get_all_server_ipv4_addresses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.checkpoint_server_get_all_server_ipv4_addresses_with_http_info(**kwargs)  # noqa: E501
            return data

    def checkpoint_server_get_all_server_ipv4_addresses_with_http_info(self, **kwargs):  # noqa: E501
        """Anonymous call that returns all the IPv4 addresses of all the checkpoint servers.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_server_get_all_server_ipv4_addresses_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method checkpoint_server_get_all_server_ipv4_addresses" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/Checkpoint/Server/Ipv4', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def checkpoint_server_get_all_server_ipv6_addresses(self, **kwargs):  # noqa: E501
        """Anonymous call that returns all the IPv6 addresses of all the checkpoint servers.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_server_get_all_server_ipv6_addresses(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.checkpoint_server_get_all_server_ipv6_addresses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.checkpoint_server_get_all_server_ipv6_addresses_with_http_info(**kwargs)  # noqa: E501
            return data

    def checkpoint_server_get_all_server_ipv6_addresses_with_http_info(self, **kwargs):  # noqa: E501
        """Anonymous call that returns all the IPv6 addresses of all the checkpoint servers.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_server_get_all_server_ipv6_addresses_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method checkpoint_server_get_all_server_ipv6_addresses" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/Checkpoint/Server/Ipv6', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def checkpoint_server_get_server(self, server_id, **kwargs):  # noqa: E501
        """Returns the requested checkpoint server.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_server_get_server(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int server_id: The Id of the requested server. (required)
        :return: CheckpointServer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.checkpoint_server_get_server_with_http_info(server_id, **kwargs)  # noqa: E501
        else:
            (data) = self.checkpoint_server_get_server_with_http_info(server_id, **kwargs)  # noqa: E501
            return data

    def checkpoint_server_get_server_with_http_info(self, server_id, **kwargs):  # noqa: E501
        """Returns the requested checkpoint server.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.checkpoint_server_get_server_with_http_info(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int server_id: The Id of the requested server. (required)
        :return: CheckpointServer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method checkpoint_server_get_server" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params or
                params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `checkpoint_server_get_server`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['serverId'] = params['server_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicauth']  # noqa: E501

        return self.api_client.call_api(
            '/Checkpoint/Server/{serverId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CheckpointServer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
