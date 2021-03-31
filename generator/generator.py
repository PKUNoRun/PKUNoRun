#!/usr/bin/env python3

import sys, os, time, datetime, random, importlib, argparse, sqlite3

parser = argparse.ArgumentParser(description='Insert a record into PKURunner.')

parser.add_argument("-db"   , required=True, help="Extracted data.db file to edit.")
parser.add_argument("-time" , required=True, help="Time of the record to insert(YYYYMMDD-HH:MM:SS).")
parser.add_argument("-speed", required=True, help="Running speed(min/km).", type=float)
parser.add_argument("-dist" , required=True, help="Distance(km).", type=float)
parser.add_argument("-freq" , required=True, help="Stride frequency(bpm).", type=float)
parser.add_argument("-verbose", help="Display arguments.")

args = parser.parse_args()

v = True if args.verbose else False

dbm = importlib.import_module("dbm")
fake = importlib.import_module("fake")

db = sqlite3.connect(args.db)
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


# dateUTC  = int(time.time()*1000)
dateUTC  = int(time.mktime(time.strptime(args.time, r'%Y%m%d-%H:%M:%S')))*1000+random.randint(0,999)
distance = args.dist
velocity = args.speed
frequency = args.freq

if v:
    print(f"{dateUTC}, {distance}, {velocity}, {frequency}")

tracks = fake.Record(distance*0.9031, velocity, frequency) # 0.9031 to correct distance

rid = dbm.append_record(cur, uid, dateUTC, tracks.distance*1000, tracks.duration, tracks.step)

dbm.append_track(cur,rid,tracks.detail)

db.commit()
db.close()
