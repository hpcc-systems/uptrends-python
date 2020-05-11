# coding: utf-8

"""
    Uptrends API v4

    This document describes Uptrends API version 4. This Swagger environment also lets you execute API methods directly.  Please note that this is not a sandbox environment: these API methods operate directly on your actual Uptrends account.  For more information, please visit https://www.uptrends.com/api.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PageElement(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'index': 'int',
        'start_time': 'int',
        'resolve_time': 'int',
        'connect_time': 'int',
        'stale_time': 'int',
        'https_handshake_time': 'int',
        'send_time': 'int',
        'wait_time': 'int',
        'receive_time': 'int',
        'timeout_time': 'int',
        'total_time': 'int',
        'http_status_code': 'int',
        'url': 'str',
        'total_bytes': 'int',
        'element_type': 'str',
        'request_headers': 'str',
        'response_headers': 'str',
        'resolved_ip_address': 'object',
        'group_ids': 'list[int]',
        'url_is_blocked': 'bool'
    }

    attribute_map = {
        'index': 'Index',
        'start_time': 'StartTime',
        'resolve_time': 'ResolveTime',
        'connect_time': 'ConnectTime',
        'stale_time': 'StaleTime',
        'https_handshake_time': 'HttpsHandshakeTime',
        'send_time': 'SendTime',
        'wait_time': 'WaitTime',
        'receive_time': 'ReceiveTime',
        'timeout_time': 'TimeoutTime',
        'total_time': 'TotalTime',
        'http_status_code': 'HttpStatusCode',
        'url': 'Url',
        'total_bytes': 'TotalBytes',
        'element_type': 'ElementType',
        'request_headers': 'RequestHeaders',
        'response_headers': 'ResponseHeaders',
        'resolved_ip_address': 'ResolvedIpAddress',
        'group_ids': 'GroupIds',
        'url_is_blocked': 'UrlIsBlocked'
    }

    def __init__(self, index=None, start_time=None, resolve_time=None, connect_time=None, stale_time=None, https_handshake_time=None, send_time=None, wait_time=None, receive_time=None, timeout_time=None, total_time=None, http_status_code=None, url=None, total_bytes=None, element_type=None, request_headers=None, response_headers=None, resolved_ip_address=None, group_ids=None, url_is_blocked=None):  # noqa: E501
        """PageElement - a model defined in Swagger"""  # noqa: E501

        self._index = None
        self._start_time = None
        self._resolve_time = None
        self._connect_time = None
        self._stale_time = None
        self._https_handshake_time = None
        self._send_time = None
        self._wait_time = None
        self._receive_time = None
        self._timeout_time = None
        self._total_time = None
        self._http_status_code = None
        self._url = None
        self._total_bytes = None
        self._element_type = None
        self._request_headers = None
        self._response_headers = None
        self._resolved_ip_address = None
        self._group_ids = None
        self._url_is_blocked = None
        self.discriminator = None

        self.index = index
        self.start_time = start_time
        self.resolve_time = resolve_time
        self.connect_time = connect_time
        self.stale_time = stale_time
        self.https_handshake_time = https_handshake_time
        self.send_time = send_time
        self.wait_time = wait_time
        self.receive_time = receive_time
        self.timeout_time = timeout_time
        self.total_time = total_time
        self.http_status_code = http_status_code
        if url is not None:
            self.url = url
        self.total_bytes = total_bytes
        if element_type is not None:
            self.element_type = element_type
        if request_headers is not None:
            self.request_headers = request_headers
        if response_headers is not None:
            self.response_headers = response_headers
        if resolved_ip_address is not None:
            self.resolved_ip_address = resolved_ip_address
        if group_ids is not None:
            self.group_ids = group_ids
        self.url_is_blocked = url_is_blocked

    @property
    def index(self):
        """Gets the index of this PageElement.  # noqa: E501

        Index of the element in the waterfall context  # noqa: E501

        :return: The index of this PageElement.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this PageElement.

        Index of the element in the waterfall context  # noqa: E501

        :param index: The index of this PageElement.  # noqa: E501
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def start_time(self):
        """Gets the start_time of this PageElement.  # noqa: E501

        Starting time in milliseconds  # noqa: E501

        :return: The start_time of this PageElement.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PageElement.

        Starting time in milliseconds  # noqa: E501

        :param start_time: The start_time of this PageElement.  # noqa: E501
        :type: int
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def resolve_time(self):
        """Gets the resolve_time of this PageElement.  # noqa: E501

        Number of milliseconds needed to perform the DNS query for this element, when appropriate.  # noqa: E501

        :return: The resolve_time of this PageElement.  # noqa: E501
        :rtype: int
        """
        return self._resolve_time

    @resolve_time.setter
    def resolve_time(self, resolve_time):
        """Sets the resolve_time of this PageElement.

        Number of milliseconds needed to perform the DNS query for this element, when appropriate.  # noqa: E501

        :param resolve_time: The resolve_time of this PageElement.  # noqa: E501
        :type: int
        """
        if resolve_time is None:
            raise ValueError("Invalid value for `resolve_time`, must not be `None`")  # noqa: E501

        self._resolve_time = resolve_time

    @property
    def connect_time(self):
        """Gets the connect_time of this PageElement.  # noqa: E501

        Number of milliseconds needed to establish a connection.  # noqa: E501

        :return: The connect_time of this PageElement.  # noqa: E501
        :rtype: int
        """
        return self._connect_time

    @connect_time.setter
    def connect_time(self, connect_time):
        """Sets the connect_time of this PageElement.

        Number of milliseconds needed to establish a connection.  # noqa: E501

        :param connect_time: The connect_time of this PageElement.  # noqa: E501
        :type: int
        """
        if connect_time is None:
            raise ValueError("Invalid value for `connect_time`, must not be `None`")  # noqa: E501

        self._connect_time = connect_time

    @property
    def stale_time(self):
        """Gets the stale_time of this PageElement.  # noqa: E501

        Number of milliseconds the connection was stale  # noqa: E501

        :return: The stale_time of this PageElement.  # noqa: E501
        :rtype: int
        """
        return self._stale_time

    @stale_time.setter
    def stale_time(self, stale_time):
        """Sets the stale_time of this PageElement.

        Number of milliseconds the connection was stale  # noqa: E501

        :param stale_time: The stale_time of this PageElement.  # noqa: E501
        :type: int
        """
        if stale_time is None:
            raise ValueError("Invalid value for `stale_time`, must not be `None`")  # noqa: E501

        self._stale_time = stale_time

    @property
    def https_handshake_time(self):
        """Gets the https_handshake_time of this PageElement.  # noqa: E501

        Number of milliseconds needed for the HTTPS handshake  # noqa: E501

        :return: The https_handshake_time of this PageElement.  # noqa: E501
        :rtype: int
        """
        return self._https_handshake_time

    @https_handshake_time.setter
    def https_handshake_time(self, https_handshake_time):
        """Sets the https_handshake_time of this PageElement.

        Number of milliseconds needed for the HTTPS handshake  # noqa: E501

        :param https_handshake_time: The https_handshake_time of this PageElement.  # noqa: E501
        :type: int
        """
        if https_handshake_time is None:
            raise ValueError("Invalid value for `https_handshake_time`, must not be `None`")  # noqa: E501

        self._https_handshake_time = https_handshake_time

    @property
    def send_time(self):
        """Gets the send_time of this PageElement.  # noqa: E501

        Number of milliseconds it took to send data  # noqa: E501

        :return: The send_time of this PageElement.  # noqa: E501
        :rtype: int
        """
        return self._send_time

    @send_time.setter
    def send_time(self, send_time):
        """Sets the send_time of this PageElement.

        Number of milliseconds it took to send data  # noqa: E501

        :param send_time: The send_time of this PageElement.  # noqa: E501
        :type: int
        """
        if send_time is None:
            raise ValueError("Invalid value for `send_time`, must not be `None`")  # noqa: E501

        self._send_time = send_time

    @property
    def wait_time(self):
        """Gets the wait_time of this PageElement.  # noqa: E501

        Number of milliseconds the connection was in waiting state  # noqa: E501

        :return: The wait_time of this PageElement.  # noqa: E501
        :rtype: int
        """
        return self._wait_time

    @wait_time.setter
    def wait_time(self, wait_time):
        """Sets the wait_time of this PageElement.

        Number of milliseconds the connection was in waiting state  # noqa: E501

        :param wait_time: The wait_time of this PageElement.  # noqa: E501
        :type: int
        """
        if wait_time is None:
            raise ValueError("Invalid value for `wait_time`, must not be `None`")  # noqa: E501

        self._wait_time = wait_time

    @property
    def receive_time(self):
        """Gets the receive_time of this PageElement.  # noqa: E501

        Number of milliseconds it took to retrieve the data  # noqa: E501

        :return: The receive_time of this PageElement.  # noqa: E501
        :rtype: int
        """
        return self._receive_time

    @receive_time.setter
    def receive_time(self, receive_time):
        """Sets the receive_time of this PageElement.

        Number of milliseconds it took to retrieve the data  # noqa: E501

        :param receive_time: The receive_time of this PageElement.  # noqa: E501
        :type: int
        """
        if receive_time is None:
            raise ValueError("Invalid value for `receive_time`, must not be `None`")  # noqa: E501

        self._receive_time = receive_time

    @property
    def timeout_time(self):
        """Gets the timeout_time of this PageElement.  # noqa: E501

        Number of milliseconds the connection was timed-out   # noqa: E501

        :return: The timeout_time of this PageElement.  # noqa: E501
        :rtype: int
        """
        return self._timeout_time

    @timeout_time.setter
    def timeout_time(self, timeout_time):
        """Sets the timeout_time of this PageElement.

        Number of milliseconds the connection was timed-out   # noqa: E501

        :param timeout_time: The timeout_time of this PageElement.  # noqa: E501
        :type: int
        """
        if timeout_time is None:
            raise ValueError("Invalid value for `timeout_time`, must not be `None`")  # noqa: E501

        self._timeout_time = timeout_time

    @property
    def total_time(self):
        """Gets the total_time of this PageElement.  # noqa: E501

        Total number of milliseconds it took for the connection to complete  # noqa: E501

        :return: The total_time of this PageElement.  # noqa: E501
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        """Sets the total_time of this PageElement.

        Total number of milliseconds it took for the connection to complete  # noqa: E501

        :param total_time: The total_time of this PageElement.  # noqa: E501
        :type: int
        """
        if total_time is None:
            raise ValueError("Invalid value for `total_time`, must not be `None`")  # noqa: E501

        self._total_time = total_time

    @property
    def http_status_code(self):
        """Gets the http_status_code of this PageElement.  # noqa: E501

        The Http status code  # noqa: E501

        :return: The http_status_code of this PageElement.  # noqa: E501
        :rtype: int
        """
        return self._http_status_code

    @http_status_code.setter
    def http_status_code(self, http_status_code):
        """Sets the http_status_code of this PageElement.

        The Http status code  # noqa: E501

        :param http_status_code: The http_status_code of this PageElement.  # noqa: E501
        :type: int
        """
        if http_status_code is None:
            raise ValueError("Invalid value for `http_status_code`, must not be `None`")  # noqa: E501

        self._http_status_code = http_status_code

    @property
    def url(self):
        """Gets the url of this PageElement.  # noqa: E501

        The requested resource url  # noqa: E501

        :return: The url of this PageElement.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PageElement.

        The requested resource url  # noqa: E501

        :param url: The url of this PageElement.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def total_bytes(self):
        """Gets the total_bytes of this PageElement.  # noqa: E501

        Total number of downloaded bytes  # noqa: E501

        :return: The total_bytes of this PageElement.  # noqa: E501
        :rtype: int
        """
        return self._total_bytes

    @total_bytes.setter
    def total_bytes(self, total_bytes):
        """Sets the total_bytes of this PageElement.

        Total number of downloaded bytes  # noqa: E501

        :param total_bytes: The total_bytes of this PageElement.  # noqa: E501
        :type: int
        """
        if total_bytes is None:
            raise ValueError("Invalid value for `total_bytes`, must not be `None`")  # noqa: E501

        self._total_bytes = total_bytes

    @property
    def element_type(self):
        """Gets the element_type of this PageElement.  # noqa: E501

        Requested resource element type, can be HTML, scripts, CSS, images, frames, objects, data and other  # noqa: E501

        :return: The element_type of this PageElement.  # noqa: E501
        :rtype: str
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this PageElement.

        Requested resource element type, can be HTML, scripts, CSS, images, frames, objects, data and other  # noqa: E501

        :param element_type: The element_type of this PageElement.  # noqa: E501
        :type: str
        """

        self._element_type = element_type

    @property
    def request_headers(self):
        """Gets the request_headers of this PageElement.  # noqa: E501

        The HTTP request headers used  # noqa: E501

        :return: The request_headers of this PageElement.  # noqa: E501
        :rtype: str
        """
        return self._request_headers

    @request_headers.setter
    def request_headers(self, request_headers):
        """Sets the request_headers of this PageElement.

        The HTTP request headers used  # noqa: E501

        :param request_headers: The request_headers of this PageElement.  # noqa: E501
        :type: str
        """

        self._request_headers = request_headers

    @property
    def response_headers(self):
        """Gets the response_headers of this PageElement.  # noqa: E501

        The HTTP response headers retrieved  # noqa: E501

        :return: The response_headers of this PageElement.  # noqa: E501
        :rtype: str
        """
        return self._response_headers

    @response_headers.setter
    def response_headers(self, response_headers):
        """Sets the response_headers of this PageElement.

        The HTTP response headers retrieved  # noqa: E501

        :param response_headers: The response_headers of this PageElement.  # noqa: E501
        :type: str
        """

        self._response_headers = response_headers

    @property
    def resolved_ip_address(self):
        """Gets the resolved_ip_address of this PageElement.  # noqa: E501

        The IP address that was found for the specified domain name as part of this monitor check.  # noqa: E501

        :return: The resolved_ip_address of this PageElement.  # noqa: E501
        :rtype: object
        """
        return self._resolved_ip_address

    @resolved_ip_address.setter
    def resolved_ip_address(self, resolved_ip_address):
        """Sets the resolved_ip_address of this PageElement.

        The IP address that was found for the specified domain name as part of this monitor check.  # noqa: E501

        :param resolved_ip_address: The resolved_ip_address of this PageElement.  # noqa: E501
        :type: object
        """

        self._resolved_ip_address = resolved_ip_address

    @property
    def group_ids(self):
        """Gets the group_ids of this PageElement.  # noqa: E501


        :return: The group_ids of this PageElement.  # noqa: E501
        :rtype: list[int]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this PageElement.


        :param group_ids: The group_ids of this PageElement.  # noqa: E501
        :type: list[int]
        """

        self._group_ids = group_ids

    @property
    def url_is_blocked(self):
        """Gets the url_is_blocked of this PageElement.  # noqa: E501

        Was the Url excluded from waterfall (timing) data by the user?  # noqa: E501

        :return: The url_is_blocked of this PageElement.  # noqa: E501
        :rtype: bool
        """
        return self._url_is_blocked

    @url_is_blocked.setter
    def url_is_blocked(self, url_is_blocked):
        """Sets the url_is_blocked of this PageElement.

        Was the Url excluded from waterfall (timing) data by the user?  # noqa: E501

        :param url_is_blocked: The url_is_blocked of this PageElement.  # noqa: E501
        :type: bool
        """
        if url_is_blocked is None:
            raise ValueError("Invalid value for `url_is_blocked`, must not be `None`")  # noqa: E501

        self._url_is_blocked = url_is_blocked

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PageElement, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PageElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
