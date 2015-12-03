#include <iostream>

using namespace std;

class Empty {

};

class A {
	char c;
};

class B {
	char c;
	char c2;
	int i;
};

class C {
	char c;
	char c2;
	//int i;
	char c3;
	char c4;
	char c5;
};

class D {
	int i1;
	int i2;
	char c1;
	char c2;
	char c3;
	char c4;
};

int main()
{
	Empty e;
	A a;
	B b;
	C c;
	D d;
	cout << sizeof(e) << endl;
	cout << sizeof(a) << endl;
	cout << sizeof(b) << endl;
	cout << sizeof(c) << endl;
	cout << sizeof(d) << endl;
}