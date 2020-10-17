import pymysql
from time import sleep
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# 数据库设置
DBip = "localhost"
DBUserName = "root"
DBpassword = "root"
DBTableName = "hduhelper"


class DBmanager(object):
    def __init__(self,_ip, _username, _password, _table):
        self.db = pymysql.connect(_ip, _username, _password, _table)

    def searchstu(self, uid=-1, name=''):
        cursor = self.db.cursor()
        sql = "SELECT * FROM `task1` WHERE "
        try:
            if uid != -1:
                sql += "`uid` = " + str(uid)
                cursor.execute(sql)
                return cursor.fetchone()
            elif name != '':
                sql += "`name` = \'" + name + "\'"
                cursor.execute(sql)
                return cursor.fetchone()
        except:
            self.db.rollback()
            print("查询学生信息错误，2秒后重试 信息输入：uid=%d，name=%s"%(uid,name))
            sleep(2)
            return self.searchStu(uid, name)

    def insertstu(self, uid, name, building, room):
        cursor = self.db.cursor()
        sql = "REPLACE INTO `task1`(`uid`, `name`, `building`, `room`) \
                VALUES (%d,'%s',%d,%d)"\
                %(uid, name, building, room)
        try:
            cursor.execute(sql)
            return 0
        except:
            print("插入学生信息错误，2秒后重试 信息输入：%d,'%s',%d,%d)" %(uid, name, building, room))
            sleep(2)
            return self.insertstu(uid, name, building, room)

    def roommate(self, uid=-1, name='', building=-1, room=-1):
        if uid != -1:
            stuinfo = self.searchstu(uid)
            sql = "SELECT * FROM `task1` WHERE `building`=%d && `room`=%d"\
                    %(stuinfo[2], stuinfo[3])
            cursor = self.db.cursor()
            try:
                cursor.execute(sql)
                return cursor.fetchall()
            except:
                self.db.rollback()
                print("查询室友错误，2秒后重试")
                sleep(2)
                return self.roommate(uid, name, building, room)



if __name__ == '__main__':
    dbm = DBmanager(DBip, DBUserName, DBpassword, DBTableName)
    print(dbm.searchstu(uid=20322230))
    print(dbm.searchstu(name='杨成锴'))
    app.run(debug=True)
    # for i in range(5):
    #     dbm.insertstu(i, str(i), 1, i)

