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

# dataFrame = pd.DataFrame(list)
# dataFrame.to_excel('./score.xlsx',encoding='UTF-8')

time_1month = 0
time_1week = 0
time_3days = 0
time_1day = 0
score1 = score2 = score3 = score4 = 0.00
time0217 = time0218 = time0219 = time0220 = time0221 = time0222 = time0223 = time0224 = time0225 = time0226 =time0227 =time0228 = time0229 = 0
time0301=time0302=time0303=time0304=time0305=time0306=time0307=time0308=time0309=time0310=time0311=time0312=time0313=time0314=time0315=time0316=time0317=time0318=time0319=time0320=time0321=time0322=time0323=time0324=time0325=time0326=time0327=time0328=time0329=time0330=time0331=0
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


# print(time_1month, time_1week, time_3days, time_1day)
# print(score1/time_1month, score2/time_1week, score3/time_3days, score4/time_1day)

# df = pd.DataFrame(list_time)
# df.to_excel('./time.xlsx',encoding='UTF-8')

for key in test_data.keys():
    for i in range(0,len(test_data[key]["cases"])):
        dict = (test_data[key]["cases"][i])
        for j in range(0,len(dict["upload_records"])):
            dict_upload = dict["upload_records"][j]
            temp = dict_upload["upload_time"]
            stamp = time.strftime("%Y-%m-%d %H:%M:%S", (time.localtime(temp/1000)))
            if stamp.startswith("2020-02-17"):
                time0217 += 1
            if stamp.startswith("2020-02-18"):
                time0218 += 1
            if stamp.startswith("2020-02-19"):
                time0219 += 1
            if stamp.startswith("2020-02-20"):
                time0220 += 1
            if stamp.startswith("2020-02-21"):
                time0221 += 1
            if stamp.startswith("2020-02-22"):
                time0222 += 1
            if stamp.startswith("2020-02-23"):
                time0223 += 1
            if stamp.startswith("2020-02-24"):
                time0224 += 1
            if stamp.startswith("2020-02-25"):
                time0225 += 1
            if stamp.startswith("2020-02-26"):
                time0226 += 1
            if stamp.startswith("2020-02-27"):
                time0227 += 1
            if stamp.startswith("2020-02-28"):
                time0228 += 1
            if stamp.startswith("2020-02-29"):
                time0229 += 1
            if stamp.startswith("2020-03-01"):
                time0301 += 1
            if stamp.startswith("2020-03-02"):
                time0302 += 1
            if stamp.startswith("2020-03-03"):
                time0303 += 1
            if stamp.startswith("2020-03-04"):
                time0304 += 1
            if stamp.startswith("2020-03-05"):
                time0305 += 1
            if stamp.startswith("2020-03-06"):
                time0306 += 1
            if stamp.startswith("2020-03-07"):
                time0307 += 1
            if stamp.startswith("2020-03-08"):
                time0308 += 1
            if stamp.startswith("2020-03-09"):
                time0309 += 1
            if stamp.startswith("2020-03-10"):
                time0310 += 1
            if stamp.startswith("2020-03-11"):
                time0311 += 1
            if stamp.startswith("2020-03-12"):
                time0312 += 1
            if stamp.startswith("2020-03-13"):
                time0313 += 1
            if stamp.startswith("2020-03-14"):
                time0314 += 1
            if stamp.startswith("2020-03-15"):
                time0315 += 1
            if stamp.startswith("2020-03-16"):
                time0316 += 1
            if stamp.startswith("2020-03-17"):
                time0317 += 1
            if stamp.startswith("2020-03-18"):
                time0318 += 1
            if stamp.startswith("2020-03-19"):
                time0319 += 1
            if stamp.startswith("2020-03-20"):
                time0320 += 1
            if stamp.startswith("2020-03-21"):
                time0321 += 1
            if stamp.startswith("2020-03-22"):
                time0322 += 1
            if stamp.startswith("2020-03-23"):
                time0323 += 1
            if stamp.startswith("2020-03-24"):
                time0324 += 1
            if stamp.startswith("2020-03-25"):
                time0325 += 1
            if stamp.startswith("2020-03-26"):
                time0326 += 1
            if stamp.startswith("2020-03-27"):
                time0327 += 1
            if stamp.startswith("2020-03-28"):
                time0328 += 1
            if stamp.startswith("2020-03-29"):
                time0329 += 1
            if stamp.startswith("2020-03-30"):
                time0330 += 1
            if stamp.startswith("2020-03-31"):
                time0331 += 1
print(time0217,time0218,time0219,time0220,time0221,time0222,time0223,time0224,time0225,time0226,time0227,time0228,time0229,time0301,time0302,time0303,time0304,time0305,time0306,time0307,time0308,time0309,time0310,time0311,time0312,time0313,time0314,time0315,time0316,time0317,time0318,time0319,time0320,time0321,time0322,time0323,time0324,time0325,time0326,time0327,time0328,time0329,time0330,time0331)