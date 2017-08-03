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

from nautilus.api.v1 import documents
from nautilus.api.v1 import root

VERSION = {
    'id': 'v1',
    'status': 'DEVELOPMENT',
    'updated': '2017-08-02T00:00:00',
    'links': [
        {
            'href': '{0}v1/',
            'rel': 'self'
        }
    ]
}


def endpoints():
    return [
        ('/', root.Resource()),
        ('/documents', documents.DocumentsListResource()),
    ]
