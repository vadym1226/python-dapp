# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.12.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1CustomResourceColumnDefinition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'json_path': 'str',
        'description': 'str',
        'format': 'str',
        'name': 'str',
        'priority': 'int',
        'type': 'str'
    }

    attribute_map = {
        'json_path': 'JSONPath',
        'description': 'description',
        'format': 'format',
        'name': 'name',
        'priority': 'priority',
        'type': 'type'
    }

    def __init__(self, json_path=None, description=None, format=None, name=None, priority=None, type=None):
        """
        V1beta1CustomResourceColumnDefinition - a model defined in Swagger
        """

        self._json_path = None
        self._description = None
        self._format = None
        self._name = None
        self._priority = None
        self._type = None
        self.discriminator = None

        self.json_path = json_path
        if description is not None:
          self.description = description
        if format is not None:
          self.format = format
        self.name = name
        if priority is not None:
          self.priority = priority
        self.type = type

    @property
    def json_path(self):
        """
        Gets the json_path of this V1beta1CustomResourceColumnDefinition.
        JSONPath is a simple JSON path, i.e. with array notation.

        :return: The json_path of this V1beta1CustomResourceColumnDefinition.
        :rtype: str
        """
        return self._json_path

    @json_path.setter
    def json_path(self, json_path):
        """
        Sets the json_path of this V1beta1CustomResourceColumnDefinition.
        JSONPath is a simple JSON path, i.e. with array notation.

        :param json_path: The json_path of this V1beta1CustomResourceColumnDefinition.
        :type: str
        """
        if json_path is None:
            raise ValueError("Invalid value for `json_path`, must not be `None`")

        self._json_path = json_path

    @property
    def description(self):
        """
        Gets the description of this V1beta1CustomResourceColumnDefinition.
        description is a human readable description of this column.

        :return: The description of this V1beta1CustomResourceColumnDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this V1beta1CustomResourceColumnDefinition.
        description is a human readable description of this column.

        :param description: The description of this V1beta1CustomResourceColumnDefinition.
        :type: str
        """

        self._description = description

    @property
    def format(self):
        """
        Gets the format of this V1beta1CustomResourceColumnDefinition.
        format is an optional OpenAPI type definition for this column. The 'name' format is applied to the primary identifier column to assist in clients identifying column is the resource name. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for more.

        :return: The format of this V1beta1CustomResourceColumnDefinition.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this V1beta1CustomResourceColumnDefinition.
        format is an optional OpenAPI type definition for this column. The 'name' format is applied to the primary identifier column to assist in clients identifying column is the resource name. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for more.

        :param format: The format of this V1beta1CustomResourceColumnDefinition.
        :type: str
        """

        self._format = format

    @property
    def name(self):
        """
        Gets the name of this V1beta1CustomResourceColumnDefinition.
        name is a human readable name for the column.

        :return: The name of this V1beta1CustomResourceColumnDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1beta1CustomResourceColumnDefinition.
        name is a human readable name for the column.

        :param name: The name of this V1beta1CustomResourceColumnDefinition.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def priority(self):
        """
        Gets the priority of this V1beta1CustomResourceColumnDefinition.
        priority is an integer defining the relative importance of this column compared to others. Lower numbers are considered higher priority. Columns that may be omitted in limited space scenarios should be given a higher priority.

        :return: The priority of this V1beta1CustomResourceColumnDefinition.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this V1beta1CustomResourceColumnDefinition.
        priority is an integer defining the relative importance of this column compared to others. Lower numbers are considered higher priority. Columns that may be omitted in limited space scenarios should be given a higher priority.

        :param priority: The priority of this V1beta1CustomResourceColumnDefinition.
        :type: int
        """

        self._priority = priority

    @property
    def type(self):
        """
        Gets the type of this V1beta1CustomResourceColumnDefinition.
        type is an OpenAPI type definition for this column. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for more.

        :return: The type of this V1beta1CustomResourceColumnDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1beta1CustomResourceColumnDefinition.
        type is an OpenAPI type definition for this column. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for more.

        :param type: The type of this V1beta1CustomResourceColumnDefinition.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1CustomResourceColumnDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
