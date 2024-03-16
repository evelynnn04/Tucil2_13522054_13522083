package main

import (
	"bezier/module"
	"fmt"
)

func main() {
	// KAMUS UMUM
	// var x1, y1, x2, y3, x3, y3 float64
	var n_points_type, itr, num_of_points int
	list_of_point := []module.Point{}
	//Input
	fmt.Print("Welcome to Beizer Graphic Generator! ")
	fmt.Println("Input type: ")
	fmt.Println("1. 3 points")
	fmt.Println("2. n point")
	for {
		fmt.Print("Enter your choice (1 or 2): ")
		_, err := fmt.Scanln(&n_points_type)
		if err != nil {
			fmt.Println("Input error!", err.Error())
			continue
		}

		if n_points_type != 1 && n_points_type != 2 {
			fmt.Println("Invalid input. Please enter 1 or 2.")
			continue
		}
		break
	}
	if n_points_type == 1 {
		fmt.Print("Input number of iterate: ")
		fmt.Scanln(&itr)
		for i := 0; i < 3; i++ {
			list_of_point = append(list_of_point,module.InputPoint(i + 1))
		}
	} else {
		fmt.Print("Input number of iterate: ")
		fmt.Scanln(&itr)
		fmt.Print("Input number of points: ")
		fmt.Scanln(&num_of_points)
		for i := 0; i < num_of_points; i++ {
			list_of_point = append(list_of_point,module.InputPoint(i + 1))
		}
	}
	module.PrintList(list_of_point)
	// Solve
	list_of_point = module.General_iterate(num_of_points,itr,0,list_of_point)
	//Output
	fmt.Println("Hasil")
	module.PrintList(list_of_point)
}
