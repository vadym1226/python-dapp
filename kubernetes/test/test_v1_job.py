# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_job import V1Job


class TestV1Job(unittest.TestCase):
    """ V1Job unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1Job(self):
        """
        Test V1Job
        """
        model = kubernetes.client.models.v1_job.V1Job()


if __name__ == '__main__':
    unittest.main()
