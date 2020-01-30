# Wordpress Plugin Updater


An Ansible & Python project that takes a list of plugins by download URL then scrapes the most upto date download URL from source, if the download URL differs from the one you currently have, it will remove the old one from your rpmbuild env & repackage the latest one in its place.

<h2> Required </h2>

<ul>
  <li> Ansible => 2.7.5 </li>
  <li>Python => 3</li>
  <li> rpmbuild tool & built environment </li>
</ul>

<h2>Usage</h2>

To run, simple run ```python plugin-check.py```.
If no plugins need updating, the script with exit with the phrase ```Line is the same.```.

If a plugin does need updating then it will ask you before updating; 
``` https://downloads.wordpress.org/plugin/404-to-301.3.0.5.zip

Do you wish to update the package?(y or n): ```

once you enter 'y' the script will run through the playbooks in around 20 seconds and create a new RPM!



```Updating!

PLAY [Remove RPM files on remote server] ***************************************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************************************
Enter passphrase for key '/root/.ssh/id_rsa': 
ok: [10.1.0.50]

TASK [remove .spec file] *******************************************************************************************************************************************************************************
changed: [10.1.0.50]

TASK [remove .tar.gz file] *****************************************************************************************************************************************************************************
changed: [10.1.0.50]

TASK [remove RPM file] *********************************************************************************************************************************************************************************
changed: [10.1.0.50]

PLAY RECAP *********************************************************************************************************************************************************************************************
10.1.0.50                  : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


PLAY [Replace line in master-plugin file] **************************************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************************************
ok: [127.0.0.1]

TASK [Replacing line] **********************************************************************************************************************************************************************************
changed: [127.0.0.1]

PLAY RECAP *********************************************************************************************************************************************************************************************
127.0.0.1                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

 ____________________
< Old Files Deleted! >
 --------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```
