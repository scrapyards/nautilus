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

import falcon

from nautilus.api import base
from nautilus.common import policy


class DocumentsListResource(base.BaseResource):

    @policy.enforce('nautilus:get_documents')
    def on_get(self, request, response):
        # GET /v1/documents  -  Lists documents
        response.body = {'getdoc': 'mmm'}
        response.status = falcon.HTTP_200

    @policy.enforce('nautilus:create_documents')
    def on_post(self, request, response):
        response.status = falcon.HTTP_201
        response.body = {'post_doc': 'BLAH BLAH BLAH'}
