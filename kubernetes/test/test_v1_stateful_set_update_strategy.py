# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.16
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1_stateful_set_update_strategy import V1StatefulSetUpdateStrategy  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1StatefulSetUpdateStrategy(unittest.TestCase):
    """V1StatefulSetUpdateStrategy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1StatefulSetUpdateStrategy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_stateful_set_update_strategy.V1StatefulSetUpdateStrategy()  # noqa: E501
        if include_optional :
            return V1StatefulSetUpdateStrategy(
                rolling_update = kubernetes.client.models.v1/rolling_update_stateful_set_strategy.v1.RollingUpdateStatefulSetStrategy(
                    partition = 56, ), 
                type = '0'
            )
        else :
            return V1StatefulSetUpdateStrategy(
        )

    def testV1StatefulSetUpdateStrategy(self):
        """Test V1StatefulSetUpdateStrategy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
