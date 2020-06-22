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
from kubernetes.client.models.v1_api_service_spec import V1APIServiceSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1APIServiceSpec(unittest.TestCase):
    """V1APIServiceSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1APIServiceSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_api_service_spec.V1APIServiceSpec()  # noqa: E501
        if include_optional :
            return V1APIServiceSpec(
                ca_bundle = 'YQ==', 
                group = '0', 
                group_priority_minimum = 56, 
                insecure_skip_tls_verify = True, 
                service = kubernetes.client.models.apiregistration/v1/service_reference.apiregistration.v1.ServiceReference(
                    name = '0', 
                    namespace = '0', 
                    port = 56, ), 
                version = '0', 
                version_priority = 56
            )
        else :
            return V1APIServiceSpec(
                group_priority_minimum = 56,
                service = kubernetes.client.models.apiregistration/v1/service_reference.apiregistration.v1.ServiceReference(
                    name = '0', 
                    namespace = '0', 
                    port = 56, ),
                version_priority = 56,
        )

    def testV1APIServiceSpec(self):
        """Test V1APIServiceSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
