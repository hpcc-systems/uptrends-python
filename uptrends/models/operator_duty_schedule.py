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


class OperatorDutySchedule(object):
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
        'id': 'int',
        'schedule_mode': 'object',
        'start_date_time': 'datetime',
        'end_date_time': 'datetime',
        'week_day': 'object',
        'month_day': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'schedule_mode': 'ScheduleMode',
        'start_date_time': 'StartDateTime',
        'end_date_time': 'EndDateTime',
        'week_day': 'WeekDay',
        'month_day': 'MonthDay',
        'start_time': 'StartTime',
        'end_time': 'EndTime'
    }

    def __init__(self, id=None, schedule_mode=None, start_date_time=None, end_date_time=None, week_day=None, month_day=None, start_time=None, end_time=None):  # noqa: E501
        """OperatorDutySchedule - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._schedule_mode = None
        self._start_date_time = None
        self._end_date_time = None
        self._week_day = None
        self._month_day = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.id = id
        self.schedule_mode = schedule_mode
        if start_date_time is not None:
            self.start_date_time = start_date_time
        if end_date_time is not None:
            self.end_date_time = end_date_time
        if week_day is not None:
            self.week_day = week_day
        if month_day is not None:
            self.month_day = month_day
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def id(self):
        """Gets the id of this OperatorDutySchedule.  # noqa: E501

        The unique ID of this maintenance period  # noqa: E501

        :return: The id of this OperatorDutySchedule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OperatorDutySchedule.

        The unique ID of this maintenance period  # noqa: E501

        :param id: The id of this OperatorDutySchedule.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def schedule_mode(self):
        """Gets the schedule_mode of this OperatorDutySchedule.  # noqa: E501

        The schedule mode (one time, daily, weekly, monthly)  # noqa: E501

        :return: The schedule_mode of this OperatorDutySchedule.  # noqa: E501
        :rtype: object
        """
        return self._schedule_mode

    @schedule_mode.setter
    def schedule_mode(self, schedule_mode):
        """Sets the schedule_mode of this OperatorDutySchedule.

        The schedule mode (one time, daily, weekly, monthly)  # noqa: E501

        :param schedule_mode: The schedule_mode of this OperatorDutySchedule.  # noqa: E501
        :type: object
        """
        if schedule_mode is None:
            raise ValueError("Invalid value for `schedule_mode`, must not be `None`")  # noqa: E501

        self._schedule_mode = schedule_mode

    @property
    def start_date_time(self):
        """Gets the start_date_time of this OperatorDutySchedule.  # noqa: E501

        The start date/time for this schedule (for one-time schedules only)  # noqa: E501

        :return: The start_date_time of this OperatorDutySchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this OperatorDutySchedule.

        The start date/time for this schedule (for one-time schedules only)  # noqa: E501

        :param start_date_time: The start_date_time of this OperatorDutySchedule.  # noqa: E501
        :type: datetime
        """

        self._start_date_time = start_date_time

    @property
    def end_date_time(self):
        """Gets the end_date_time of this OperatorDutySchedule.  # noqa: E501

        The end date/time for this maintenance period (for one-time maintenance periods only)  # noqa: E501

        :return: The end_date_time of this OperatorDutySchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this OperatorDutySchedule.

        The end date/time for this maintenance period (for one-time maintenance periods only)  # noqa: E501

        :param end_date_time: The end_date_time of this OperatorDutySchedule.  # noqa: E501
        :type: datetime
        """

        self._end_date_time = end_date_time

    @property
    def week_day(self):
        """Gets the week_day of this OperatorDutySchedule.  # noqa: E501

        The weekday for this maintenance period (for weekly maintenance periods only)  # noqa: E501

        :return: The week_day of this OperatorDutySchedule.  # noqa: E501
        :rtype: object
        """
        return self._week_day

    @week_day.setter
    def week_day(self, week_day):
        """Sets the week_day of this OperatorDutySchedule.

        The weekday for this maintenance period (for weekly maintenance periods only)  # noqa: E501

        :param week_day: The week_day of this OperatorDutySchedule.  # noqa: E501
        :type: object
        """

        self._week_day = week_day

    @property
    def month_day(self):
        """Gets the month_day of this OperatorDutySchedule.  # noqa: E501

        the month day for this maintenance period (for montly maintenance periods only)  # noqa: E501

        :return: The month_day of this OperatorDutySchedule.  # noqa: E501
        :rtype: int
        """
        return self._month_day

    @month_day.setter
    def month_day(self, month_day):
        """Sets the month_day of this OperatorDutySchedule.

        the month day for this maintenance period (for montly maintenance periods only)  # noqa: E501

        :param month_day: The month_day of this OperatorDutySchedule.  # noqa: E501
        :type: int
        """

        self._month_day = month_day

    @property
    def start_time(self):
        """Gets the start_time of this OperatorDutySchedule.  # noqa: E501

        The start time of this maintenance period  # noqa: E501

        :return: The start_time of this OperatorDutySchedule.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this OperatorDutySchedule.

        The start time of this maintenance period  # noqa: E501

        :param start_time: The start_time of this OperatorDutySchedule.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this OperatorDutySchedule.  # noqa: E501

        The end time of this maintenance period  # noqa: E501

        :return: The end_time of this OperatorDutySchedule.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this OperatorDutySchedule.

        The end time of this maintenance period  # noqa: E501

        :param end_time: The end_time of this OperatorDutySchedule.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

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
        if issubclass(OperatorDutySchedule, dict):
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
        if not isinstance(other, OperatorDutySchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other