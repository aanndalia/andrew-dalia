#include <iostream>
#include <vector>

using namespace std;

int fibonacci(int n){
	if(n <= 1){
		return 0;
	}

	if(n == 2){
		return 1;
	}

	int prev2 = 0;
	int prev1 = 1;
	for(int i=2; i<n; i++){
		int temp = prev2;
		prev2 = prev1;
		prev1 = prev1 + temp;
	}
	return prev1;
}

vector<int> genFibonacciToN(int n){
	vector<int> fibNums;
	for(int i=1; i <= n; i++){
		fibNums.push_back(fibonacci(i));
	}
	return fibNums;
} 

int main()
{
	int n = 6;
	cout << fibonacci(n) << endl;

	n = 10;
	vector<int> fibNums = genFibonacciToN(n);
	for(int i=0; i < n; i++){
		cout << fibNums[i] << " ";
	}
	cout << endl;
}