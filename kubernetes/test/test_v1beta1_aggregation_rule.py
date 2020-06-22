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
from kubernetes.client.models.v1beta1_aggregation_rule import V1beta1AggregationRule  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1AggregationRule(unittest.TestCase):
    """V1beta1AggregationRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1AggregationRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_aggregation_rule.V1beta1AggregationRule()  # noqa: E501
        if include_optional :
            return V1beta1AggregationRule(
                cluster_role_selectors = [
                    kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                        match_expressions = [
                            kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                key = '0', 
                                operator = '0', 
                                values = [
                                    '0'
                                    ], )
                            ], 
                        match_labels = {
                            'key' : '0'
                            }, )
                    ]
            )
        else :
            return V1beta1AggregationRule(
        )

    def testV1beta1AggregationRule(self):
        """Test V1beta1AggregationRule"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
