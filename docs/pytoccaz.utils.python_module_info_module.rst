.. _pytoccaz.utils.python_module_info_module:


*********************************
pytoccaz.utils.python_module_info
*********************************

**Checks whether a python module is installed or not**


Version added: 1.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Checks a python module or package is available on target host
- importlib.util.find_spec wrapper




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 1.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Fully qualified name of the python module or package.</div>
                        <div>Relative name preceded with a dot if used in combinaison with <code>package</code> parameter</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: module_name, module</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>package</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 1.1.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Fully qualified name of the python package</div>
                        <div>Start <code>name</code> parameter value with a dot</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - This module cannot check modules installed via galaxy collections



Examples
--------

.. code-block:: yaml

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



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>is_installed</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>success</td>
                <td>
                            <div>If the python module or package is actually installed</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">True</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td>succes</td>
                <td>
                            <div>The python module fully qualified name <code>package_name.?module_name</code></div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">html.parser</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Olivier Bernard (@pytoccaz)
