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


class MonitorCheckResponse(object):
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
        'data': 'list[MonitorCheck]',
        'links': 'LinksData',
        'relationships': 'list[RelationObject]',
        'meta': 'MetaData',
        'cursors': 'object'
    }

    attribute_map = {
        'data': 'Data',
        'links': 'Links',
        'relationships': 'Relationships',
        'meta': 'Meta',
        'cursors': 'Cursors'
    }

    def __init__(self, data=None, links=None, relationships=None, meta=None, cursors=None):  # noqa: E501
        """MonitorCheckResponse - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._links = None
        self._relationships = None
        self._meta = None
        self._cursors = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if links is not None:
            self.links = links
        if relationships is not None:
            self.relationships = relationships
        if meta is not None:
            self.meta = meta
        if cursors is not None:
            self.cursors = cursors

    @property
    def data(self):
        """Gets the data of this MonitorCheckResponse.  # noqa: E501


        :return: The data of this MonitorCheckResponse.  # noqa: E501
        :rtype: list[MonitorCheck]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this MonitorCheckResponse.


        :param data: The data of this MonitorCheckResponse.  # noqa: E501
        :type: list[MonitorCheck]
        """

        self._data = data

    @property
    def links(self):
        """Gets the links of this MonitorCheckResponse.  # noqa: E501


        :return: The links of this MonitorCheckResponse.  # noqa: E501
        :rtype: LinksData
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MonitorCheckResponse.


        :param links: The links of this MonitorCheckResponse.  # noqa: E501
        :type: LinksData
        """

        self._links = links

    @property
    def relationships(self):
        """Gets the relationships of this MonitorCheckResponse.  # noqa: E501


        :return: The relationships of this MonitorCheckResponse.  # noqa: E501
        :rtype: list[RelationObject]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this MonitorCheckResponse.


        :param relationships: The relationships of this MonitorCheckResponse.  # noqa: E501
        :type: list[RelationObject]
        """

        self._relationships = relationships

    @property
    def meta(self):
        """Gets the meta of this MonitorCheckResponse.  # noqa: E501


        :return: The meta of this MonitorCheckResponse.  # noqa: E501
        :rtype: MetaData
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this MonitorCheckResponse.


        :param meta: The meta of this MonitorCheckResponse.  # noqa: E501
        :type: MetaData
        """

        self._meta = meta

    @property
    def cursors(self):
        """Gets the cursors of this MonitorCheckResponse.  # noqa: E501

        Cursors can be used to navigate the dataset in a fixed manner  # noqa: E501

        :return: The cursors of this MonitorCheckResponse.  # noqa: E501
        :rtype: object
        """
        return self._cursors

    @cursors.setter
    def cursors(self, cursors):
        """Sets the cursors of this MonitorCheckResponse.

        Cursors can be used to navigate the dataset in a fixed manner  # noqa: E501

        :param cursors: The cursors of this MonitorCheckResponse.  # noqa: E501
        :type: object
        """

        self._cursors = cursors

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
        if issubclass(MonitorCheckResponse, dict):
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
        if not isinstance(other, MonitorCheckResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
