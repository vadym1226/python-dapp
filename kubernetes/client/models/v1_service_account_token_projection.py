# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.11.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ServiceAccountTokenProjection(object):
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
        'audience': 'str',
        'expiration_seconds': 'int',
        'path': 'str'
    }

    attribute_map = {
        'audience': 'audience',
        'expiration_seconds': 'expirationSeconds',
        'path': 'path'
    }

    def __init__(self, audience=None, expiration_seconds=None, path=None):
        """
        V1ServiceAccountTokenProjection - a model defined in Swagger
        """

        self._audience = None
        self._expiration_seconds = None
        self._path = None
        self.discriminator = None

        if audience is not None:
          self.audience = audience
        if expiration_seconds is not None:
          self.expiration_seconds = expiration_seconds
        self.path = path

    @property
    def audience(self):
        """
        Gets the audience of this V1ServiceAccountTokenProjection.
        Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.

        :return: The audience of this V1ServiceAccountTokenProjection.
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """
        Sets the audience of this V1ServiceAccountTokenProjection.
        Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.

        :param audience: The audience of this V1ServiceAccountTokenProjection.
        :type: str
        """

        self._audience = audience

    @property
    def expiration_seconds(self):
        """
        Gets the expiration_seconds of this V1ServiceAccountTokenProjection.
        ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.

        :return: The expiration_seconds of this V1ServiceAccountTokenProjection.
        :rtype: int
        """
        return self._expiration_seconds

    @expiration_seconds.setter
    def expiration_seconds(self, expiration_seconds):
        """
        Sets the expiration_seconds of this V1ServiceAccountTokenProjection.
        ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.

        :param expiration_seconds: The expiration_seconds of this V1ServiceAccountTokenProjection.
        :type: int
        """

        self._expiration_seconds = expiration_seconds

    @property
    def path(self):
        """
        Gets the path of this V1ServiceAccountTokenProjection.
        Path is the path relative to the mount point of the file to project the token into.

        :return: The path of this V1ServiceAccountTokenProjection.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1ServiceAccountTokenProjection.
        Path is the path relative to the mount point of the file to project the token into.

        :param path: The path of this V1ServiceAccountTokenProjection.
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")

        self._path = path

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
        if not isinstance(other, V1ServiceAccountTokenProjection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
