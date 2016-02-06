#include <iostream>
#include <array>
#include <memory>
#include <thread>

using namespace std;

void fn(){
	for(int i=0; i < 20; i++){
		cout << "count: " << i << endl;
	}
}

int main
{
	//std::array<int, 3> arr = {2, 3, 5};
	std::thread t1(fn);
	//t1.
}