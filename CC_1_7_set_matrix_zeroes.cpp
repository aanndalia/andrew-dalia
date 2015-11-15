#include <iostream>
 
using namespace std;

const int M = 4;
const int N = 3;

void setMatrixZeroes(int arr[][N]){
	bool zeroRows[M] = {false};
	bool zeroCols[N] = {false};
	for(int i=0; i < M; i++){
		for(int j=0; j < N; j++){
			if(arr[i][j] == 0){
				zeroRows[i] = true;
				zeroCols[j] = true;
			}
		}
	}

	for(int i=0; i < M; i++){
		for(int j=0; j < N; j++){
			if(zeroRows[i] || zeroCols[j]){
				arr[i][j] = 0;
			}
		}
	}
}

void printMatrix(int arr[][N]){
	for(int i=0; i < M; i++){
		for(int j=0; j < N; j++){
			cout << arr[i][j] << " ";
		}
		cout << endl;
	}
}

int main(){
	int arr[][N] = {{11,0,13},{15,16,17},{19,0,21},{23,24,25}};
	printMatrix(arr);
	setMatrixZeroes(arr);
	cout << "\nafter" << endl;
	printMatrix(arr);
}