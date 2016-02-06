#include <iostream>
#include <thread>
#include <mutex>

using namespace std;

class B;

class A
{
public:
	mutex aMutex;
	//B bObj;
	A() {}
	//A(B& b) : bObj(b) {}
	/*void setB(B& b){
		bObj = b;
	}*/
	void getMutexB(B& b){
		lock_guard<mutex> guard(aMutex);
		lock_guard<mutex> guardB(b.bMutex);
	}
};

class B
{
public:
	mutex bMutex;
	//A aObj;
	//B(A& a) : aObj(a) {}
	B() {}
	void getMutexA(A& a){
		lock_guard<mutex> guard(bMutex);
		lock_guard<mutex> guardA(a.aMutex);
	}
};

int main()
{
	A a;
	B b;
	/*thread tA(a.getMutexB, b);
	thread tB(b.getMutexA, a);
	tA.join();
	tB.join();*/
}