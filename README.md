# Ansible Collection - pytoccaz.utils

 Find a system executable path, check if a python module is installed

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.13.13**.

<!--end requires_ansible-->

## Installation

Download from Galaxy:

```bash
ansible-galaxy collection install pytoccaz.utils
```

## Collection content

<!--start collection content-->
### Lookup plugins
Name | Description
--- | ---
[pytoccaz.utils.binary_path](https://github.com/pytoccaz/ansible_utils/blob/main/docs/pytoccaz.utils.binary_path_lookup.rst)|Returns a system executable path

### Modules
Name | Description
--- | ---
[pytoccaz.utils.binary_info](https://github.com/pytoccaz/ansible_utils/blob/main/docs/pytoccaz.utils.binary_info_module.rst)|Finds a system executable
[pytoccaz.utils.python_module_info](https://github.com/pytoccaz/ansible_utils/blob/main/docs/pytoccaz.utils.python_module_info_module.rst)|Checks whether a python module is installed or not

<!--end collection content-->
