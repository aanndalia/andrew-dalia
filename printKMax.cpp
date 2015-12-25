#include <iostream>
#include <deque>
#include <cstdio>

using namespace std;

void printKMax(int arr[], int n, int k){
   //Write your code here.
   if(k > n){
      return;
   }

   //deque<int> d;
   int max = arr[0];
   int maxIndex = 0;
   for(int i = 1; i < k; i++){
      //d.push_back(arr[i]);
      if(arr[i] > max){
          maxIndex = i;
          max = arr[i]; 
      }
   }
   
   printf("%d ", max);
   for(int i = 1; i <= (n-k); i++){
      if(maxIndex == i-1){
          max = arr[i];
          maxIndex = i;
          for(int j=i+1; j<(i+k); j++){
            if(arr[j] > max){
               max = arr[j];
               maxIndex = j;
            }
          }
      }
      else if(arr[i+k-1] > max){
         max = arr[i+k-1];
         maxIndex = i+k-1;
      }
      printf("%d ", max);
   }
   printf("\n");
}

int main(){
  
   int t;
   cin >> t;
   while(t>0) {
      int n,k;
       cin >> n >> k;
       int i;
       int arr[n];
       for(i=0;i<n;i++)
            cin >> arr[i];
       printKMax(arr, n, k);
       t--;
     }
     return 0;
}
