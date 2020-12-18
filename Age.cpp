#include<iostream>
using namespace std;

int main()
{
	int age;char check[10];
	cout<<"Enter your age: ";//Asking user to enter his/her age 
	cin>>age;
	(age>=18)?cout<<"You are Eligible":cout<<"You are Not Eligible"; //Checking whether the person is eligible using ternary operator
	return 0;
}
