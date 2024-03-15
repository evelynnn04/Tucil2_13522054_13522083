package module

import (
	"fmt"
	"math"
	// "strconv"
	// "strings"
	// "time"
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
	// menghsilkan point yang merupakan titik tengah p1 dan p2
	return Point{(get_value_x(p1) + get_value_x(p2)) / 2, (get_value_y(p1) + get_value_y(p2)) / 2}
}

func set_point(idx int, list []Point, new Point) {
	// isi list ke idx diisi dengan new
	list[idx] = new
}

// Kuadratik
func Iterate(list []Point) []Point {
	// membuat array of point untuk kurva bezeir yang kuadratik
	temp := []Point{}
	for i := 0; i < len(list)-1; i++ {
		temp = append(temp, midPoint(list[i], list[i+1]))
	}
	for i := 0; i < len(list)-2; i++ {
		set_point(i+1, list, midPoint(temp[i], temp[i+1]))
	}
	n := len(list) - 1
	for j := 0; j < n; j++ {
		list = append(list, Point{0, 0})
	}
	for i := n; i > 0; i-- {
		list[2*i] = list[i]
		list[2*i-1] = temp[i-1]
	}
	return list
}

// Generalisasi
func wide(i Point, list []Point, f Point) []Point {
	// membuat array yang berisi {i, semua isi list, f}
	result := []Point{}
	result = append(result, i)
	for i := 0; i < len(list); i++ {
		result = append(result, list[i])
	}
	result = append(result, f)
	return result
}

func base_iterate(n int, list []Point) []Point {
	// n itu banyak titik kontrol
	// membuat array turunan/anak dari list
	if n == 1 {
		return list
	} else {
		temp := []Point{}
		for i := 0; i < n-1; i++ {
			temp = append(temp, midPoint(list[i], list[i+1]))
		}
		return wide(list[0], base_iterate(n-1, temp), list[len(list)-1])
	}
}

func connect(p1 []Point, p2 []Point) []Point {
	// membuat array gabungan p1 dan p2
	// jika elemen terakhir p1 == elemen pertama p2,
	// maka elemen hanya diambil 1 saja
	if len(p1) != 0 {
		temp := []Point{}
		for i := 0; i < len(p1); i++ {
			temp = append(temp, p1[i])
		}
		for i := 0; i < len(p2); i++ {
			if i == 0 {
				if p2[i].x == temp[len(temp)-1].x && p2[i].y == temp[len(temp)-1].y {
					continue
				} else {
					temp = append(temp, p2[i])
				}
			}
			temp = append(temp, p2[i])
		}
		return temp
	} else {
		return p2
	}
}

func general_iterate(n int, iterate int, count int, list []Point) []Point {
	// n adalah banyak titik kontrol
	// iterate adalah jumlah iterasi
	// count adalah pencacah iterasi
	if iterate == count {
		return list
	} else {
		result := []Point{}
		length := math.Pow(2, float64(count))
		fmt.Println(length)
		for i := 0; i < int(length); i++ {
			temp := []Point{}
			for j := 0; j < n; j++ {
				temp = append(temp, list[(n-1)*i+j])
			}
			temp = base_iterate(n, temp)
			result = connect(result, temp)
		}
		return general_iterate(n, iterate, count+1, result)
	}
}

// print
func printPoint(p Point) {
	fmt.Println(p.x)
	fmt.Println(p.y)
}

func PrintList(list []Point) {
	for i := 0; i < len(list); i++ {
		fmt.Println(i+1, list[i])
	}
}

func print_result_points(list []Point, n int) {
	for i := 0; i < len(list); i++ {
		if i%(n-1) == 0 {
			fmt.Println(list[i])
		}
	}
}

func take_result_points(list []Point, n int) []Point {
	result := []Point{}
	for i := 0; i < len(list); i++ {
		if i%(n-1) == 0 {
			result = append(result, list[i])
		}
	}
	return result
}

// Input
func InputPoint(pointN int) Point {
	var px, py float64
	for {
		fmt.Printf("Enter coordinates for p%d.x and p%d.y separated by space: ", pointN, pointN)
		fmt.Scanf("%f %f\n", &px, &py)
		// _, err := fmt.Scanf(%f %f, &input)
		// if err != nil {
		// 	fmt.Println("Input error!", err)
		// 	continue
		// }

		// coordinates := strings.Fields(input)
		// if len(coordinates) != 2 {
		// 	fmt.Println("Invalid input. Please enter two coordinates separated by space.")
		// 	continue
		// }

		// px, err = strconv.ParseFloat(coordinates[0], 64)
		// if err != nil {
		// 	fmt.Println("Invalid input for x coordinate:", err)
		// 	continue
		// }

		// py, err = strconv.ParseFloat(coordinates[1], 64)
		// if err != nil {
		// 	fmt.Println("Invalid input for y coordinate:", err)
		// 	continue
		// }

		return Point{px, py}
	}
}

// func main() {
// 	fmt.Println("Beizer")
// 	beizer := []Point{Point{0, 0}, Point{4, 4}, Point{8, 0}}
// 	fmt.Println(beizer)
// 	start := time.Now()
// 	beizer = iterate(beizer)
// 	beizer = iterate(beizer)
// 	beizer = iterate(beizer)
// 	beizer = iterate(beizer)
// 	beizer = iterate(beizer)
// 	duration := time.Since(start)
// 	printList(beizer)
// 	fmt.Println("Program execution time:", duration)
// 	fmt.Println("General Beizer")
// 	fmt.Println("Hasil kuadratik")
// 	b := []Point{Point{0, 0}, Point{4, 4}, Point{8, 0}}
// 	printList(b)
// 	fmt.Println("Hasil generalisasi")
// 	b = general_iterate(3, 5, 0, b)
// 	printList(b)
// 	fmt.Println("Hasil generalisasi kubik")
// 	bb := []Point{Point{0, 0}, Point{2, 4}, Point{4, 2}, Point{8, 0}}
// 	bb = general_iterate(4, 4, 0, bb)
// 	printList(bb)
// 	// print_result_points(bb, 4)
// 	fmt.Println("result points:")
// 	hasil := take_result_points(bb, 4)
// 	printList(hasil)
// }
