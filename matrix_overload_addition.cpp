#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Matrix
{
public:
	vector<vector<int> > a;
	Matrix operator+(const Matrix &other){
		Matrix resultMatrix;
		for(int row = 0; row < a.size(); row++){
			vector<int> currentRow;
			for(int col = 0; col < a[0].size(); col++){
				//cout << row << " " << col << " " << (this->a)[row][col] << " " << other.a[row][col] << endl; 
				currentRow.push_back((this->a)[row][col] + (other.a)[row][col]);
			}
			resultMatrix.a.push_back(currentRow);
		}
		return resultMatrix;
	}	
};

int main () {
   int cases,k;
   cin >> cases;
   for(k=0;k<cases;k++) {
      Matrix x;
      Matrix y;
      Matrix result;
      int n,m,i,j;
      cin >> n >> m;
      for(i=0;i<n;i++) {
         vector<int> b;
         int num;
         for(j=0;j<m;j++) {
            cin >> num;
            b.push_back(num);
         }
         x.a.push_back(b);
      }
      for(i=0;i<n;i++) {
         vector<int> b;
         int num;
         for(j=0;j<m;j++) {
            cin >> num;
            b.push_back(num);
         }
         y.a.push_back(b);
      }
      result = x+y;
      for(i=0;i<n;i++) {
         for(j=0;j<m;j++) {
            cout << result.a[i][j] << " ";
         }
         cout << endl;
      }
   }  
   return 0;
}
