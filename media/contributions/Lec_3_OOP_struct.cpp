#include <iostream>
#include <string>
using namespace std;

struct Date 
{
	int dd;
	int mm; 
	int yyyy; 
};

bool isEqual(Date d1, Date d2)
{
	if (d1.dd == d2.dd && d1.mm == d2.mm && d1.yyyy == d2.yyyy)
		return true; 
	else 
		return false; 
}

Date getDate(Date d)
{
	d.dd=12;
	d.mm=01;
	d.yyyy=2000;
	return d;
}

int main()
{
	Date date[3];
	Date today; 
	today = getDate(today);

	for (int i=0; i<3; i++)
	{
		cout << "Enter Date day: "; 
		cin >> date[i].dd;
		while (date[i].dd > 31)
		{
			cout << "Invalid day please enter day again"<< endl;
			cin >>date[i].dd;
			}
	}
			return 0;}