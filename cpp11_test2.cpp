#include <iostream>
#include <thread>
#include <chrono>
#include <mutex>
#include <atomic>

//int count = 0;
//int numOps = 0;
std::atomic<int> count(0);
std::atomic<int> numOps(0);
const int maxNumOps = 100;
std::mutex m;

void producer(){
	std::this_thread::sleep_for(std::chrono::seconds(1));
	while(numOps < maxNumOps)
	{
		std::lock_guard<std::mutex> guard(m);
		count++;
		numOps++;
		//std::mutex m;
		//{
		//std::lock_guard<std::mutex> guard(m);
		std::cout << "Produced! Count: " << count << ", num ops: " << numOps << std::endl;
		//}
	}
}

void consumer(){
	std::this_thread::sleep_for(std::chrono::seconds(1));
	while(numOps < maxNumOps)
	{
		std::lock_guard<std::mutex> guard(m);
		//std::cout << "In consumer" << std::endl;
		count--;
		numOps++;
		//std::mutex m;
		//{
		//std::lock_guard<std::mutex> guard(m);
		std::cout << "Consumed! Count: " << count << ", num ops: " << numOps << std::endl;
		//}
	}
}

int main()
{
    auto lambda = [](auto x){ return x; };
    std::cout << lambda("Hello generic lambda!\n");
	std::cout << "Number of threads = " <<  std::thread::hardware_concurrency() << std::endl;
	std::thread t1(producer);
	std::thread t2(consumer);
	//std::this_thread::sleep_for(std::chrono::seconds(5));
	t1.join();
	t2.join();
    return 0;
}