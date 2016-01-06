#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
#include <set>
//#include <pair>
using namespace std;

/*
void clearMatrix(vector< vector<int> >& matrix){
    d
}*/

void printMatrix(vector< vector<int> > matrix, int rows, int cols){
    for(int r = 0; r < rows; r++){
        for(int c = 0; c < cols; c++){
            cout << matrix[r][c] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

int calculateComponentSize(vector< vector<int> >& matrix, int row, int col){
    int rows = matrix.size();
    int cols = matrix[0].size();
    int componentSize = 0;
    stack< pair<int, int> > s;
    set< pair<int, int> > visited;
    //int hash = row * rows + col;
    s.push(pair<int,int>(row, col));
    visited.insert(pair<int,int>(row, col));
    
    /*int visited[rows][cols];
    for(int i = 0; i < rows; i++)
        for(int j = 0; j < cols; j++)
            visited[i][j] = 0;*/
        
    while(!s.empty()){
        pair<int, int> cellPair = s.top();
        s.pop();
        componentSize++;
        int curRow = cellPair.first;
        int curCol = cellPair.second;
        matrix[curRow][curCol] = 2;
        for(int r = curRow - 1; r <= curRow + 1; r++){
            for(int c = curCol - 1; c <= curCol + 1; c++){
                if(r >= 0 && c >= 0 && r < rows && c < cols && matrix[r][c] == 1){
                    //cout << "found unvisited pair " << r << " " << c << endl;
                    //hash = r * rows + c;
                    //cout << "found unvisited pair " << r << " " << c  << endl;
                    if(visited.find(pair<int, int>(r, c)) == visited.end()){
                        //cout << "pushing pair " << r << " " << c << endl;
                        s.push(pair<int, int>(r, c));
                        visited.insert(pair<int, int>(r, c));
                    }
                }
            }
        }
    }
    
    //cout << "after component size " << componentSize << endl;
    //printMatrix(matrix, rows, cols);
    return componentSize;
}

int largestConnection(vector< vector<int> > matrix){
    if(matrix.size() == 0){
        return 0;
    }
    
    const int EMPTY = 0;
    
    int rows = matrix.size();
    int cols = matrix[0].size();
    int startingRow, startingCol;
    int largestComponent = 0;
    
    //cout << "initial" << endl;
    //printMatrix(matrix, rows, cols);
    
    for(int r = 0; r < rows; r++){
        for(int c = 0; c < cols; c++){
            if(matrix[r][c] == 1){
                int compSize = calculateComponentSize(matrix, r, c);
                if(compSize > largestComponent){
                    largestComponent = compSize;
                }
            }
        }
    }
    
    return largestComponent;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int rows;
    int cols;
    cin >> rows;
    cin >> cols;
    vector< vector<int> > matrix;
    for(int r=0; r < rows; r++){
        vector<int> curRow;
        int temp;
        for(int c=0; c < cols; c++){
            cin >> temp;
            curRow.push_back(temp);
        }
        matrix.push_back(curRow);
    }
    
    cout << largestConnection(matrix) << endl;
    
    return 0;
}
