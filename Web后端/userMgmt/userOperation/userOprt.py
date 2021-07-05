import pymysql as sql
from flask import jsonify
import datetime
import random

connect = sql.Connect(
    host='rm-bp131vjnd9b99vmuq2o.mysql.rds.aliyuncs.com',
    port=3306,
    user='lin_432718',
    passwd='Lin817818',
    db='rail_traffic',
    charset='utf8'
)
cursor = connect.cursor()

def idenfity(name, password):

    sql = "SELECT user_id FROM user WHERE user_id = '" + name + "' AND password = '" + password + "'"
    print(sql)
    cursor.execute(sql)
    temp = cursor.fetchall()
    print(temp)
    if temp == ():
        print("登录失败")
        return jsonify(0)
    else:
        print("登录成功")
        return jsonify(1)

def getUserID(name):

    sql = "SELECT staff_id FROM user WHERE user_id = '" + name + "'"
    print(sql)
    cursor.execute(sql)
    return cursor.fetchall()[0][0]

def updatepass(word):
    sql = "UPDATE user SET password = " + str(word) +" WHERE user_id = 'admin';"
    print(sql)
    try:
        cursor.execute(sql)
        connect.commit()
    except:
        return False
    else:
        return True

def getData():
    sql = "select staff_id, user_id, password from user"

    print(sql)
    cursor.execute(sql)

    attribute = ['staff_id', 'user_id', 'password']
    l = []
    for item in cursor.fetchall():
        dic = dict(map(lambda x, y: [x, y], attribute, item))
        l.append(dic)
    # print(l)
    return jsonify(l)

def vague(word):

    sql = "select staff_id, user_id, password from user WHERE user_id LIKE '%" + word + "%'"
    # print(sql)
    cursor.execute(sql)

    attribute = ['staff_id', 'user_id', 'password']
    l = []
    for item in cursor.fetchall():
        dic = dict(map(lambda x, y: [x, y], attribute, item))
        l.append(dic)
    # print(l)
    return jsonify(l)

def initpass(user_id):

    newPass = ""
    for i in range(6):
        newPass = newPass + str(random.randrange(10))
    print(newPass)
    sql = "update user set password = '" + newPass + "' where user_id = '" + user_id + "'"
    print(sql)
    try:
        cursor.execute(sql)
        connect.commit()
    except:
        return jsonify(0)
    else:
        return jsonify(1)

