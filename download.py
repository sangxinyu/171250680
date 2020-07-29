import os
import urllib.request,urllib.parse

import json

path = './test_data.json'
filename = path
test_data = json.load(open(filename,encoding='UTF-8'))

for key in test_data.keys():
    for i in range(0,len(test_data[key]["cases"])):
        dict = (test_data[key]["cases"][i])
        file = urllib.parse.quote(os.path.basename(dict["case_zip"]))
        file2 = urllib.parse.unquote(os.path.basename(dict["case_zip"]))
        url = dict["case_zip"][0:57] + file
        urllib.request.urlretrieve(url, file2)