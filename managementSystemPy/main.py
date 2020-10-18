import pymysql
from pymysql.cursors import DictCursor
from time import sleep
from flask import Flask, redirect, request
import json

app = Flask(__name__, static_folder='./static', static_url_path='')


@app.route('/')
def index():
    return redirect("/index.html")


@app.route('/search', methods=['POST'])
def handle_search():
    uid = request.form.get('uid', type=int, default=-1)
    name = request.form.get('name', type=str, default='')
    return dbm.search_stu(uid, name)


@app.route('/add', methods=['POST'])
def handle_add():
    uid = request.form.get('uid', type=int, default=-1)
    name = request.form.get('name', type=str, default='')
    building = request.form.get('building', type=int, default=-1)
    room = request.form.get('room', type=int, default=-1)
    bed = request.form.get('bed', type=int, default=-1)
    return str(dbm.insert_stu(uid, name, building, room, bed))


@app.route('/del', methods=['POST'])
def handle_del():
    uid = request.form.get('uid', type=int, default=-1)
    return str(dbm.del_stu(uid))


@app.route('/roommate', methods=['POST'])
def handle_roommate():
    uid = request.form.get('uid', type=int, default=-1)
    name = request.form.get('name', type=str, default='')
    building = request.form.get('building', type=int, default=-1)
    room = request.form.get('room', type=int, default=-1)
    return json.dumps(list(dbm.roommate(uid, name, building, room)))


# 数据库设置
DBIp = "localhost"
DBUserName = "root"
DBPassword = "root"
DBTableName = "hduhelper"


class DBManager(object):
    def __init__(self, _ip, _username, _password, _table):
        self.db = pymysql.connect(_ip, _username, _password, _table)

    def search_stu(self, uid=-1, name=''):
        self.db.ping(reconnect=True)
        cursor = self.db.cursor()
        try:
            if uid != -1:
                sql = "SELECT * FROM `task1` WHERE `uid` = " + str(uid)
                cursor.execute(sql)
                return cursor.fetchone()
            elif name != '':
                sql = "SELECT * FROM `task1` WHERE `name` = \'" + name + "\'"
                cursor.execute(sql)
                return cursor.fetchone()
        except:
            self.db.rollback()
            print("查询学生信息错误，2秒后重试 信息输入：uid=%d，name=%s" % (uid, name))
            sleep(2)
            return self.search_stu(uid, name)

    def insert_stu(self, uid, name, building, room, bed):
        self.db.ping(reconnect=True)
        cursor = self.db.cursor()
        sql = "REPLACE INTO `task1`(`uid`, `name`, `building`, `room`, `bed`) \
                VALUES (%d,'%s',%d,%d,%d)" \
              % (uid, name, building, room, bed)
        try:
            cursor.execute(sql)
            return 0
        except:
            print("插入学生信息错误，2秒后重试 信息输入：%d,'%s',%d,%d,%d)" % (uid, name, building, room, bed))
            sleep(2)
            return self.insert_stu(uid, name, building, room)

    def del_stu(self, uid):
        self.db.ping(reconnect=True)
        cursor = self.db.cursor()
        sql = "DELETE FROM `task1` WHERE `uid` = %d" % (uid)
        try:
            cursor.execute(sql)
            return 0
        except:
            print("删除学生信息错误，2秒后重试 信息输入：%d" % (uid))
            sleep(2)
            return self.del_stu(uid)

    def roommate(self, uid=-1, name='', building=-1, room=-1):
        if uid != -1 or name != '' or building != -1 or room != -1:
            if uid != -1:
                stu_info = self.search_stu(uid=uid)
                sql = "SELECT * FROM `task1` WHERE `building`=%d && `room`=%d" \
                      % (stu_info[2], stu_info[3])
            if name != '':
                stu_info = self.search_stu(name=name)
                sql = "SELECT * FROM `task1` WHERE `building`=%d && `room`=%d" \
                      % (stu_info[2], stu_info[3])
            if building != -1 and room != -1:
                sql = "SELECT * FROM `task1` WHERE `building`=%d && `room`=%d" \
                      % (building, room)
            cursor = self.db.cursor(DictCursor)
            try:
                self.db.ping(reconnect=True)
                cursor.execute(sql)
                res = cursor.fetchall()
                print(res)
                return res
            except:
                self.db.rollback()
                print("查询室友错误，2秒后重试")
                sleep(2)
                return self.roommate(uid, name, building, room)


    def housework(self, building = -1, room = -1):
        if building != -1 and room != -1:
            sql = "SELECT * FROM `task1_work` WHERE `building` = %d && `room` = %d" % (building, room)
            cursor = self.db.cursor(DictCursor)
            try:
                self.db.ping(reconnect=True)
                cursor.execute(sql)
                res = cursor.fetchall()
                print(res)
                return res
            except:
                self.db.rollback()
                print("查询值日信息错误，2秒后重试")
                sleep(2)
                return self.housework(building, room)

    def set_housework(self, building = -1, room = -1, first = -1, second = -1, third = -1, forth = -1, fifth = -1):
        if building != -1 and room != -1:
            sql = "REPLACE INTO `task1_work` (`building`, `room`, `1`, `2`, `3`, `4`, `5`) \
                  VALUES (%d,'%d',%d,%d,%d)"\
                  % (building, room, first, second, third, forth, fifth)
            cursor = self.db.cursor(DictCursor)
            try:
                self.db.ping(reconnect=True)
                cursor.execute(sql)
                res = cursor.fetchall()
                print(res)
                return res
            except:
                self.db.rollback()
                print("设置值日信息错误，2秒后重试")
                sleep(2)
                return self.housework(building, room)


if __name__ == '__main__':
    dbm = DBManager(DBIp, DBUserName, DBPassword, DBTableName)
    print(dbm.search_stu(uid=20322230))
    print(dbm.search_stu(name='杨成锴'))
    print(type(dbm.roommate(name='杨成锴')))
    app.run(debug=True)
    # for i in range(5):
    #     dbm.insertstu(i, str(i), 1, i)
