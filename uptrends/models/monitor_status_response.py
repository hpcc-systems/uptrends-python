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


class MonitorStatusResponse(object):
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
        'data': 'MonitorStatus',
        'links': 'LinksData',
        'relationships': 'list[RelationObject]',
        'meta': 'MetaData'
    }

    attribute_map = {
        'data': 'Data',
        'links': 'Links',
        'relationships': 'Relationships',
        'meta': 'Meta'
    }

    def __init__(self, data=None, links=None, relationships=None, meta=None):  # noqa: E501
        """MonitorStatusResponse - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._links = None
        self._relationships = None
        self._meta = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if links is not None:
            self.links = links
        if relationships is not None:
            self.relationships = relationships
        if meta is not None:
            self.meta = meta

    @property
    def data(self):
        """Gets the data of this MonitorStatusResponse.  # noqa: E501


        :return: The data of this MonitorStatusResponse.  # noqa: E501
        :rtype: MonitorStatus
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this MonitorStatusResponse.


        :param data: The data of this MonitorStatusResponse.  # noqa: E501
        :type: MonitorStatus
        """

        self._data = data

    @property
    def links(self):
        """Gets the links of this MonitorStatusResponse.  # noqa: E501


        :return: The links of this MonitorStatusResponse.  # noqa: E501
        :rtype: LinksData
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MonitorStatusResponse.


        :param links: The links of this MonitorStatusResponse.  # noqa: E501
        :type: LinksData
        """

        self._links = links

    @property
    def relationships(self):
        """Gets the relationships of this MonitorStatusResponse.  # noqa: E501


        :return: The relationships of this MonitorStatusResponse.  # noqa: E501
        :rtype: list[RelationObject]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this MonitorStatusResponse.


        :param relationships: The relationships of this MonitorStatusResponse.  # noqa: E501
        :type: list[RelationObject]
        """

        self._relationships = relationships

    @property
    def meta(self):
        """Gets the meta of this MonitorStatusResponse.  # noqa: E501


        :return: The meta of this MonitorStatusResponse.  # noqa: E501
        :rtype: MetaData
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this MonitorStatusResponse.


        :param meta: The meta of this MonitorStatusResponse.  # noqa: E501
        :type: MetaData
        """

        self._meta = meta

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
        if issubclass(MonitorStatusResponse, dict):
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
        if not isinstance(other, MonitorStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
