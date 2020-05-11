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


class ApiVariableDefinition(object):
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
        'source': 'ApiSourceType',
        '_property': 'str',
        'name': 'str',
        'arguments': 'list[ApiVariableDefinition]'
    }

    attribute_map = {
        'source': 'Source',
        '_property': 'Property',
        'name': 'Name',
        'arguments': 'Arguments'
    }

    def __init__(self, source=None, _property=None, name=None, arguments=None):  # noqa: E501
        """ApiVariableDefinition - a model defined in Swagger"""  # noqa: E501

        self._source = None
        self.__property = None
        self._name = None
        self._arguments = None
        self.discriminator = None

        self.source = source
        if _property is not None:
            self._property = _property
        if name is not None:
            self.name = name
        if arguments is not None:
            self.arguments = arguments

    @property
    def source(self):
        """Gets the source of this ApiVariableDefinition.  # noqa: E501


        :return: The source of this ApiVariableDefinition.  # noqa: E501
        :rtype: ApiSourceType
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ApiVariableDefinition.


        :param source: The source of this ApiVariableDefinition.  # noqa: E501
        :type: ApiSourceType
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def _property(self):
        """Gets the _property of this ApiVariableDefinition.  # noqa: E501


        :return: The _property of this ApiVariableDefinition.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this ApiVariableDefinition.


        :param _property: The _property of this ApiVariableDefinition.  # noqa: E501
        :type: str
        """

        self.__property = _property

    @property
    def name(self):
        """Gets the name of this ApiVariableDefinition.  # noqa: E501


        :return: The name of this ApiVariableDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiVariableDefinition.


        :param name: The name of this ApiVariableDefinition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def arguments(self):
        """Gets the arguments of this ApiVariableDefinition.  # noqa: E501


        :return: The arguments of this ApiVariableDefinition.  # noqa: E501
        :rtype: list[ApiVariableDefinition]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this ApiVariableDefinition.


        :param arguments: The arguments of this ApiVariableDefinition.  # noqa: E501
        :type: list[ApiVariableDefinition]
        """

        self._arguments = arguments

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
        if issubclass(ApiVariableDefinition, dict):
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
        if not isinstance(other, ApiVariableDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other