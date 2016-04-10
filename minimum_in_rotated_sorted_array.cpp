/* Find minimum in a rotated sorted array */
#include <iostream>
#include <vector>

using namespace std;

int findMin(vector<int>& nums) {
    if(!nums.size()){
        return 0;
    }
    
    int begin = 0;
	int end = nums.size() - 1;
	if(nums[begin] <= nums[end]){
		return nums[begin];
	}

	int lastIdx = begin;
	while(begin < end){
		int mid = begin + (end - begin) / 2;
		if(nums[mid] < nums[mid-1]){
			return nums[mid];
		}
		else if(nums[begin] <= nums[end]){
    		return nums[begin];
    	}
		else if(nums[mid] > nums[end]){
			begin = mid + 1;
			lastIdx = begin;
		}
		else if(nums[mid] < nums[begin]){
			end = mid - 1; 
			lastIdx = end;
		}
	}

	return nums[lastIdx];
}

int main(){
	int arr[] = {6,7,0,1,2,4,5};
	vector<int> vec (arr, arr + sizeof(arr) / sizeof(arr[0]) );
	int ret = findMinInRotatedSortedArray(vec);
	cout << "ret: " << ret << endl;
}