# 学生宿舍信息管理系统

---





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

返回：