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


class Schedule(object):
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
        'schedule_type': 'ScheduleType',
        'time': 'str',
        'week_day': 'DayOfWeek',
        'month_day': 'int'
    }

    attribute_map = {
        'schedule_type': 'ScheduleType',
        'time': 'Time',
        'week_day': 'WeekDay',
        'month_day': 'MonthDay'
    }

    def __init__(self, schedule_type=None, time=None, week_day=None, month_day=None):  # noqa: E501
        """Schedule - a model defined in Swagger"""  # noqa: E501

        self._schedule_type = None
        self._time = None
        self._week_day = None
        self._month_day = None
        self.discriminator = None

        if schedule_type is not None:
            self.schedule_type = schedule_type
        if time is not None:
            self.time = time
        if week_day is not None:
            self.week_day = week_day
        if month_day is not None:
            self.month_day = month_day

    @property
    def schedule_type(self):
        """Gets the schedule_type of this Schedule.  # noqa: E501


        :return: The schedule_type of this Schedule.  # noqa: E501
        :rtype: ScheduleType
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this Schedule.


        :param schedule_type: The schedule_type of this Schedule.  # noqa: E501
        :type: ScheduleType
        """

        self._schedule_type = schedule_type

    @property
    def time(self):
        """Gets the time of this Schedule.  # noqa: E501


        :return: The time of this Schedule.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Schedule.


        :param time: The time of this Schedule.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def week_day(self):
        """Gets the week_day of this Schedule.  # noqa: E501


        :return: The week_day of this Schedule.  # noqa: E501
        :rtype: DayOfWeek
        """
        return self._week_day

    @week_day.setter
    def week_day(self, week_day):
        """Sets the week_day of this Schedule.


        :param week_day: The week_day of this Schedule.  # noqa: E501
        :type: DayOfWeek
        """

        self._week_day = week_day

    @property
    def month_day(self):
        """Gets the month_day of this Schedule.  # noqa: E501


        :return: The month_day of this Schedule.  # noqa: E501
        :rtype: int
        """
        return self._month_day

    @month_day.setter
    def month_day(self, month_day):
        """Sets the month_day of this Schedule.


        :param month_day: The month_day of this Schedule.  # noqa: E501
        :type: int
        """

        self._month_day = month_day

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
        if issubclass(Schedule, dict):
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
        if not isinstance(other, Schedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other