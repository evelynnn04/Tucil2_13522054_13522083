#include <chrono>
#include "Point.hpp"
using namespace std;

int main()
{
    Point a(0, 0);
    Point b(4, 4);
    Point c(8, 0);
    List bezier(2);
    bezier.insert(a);
    bezier.insert(b);
    bezier.insert(c);
    bezier.printList();
    auto start = std::chrono::high_resolution_clock::now();
    // for (int i = 0; i < 5; i++)
    // {
    //     bezier.iterate();
    //     // cout << i + 1 << " iterate" << endl;
    // }
    bezier.iterate();
    bezier.iterate();
    bezier.iterate();
    bezier.iterate();
    bezier.iterate();
    bezier.printList();
    bezier.iterate();
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    std::cout << "Time taken by function: " << duration.count() << " milliseconds" << std::endl;
}