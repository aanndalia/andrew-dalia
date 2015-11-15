#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

template <class T>
void printVector(const vector<T> &vect, const string& message = "")
{
	cout << message << ": ";
	for(int i=0; i < vect.size(); i++){
		cout << vect[i] << " ";
	}
	cout << endl;
}

template <class T>
void swap2(T& a, T& b){
	T temp = a;
	a = b;
	b = temp;
}

template <class T>
vector<T> quickSort(vector<T> &vect){
	if(vect.size() < 2){
		return vect;
	}

	T first = vect[0];
	T midpoint = vect[vect.size() / 2];
	T last = vect[vect.size()];
	
	T partition = midpoint;
	
	if((first <= midpoint && first >= last) || (first <= last && first >= midpoint)){
		partition = first;
	}
	else if((last <= first && last >= midpoint) || (last <= midpoint && last >= first)){
		partition = last;
	}
	
	vector<T> lesser;
	vector<T> equal;
	vector<T> greater;
	for(int i=0; i < vect.size(); i++){
		if(vect[i] < partition){
			lesser.push_back(vect[i]);
		}
		else if(vect[i] > partition){
			greater.push_back(vect[i]);
		}
		else{
			equal.push_back(vect[i]);
		}
	}
	
	vector<T> lesserSorted = quickSort(lesser);
	vector<T> greaterSorted = quickSort(greater);
	
	vector<T> combinedSortedVect;
	combinedSortedVect.reserve( lesserSorted.size() + greaterSorted.size() + equal.size() ); // preallocate memory
	combinedSortedVect.insert( combinedSortedVect.end(), lesserSorted.begin(), lesserSorted.end() );
	combinedSortedVect.insert( combinedSortedVect.end(), equal.begin(), equal.end() );
	combinedSortedVect.insert( combinedSortedVect.end(), greaterSorted.begin(), greaterSorted.end() );
	
	return combinedSortedVect;
}

template <class T>
void quickSort2(vector<T> &vect, int begin, int end){
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

	quickSort2(vect, begin, pivot - 1);
	quickSort2(vect, pivot + 1, end);
	
	return;
}

int main()
{
	//int arr[] = {7,3,9,5,6};
	int arr[] = {7,3,9,5,6,8,3,7,5,9,2};
	vector<int> nums(&arr[0], &arr[0]+11);
	printVector(nums, "original vector");
	//vector<int> sortedVector = mergeSort(nums, 0, nums.size() - 1);
	vector<int> sortedVector = quickSort(nums);
	printVector(sortedVector, "final result-with copies");
	
	quickSort2(nums, 0, nums.size() - 1);
	//mergeSort2(nums, 0, nums.size() - 1);
	printVector(nums, "final result in-place   ");
}