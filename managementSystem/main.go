package main

import (
	"fmt"
)

var data [][]string

func main() {
	for true {
		uid,name,buildingNum,roomNum := "","","",""
		fmt.Scanf("%s %s %s %s",&uid,&name,&buildingNum,&roomNum)
		temp := make([uid,name,buildingNum,roomNum])
		data = append(data,temp)
	}
	fmt.Println()
	fmt.Println("hello")
}
