#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2023 Olivier Bernard (@pytoccaz)
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)


__metaclass__ = type

DOCUMENTATION = '''
---
module: python_module_info
short_description: Check a python module is installed or not
description:
    - Check a python module or package is available on target host
    - importlib.util.find_spec wrapper

version_added: "1.1.0"

options:
    name:
        description:
            - Fully qualified name of the python module or package.
            - Relative name preceded with a dot if used in combinaison with C(package) parameter
        required: true
        type: str
        aliases:
            - module_name
            - module
        version_added: '1.1.0'
    package:
        description:
            - Fully qualified name of the python package
            - Start C(name) parameter value with a dot
        required: false
        type: str
        version_added: '1.1.0'

author:
    - Olivier Bernard (@pytoccaz)

notes:
    - This module cannot check modules installed via galaxy collections
'''

RETURN = '''
is_installed:
    description: If the python module or package is actually installed
    sample: true
    returned: success
    type: bool
name:
    description: The python module fully qualified name C(package_name.?module_name)
    sample: html.parser
    returned: succes
    type: str
'''

EXAMPLES = '''
    - name: Is python-docker available ?
      pytoccaz.utils.python_module_info:
        name: docker
      register: module_docker

    - debug:
        var: module_docker.is_installed

    - name: Is html.parser available ?
      pytoccaz.utils.python_module_info:
        name: html.parser
      register: module_parser

    - debug:
        var: module_parser.is_installed

    - name: Is html.parser available (using package parameter) ?
      pytoccaz.utils.python_module_info:
        name: .parser
        package: html
      register: module_parser

    - debug:
        var: module_parser.is_installed
'''
from ansible.module_utils.basic import AnsibleModule
from importlib.util import find_spec, resolve_name
from importlib.metadata import version


def available(modulename: str, path: str = None) -> bool:
    """ Check module is available
    """
    if find_spec(modulename, path) is None:
        return False
    else:
        return True


def main():
    module = AnsibleModule(argument_spec=dict(
        name=dict(required=True, type='str', aliases=['module_name', 'module']),
        package=dict(required=False, type='str'),
    ),
        supports_check_mode=True
    )

    name = module.params['name']
    package = module.params['package']

    try:
        is_installed = available(name, package)
    except (ModuleNotFoundError):
        is_installed = False
    except (ValueError, AttributeError) as e:
        module.fail_json(msg=str(e), changed=False)

    module.exit_json(changed=False, name=resolve_name(name, package), is_installed=is_installed)


if __name__ == "__main__":
    main()
