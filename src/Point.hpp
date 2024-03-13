#include <iostream>
using namespace std;

class Point
{
private:
    double x;
    double y;

public:
    Point()
    {
        this->x = 0;
        this->y = 0;
    }
    Point(double xx, double yy)
    {
        this->x = xx;
        this->y = yy;
    }
    ~Point() { ; }
    double get_value_x() { return x; }
    double get_value_y() { return y; }
    Point &operator=(const Point &p)
    {
        this->x = p.x;
        this->y = p.y;
        return *this;
    }
    void printPoint()
    {
        cout << "Point: (" << x << ", " << y << ")" << endl;
    }
    static Point midPoint(const Point &p1, const Point &p2)
    {
        double new_x = (p1.x + p2.x) / 2;
        double new_y = (p1.y + p2.y) / 2;
        return Point(new_x, new_y);
    }
};

class List
{
private:
    int size;
    Point *buffer;
    int Neff;

public:
    List()
    {
        size = 100;
        buffer = new Point[100];
        Neff = 0;
    }
    List(int ukuran)
    {
        size = ukuran;
        buffer = new Point[size];
        for (int i = 0; i < size; i++)
        {
            buffer[i] = Point();
        }
        Neff = 0;
    }
    ~List()
    {
        delete[] buffer;
    }

    Point get_value(int idx)
    {
        return buffer[idx];
    }

    int get_size()
    {
        return size;
    }

    int get_len()
    {
        return Neff;
    }

    void change_value(int idx, const Point &p)
    {
        buffer[idx] = p;
    }

    void extend()
    {
        Point *temp = new Point[size];
        for (int i = 0; i < size; i++)
        {
            temp[i] = buffer[i];
        }
        delete[] buffer;
        size *= 2;
        buffer = new Point[size];
        for (int i = 0; i < size; i++)
        {
            buffer[i] = temp[i];
        }
        delete[] temp;
    }

    void insert(Point p)
    {
        if (Neff == size)
        {
            extend();
        }

        // int idx = Neff; // Index to insert the new point

        // // Find the correct index to insert the new point while maintaining sorted order
        // while (idx > 0 && buffer[idx - 1].get_value_x() > p.get_value_x())
        // {
        //     buffer[idx] = buffer[idx - 1];
        //     idx--;
        // }

        buffer[Neff] = Point(p.get_value_x(), p.get_value_y());
        Neff++;
    }

    void concat(List &other)
    {
        if (size != 2 * Neff)
        {
            this->extend();
        }
        for (int i = Neff; i > 0; i--)
        {
            this->buffer[2 * i] = this->buffer[i];
            this->buffer[2 * i - 1] = other.buffer[i - 1];
        }
        Neff += Neff - 1;
    }

    void iterate()
    {
        List temp(Neff - 1);
        for (int i = 0; i < Neff - 1; i++)
        {
            Point tempE = Point::midPoint(buffer[i], buffer[i + 1]);
            temp.change_value(i, tempE);
        }
        for (int i = 0; i < Neff - 2; i++)
        {
            buffer[i + 1] = Point::midPoint(temp.buffer[i], temp.buffer[i + 1]);
        }
        concat(temp);
    }

    void printList()
    {
        for (int i = 0; i < Neff; i++)
        {
            cout << i << " ";
            buffer[i].printPoint();
        }
    }
};
