#include <iostream>
#include <vector>

using namespace std;

int findTargetInRotatedSortedArray(const vector<int>& nums, int target){
	if(!nums.size()){
		return -1;
	}

	int begin = 0;
	int end = nums.size() - 1;
	while(begin <= end){
		int mid = begin + (end - begin) / 2;
		cout << begin << " " << mid << " " << end << endl;
		if(nums[mid] == target){
			return mid;
		}
		else if(nums[mid] < target){
			// number in middle is less than target
			if(nums[mid] < nums[begin]){
				// right sorted -- not sure
				if(nums[end] < target)
					end = mid - 1;
				else
					begin = mid + 1;
			}
			else if(nums[mid] > nums[end]){
				// left sorted
				begin = mid + 1;
			}
			else{
				// sorted
				begin = mid + 1;
			}
		}
		else{
			// number in middle is greater than target
			if(nums[mid] < nums[begin]){
				// right sorted
				end = mid - 1;
			}
			else if(nums[mid] > nums[end]){
				// left sorted -- not sure
				if(nums[begin] > target){
					begin = mid + 1;
				}
				else{
					end = mid - 1;
				}
			}
			else{
				// sorted
				end = mid - 1;
			}
		}
	}

	return -1;
}

int main(){
	int arr[] = {6,7,0,1,2,4,5};
	int target = 5;
	vector<int> vec (arr, arr + sizeof(arr) / sizeof(arr[0]) );
	int ret = findTargetInRotatedSortedArray(vec, target);
	cout << "ret: " << ret << endl;
}