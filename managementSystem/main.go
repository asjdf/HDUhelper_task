package main

import (
	"encoding/json"
	"fmt"
	"github.com/gin-gonic/gin"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

type StuManager struct {
	db *gorm.DB
}

func NewStuManager(db *gorm.DB)  *StuManager{
	return &StuManager{db}
}

func (s StuManager) SearchStu(uid int, name string) Task1Go {
	data := Task1Go{}
	if uid != 0 {
		fmt.Println(uid)
		s.db.Where("uid = ?", uid).Find(&data)
	}else if name != ""{
		fmt.Println(name)
		s.db.Where("uid = ?", uid).Find(&data)
	}else{
		fmt.Println("error: 无传入参数")
	}
	return data
}

func (s StuManager) DelStu(uid int) int {
	data := Task1Go{}
	s.db.Where("uid = ?", uid).Delete(&data)
	return 0
}

func (s StuManager) InsertStu(uid int, name string, building int, room int, bed int) int {
	if uid != 0 && name != "" && building != 0 && room != 0 && bed != 0{
		data := Task1Go{
			Uid:      uid,
			Name:     name,
			Building: building,
			Room:     room,
			Bed:      bed,
		}
		s.db.Where("uid = ?",data.Uid).Save(&data)
		return 0
	}else{
		return 1
	}
}

func (s StuManager) Roommate(uid int, name string, building int, room int) Task1Go {
	data := Task1Go{}
	if uid != 0 {
		s.db.Where("uid = ?", uid).Find(&data)
	}else if name != "" {
		s.db.Where("name = ?", name).Find(&data)
	}else if building != 0 && room != 0{
		s.db.Where("building = ? AND room = ？", building, room).Find(&data)
	}
	return data
}

func (s StuManager) SetHousework(building int, room int, first int, second int,third int, forth int,fifth int) int {
	if building != 0 && room != 0 && first != 0 && second != 0 && third != 0 && forth != 0 && fifth != 0{
		data := Task1GoWork{
			Building: building,
			Room:     room,
			First:    first,
			Second:   second,
			Third:    third,
			Forth:    forth,
			Fifth:    fifth,
		}
		s.db.Where("building = ? AND room = ?", building, room).Save(&data)
		return 0
	}else{
		return 1
	}
}

func (s StuManager) Housework(building int, room int) Task1GoWork {
	data :=Task1GoWork{}
	if building != 0 && room != 0 {
		s.db.Where("building = ? AND room = ?", building, room).Find(&data)
	}
	return data
}

type Task1Go struct {
	gorm.Model
	Uid int `gorm:"uniqueIndex"`
	Name string
	Building int
	Room int
	Bed int``
}
type Task1GoWork struct {
	gorm.Model
	Building int
	Room int
	First int
	Second int
	Third int
	Forth int
	Fifth int
}

func main() {
	dsn := "root:root@tcp(127.0.0.1:3306)/hduhelper?charset=utf8mb4&parseTime=True&loc=Local"
	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	if err != nil{
		fmt.Println("数据库初始化出错")
	}
	//fmt.Println(db.Take(&test_go))
	db.AutoMigrate(&Task1Go{})
	db.AutoMigrate(&Task1GoWork{})
	fmt.Println(err)
	data := &Task1Go{
		Uid: 20322231,
		Name:  "test2",
		Building: 27,
		Room: 624,
		Bed: 4,
	}
	//db.Create(&data)
	db.Where("uid = ?",data.Uid).Save(&data)
	dataM,_ := json.Marshal(data)
	fmt.Println(string(dataM))
	//fmt.Println(db.Take(&Task1Go{}))
	//for true {
	//	uid,name,buildingNum,roomNum := "","","",""
	//	fmt.Scanf("%s %s %s %s",&uid,&name,&buildingNum,&roomNum)
	//	if uid == "-1" {
	//		break
	//	}
	//	temp:= []string{uid,name,buildingNum,roomNum}
	//	data = append(data,temp)
	//	fmt.Println(data)
	//}
	//fmt.Println(data)
	//fmt.Println("hello")
	r := gin.Default()

	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
	r.Run(":8085")
}
