.. _pytoccaz.utils.env_info_module:


***********************
pytoccaz.utils.env_info
***********************

**Queries environment variables on the target host**


Version added: 1.4.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Queries environment variables on the target host (python os.getenv wrapper)




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
                    <b>envs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of system environment variables to retrieve</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: get, get_envs, env_list</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    - name: Query for some envs
      pytoccaz.utils.env_info:
        envs:
          - HOME
          - LANG
      register: get_envs



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
                    <b>result</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>success</td>
                <td>
                            <div>A key-value dictionary with keys as variable names and their corresponding values as values</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;PATH&#x27;: &#x27;/usr/bin:/etc/local/bin&#x27;, &#x27;USERNAME&#x27;: &#x27;olivier&#x27;}</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Olivier Bernard (@pytoccaz)
