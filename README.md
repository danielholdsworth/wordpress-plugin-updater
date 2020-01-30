# Wordpress Plugin Updater


An Ansible & Python project that takes a list of plugins by download URL then scrapes the most upto date download URL from source, if the download URL differs from the one you currently have, it will remove the old one from your rpmbuild env & repackage the latest one in its place.

<h2> Required </h2>

<ul>
  <li> Ansible => 2.7.5 </li>
  <li>Python => 3</li>
  <li> rpmbuild tool & built environment </li>
