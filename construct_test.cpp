#include <iostream>

using namespace std;

class ConstructTest
{
public:
	int a;
	int *iPtr;
	ConstructTest(int a, int i) : a(a){
		cout << "Constructor" << endl;
		iPtr = new int(i);
		this->printVals("in Constructor");
	}
	ConstructTest(const ConstructTest& other){
		cout << "copy constructor" << endl;
		this->a = other.a;
		this->iPtr = new int;
		memcpy(this->iPtr, other.iPtr, sizeof(int));
	}
	ConstructTest& operator=(const ConstructTest& rhs){
		cout << "assignment operator" << endl;
		if(this == &rhs){
			return *this;
		}
		this->a = rhs.a;
		this->iPtr = new int;
		memcpy(this->iPtr, rhs.iPtr, sizeof(int));
		return *this;
	}
	void printVals(const string& name){
		cout << name << endl;
		cout << "a: " << a << endl;
		cout << "iPtr: " << iPtr << endl;
		cout << "*iPtr: " << *iPtr << endl;
		cout << endl;
 	}
 	
};

int main(){
	ConstructTest c(9, 7);
	c.printVals("c");
	ConstructTest cCopy(c);
	cCopy.printVals("cCopy");
	c.printVals("c");
	ConstructTest cAssigned(8, 10);
	cAssigned.printVals("cAssigned before assignment");
	cAssigned = c;
	cAssigned.printVals("cAssigned after assignment");
	c.printVals("c");
}