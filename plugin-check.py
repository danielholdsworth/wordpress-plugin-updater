#  python version: 3
#  Author: Dan Holdsworth
#  Description: Checks if wp plugin has changed versions

########################################################
import requests
import re
from bs4 import BeautifulSoup
import os


path = './mytemplates/plugin-versions.txt'
########################################################

##list of plugin URLs, has to be the same order as mytemplates/plugin-master.txt
list = ['https://wordpress.org/plugins/404-to-301/',
        'https://wordpress.org/plugins/acf-content-analysis-for-yoast-seo/',
        'https://wordpress.org/plugins/advanced-custom-fields/',
        'https://wordpress.org/plugins/autoptimize/',
        'https://wordpress.org/plugins/civic-cookie-control-8/',
        'https://wordpress.org/plugins/classic-editor-addon/',
        'https://wordpress.org/plugins/contact-form-7/',
        'https://wordpress.org/plugins/cookie-law-info/',
        'https://wordpress.org/plugins/custom-twitter-feeds/',
        'https://wordpress.org/plugins/daggerhart-openid-connect-generic/',
        'https://wordpress.org/plugins/easy-wp-smtp/',
        'https://wordpress.org/plugins/flamingo/',
        'https://wordpress.org/plugins/force-strong-passwords/',
        'https://wordpress.org/plugins/gdpr-cookie-compliance/',
        'https://wordpress.org/plugins/lead-forensics-roi/',
        'https://wordpress.org/plugins/no-category-base-wpml/',
        'https://wordpress.org/plugins/post-types-order/',
        'https://wordpress.org/plugins/redirection/',
        'https://wordpress.org/plugins/search-filter/',
        'https://wordpress.org/plugins/simple-custom-post-order/',
        'https://wordpress.org/plugins/taxonomy-terms-order/',
        'https://wordpress.org/plugins/tiny-compress-images/',
        'https://wordpress.org/plugins/updraftplus/',
        'https://wordpress.org/plugins/wordpress-importer/',
        'https://wordpress.org/plugins/wordpress-seo/',
        'https://wordpress.org/plugins/wp-security-audit-log/',
        'https://wordpress.org/plugins/wps-hide-login/']


##creates plugin-versions.txt file
f = open(path, 'w')
f.write('')
f.close()

print("Loading Plugins...")

##iterates through above list URLs and gathers latest version DL link URL
for i in list:

    URL = i
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    plugin = soup.find_all('div',class_='plugin-actions')

    for plugin in plugin:
        download_li = plugin.find('a', class_='plugin-download button download-button button-large')
        download = download_li.get('href')
        print(".")
        plugin_urls = open(path, 'a')
        plugin_urls.write(download + '\n')
        plugin_urls.close()

##defines the two lists used, current, and the new upto date one.
master_plugin = open("./mytemplates/plugin-master.txt","r")
new_plugin = open("./mytemplates/plugin-versions.txt","r")

##Reads in the content of the current file
lines1 = master_plugin.readlines()

print("All Done Writing...Checking Diff...")

##Does a DIFF against the two files.
for i,lines2 in enumerate(new_plugin):

    ##IF a line in the new file does not match the old, then it will tell you.
    if lines2 != lines1[i]:
        print ("line ", i, " in master is different \n")
        print (lines2)

        ##When the files don't match, it will use ansible to update the plugin that has changed.
        ##This is done in three plays, 1. delete old files. 2. replace the URL in the master file with the new one
        ##3. create the new RPM based on the latest download URL
        rpm_update = input("Do you wish to update the package?(y or n): ")
        if rpm_update == 'y':
            print("Updating!")
            newurl = lines2
            lines2 = lines2.split("plugin/")[1]
            lines2 = lines2.split(".")[0]
            os.system('ansible-playbook -i hosts delete-files.yml -e "package='+lines2+'"')
            os.system('ansible-playbook -i hosts replace-line.yml -e "package='+lines2+' new_line='+newurl+'"')
            os.system('cowsay Old Files Deleted!')
            os.system('ansible-playbook -i hosts create-rpm.yml -e "package='+lines2+' url='+newurl+'"')
            pass
        else:
            pass

    else:
        print ("Line is the same.")
