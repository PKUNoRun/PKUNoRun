#!/usr/bin/env python3

import sys, os, time, datetime, random
import importlib

try:
    import sqlite3
except Exception as e:
    print("sqlite3 required. execute 'pip install sqlite3' to install.")
    os._exit(0)

dbm = importlib.import_module("dbm")
fake = importlib.import_module("fake")

if len(sys.argv) < 2:
    print("usage: generator.py database.db")
    print("usage: generator.py database.db time_utc")
    print("time_utc should be 13-digit int")
    os._exit(0)


db = sqlite3.connect(sys.argv[1])
cur = db.cursor()
# init output
dbm.init(cur)
# get user info
usr = dbm.get_users(cur)
if len(usr)==1:
    keys = list(usr.keys())
    uid=keys[0]
else:
    print("name\t\tdepartment\t\tuserId")
    for i in usr:
        print(usr[i][0] + "\t\t" + usr[i][1] + "\t\t" + i)
    while True:
        uid = input("select a user to walk:\t")
        if uid in usr:
            break
# make record
""" 
    duration            int      总跑步时间/s
    date                str      结束时间（时间戳）
    step                int      总步数
    detail              list     跑步路径 GPS 数据， 1 point/s （一秒一个点）
    distance            float    跑步距离/km
    pace                float    跑步速度/(min/km)
            stride_frequncy     int      步频/(step/min)
"""
""" 由距离、速度、步频来生成一次跑步记录
    Args:
        distance           float   跑步距离/km
        pace               float   跑步速度/(min/km)
        stride_frequncy    int     步频/(step/min)
"""
if len(sys.argv)==3:
    dateUTC = int(sys.argv[2])
    distance = 6.0
    velocity = 8.0
    frequncy = 120
else:
    dateUTC  = input("input time (YYYY-MM-DD HH:MM:SS)      :\t")
    distance = input("input distance ( km )                 :\t")
    velocity = input("input velocity ( min/km )             :\t")
    frequncy = input("input stride frequncy (bpm)           :\t")
    if dateUTC ==  '':
        dateUTC  = int(time.time()*1000)
    else:
        dateUTC  = int(time.mktime(time.strptime(dateUTC, r'%Y-%m-%d %H:%M:%S')))*1000+random.randint(0,999)
    if distance == '':
        distance = 6.0
    else:
        distance = float(distance)
    if velocity == '':
        velocity = 8.0
    else:
        velocity = float(velocity)
    if frequncy == '':
        frequncy = 120
    else:
        frequncy = float(frequncy)
tracks = fake.Record(distance*0.9031, velocity, frequncy) # 0.9031 to correct distance

rid = dbm.append_record(cur, uid, dateUTC, tracks.distance*1000, tracks.duration, tracks.step)

dbm.append_track(cur,rid,tracks.detail)

db.commit()
db.close()
print("done")
