# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_resource_quota_status import V1ResourceQuotaStatus


class TestV1ResourceQuotaStatus(unittest.TestCase):
    """ V1ResourceQuotaStatus unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1ResourceQuotaStatus(self):
        """
        Test V1ResourceQuotaStatus
        """
        model = kubernetes.client.models.v1_resource_quota_status.V1ResourceQuotaStatus()


if __name__ == '__main__':
    unittest.main()
