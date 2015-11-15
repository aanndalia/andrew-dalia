#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

template <class T>
void printVector(const vector<T> &vect)
{
	cout << "Print vector: ";
	for(int i=0; i < vect.size(); i++){
		cout << vect[i] << " ";
	}
	cout << endl;
}

template <class T>
vector<T> merge(const vector<T> &left, const vector<T> &right)
{
	vector<T> mergedVector(left.size() + right.size());
	
	int leftCursor = 0;
	int rightCursor = 0;
	int mergedCursor = 0;
	
	while(leftCursor < left.size() and rightCursor < right.size()){
		if(left[leftCursor] < right[rightCursor]){
			mergedVector[mergedCursor++] = left[leftCursor++];
		}
		else if(left[leftCursor] > right[rightCursor]){
			mergedVector[mergedCursor++] = right[rightCursor++];
		}
		else {
			mergedVector[mergedCursor++] = left[leftCursor++];
			mergedVector[mergedCursor++] = right[rightCursor++];
		}
	}
	
	while(leftCursor < left.size()){
		mergedVector[mergedCursor++] = left[leftCursor++];
	}
	
	while(rightCursor < right.size()){
		mergedVector[mergedCursor++] = right[rightCursor++];
	}
	
	return mergedVector;
}

template <class T>
void merge2(vector<T> &vect, int left, int midpoint, int right)
{
	vector<T> copyVect(vect.begin(), vect.end());
	
	int leftCursor = left;
	int rightCursor = midpoint + 1;
	int mergedCursor = left;
	
	while(leftCursor <= midpoint and rightCursor <= right){
		if(copyVect[leftCursor] < copyVect[rightCursor]){
			vect[mergedCursor++] = copyVect[leftCursor++];
		}
		else if(copyVect[leftCursor] > copyVect[rightCursor]){
			vect[mergedCursor++] = copyVect[rightCursor++];
		}
		else {
			vect[mergedCursor++] = copyVect[leftCursor++];
			vect[mergedCursor++] = copyVect[rightCursor++];
		}
	}
	
	while(leftCursor <= midpoint){
		vect[mergedCursor++] = copyVect[leftCursor++];
	}
	
	while(rightCursor <= right){
		vect[mergedCursor++] = copyVect[rightCursor++];
	}
}

template <class T>
void mergeSort2(vector<T> &vect, int left, int right){
	if(right - left < 1){
		return;
	}
	
	int midpoint = (left + right) / 2;
	
	mergeSort2(vect, left, midpoint);
	mergeSort2(vect, midpoint + 1, right);
	
	merge2(vect, left, midpoint, right);
	return;
}

template <class T>
vector<T> mergeSort(const vector<T> &vect){
	if(vect.size() < 2)
		return vect;
	
	int midpoint = vect.size() / 2;
	
	vector<T> leftVect(vect.begin(), vect.begin() + midpoint);
	vector<T> rightVect(vect.begin() + midpoint , vect.end());
	
	vector<T> sortedLeftVect = mergeSort(leftVect);
	vector<T> sortedRightVect = mergeSort(rightVect);
	
	return merge(sortedLeftVect, sortedRightVect);
}

int main()
{
	int arr[] = {7,3,9,5,6};
	vector<int> nums(&arr[0], &arr[0]+5);
	printVector(nums);
	//vector<int> sortedVector = mergeSort(nums, 0, nums.size() - 1);
	vector<int> sortedVector = mergeSort(nums);
	//printVector(nums);
	printVector(sortedVector);
	mergeSort2(nums, 0, nums.size() - 1);
	printVector(nums);
}