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


class Recipients(object):
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
        'operators': 'list[str]',
        'operator_groups': 'list[str]',
        'extra_email_addresses': 'list[str]'
    }

    attribute_map = {
        'operators': 'Operators',
        'operator_groups': 'OperatorGroups',
        'extra_email_addresses': 'ExtraEmailAddresses'
    }

    def __init__(self, operators=None, operator_groups=None, extra_email_addresses=None):  # noqa: E501
        """Recipients - a model defined in Swagger"""  # noqa: E501

        self._operators = None
        self._operator_groups = None
        self._extra_email_addresses = None
        self.discriminator = None

        if operators is not None:
            self.operators = operators
        if operator_groups is not None:
            self.operator_groups = operator_groups
        if extra_email_addresses is not None:
            self.extra_email_addresses = extra_email_addresses

    @property
    def operators(self):
        """Gets the operators of this Recipients.  # noqa: E501


        :return: The operators of this Recipients.  # noqa: E501
        :rtype: list[str]
        """
        return self._operators

    @operators.setter
    def operators(self, operators):
        """Sets the operators of this Recipients.


        :param operators: The operators of this Recipients.  # noqa: E501
        :type: list[str]
        """

        self._operators = operators

    @property
    def operator_groups(self):
        """Gets the operator_groups of this Recipients.  # noqa: E501


        :return: The operator_groups of this Recipients.  # noqa: E501
        :rtype: list[str]
        """
        return self._operator_groups

    @operator_groups.setter
    def operator_groups(self, operator_groups):
        """Sets the operator_groups of this Recipients.


        :param operator_groups: The operator_groups of this Recipients.  # noqa: E501
        :type: list[str]
        """

        self._operator_groups = operator_groups

    @property
    def extra_email_addresses(self):
        """Gets the extra_email_addresses of this Recipients.  # noqa: E501


        :return: The extra_email_addresses of this Recipients.  # noqa: E501
        :rtype: list[str]
        """
        return self._extra_email_addresses

    @extra_email_addresses.setter
    def extra_email_addresses(self, extra_email_addresses):
        """Sets the extra_email_addresses of this Recipients.


        :param extra_email_addresses: The extra_email_addresses of this Recipients.  # noqa: E501
        :type: list[str]
        """

        self._extra_email_addresses = extra_email_addresses

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
        if issubclass(Recipients, dict):
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
        if not isinstance(other, Recipients):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other