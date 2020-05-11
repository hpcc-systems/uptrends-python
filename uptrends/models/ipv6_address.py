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


class Ipv6Address(object):
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
        'ip_address': 'str',
        'is_native': 'bool'
    }

    attribute_map = {
        'ip_address': 'IpAddress',
        'is_native': 'IsNative'
    }

    def __init__(self, ip_address=None, is_native=None):  # noqa: E501
        """Ipv6Address - a model defined in Swagger"""  # noqa: E501

        self._ip_address = None
        self._is_native = None
        self.discriminator = None

        if ip_address is not None:
            self.ip_address = ip_address
        self.is_native = is_native

    @property
    def ip_address(self):
        """Gets the ip_address of this Ipv6Address.  # noqa: E501

        The IPv6 address  # noqa: E501

        :return: The ip_address of this Ipv6Address.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this Ipv6Address.

        The IPv6 address  # noqa: E501

        :param ip_address: The ip_address of this Ipv6Address.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def is_native(self):
        """Gets the is_native of this Ipv6Address.  # noqa: E501

        This indicates whether this is a native IPv6 address  # noqa: E501

        :return: The is_native of this Ipv6Address.  # noqa: E501
        :rtype: bool
        """
        return self._is_native

    @is_native.setter
    def is_native(self, is_native):
        """Sets the is_native of this Ipv6Address.

        This indicates whether this is a native IPv6 address  # noqa: E501

        :param is_native: The is_native of this Ipv6Address.  # noqa: E501
        :type: bool
        """
        if is_native is None:
            raise ValueError("Invalid value for `is_native`, must not be `None`")  # noqa: E501

        self._is_native = is_native

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
        if issubclass(Ipv6Address, dict):
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
        if not isinstance(other, Ipv6Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other