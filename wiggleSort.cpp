#include <iostream>
#include <vector>

using namespace std;

void wiggleSort(vector<int>& nums) {
    if(nums.size() < 2)
        return;
        
    for(int i=0; i < nums.size() - 1; i++){
        if(i % 2){
            //odd
            if(nums[i] < nums[i+1]){
                int temp = nums[i];
                nums[i] = nums[i+1];
                nums[i+1] = temp;
            }
        }
        else {
            //odd
            if(nums[i] > nums[i+1]){
                int temp = nums[i];
                nums[i] = nums[i+1];
                nums[i+1] = temp;
            }
        }
    }
}

int main(){
	//vector<int> v;
	//int arr[] = {1, 5, 1, 1, 6, 4};
	int arr[] = {1, 3, 2, 2, 3, 1};
	int arrLen = sizeof(arr) / sizeof(arr[0]);
	vector<int> v(&arr[0], &arr[0]+arrLen);
	wiggleSort(v);

	for(int i=0; i < arrLen; i++){
		cout << v[i] << " ";
	}
	cout << endl;
}