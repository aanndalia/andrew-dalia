#include <iostream>
#include <vector>
#include <iterator>

using namespace std;

void selectionSort(int arr[], int length){
	for(int i=0; i<length;i++){
		for(int j=i+1; j<length; j++){
			if(arr[j] < arr[i]){
				int temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	}
}

void insertionSort(int arr[], int length){
	for(int i=1; i<length; i++){
		int j = i;
		int temp = arr[i];
		while(j > 0 && arr[j-1] > temp){
			arr[j] = arr[j-1];
			j--;
		}
		arr[j] = temp;			
	}
}

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
void merge(vector<T> &vect, int left, int midpoint, int right)
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
void mergeSort(vector<T> &vect, int left, int right){
	if(right - left < 1){
		return;
	}
	
	int midpoint = (left + right) / 2;
	
	mergeSort(vect, left, midpoint);
	mergeSort(vect, midpoint + 1, right);
	
	merge(vect, left, midpoint, right);
	return;
}

template <class T>
void swap2(T& a, T& b){
	T temp = a;
	a = b;
	b = temp;
}

template <class T>
void quickSort(vector<T> &vect, int begin, int end){
	if(end - begin < 1){
		return;
	}
	
	int pivot = end;

	//printVector(vect, "before swapping");
	int swapIdx = begin;
	for(int i=begin; i < end; i++){
		if(vect[i] < vect[pivot]){
			swap2(vect[i], vect[swapIdx++]);
		}
	}

	swap2(vect[pivot], vect[swapIdx]);
	pivot = swapIdx;
	
	//printVector(vect, "after swapping");
	//cout << begin << " " << end << " " << pivot << " " << vect[pivot] << endl;

	quickSort(vect, begin, pivot - 1);
	quickSort(vect, pivot + 1, end);
	
	return;
}

int main() {
	int arr[] = {9,9,8,7,7,6,5,5,3,3,2};
	//int arr[] = {7,3,9,5,6,8,3,7,5,9,2};
	//int arr[] = {7,3,9,5,6};
	int length = sizeof arr / sizeof arr[0];
	vector<int> nums(&arr[0], &arr[0]+length);
	
	//selectionSort(arr, length);
	//insertionSort(arr, length);
	//mergeSort(nums, 0, nums.size() - 1);
	quickSort(nums, 0, nums.size() - 1);
	
	/*for(int i=0;i<length;i++){
		cout << arr[i] << " ";
	}
	cout << endl; */
	printVector(nums);
} 