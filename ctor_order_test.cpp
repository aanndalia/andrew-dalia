#include <iostream>

using namespace std;

class Base {
public:
	Base(){
		cout << "In base class constructor" << endl;
	}
	~Base(){
		cout << "In base class destructor" << endl;
	}
};

class Derived : public Base {
private:
	int x;
	int s;
public:
	Derived(){
		cout << "In Derived class constructor" << endl;
	}
	~Derived(){
		cout << "In Derived class destructor" << endl;
	}
};

int main(){
	//Derived d = Derived();

	Derived* nd = new Derived();
	cout << sizeof(*nd) << endl;
	//cout << sizeof(short) << endl;
	delete nd;
}