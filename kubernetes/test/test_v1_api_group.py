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
from kubernetes.client.models.v1_api_group import V1APIGroup  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1APIGroup(unittest.TestCase):
    """V1APIGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1APIGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_api_group.V1APIGroup()  # noqa: E501
        if include_optional :
            return V1APIGroup(
                api_version = '0', 
                kind = '0', 
                name = '0', 
                preferred_version = kubernetes.client.models.v1/group_version_for_discovery.v1.GroupVersionForDiscovery(
                    group_version = '0', 
                    version = '0', ), 
                server_address_by_client_cid_rs = [
                    kubernetes.client.models.v1/server_address_by_client_cidr.v1.ServerAddressByClientCIDR(
                        kubernetes.client_cidr = '0', 
                        server_address = '0', )
                    ], 
                versions = [
                    kubernetes.client.models.v1/group_version_for_discovery.v1.GroupVersionForDiscovery(
                        group_version = '0', 
                        version = '0', )
                    ]
            )
        else :
            return V1APIGroup(
                name = '0',
                versions = [
                    kubernetes.client.models.v1/group_version_for_discovery.v1.GroupVersionForDiscovery(
                        group_version = '0', 
                        version = '0', )
                    ],
        )

    def testV1APIGroup(self):
        """Test V1APIGroup"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
