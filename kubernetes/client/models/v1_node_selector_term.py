# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1NodeSelectorTerm(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, match_expressions=None):
        """
        V1NodeSelectorTerm - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'match_expressions': 'list[V1NodeSelectorRequirement]'
        }

        self.attribute_map = {
            'match_expressions': 'matchExpressions'
        }

        self._match_expressions = match_expressions

    @property
    def match_expressions(self):
        """
        Gets the match_expressions of this V1NodeSelectorTerm.
        Required. A list of node selector requirements. The requirements are ANDed.

        :return: The match_expressions of this V1NodeSelectorTerm.
        :rtype: list[V1NodeSelectorRequirement]
        """
        return self._match_expressions

    @match_expressions.setter
    def match_expressions(self, match_expressions):
        """
        Sets the match_expressions of this V1NodeSelectorTerm.
        Required. A list of node selector requirements. The requirements are ANDed.

        :param match_expressions: The match_expressions of this V1NodeSelectorTerm.
        :type: list[V1NodeSelectorRequirement]
        """
        if match_expressions is None:
            raise ValueError("Invalid value for `match_expressions`, must not be `None`")

        self._match_expressions = match_expressions

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
        if not isinstance(other, V1NodeSelectorTerm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
