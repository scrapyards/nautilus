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

import json

import falcon

from nautilus import exceptions as exc


class BaseResource(object):
    """Base resource class for RESTful API calls."""

    def on_options(self, request, response):
        methods = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'PATCH']
        allowed_methods = [m for m in methods if 'on_' + m.lower()
                           in dir(self)]

        response.headers['Allow'] = ','.join(allowed_methods)
        response.status = falcon.HTTP_200

    @staticmethod
    def json_body(req):
        if not req.content_type:
            return {}
        try:
            raw_json = req.stream.read()
        except Exception:
            raise exc.ObjectNotFound('Oh em gee, exception!')

        try:
            data = json.loads(raw_json, 'utf-8')
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_753, 'Malformed JSON')

        return data
