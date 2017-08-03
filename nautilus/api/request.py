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

from oslo_context import context

from nautilus import exceptions as n_exc


class Request(falcon.Request):

    def __init__(self, env, options=None):
        super(Request, self).__init__(env, options)
        self.context = context.RequestContext.from_environ(self.env)

    @property
    def project_id(self):
        return self.context.tenant

    @property
    def user_id(self):
        return self.context.user

    @property
    def roles(self):
        return self.context.roles

    def __repr__(self):
        return '%s, context=%s' % (self.path, self.context)
