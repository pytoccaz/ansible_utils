# -*- coding: utf-8 -*-

# Copyright (c) 2023 Olivier Bernard (@pytoccaz)
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
  name: lower_keys
  short_description: Puts the key of a dictionary in lowercase
  version_added: 1.5.0
  author: Olivier Bernard (@pytoccaz)
  description:
    - Puts the key (not the values) of a dictionary in lowercase
  positional: attribute
  options:
    _input:
      description: A dictionaries
      type: dict
      required: true
'''

EXAMPLES = '''
- name: Lower keys
  ansible.builtin.debug:
    msg: "{{ dictionary1 | pytoccaz.utils.lower_keys() }}"
  vars:
    dictionary1:
      KEY1: VALUE
      foo: bar

  # Produces the following dictionary:
  # _value:
  #    key1: VALUE
  #    foo: bar
'''

RETURN = '''
  _value:
    description: A dictionary with keys in lowcase.
    type: dictionary
'''

from ansible.errors import AnsibleFilterError


def lower_keys(dic: dict) -> dict:
    '''
        Puts the keys of the input dictionary in lowcase 
    '''
    return { k.lower(): v for k, v in dic.items() } 


class FilterModule(object):
    ''' Ansible list filters '''

    def filters(self):
        return {
            'lower_keys': lower_keys,
        }