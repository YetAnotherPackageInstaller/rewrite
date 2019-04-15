#YAPI Rewrite - Yet Another Package Installer

#Imports
import modules.cross_platform as cross_platform
import modules.config_import as config_import
import modules.installer as installer
import gui.interface as interface
import modules.search as search
import json
import sys
import os
try:
    os.chdir(os.path.dirname(__file__)) #Change file location if outside of YAPI
except:
    pass #Already in directory of YAPI.
if len(sys.argv) != 2:
    try:
        config = json.loads(config_import.get_config())
        os_platform = config['OS.platform']
        cache_boolean = ('True' == config['Cache.keep_cache'])
        cache_location = config['Cache.cache_location']
        search_local = ('True' == config['Search.search_local'])
        search_url = config['Search.search_url']
        remote_location = config['Remote.location']
        remote_branch = config['Remote.branch']
        file_extension = config['Remote.file_extension']
        language_selected = config['Languages.selected']
    except:
        print('Config not able to be imported. Run \'python3 yapi.py config\' to fix the error')

#Main Program
if len(sys.argv) == 1:
    result = interface.start()

elif len(sys.argv) == 2:
    if sys.argv[1] == 'config':
        config_import.update_config()

elif len(sys.argv) == 3:
    if sys.argv[1] == 'search':
        matches = search.search(search_url, file_extension, search_local, cache_location, sys.argv[2])
        cross_platform.tabprint(matches)
    elif sys.argv[1] == 'type':
        matches = search.searchType(os_platform, search_url, remote_location, remote_branch, file_extension, cache_boolean, cache_location, sys.argv[2])
        cross_platform.tabprint(matches)
    elif sys.argv[1] == 'download':
        file_name = sys.argv[2] + file_extension
        file_url = remote_location + os_platform + '/' + remote_branch + '/scripts/' + file_name
        os.chdir(cache_location)
        output = installer.get_file(file_url, file_name)
    elif sys.argv[1] == 'run':
        file_name = sys.argv[2] + file_extension
        os.chdir(cache_location)
        output = installer.run_script(file_name, cache_boolean)
    elif sys.argv[1] == 'install':
        output = installer.full_install(sys.argv[2])

elif len(sys.argv) == 4:
    import modules.new_installer as ni
    if sys.argv[2] == 'search':
        print('Search not supported for new file definition yet.')
    elif sys.argv[2] == 'type':
        print('Search by type not supported for new file definition yet.')
    elif sys.argv[2] == 'download':
        ni.download(sys.argv[3], config)
    elif sys.argv[2] == 'run':
        ni.install(sys.argv[3], config)
    elif sys.argv[2] == 'install':
        ni.download(sys.argv[3], config)
        ni.install(sys.argv[3], config)
    elif sys.argv[2] == 'uninstall':
        ni.uninstall(sys.argv[3], config)
