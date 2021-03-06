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


class PSPAuthorization(object):
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
        'authorization_id': 'str',
        'authorization_type': 'PSPAuthorizationType',
        'operator_guid': 'str',
        'operator_group_guid': 'str'
    }

    attribute_map = {
        'authorization_id': 'AuthorizationId',
        'authorization_type': 'AuthorizationType',
        'operator_guid': 'OperatorGuid',
        'operator_group_guid': 'OperatorGroupGuid'
    }

    def __init__(self, authorization_id=None, authorization_type=None, operator_guid=None, operator_group_guid=None):  # noqa: E501
        """PSPAuthorization - a model defined in Swagger"""  # noqa: E501

        self._authorization_id = None
        self._authorization_type = None
        self._operator_guid = None
        self._operator_group_guid = None
        self.discriminator = None

        if authorization_id is not None:
            self.authorization_id = authorization_id
        self.authorization_type = authorization_type
        if operator_guid is not None:
            self.operator_guid = operator_guid
        if operator_group_guid is not None:
            self.operator_group_guid = operator_group_guid

    @property
    def authorization_id(self):
        """Gets the authorization_id of this PSPAuthorization.  # noqa: E501


        :return: The authorization_id of this PSPAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._authorization_id

    @authorization_id.setter
    def authorization_id(self, authorization_id):
        """Sets the authorization_id of this PSPAuthorization.


        :param authorization_id: The authorization_id of this PSPAuthorization.  # noqa: E501
        :type: str
        """

        self._authorization_id = authorization_id

    @property
    def authorization_type(self):
        """Gets the authorization_type of this PSPAuthorization.  # noqa: E501


        :return: The authorization_type of this PSPAuthorization.  # noqa: E501
        :rtype: PSPAuthorizationType
        """
        return self._authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type):
        """Sets the authorization_type of this PSPAuthorization.


        :param authorization_type: The authorization_type of this PSPAuthorization.  # noqa: E501
        :type: PSPAuthorizationType
        """
        if authorization_type is None:
            raise ValueError("Invalid value for `authorization_type`, must not be `None`")  # noqa: E501

        self._authorization_type = authorization_type

    @property
    def operator_guid(self):
        """Gets the operator_guid of this PSPAuthorization.  # noqa: E501


        :return: The operator_guid of this PSPAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._operator_guid

    @operator_guid.setter
    def operator_guid(self, operator_guid):
        """Sets the operator_guid of this PSPAuthorization.


        :param operator_guid: The operator_guid of this PSPAuthorization.  # noqa: E501
        :type: str
        """

        self._operator_guid = operator_guid

    @property
    def operator_group_guid(self):
        """Gets the operator_group_guid of this PSPAuthorization.  # noqa: E501


        :return: The operator_group_guid of this PSPAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._operator_group_guid

    @operator_group_guid.setter
    def operator_group_guid(self, operator_group_guid):
        """Sets the operator_group_guid of this PSPAuthorization.


        :param operator_group_guid: The operator_group_guid of this PSPAuthorization.  # noqa: E501
        :type: str
        """

        self._operator_group_guid = operator_group_guid

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
        if issubclass(PSPAuthorization, dict):
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
        if not isinstance(other, PSPAuthorization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
