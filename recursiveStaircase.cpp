#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int recursiveStaircase(int n){
    if(n<0){
        return 0;
    }
    
    if(n==0){
        return 1;
    }

    int s1=recursiveStaircase(n-1);
    int s2=recursiveStaircase(n-2);
    int s3=recursiveStaircase(n-3);
    
    return s1+s2+s3;
}

int recursiveStaircaseDp(int n, map<int, int>& cache){
    if(n<0){
        return 0;
    }
    
    if(n==0){
        return 1;
    }
    
    if(cache.find(n) != cache.end()){
        return cache[n];
    }

    int s1=recursiveStaircaseDp(n-1, cache);
    int s2=recursiveStaircaseDp(n-2, cache);
    int s3=recursiveStaircaseDp(n-3, cache);
    
    int res=s1+s2+s3;
    if(cache.find(n) == cache.end()){
        cache[n]=res;
    }
    
    return res;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int s;
    vector<int> ns;
    map<int, int> cache;
   
    cin >> s;
    for(int i=0; i<s; i++){
        int n;
        cin >> n;
        //cout << recursiveStaircase(n) << endl;
        cout << recursiveStaircaseDp(n, cache) << endl;
    }
    
    return 0;
}
