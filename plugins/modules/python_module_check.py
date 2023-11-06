#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2023 Olivier Bernard (@pytoccaz)
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)


__metaclass__ = type

DOCUMENTATION = '''
---
module: python_module_check
short_description: Is a python module available
description:  Is a python module available on target host

version_added: "1.1.0"

options:
    name:
        description:
            - Name of the python module
        required: true
        type: str
        aliases:
            - module_name
        version_added: '1.1.0'
    package:
        description:
            - Path of the python package
            - Start name parameter value with a dot
        required: false
        type: str
        version_added: '1.1.0'

author:
    - Olivier Bernard (@pytoccaz)

notes:
    - this module cannot check modules installed via galaxy collections
'''

RETURN = '''
is_installed:
    description: If the python module is actually installed
    sample: true
    returned: always
    type: bool

'''

EXAMPLES = '''
    - name: Is python-docker available ?
      pytoccaz.utils.python_module_check:
        name: docker
      register: module_docker

    - debug:
        var: module_docker.is_installed

    - name: Is html.parser available ?
      pytoccaz.utils.python_module_check:
        name: html.parser
      register: module_parser

    - debug:
        var: module_parser.is_installed

    - name: Is html.parser available (using package parameter) ?
      pytoccaz.utils.python_module_check:
        name: .parser
        package: html
      register: module_parser

    - debug:
        var: module_parser.is_installed
'''
from ansible.module_utils.basic import AnsibleModule
from importlib.util import find_spec


def available(modulename: str, path: str = None) -> bool:
    """ Check module is available
    """
    if find_spec(modulename, path) is None:
        return False
    else:
        return True


def main():
    module = AnsibleModule(argument_spec=dict(
        name=dict(required=True, type='str', aliases=['module_name']),
        package=dict(required=False, type='str'),
    ),
        supports_check_mode=True
    )

    try:
        is_installed = available(
            module.params['name'], module.params['package'])
    except ModuleNotFoundError as e:
        module.fail_json(e.msg, changed=False)

    module.exit_json(changed=False, is_installed=available(
        module.params['name'], module.params['package']))


if __name__ == "__main__":
    main()
