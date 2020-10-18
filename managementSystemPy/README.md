# 学生宿舍信息管理系统 by asjdf

---

运行后打开浏览器访问：127.0.0.1:5000

就这样吧 懒得完善了 能用就行（狗头

记得导入数据库



## 后台API地址：

### /search

POST：uid（学号）或者name（姓名）

返回：第一个符合要求的学生 当uid和姓名同时提交时 优先使用uid检索



### /add

POST：uid（学号） name（姓名） building（寝室楼号） room（寝室房间号）

返回：0（成功） 1（失败）



### /del

POST：uid（学号）

返回：0（成功） 1（失败）



### /roommate

POST：uid（学号）或者name（姓名）

返回：json



### /housework

POST：building（楼号） room（房间号）

返回：json（待定



### /set-housework

POST：building room 1 2 3 4 5（值日顺序）