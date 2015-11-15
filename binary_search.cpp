#include <iostream>
#include <vector>

using namespace std;

int binarySearch(int arr[], int targetValue, int length) {
	if(length < 1)
		return -1;
		
	if(length == 1){
		if(arr[0] == targetValue)
			return targetValue;
		else
			return -1;
	}
	
	int maxIdx = length - 1;
	int minIdx = 0;
	while(maxIdx >= minIdx){
		int midpoint = (maxIdx + minIdx) / 2;
		if(arr[midpoint] == targetValue)
			return arr[midpoint];
		else if(arr[midpoint] < targetValue){
			minIdx = midpoint + 1;
		}
		else {
			maxIdx = midpoint - 1;
		}
	}
	return -1;
}

int binarySearchVector(vector<int> nums, int targetValue) {
	int length = nums.size();
	if(length < 1)
		return -1;
		
	if(length == 1){
		if(nums[0] == targetValue)
			return targetValue;
		else
			return -1;
	}
	
	int maxIdx = length - 1;
	int minIdx = 0;
	while(maxIdx >= minIdx){
		int midpoint = (maxIdx + minIdx) / 2;
		if(nums[midpoint] == targetValue)
			return nums[midpoint];
		else if(nums[midpoint] < targetValue){
			minIdx = midpoint + 1;
		}
		else {
			maxIdx = midpoint - 1;
		}
	}
	return -1;
}

int binRecurse(vector<int> nums, int targetValue, int minIdx, int maxIdx)
{
	if(minIdx > maxIdx)
		return -1;
		
	int midpoint = (maxIdx + minIdx) / 2;
	
	if(nums[midpoint] == targetValue)
		return targetValue;
	else if(nums[midpoint] < targetValue)
		return binRecurse(nums, targetValue, midpoint + 1, maxIdx);
	else
		return binRecurse(nums, targetValue, minIdx, midpoint - 1);
}

int binarySearchVectorRecursive(vector<int> nums, int targetValue) {
	int length = nums.size();
	if(length < 1)
		return -1;
		
	if(length == 1){
		if(nums[0] == targetValue)
			return targetValue;
		else
			return -1;
	}
	
	int maxIdx = length - 1;
	int minIdx = 0;
	
	int ret = binRecurse(nums, targetValue, minIdx, maxIdx);
	return ret;
}

int main(){
	int arr[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};	
	int targetValue = 75;
	int binarySearchRet = binarySearch(arr, targetValue, 25);
	cout << "binarySearchRet: " << binarySearchRet << endl;
	
	std::vector<int> nums(arr, arr + sizeof arr / sizeof arr[0]);
	//vector<int> nums {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};	
	targetValue = 97;
	int binarySearchVectorRet = binarySearchVector(nums, targetValue);
	cout << "binarySearchVectorRet: " << binarySearchVectorRet << endl;
	
	int binarySearchVectorRecursiveRet = binarySearchVectorRecursive(nums, targetValue);
	cout << "binarySearchVectorRecursiveRet: " << binarySearchVectorRecursiveRet << endl;
}