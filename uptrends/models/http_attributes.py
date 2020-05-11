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


class HttpAttributes(object):
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
        'response_body': 'str',
        'response_headers': 'str'
    }

    attribute_map = {
        'response_body': 'ResponseBody',
        'response_headers': 'ResponseHeaders'
    }

    def __init__(self, response_body=None, response_headers=None):  # noqa: E501
        """HttpAttributes - a model defined in Swagger"""  # noqa: E501

        self._response_body = None
        self._response_headers = None
        self.discriminator = None

        if response_body is not None:
            self.response_body = response_body
        if response_headers is not None:
            self.response_headers = response_headers

    @property
    def response_body(self):
        """Gets the response_body of this HttpAttributes.  # noqa: E501

        The HTML code retrieved from the target  # noqa: E501

        :return: The response_body of this HttpAttributes.  # noqa: E501
        :rtype: str
        """
        return self._response_body

    @response_body.setter
    def response_body(self, response_body):
        """Sets the response_body of this HttpAttributes.

        The HTML code retrieved from the target  # noqa: E501

        :param response_body: The response_body of this HttpAttributes.  # noqa: E501
        :type: str
        """

        self._response_body = response_body

    @property
    def response_headers(self):
        """Gets the response_headers of this HttpAttributes.  # noqa: E501

        The HTTP response headers retrieved from the target   # noqa: E501

        :return: The response_headers of this HttpAttributes.  # noqa: E501
        :rtype: str
        """
        return self._response_headers

    @response_headers.setter
    def response_headers(self, response_headers):
        """Sets the response_headers of this HttpAttributes.

        The HTTP response headers retrieved from the target   # noqa: E501

        :param response_headers: The response_headers of this HttpAttributes.  # noqa: E501
        :type: str
        """

        self._response_headers = response_headers

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
        if issubclass(HttpAttributes, dict):
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
        if not isinstance(other, HttpAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other