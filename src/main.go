package main

import (
	"fmt"
	"time"
)

type Point struct {
	x float64
	y float64
}

// setter, getter
func get_value_x(p Point) float64 {
	return p.x
}

func get_value_y(p Point) float64 {
	return p.y
}

func set_value_x(new_x float64, p *Point) {
	p.x = new_x
}

func set_value_y(new_y float64, p *Point) {
	p.y = new_y
}

// function
func midPoint(p1 Point, p2 Point) Point {
	return Point{(get_value_x(p1) + get_value_x(p2)) / 2, (get_value_y(p1) + get_value_y(p2))/2}
}

func set_point(idx int,list []Point, new Point) {
	list[idx] = new
}

func iterate(list []Point) []Point{
	temp := []Point{}
	for i:=0; i < len(list)-1; i++{
		temp = append(temp, midPoint(list[i],list[i+1]))
	}
	for i:=0 ;i < len(list)-2; i++{
		set_point(i+1,list,midPoint(temp[i],temp[i+1]))
	}
	n := len(list) - 1
	for j:=0 ; j < n ; j++{
		list = append(list, Point{0,0})
	}
	for i := n; i > 0; i--{
		list[2*i] = list[i]
		list[2*i-1] = temp[i-1]
	}
	return list
}

// print
func printPoint(p Point) {
	fmt.Println(p.x)
	fmt.Println(p.y) 
}

func printList(list []Point){
	for i:=0 ; i < len(list) ; i++ {
		fmt.Println(i+1, list[i])
	}
}

func main() {
	var p = Point{3, 4}
	printPoint(p)
	fmt.Println(get_value_x(p))
	fmt.Println(get_value_y(p))
	set_value_x(0, &p)
	set_value_y(0, &p)
	printPoint(p)
	var pp = Point{-3, -4}
	printPoint(pp)
	var ppp = midPoint(p, pp)
	printPoint(ppp)
	a := []Point{p,pp,ppp}
	fmt.Println(a)
	set_point(1, a, p)
	a = append(a, Point{5,12})
	fmt.Println(a)
	fmt.Println("Beizer")
	beizer := []Point{Point{0,0},Point{4,4},Point{8,0}}
	fmt.Println(beizer)
	start := time.Now()
	beizer = iterate(beizer)
	beizer = iterate(beizer)
	beizer = iterate(beizer)
	beizer = iterate(beizer)
	beizer = iterate(beizer)
	beizer = iterate(beizer)
	beizer = iterate(beizer)
	beizer = iterate(beizer)
	beizer = iterate(beizer)
	beizer = iterate(beizer)
	beizer = iterate(beizer)
	beizer = iterate(beizer)
	beizer = iterate(beizer)
	duration := time.Since(start)
	printList(beizer)
	fmt.Println("Program execution time:", duration)
}