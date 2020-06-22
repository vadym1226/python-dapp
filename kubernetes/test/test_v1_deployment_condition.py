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
from kubernetes.client.models.v1_deployment_condition import V1DeploymentCondition  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1DeploymentCondition(unittest.TestCase):
    """V1DeploymentCondition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1DeploymentCondition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_deployment_condition.V1DeploymentCondition()  # noqa: E501
        if include_optional :
            return V1DeploymentCondition(
                last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                message = '0', 
                reason = '0', 
                status = '0', 
                type = '0'
            )
        else :
            return V1DeploymentCondition(
                status = '0',
                type = '0',
        )

    def testV1DeploymentCondition(self):
        """Test V1DeploymentCondition"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
