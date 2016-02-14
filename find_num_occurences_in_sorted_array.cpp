#include <iostream>
#include <vector>

using namespace std;

int binarySearchIndexForKey(const vector<int> &nums, int key){
	int low = 0;
	int high = nums.size() - 1;
	while(high >= low){
		int midpoint = low + (high - low) / 2;
		if(nums[key] < nums[midpoint]){
			high = midpoint - 1;
		}
		else if(nums[key] > nums[midpoint]){
			low = midpoint + 1;
		}
		else {
			return midpoint;
		}
	}

	return -1;
}

int findFirstOccurence(const vector<int> &nums, int key){
	int low = 0;
	int high = nums.size() - 1;
	while(high >= low){
		int midpoint = low + (high - low) / 2;
		//cout << "midpoint: " << midpoint << endl;
		if(key < nums[midpoint]){
			high = midpoint - 1;
		}
		else if(key > nums[midpoint]){
			low = midpoint + 1;
		}
		else {
			if(nums[midpoint - 1] != key){
				return midpoint;
			}
	 
			high = midpoint - 1;
		}
	}

	return -1;
}

int findLastOccurence(const vector<int> &nums, int key){
	int low = 0;
	int high = nums.size() - 1;
	while(high >= low){
		int midpoint = low + (high - low) / 2;
		//cout << "midpoint: " << midpoint << endl;
		if(key < nums[midpoint]){
			high = midpoint - 1;
		}
		else if(key > nums[midpoint]){
			low = midpoint + 1;
		}
		else {
			if(nums[midpoint + 1] != key){
				return midpoint;
			}
	 
			low = midpoint + 1;
		}
	}

	return -1;
}

int countNumOccurences(const vector<int> &nums, int key){
	int firstIdx = findFirstOccurence(nums, key);
	int lastIdx = findLastOccurence(nums, key);
	if(firstIdx == -1)
		return -1;

	return lastIdx - firstIdx + 1;
}

int main()
{
	int arr[] =  { 1, 1, 1, 1, 2, 2, 3, 3, 3 };
	vector<int> nums(&arr[0], &arr[0]+9);
	int key = 1;
	int binSearchIdx = binarySearchIndexForKey(nums, key);
	cout << "binary search found index " << binSearchIdx << endl;
	int firstIdx = findFirstOccurence(nums, key);
	cout << "first occurrence of " << key << " is at index " << firstIdx << endl;
	int lastIdx = findLastOccurence(nums, key);
	cout << "last occurrence of " << key << " is at index " << lastIdx << endl;
	int numOccurences = countNumOccurences(nums, key);
	cout << "number of occurences of " << key << " is " << numOccurences << endl;
}