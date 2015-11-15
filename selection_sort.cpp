#include <iostream>
#include <vector>

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

int main() {
	int arr[] = {7,3,9,5,6,8,3,7,5,9,2};
	int length = sizeof arr / sizeof arr[0];
	//selectionSort(arr, length);
	insertionSort(arr, length);
	for(int i=0;i<length;i++){
		cout << arr[i] << " ";
	}
	cout << endl;
}