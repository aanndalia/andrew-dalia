#include <iostream>
#include <thread>
#include <mutex>
#include <chrono>

using namespace std;

mutex mutexA;
mutex mutexB;

void get_a_then_b(){
	lock_guard<mutex> guardA(mutexA);
	this_thread::sleep_for(chrono::seconds(1));
	lock_guard<mutex> guardB(mutexB);
}

void get_b_then_a(){
	lock_guard<mutex> guardB(mutexB);
	lock_guard<mutex> guardA(mutexA);
}

int main()
{
	thread t1(get_a_then_b);
	thread t2(get_b_then_a);
	t1.join();
	t2.join();
}