package main

import (
	"fmt"
	"strconv"
)


func createHash() map[string]int{
	
	hash := map[string]int{}

	for i:=1;i<=26;i++{
		hash[strconv.Itoa(i)] = i	
	}
	return hash

}

func aux(value string,hash map[string]int,actualIndex int,dp map[[2]int]int) int{	
	println("ai",actualIndex)
	if(actualIndex <= 0){
		return 1
	}
	existTwo := false
	existOne := false
	if(actualIndex - 2 >= 0){
		println("value2",value[actualIndex-2:actualIndex],actualIndex)
		_,existTwo = hash[value[actualIndex-2:actualIndex]]
	}
	if(actualIndex-1>=0){
		println("value1",value[actualIndex-1:actualIndex],actualIndex)
		_,existOne = hash[value[actualIndex-1:actualIndex]]
	}
	twoValue := 0
	oneValue := 0
	if(existTwo){
		dpTwoValue,dpTwoExist := dp[[2]int{actualIndex-2,actualIndex}]
		if(dpTwoExist){
			twoValue = dpTwoValue 
		}else{ 
			twoValue = aux(value,hash,actualIndex-2,dp)
			dp[[2]int{actualIndex-2,actualIndex}] = twoValue
		}

	}
	if(existOne){
		dpOneValue,dpOneExist := dp[[2]int{actualIndex-1,actualIndex}]
		if(dpOneExist){
			oneValue = dpOneValue 
		}else{ 
			oneValue = aux(value,hash,actualIndex-1,dp)
			dp[[2]int{actualIndex-1,actualIndex}] = oneValue
		}

	}
	return oneValue + twoValue
}


func main(){
	teste := "06"
	print(teste[0:2])
	dp := map[[2]int]int{}
	result := aux(teste,createHash(),len(teste),dp)
	fmt.Println(dp)
	fmt.Println(result)
}

