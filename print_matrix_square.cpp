#include <iostream>
#include <vector>

using namespace std;

vector<vector<int> > populateSquareSpiral(const int n){
	int top = 0;
	int bottom = n - 1;
	int left = 0;
	int right = n - 1;
	//int** matrix = new int[n][n];
	vector<vector<int> > matrix;
	matrix.resize(n , vector<int>(n , 0));
	int count = 1;
	while(top <= bottom && left <= right){
		// top
		for(int i=left; i <= right; i++){
			matrix[top][i] = count++;
		}
		if(++top > bottom){
			break;
		}

		// right
		for(int i=top; i <= bottom; i++){
			matrix[i][right] = count++;
		}
		if(--right < left){
			break;
		}

		// bottom
		for(int i=right; i >= left; i--){
			matrix[bottom][i] = count++;
		}
		if(--bottom < top){
			break;
		}

		// left
		for(int i=bottom; i >= top; i--){
			matrix[i][left] = count++;
		}
		if(++left > right){
			break;
		}

	}
	return matrix;
}

void printSquareSpiral(vector<vector<int> > matrix, int n){
	cout << "\nPrinting square spiral...\n";
	for(int r = 0; r < n; r++){
		for(int c = 0; c < n; c++){
			cout << matrix[r][c] << " ";
		}
		cout << "\n";
	}
}

int main(){
	const int n = 5;
	vector<vector<int> > matrix = populateSquareSpiral(n);
	printSquareSpiral(matrix, n);
}