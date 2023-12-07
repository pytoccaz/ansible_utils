#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2023 Olivier Bernard (@pytoccaz)
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)


__metaclass__ = type

DOCUMENTATION = '''
---
module: env_info
short_description: Queries environment variables on the target host
description: Queries environment variables on the target host (python os.getenv wrapper)

version_added: "1.4.0"

options:
    envs:
        description: |
            A list of system environment variables to retrieve
        required: true
        elements: str
        type: list
        aliases: [ "get", "get_envs", "env_list"]
    lower:
        description: |
            Whether to lower variable names (dictionary keys) in result output
        default: no
        type: bool
        aliases: [ "lower_keys", "lower_env_names" ]

author:
    - Olivier Bernard (@pytoccaz)
'''

RETURN = '''
result:
    description: A key-value dictionary with keys as variable names and their corresponding values as values
    sample:
        PATH: "/usr/bin:/etc/local/bin"
        USERNAME: "olivier"
    returned: success
    type: dict
'''

EXAMPLES = '''
- name: Query for some envs
  pytoccaz.utils.env_info:
    envs:
      - HOME
      - LANG
  register: get_envs
'''
from os import getenv
from ansible.module_utils.basic import AnsibleModule


def get_envs(lst: list) -> dict:
    return {env: getenv(env) for env in lst}

def lower_keys(dic: dict) -> dict:
    '''
        Puts the keys of the input dictionary in lowcase 
    '''
    return { k.lower(): v for k, v in dic.items() } 

def main():
    module = AnsibleModule(
        argument_spec=dict(
            envs=dict(required=True, type="list", elements="str",
                      aliases=["get", "get_envs", "env_list"]),
            lower=dict(type="bool", default=False,  
                      aliases=["lower_keys", "lower_env_names"]),
        ),
        supports_check_mode=True
    )

    envs = get_envs(module.params["envs"])

    if module.params["lower"]:
        envs = lower_keys(envs)

    module.exit_json(changed=False, result=envs)


if __name__ == "__main__":
    main()
