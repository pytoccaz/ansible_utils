# -*- coding: utf-8 -*-

# Copyright (c) 2023 Olivier Bernard (@pytoccaz)
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
    name: binary_path
    author:
      - Olivier Bernard (@pytoccaz)
    short_description: Returns a system executable path
    version_added: '1.3.0'
    description:
      - Returns the absolute path of a system executable within C($PATH)
    options:
      name:
        description: The name of the executable to find.
        type: str
"""

EXAMPLES = r"""
- name: Generate random string with length 12
  ansible.builtin.debug:
    var: lookup('pytoccaz.utils.binary_path', name='python3')
  # Example result: ['/usr/bin/python3']
"""

RETURN = r"""
  _raw:
    description: A one-element list containing the path when the executable is found, else an empty string
    type: list
    elements: str
"""


from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup import LookupBase
from ansible.module_utils.common.process import get_bin_path
from ansible.module_utils.common.text.converters import to_text


class LookupModule(LookupBase):

    def get_bin_path(self, arg, required=False, opt_dirs=None):
        '''
        Find system executable in PATH.

        :param arg: The executable to find.
        :param required: if executable is not found and required is ``True``, fail_json
        :param opt_dirs: optional list of directories to search in addition to ``PATH``
        :returns: if found return full path; otherwise return None
        '''

        bin_path = None
        try:
            bin_path = get_bin_path(arg=arg, opt_dirs=opt_dirs)
        except ValueError as e:
            if required:
                raise AnsibleLookupError(to_text(e))
            else:
                return bin_path

        return bin_path

    def run(self, terms, variables=None, **kwargs):

        self.set_options(var_options=variables, direct=kwargs)

        name = self.get_option("name")

        return [self.get_bin_path(name)]
