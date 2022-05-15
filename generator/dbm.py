#!/usr/bin/env python3

import sqlite3
from functools import reduce

def init(cursor):
    init_commands = {
        "android_metadata":r'''CREATE TABLE android_metadata (locale TEXT)''',
        # "partial_record":r'''CREATE TABLE "partial_record" ( "id" INTEGER PRIMARY KEY AUTOINCREMENT, "date" INTEGER ,"distance" INTEGER ,"duration" INTEGER ,"step" INTEGER )''',
        # "partial_track":r'''CREATE TABLE "partial_track" ( "id" INTEGER PRIMARY KEY AUTOINCREMENT, "latitude" REAL ,"longitude" REAL ,"recordDbId" INTEGER ,"sequence" INTEGER ,"status" INTEGER )''',
        "record":r'''CREATE TABLE "record" ( "id" INTEGER PRIMARY KEY AUTOINCREMENT, "extra" TEXT ,"date" INTEGER ,"detailed" INTEGER ,"distance" INTEGER ,"duration" INTEGER ,"invalidReason" INTEGER ,"photoName" TEXT ,"photoRemotePath" TEXT ,"placeHint" TEXT ,"recordId" INTEGER ,"step" INTEGER ,"uploaded" INTEGER ,"userId" TEXT ,"verified" INTEGER  )''',
        "track":r'''CREATE TABLE "track" ( "id" INTEGER PRIMARY KEY AUTOINCREMENT, "latitude" REAL ,"longitude" REAL ,"recordDbId" INTEGER ,"sequence" INTEGER ,"status" INTEGER  )''',
        "user":r'''CREATE TABLE "user" ( "id"TEXT PRIMARY KEY, "PESpecialty" INTEGER ,"department" TEXT ,"gender" INTEGER ,"name" TEXT ,"offline" INTEGER ,"token" TEXT  )''',
    }
    tables = [x[0] for x in cursor.execute("SELECT tbl_name FROM sqlite_master WHERE type='table' ")]
    # cursor.execute('''drop table "record" if exists''')
    for t in init_commands:
        if not t in tables:
            print(f"create table {t}...")
            cursor.execute(init_commands[t])

def insert(cursor, table, dict):
    keys = list(dict.keys())
    vals = tuple(dict.values())
    cursor.execute(f"INSERT INTO '{table}' ({', '.join(keys)}) VALUES ({', '.join(['?'] * len(keys))})",vals)
    return cursor.lastrowid

def get_users(cursor):
    return {x[0]:(x[1],x[2]) for x in cursor.execute("SELECT id, name, department FROM user")}

from Crypto.Cipher import AES
import base64

class C0022a:
    @classmethod
    def a(cls, bArr):
        if isinstance(bArr, bytes):
            return base64.b64encode(bArr).decode()
        elif isinstance(bArr, str):
            return base64.b64decode(str)


def generateCheckField(s: str, date: str):
    def PKCS5(s):
        blocksize = 16
        return s + ((blocksize - len(s) % blocksize) * chr(blocksize - len(s) % blocksize)).encode()
    def a(s1, s2):
        if s1 == None or len(s1) == 0:
            return None
        byts = s1.encode('utf-8')
        keyb = s2.encode('utf-8')
        cipher = AES.new(keyb, AES.MODE_ECB)
        byts = PKCS5(byts)
        return C0022a.a(cipher.encrypt(byts))
    return a("android11", f"{s}_{date}")

def append_record(cursor, userId, dateUTC, distance, duration, step):
    rid = insert(cursor, "record", {
        "userId":userId,
        "date":dateUTC,
        "distance":int(distance),
        "duration":int(duration),
        "step":int(step),
        "detailed":1,
        "invalidReason":0,
        "recordId":-1,
        "uploaded":0,
        "verified":0,
        "extra": generateCheckField(userId, str(dateUTC))
    })
    return rid

def append_track(cursor, recordDbId, lat_lon_list):
    # [(lat,lon),..]
    i=0
    for t in lat_lon_list:
        insert(cursor, "track",{
            "latitude":t[1],
            "longitude":t[0],
            "recordDbId":recordDbId,
            "status":0,
            "sequence":i
        })
        i+=1
