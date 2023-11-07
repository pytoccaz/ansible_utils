#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2023 Olivier Bernard (@pytoccaz)
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = '''
---
module: binary_info
short_description: Find system executable
description: Find system executable in PATH.

version_added: "1.0.0"

options:
    name:
        description:
            - Name of the binary
        required: true
        type: str
        aliases:
            - binary
        version_added: '1.0.0'
    option_dirs:
        description:
            - Optional list of directories to search in addition to PATH
        required: false
        type: list
        elements: str
        aliases:
            - opt_dirs
        version_added: '1.0.0'

author:
    - Olivier Bernard (@pytoccaz)

'''

RETURN = '''
path:
    description: Path of the searched binary if it exists in PATH and the user can access it, else null
    sample: "/usr/bin/python3"
    returned: always
    type: str
exists:
    description: If the destination path actually exists and the user can access it
    sample: true
    returned: always
    type: bool
gid:
    description: Numeric id representing the group of the owner
    sample: 0
    returned: when exists is true
    type: int
mode:
    description: Unix permissions of the file in octal representation as a string
    sample: "0777"
    returned: when exists is true
    type: str
group:
    description: Group name of owner
    sample: "root"
    returned: when exists is true
    type: str
owner:
    description: Name of owner
    sample: "root"
    returned: when exists is true
    type: str
size:
    description: Size in bytes for a plain file, amount of data for some special files
    sample: 9
    returned: when exists is true
    type: int
state:
    description: Nature of the file
    sample: "link"
    returned: when exists is true
    type: str
uid:
    description: Numeric id representing the file owner
    sample: 0
    returned: when exists is true
    type: int
'''

EXAMPLES = '''
    - name: Search python3 in PATH
      pytoccaz.utils.binary_info:
        name: python3
      register: python_binary

    - debug:
        var: python_binary.path

'''

from ansible.module_utils.basic import AnsibleModule


def binary(module, path, opt_dirs):
    return module.get_bin_path(path, opt_dirs=opt_dirs)


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str', aliases=['binary']),
            option_dirs=dict(required=False, type='list', elements='str', aliases=['opt_dirs'])
        ),
        supports_check_mode=True
    )

    path = binary(module, module.params["name"], module.params["option_dirs"])

    module.exit_json(changed=False, path=path, exists=path is not None)


if __name__ == "__main__":
    main()
