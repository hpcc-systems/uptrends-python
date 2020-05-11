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


class PredefinedVariable(object):
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
        'key': 'str',
        'value': 'str',
        'sensitive': 'bool'
    }

    attribute_map = {
        'key': 'Key',
        'value': 'Value',
        'sensitive': 'Sensitive'
    }

    def __init__(self, key=None, value=None, sensitive=None):  # noqa: E501
        """PredefinedVariable - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._value = None
        self._sensitive = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        self.sensitive = sensitive

    @property
    def key(self):
        """Gets the key of this PredefinedVariable.  # noqa: E501


        :return: The key of this PredefinedVariable.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PredefinedVariable.


        :param key: The key of this PredefinedVariable.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def value(self):
        """Gets the value of this PredefinedVariable.  # noqa: E501


        :return: The value of this PredefinedVariable.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PredefinedVariable.


        :param value: The value of this PredefinedVariable.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def sensitive(self):
        """Gets the sensitive of this PredefinedVariable.  # noqa: E501


        :return: The sensitive of this PredefinedVariable.  # noqa: E501
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """Sets the sensitive of this PredefinedVariable.


        :param sensitive: The sensitive of this PredefinedVariable.  # noqa: E501
        :type: bool
        """
        if sensitive is None:
            raise ValueError("Invalid value for `sensitive`, must not be `None`")  # noqa: E501

        self._sensitive = sensitive

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
        if issubclass(PredefinedVariable, dict):
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
        if not isinstance(other, PredefinedVariable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
