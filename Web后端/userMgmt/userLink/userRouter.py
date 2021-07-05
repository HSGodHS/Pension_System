from flask import Blueprint, jsonify, request, json
import pymysql as sql
import userMgmt.userOperation.userOprt as userOprt
import datetime

user = Blueprint('user', __name__)

connect = sql.Connect(
    host='rm-bp131vjnd9b99vmuq2o.mysql.rds.aliyuncs.com',
    port=3306,
    user='lin_432718',
    passwd='Lin817818',
    db='rail_traffic',
    charset='utf8'
)
cursor = connect.cursor()

admin = '18301010'

@user.route('/', methods=['GET'])
def index():
    print("here is base")
    return jsonify('cbq sb')


# ###########################################################################################################登录
@user.route('/login', methods=['POST'])
def login():
    global admin
    data = request.get_data()
    json_data = json.loads(data.decode("utf-8"))
    name = json_data.get('id')
    password = json_data.get('password')

    admin = name
    return userOprt.idenfity(name, password)


@user.route('/updatepass', methods=['POST'])
def updatepass():
    global admin
    data = request.get_data()
    json_data = json.loads(data.decode("utf-8"))
    old_pass = json_data.get('old_pass')
    new_pass = json_data.get('new_pass')
    conf_pass = json_data.get('conf_pass')
    if new_pass != conf_pass:
        return jsonify(2)
    sql0 = "SELECT password from user where user_id='" + admin + "'"
    print(sql0)
    cursor.execute(sql0)
    temp = cursor.fetchall()
    print(temp)
    if temp[0][0] == old_pass:
        sql1 = "UPDATE user SET password = " + str(new_pass) + " WHERE user_id = '" + admin + "'"
        print(sql1)
        cursor.execute(sql1)
        connect.commit()
        return jsonify(0)
    else:
        return jsonify(1)


# 获取用户修改信息
@user.route('/userInfo', methods=['GET'])
def userInfo():
    return userOprt.getData()

# 获取当前用户的用户名
@user.route('/userName', methods=['GET'])
def userName():
    return staffOprt.getName(admin)

# 模糊搜索
@user.route('/userVagueSelect', methods=['POST'])
def userVagueSelect():

    data = request.get_data()
    json_data = json.loads(data.decode("utf-8"))
    word = json_data.get('word')
    return userOprt.vague(word)

# 身份判断
@user.route('/identify', methods=['GET'])
def identify():
    return ocpsOprt.is003(admin)

# 初始化密码
@user.route('/initPassword', methods=['POST'])
def initPassword():

    data = request.get_data()
    json_data = json.loads(data.decode("utf-8"))
    user_id = json_data.get('user_id')
    return userOprt.initpass(user_id)