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


class V1OwnerReference(object):
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
        'api_version': 'str',
        'block_owner_deletion': 'bool',
        'controller': 'bool',
        'kind': 'str',
        'name': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'block_owner_deletion': 'blockOwnerDeletion',
        'controller': 'controller',
        'kind': 'kind',
        'name': 'name',
        'uid': 'uid'
    }

    def __init__(self, api_version=None, block_owner_deletion=None, controller=None, kind=None, name=None, uid=None):
        """
        V1OwnerReference - a model defined in Swagger
        """

        self._api_version = None
        self._block_owner_deletion = None
        self._controller = None
        self._kind = None
        self._name = None
        self._uid = None
        self.discriminator = None

        self.api_version = api_version
        if block_owner_deletion is not None:
          self.block_owner_deletion = block_owner_deletion
        if controller is not None:
          self.controller = controller
        self.kind = kind
        self.name = name
        self.uid = uid

    @property
    def api_version(self):
        """
        Gets the api_version of this V1OwnerReference.
        API version of the referent.

        :return: The api_version of this V1OwnerReference.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1OwnerReference.
        API version of the referent.

        :param api_version: The api_version of this V1OwnerReference.
        :type: str
        """
        if api_version is None:
            raise ValueError("Invalid value for `api_version`, must not be `None`")

        self._api_version = api_version

    @property
    def block_owner_deletion(self):
        """
        Gets the block_owner_deletion of this V1OwnerReference.
        If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. Defaults to false. To set this field, a user needs \"delete\" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.

        :return: The block_owner_deletion of this V1OwnerReference.
        :rtype: bool
        """
        return self._block_owner_deletion

    @block_owner_deletion.setter
    def block_owner_deletion(self, block_owner_deletion):
        """
        Sets the block_owner_deletion of this V1OwnerReference.
        If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. Defaults to false. To set this field, a user needs \"delete\" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.

        :param block_owner_deletion: The block_owner_deletion of this V1OwnerReference.
        :type: bool
        """

        self._block_owner_deletion = block_owner_deletion

    @property
    def controller(self):
        """
        Gets the controller of this V1OwnerReference.
        If true, this reference points to the managing controller.

        :return: The controller of this V1OwnerReference.
        :rtype: bool
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """
        Sets the controller of this V1OwnerReference.
        If true, this reference points to the managing controller.

        :param controller: The controller of this V1OwnerReference.
        :type: bool
        """

        self._controller = controller

    @property
    def kind(self):
        """
        Gets the kind of this V1OwnerReference.
        Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1OwnerReference.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1OwnerReference.
        Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1OwnerReference.
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")

        self._kind = kind

    @property
    def name(self):
        """
        Gets the name of this V1OwnerReference.
        Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names

        :return: The name of this V1OwnerReference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1OwnerReference.
        Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names

        :param name: The name of this V1OwnerReference.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def uid(self):
        """
        Gets the uid of this V1OwnerReference.
        UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids

        :return: The uid of this V1OwnerReference.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this V1OwnerReference.
        UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids

        :param uid: The uid of this V1OwnerReference.
        :type: str
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")

        self._uid = uid

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
        if not isinstance(other, V1OwnerReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
