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


class Operator(object):
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
        'operator_guid': 'str',
        'hash': 'str',
        'password': 'str',
        'full_name': 'str',
        'email': 'str',
        'mobile_phone': 'str',
        'outgoing_phone_number_id': 'int',
        'outgoing_phone_number_id_specified': 'bool',
        'is_account_administrator': 'bool',
        'backup_email': 'str',
        'is_on_duty': 'bool',
        'culture_name': 'str',
        'culture_name_specified': 'bool',
        'time_zone_id': 'int',
        'time_zone_id_specified': 'bool',
        'sms_provider': 'object',
        'use_numeric_sender': 'bool',
        'use_numeric_sender_specified': 'bool',
        'allow_native_login': 'bool',
        'allow_native_login_specified': 'bool',
        'allow_single_signon': 'bool',
        'allow_single_signon_specified': 'bool'
    }

    attribute_map = {
        'operator_guid': 'OperatorGuid',
        'hash': 'Hash',
        'password': 'Password',
        'full_name': 'FullName',
        'email': 'Email',
        'mobile_phone': 'MobilePhone',
        'outgoing_phone_number_id': 'OutgoingPhoneNumberId',
        'outgoing_phone_number_id_specified': 'OutgoingPhoneNumberIdSpecified',
        'is_account_administrator': 'IsAccountAdministrator',
        'backup_email': 'BackupEmail',
        'is_on_duty': 'IsOnDuty',
        'culture_name': 'CultureName',
        'culture_name_specified': 'CultureNameSpecified',
        'time_zone_id': 'TimeZoneId',
        'time_zone_id_specified': 'TimeZoneIdSpecified',
        'sms_provider': 'SmsProvider',
        'use_numeric_sender': 'UseNumericSender',
        'use_numeric_sender_specified': 'UseNumericSenderSpecified',
        'allow_native_login': 'AllowNativeLogin',
        'allow_native_login_specified': 'AllowNativeLoginSpecified',
        'allow_single_signon': 'AllowSingleSignon',
        'allow_single_signon_specified': 'AllowSingleSignonSpecified'
    }

    def __init__(self, operator_guid=None, hash=None, password=None, full_name=None, email=None, mobile_phone=None, outgoing_phone_number_id=None, outgoing_phone_number_id_specified=None, is_account_administrator=None, backup_email=None, is_on_duty=None, culture_name=None, culture_name_specified=None, time_zone_id=None, time_zone_id_specified=None, sms_provider=None, use_numeric_sender=None, use_numeric_sender_specified=None, allow_native_login=None, allow_native_login_specified=None, allow_single_signon=None, allow_single_signon_specified=None):  # noqa: E501
        """Operator - a model defined in Swagger"""  # noqa: E501

        self._operator_guid = None
        self._hash = None
        self._password = None
        self._full_name = None
        self._email = None
        self._mobile_phone = None
        self._outgoing_phone_number_id = None
        self._outgoing_phone_number_id_specified = None
        self._is_account_administrator = None
        self._backup_email = None
        self._is_on_duty = None
        self._culture_name = None
        self._culture_name_specified = None
        self._time_zone_id = None
        self._time_zone_id_specified = None
        self._sms_provider = None
        self._use_numeric_sender = None
        self._use_numeric_sender_specified = None
        self._allow_native_login = None
        self._allow_native_login_specified = None
        self._allow_single_signon = None
        self._allow_single_signon_specified = None
        self.discriminator = None

        if operator_guid is not None:
            self.operator_guid = operator_guid
        if hash is not None:
            self.hash = hash
        if password is not None:
            self.password = password
        if full_name is not None:
            self.full_name = full_name
        if email is not None:
            self.email = email
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if outgoing_phone_number_id is not None:
            self.outgoing_phone_number_id = outgoing_phone_number_id
        if outgoing_phone_number_id_specified is not None:
            self.outgoing_phone_number_id_specified = outgoing_phone_number_id_specified
        if is_account_administrator is not None:
            self.is_account_administrator = is_account_administrator
        if backup_email is not None:
            self.backup_email = backup_email
        if is_on_duty is not None:
            self.is_on_duty = is_on_duty
        if culture_name is not None:
            self.culture_name = culture_name
        if culture_name_specified is not None:
            self.culture_name_specified = culture_name_specified
        if time_zone_id is not None:
            self.time_zone_id = time_zone_id
        if time_zone_id_specified is not None:
            self.time_zone_id_specified = time_zone_id_specified
        if sms_provider is not None:
            self.sms_provider = sms_provider
        if use_numeric_sender is not None:
            self.use_numeric_sender = use_numeric_sender
        if use_numeric_sender_specified is not None:
            self.use_numeric_sender_specified = use_numeric_sender_specified
        if allow_native_login is not None:
            self.allow_native_login = allow_native_login
        if allow_native_login_specified is not None:
            self.allow_native_login_specified = allow_native_login_specified
        if allow_single_signon is not None:
            self.allow_single_signon = allow_single_signon
        if allow_single_signon_specified is not None:
            self.allow_single_signon_specified = allow_single_signon_specified

    @property
    def operator_guid(self):
        """Gets the operator_guid of this Operator.  # noqa: E501

        The unique identifier of this operator  # noqa: E501

        :return: The operator_guid of this Operator.  # noqa: E501
        :rtype: str
        """
        return self._operator_guid

    @operator_guid.setter
    def operator_guid(self, operator_guid):
        """Sets the operator_guid of this Operator.

        The unique identifier of this operator  # noqa: E501

        :param operator_guid: The operator_guid of this Operator.  # noqa: E501
        :type: str
        """

        self._operator_guid = operator_guid

    @property
    def hash(self):
        """Gets the hash of this Operator.  # noqa: E501

        The hash of this operator.  # noqa: E501

        :return: The hash of this Operator.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this Operator.

        The hash of this operator.  # noqa: E501

        :param hash: The hash of this Operator.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def password(self):
        """Gets the password of this Operator.  # noqa: E501

        The password is a required field if AllowNativeLogin is set to True  # noqa: E501

        :return: The password of this Operator.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Operator.

        The password is a required field if AllowNativeLogin is set to True  # noqa: E501

        :param password: The password of this Operator.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def full_name(self):
        """Gets the full_name of this Operator.  # noqa: E501

        The full name of this operator  # noqa: E501

        :return: The full_name of this Operator.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Operator.

        The full name of this operator  # noqa: E501

        :param full_name: The full_name of this Operator.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def email(self):
        """Gets the email of this Operator.  # noqa: E501

        The email address of this operator. This also serves as the username  # noqa: E501

        :return: The email of this Operator.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Operator.

        The email address of this operator. This also serves as the username  # noqa: E501

        :param email: The email of this Operator.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this Operator.  # noqa: E501

        The phone number of this operator to which SMS and phone alerts can be sent. Start with a plus (+) sign and your country code  # noqa: E501

        :return: The mobile_phone of this Operator.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this Operator.

        The phone number of this operator to which SMS and phone alerts can be sent. Start with a plus (+) sign and your country code  # noqa: E501

        :param mobile_phone: The mobile_phone of this Operator.  # noqa: E501
        :type: str
        """

        self._mobile_phone = mobile_phone

    @property
    def outgoing_phone_number_id(self):
        """Gets the outgoing_phone_number_id of this Operator.  # noqa: E501

        The id of the phone number that will be used to send phone alerts (See /OutgoingPhoneNumber API under Miscellaneous for available ids)  # noqa: E501

        :return: The outgoing_phone_number_id of this Operator.  # noqa: E501
        :rtype: int
        """
        return self._outgoing_phone_number_id

    @outgoing_phone_number_id.setter
    def outgoing_phone_number_id(self, outgoing_phone_number_id):
        """Sets the outgoing_phone_number_id of this Operator.

        The id of the phone number that will be used to send phone alerts (See /OutgoingPhoneNumber API under Miscellaneous for available ids)  # noqa: E501

        :param outgoing_phone_number_id: The outgoing_phone_number_id of this Operator.  # noqa: E501
        :type: int
        """

        self._outgoing_phone_number_id = outgoing_phone_number_id

    @property
    def outgoing_phone_number_id_specified(self):
        """Gets the outgoing_phone_number_id_specified of this Operator.  # noqa: E501


        :return: The outgoing_phone_number_id_specified of this Operator.  # noqa: E501
        :rtype: bool
        """
        return self._outgoing_phone_number_id_specified

    @outgoing_phone_number_id_specified.setter
    def outgoing_phone_number_id_specified(self, outgoing_phone_number_id_specified):
        """Sets the outgoing_phone_number_id_specified of this Operator.


        :param outgoing_phone_number_id_specified: The outgoing_phone_number_id_specified of this Operator.  # noqa: E501
        :type: bool
        """

        self._outgoing_phone_number_id_specified = outgoing_phone_number_id_specified

    @property
    def is_account_administrator(self):
        """Gets the is_account_administrator of this Operator.  # noqa: E501

        This indicates if the operator is the account administrator.  # noqa: E501

        :return: The is_account_administrator of this Operator.  # noqa: E501
        :rtype: bool
        """
        return self._is_account_administrator

    @is_account_administrator.setter
    def is_account_administrator(self, is_account_administrator):
        """Sets the is_account_administrator of this Operator.

        This indicates if the operator is the account administrator.  # noqa: E501

        :param is_account_administrator: The is_account_administrator of this Operator.  # noqa: E501
        :type: bool
        """

        self._is_account_administrator = is_account_administrator

    @property
    def backup_email(self):
        """Gets the backup_email of this Operator.  # noqa: E501

        The backup email address of this operator  # noqa: E501

        :return: The backup_email of this Operator.  # noqa: E501
        :rtype: str
        """
        return self._backup_email

    @backup_email.setter
    def backup_email(self, backup_email):
        """Sets the backup_email of this Operator.

        The backup email address of this operator  # noqa: E501

        :param backup_email: The backup_email of this Operator.  # noqa: E501
        :type: str
        """

        self._backup_email = backup_email

    @property
    def is_on_duty(self):
        """Gets the is_on_duty of this Operator.  # noqa: E501

        Indicates whether the operator is currently active  # noqa: E501

        :return: The is_on_duty of this Operator.  # noqa: E501
        :rtype: bool
        """
        return self._is_on_duty

    @is_on_duty.setter
    def is_on_duty(self, is_on_duty):
        """Sets the is_on_duty of this Operator.

        Indicates whether the operator is currently active  # noqa: E501

        :param is_on_duty: The is_on_duty of this Operator.  # noqa: E501
        :type: bool
        """

        self._is_on_duty = is_on_duty

    @property
    def culture_name(self):
        """Gets the culture_name of this Operator.  # noqa: E501

        If ommitted the operator will use the account culture. If set it will override the account default  # noqa: E501

        :return: The culture_name of this Operator.  # noqa: E501
        :rtype: str
        """
        return self._culture_name

    @culture_name.setter
    def culture_name(self, culture_name):
        """Sets the culture_name of this Operator.

        If ommitted the operator will use the account culture. If set it will override the account default  # noqa: E501

        :param culture_name: The culture_name of this Operator.  # noqa: E501
        :type: str
        """

        self._culture_name = culture_name

    @property
    def culture_name_specified(self):
        """Gets the culture_name_specified of this Operator.  # noqa: E501


        :return: The culture_name_specified of this Operator.  # noqa: E501
        :rtype: bool
        """
        return self._culture_name_specified

    @culture_name_specified.setter
    def culture_name_specified(self, culture_name_specified):
        """Sets the culture_name_specified of this Operator.


        :param culture_name_specified: The culture_name_specified of this Operator.  # noqa: E501
        :type: bool
        """

        self._culture_name_specified = culture_name_specified

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this Operator.  # noqa: E501

        The id of the timezone of this operator (See /Timezone API under Miscellaneous for available timezones)  # noqa: E501

        :return: The time_zone_id of this Operator.  # noqa: E501
        :rtype: int
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this Operator.

        The id of the timezone of this operator (See /Timezone API under Miscellaneous for available timezones)  # noqa: E501

        :param time_zone_id: The time_zone_id of this Operator.  # noqa: E501
        :type: int
        """

        self._time_zone_id = time_zone_id

    @property
    def time_zone_id_specified(self):
        """Gets the time_zone_id_specified of this Operator.  # noqa: E501


        :return: The time_zone_id_specified of this Operator.  # noqa: E501
        :rtype: bool
        """
        return self._time_zone_id_specified

    @time_zone_id_specified.setter
    def time_zone_id_specified(self, time_zone_id_specified):
        """Sets the time_zone_id_specified of this Operator.


        :param time_zone_id_specified: The time_zone_id_specified of this Operator.  # noqa: E501
        :type: bool
        """

        self._time_zone_id_specified = time_zone_id_specified

    @property
    def sms_provider(self):
        """Gets the sms_provider of this Operator.  # noqa: E501

        The SMS provider used to send out SMS alerts  # noqa: E501

        :return: The sms_provider of this Operator.  # noqa: E501
        :rtype: object
        """
        return self._sms_provider

    @sms_provider.setter
    def sms_provider(self, sms_provider):
        """Sets the sms_provider of this Operator.

        The SMS provider used to send out SMS alerts  # noqa: E501

        :param sms_provider: The sms_provider of this Operator.  # noqa: E501
        :type: object
        """

        self._sms_provider = sms_provider

    @property
    def use_numeric_sender(self):
        """Gets the use_numeric_sender of this Operator.  # noqa: E501

        Set to True to override the default behavior of sending SMS alerts with textual sender ID  # noqa: E501

        :return: The use_numeric_sender of this Operator.  # noqa: E501
        :rtype: bool
        """
        return self._use_numeric_sender

    @use_numeric_sender.setter
    def use_numeric_sender(self, use_numeric_sender):
        """Sets the use_numeric_sender of this Operator.

        Set to True to override the default behavior of sending SMS alerts with textual sender ID  # noqa: E501

        :param use_numeric_sender: The use_numeric_sender of this Operator.  # noqa: E501
        :type: bool
        """

        self._use_numeric_sender = use_numeric_sender

    @property
    def use_numeric_sender_specified(self):
        """Gets the use_numeric_sender_specified of this Operator.  # noqa: E501


        :return: The use_numeric_sender_specified of this Operator.  # noqa: E501
        :rtype: bool
        """
        return self._use_numeric_sender_specified

    @use_numeric_sender_specified.setter
    def use_numeric_sender_specified(self, use_numeric_sender_specified):
        """Sets the use_numeric_sender_specified of this Operator.


        :param use_numeric_sender_specified: The use_numeric_sender_specified of this Operator.  # noqa: E501
        :type: bool
        """

        self._use_numeric_sender_specified = use_numeric_sender_specified

    @property
    def allow_native_login(self):
        """Gets the allow_native_login of this Operator.  # noqa: E501

        This can only be set to false if the account has SSO enabled. Ommitting or providing null will use the account default  # noqa: E501

        :return: The allow_native_login of this Operator.  # noqa: E501
        :rtype: bool
        """
        return self._allow_native_login

    @allow_native_login.setter
    def allow_native_login(self, allow_native_login):
        """Sets the allow_native_login of this Operator.

        This can only be set to false if the account has SSO enabled. Ommitting or providing null will use the account default  # noqa: E501

        :param allow_native_login: The allow_native_login of this Operator.  # noqa: E501
        :type: bool
        """

        self._allow_native_login = allow_native_login

    @property
    def allow_native_login_specified(self):
        """Gets the allow_native_login_specified of this Operator.  # noqa: E501


        :return: The allow_native_login_specified of this Operator.  # noqa: E501
        :rtype: bool
        """
        return self._allow_native_login_specified

    @allow_native_login_specified.setter
    def allow_native_login_specified(self, allow_native_login_specified):
        """Sets the allow_native_login_specified of this Operator.


        :param allow_native_login_specified: The allow_native_login_specified of this Operator.  # noqa: E501
        :type: bool
        """

        self._allow_native_login_specified = allow_native_login_specified

    @property
    def allow_single_signon(self):
        """Gets the allow_single_signon of this Operator.  # noqa: E501

        This can only be set to true if the account has SSO enabled. Ommitting or providing null will use the account default  # noqa: E501

        :return: The allow_single_signon of this Operator.  # noqa: E501
        :rtype: bool
        """
        return self._allow_single_signon

    @allow_single_signon.setter
    def allow_single_signon(self, allow_single_signon):
        """Sets the allow_single_signon of this Operator.

        This can only be set to true if the account has SSO enabled. Ommitting or providing null will use the account default  # noqa: E501

        :param allow_single_signon: The allow_single_signon of this Operator.  # noqa: E501
        :type: bool
        """

        self._allow_single_signon = allow_single_signon

    @property
    def allow_single_signon_specified(self):
        """Gets the allow_single_signon_specified of this Operator.  # noqa: E501


        :return: The allow_single_signon_specified of this Operator.  # noqa: E501
        :rtype: bool
        """
        return self._allow_single_signon_specified

    @allow_single_signon_specified.setter
    def allow_single_signon_specified(self, allow_single_signon_specified):
        """Sets the allow_single_signon_specified of this Operator.


        :param allow_single_signon_specified: The allow_single_signon_specified of this Operator.  # noqa: E501
        :type: bool
        """

        self._allow_single_signon_specified = allow_single_signon_specified

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
        if issubclass(Operator, dict):
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
        if not isinstance(other, Operator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
