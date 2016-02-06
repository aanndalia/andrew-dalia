#include <iostream>
#include <thread>
#include <mutex>
#include <ctime>
#include <cstdlib>
#include <atomic>

using namespace std;

mutex m;
//int counter = 0;
atomic_int counter(0);

void countToN(int n){
	int i = 0;
	while(i < n){
		i++;
		//lock_guard<mutex> guard(m);
		counter++;
	}
}

int main()
{
	const int N = 100000;
	clock_t startTime = clock(); //Start timer
	thread t1(countToN, N);
	thread t2(countToN, N);
	t1.join();
	t2.join();
	double secondsPassed = (clock() - startTime) / (double) CLOCKS_PER_SEC;
	cout << "Number of threads = " <<  std::thread::hardware_concurrency() << endl;
	cout << "counter: " << counter << endl;
	cout << "time elapsed: " << secondsPassed << endl;
}