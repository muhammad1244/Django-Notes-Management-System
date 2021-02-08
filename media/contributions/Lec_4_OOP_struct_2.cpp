#include<iostream>
using namespace std;


struct Date
{
	int day; 
	int month; 
	int year; 
};

struct Student
{
	string name; 
	string rollNo; 
	double cgpa; 
	Date dob; 
	int subjectCount; 
	string* subjects; 
};

void print(const Student &s)
{
	cout << "Name: " << s.name << endl; 
	cout << "Roll No." << s.rollNo << endl;
	cout << "CGPA: " << s.cgpa << endl;
	cout << "Date of Birth: " << s.dob.day << "/" << s.dob.month << "/" << s.dob.year << endl;
	cout << "Subjects:- " << endl;
	for (int i = 0; i < s.subjectCount; i++)
		cout << s.subjects[i] << endl;
}

int main()
{
	Student st;
	Student st2;
	Student* stPtr = &st2; 
	st.name = "Ahmed Shahzad";
	
	st.rollNo = "BITF16M003"; 
	st.cgpa = 3.22; 
	st.dob.day = 22;
	st.dob.month = 04; 
	st.dob.year = 2002;
	st.subjectCount = 5; 
	st.subjects = new string[5];
	for (int i = 0; i < 5; i++)
	{
		cout << "Enter your subjects: ";
		cin >> st.subjects[i];
	}
	print(st);
	delete []st.subjects;

	(*stPtr).name = "Asma";
	(*stPtr).rollNo = "BCSF16M025";
	stPtr->cgpa = 3.65; 
	stPtr->dob.day = 1; 
	stPtr->dob.month = 1; 
	stPtr->dob.year = 2000;
	stPtr->subjectCount = 3;
	stPtr->subjects = new string[3]; 
	for (int i = 0; i < 3; i++)
	{
		cout << "Enter your subjects: "; 
		cin >> stPtr->subjects[i]; 
	}
	print(st2);
	delete []stPtr->subjects;
	return 0;


}




