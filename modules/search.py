def search(api_url, file_extension, local_boolean, local_dir, search_pattern):
    from urllib import request
    import shutil
    import json
    import os
    import re

    files = []

    #Get search.json
    with request.urlopen(api_url) as api_result, open('search.json', 'wb') as search_file:
        shutil.copyfileobj(api_result, search_file)

    #Parse search.json
    with open('search.json', "r") as search_file:
        data = json.load(search_file)
        for file in data:
            name = file['name']
            if name.endswith(file_extension):
                files.append(name.replace(file_extension, ''))

    #Get local files
    if local_boolean:
        for file in os.listdir(local_dir):
            if file.endswith(file_extension):
                if file.replace(file_extension, '') not in files:
                    files.append(file.replace('.sh', ''))
    #Search
    r = re.compile(search_pattern)
    result = list(filter(r.match, files))
    return result
