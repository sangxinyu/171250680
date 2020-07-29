import json
import pandas as pd
import csv
import xlwt
import collections
import time
import os
import urllib.request,urllib.parse

path = './test_data.json'
filename = path
test_data = json.load(open(filename,encoding='UTF-8'))
list = []
list_time = []

for key in test_data.keys():
    for i in range(0,len(test_data[key]["cases"])):
        dict = (test_data[key]["cases"][i])
        list.append([test_data[key]["user_id"],dict["case_type"], dict["final_score"]])

dataFrame = pd.DataFrame(list)
dataFrame.to_excel('./score.xlsx',encoding='UTF-8')

time_1month = 0
time_1week = 0
time_3days = 0
time_1day = 0
score1 = score2 = score3 = score4 = 0.00

for key in test_data.keys():
    for i in range(0,len(test_data[key]["cases"])):
        dict = (test_data[key]["cases"][i])
        for j in range(0,len(dict["upload_records"])):
            dict_upload = dict["upload_records"][j]
            temp = dict_upload["upload_time"]
            stamp = time.strftime("%Y-%m-%d %H:%M:%S", (time.localtime(temp/1000)))
            if stamp < "2020-03-01":
                time_1month += 1
                score1 += dict_upload["score"]
            elif stamp >= "2020-03-01" and stamp < "2020-03-25":
                time_1week += 1
                score2 += dict_upload["score"]
            elif stamp >= "2020-03-25" and stamp < "2020-03-29":
                time_3days += 1
                score3 += dict_upload["score"]
            elif stamp >= "2020-03-29":
                time_1day += 1
                score4 += dict_upload["score"]
            list_time.append([test_data[key]["user_id"], stamp, dict_upload["score"]])


print(time_1month, time_1week, time_3days, time_1day)
print(score1/time_1month, score2/time_1week, score3/time_3days, score4/time_1day)

df = pd.DataFrame(list_time)
df.to_excel('./time.xlsx',encoding='UTF-8')