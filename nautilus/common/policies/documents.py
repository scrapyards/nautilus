# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_policy import policy

from nautilus.common.policies import base


documents_policies = [
    policy.DocumentedRuleDefault(
        name=base.NAUTILUS % 'get_documents',
        check_str=base.RULE_SERVICE_OR_ADMIN,
        description='List documents',
        operations=[{'path': '/v1/documents/',
                     'method': 'GET'}]),

    policy.DocumentedRuleDefault(
        name=base.NAUTILUS % 'create_documents',
        check_str=base.RULE_ADMIN_REQUIRED,
        description='List documents',
        operations=[{'path': '/v1/documents/',
                     'method': 'POST'}]),
]


def list_rules():
    return documents_policies
