# coding=utf-8
#
# Copyright 2016 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from f5.bigiq.cm.asm import Asm
from f5.bigiq.cm.device import Device
from f5.bigiq.cm.shared import Shared
from f5.bigiq.resource import OrganizingCollection


class Cm(OrganizingCollection):
    """An organizing collection for CM resources."""
    def __init__(self, bigiq):
        super(Cm, self).__init__(bigiq)
        self._meta_data['allowed_lazy_attributes'] = [
            Asm,
            Device,
            Shared
        ]
