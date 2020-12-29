#include<iostream>
using namespace std;

int main()
{
	int a[5];
	int *p = a;
	cout<<"Enter elements: ";
	for(int i=0;i<5;i++)
	{
		cin>>a[i];
	}
	cout<<"You entered: ";
	for(int i=0;i<5;i++)
	{
		cout<<*p<<" ";
		p++;
	}
}
