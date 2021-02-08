#include <iostream>
using namespace std;

struct date
{
    int day;
    int month;
    int year;
};

bool is_same(date d1, date d2)
{
    if (d1.day==d2.day && d1.month==d2.month && d1.year==d2.year)
        return true;
    else
        return false;
}

int main()
{
    date t1={11, 12, 2001};
    date t2={111, 12, 2001};
    if (is_same(t1, t2))
        cout << "\n Both dates are same! ";
    else
        cout << "\n Date are different! ";
    
    return 0;
}
