#include <iostream>

using namespace std;

const int N = 4;

void rotateMatrix(int arr[][N]){
	for(int layer = 0; layer < N / 2; layer++){
		int first = layer;
		int last = N-1-layer;
		for(int i = first; i < last; i++){
			int offset = i - first;

			// top
			int temp = arr[first][i];

			// top <- left
			arr[first][i] = arr[last - offset][first];

			// left <- bottom
			arr[last - offset][first] = arr[last][last - offset];

			// bottom <- right
			arr[last][last - offset] = arr[i][last];

			// right <- top
			arr[i][last] = temp;
			
		}
	}
}

void printMatrix(int arr[][N]){
	for(int i=0; i < N; i++){
		for(int j=0; j < N; j++){
			cout << arr[i][j] << " ";
		}
		cout << endl;
	}
}

int main(){
	int arr[][N] = {{11,12,13,14},{15,16,17,18},{19,20,21,22},{23,24,25,26}};
	printMatrix(arr);
	rotateMatrix(arr);
	cout << "\nafter" << endl;
	printMatrix(arr);
}