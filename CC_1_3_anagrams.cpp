#include <iostream>

using namespace std;

bool areAnagrams(const string& str1, const string& str2){
	if(str1.length() != str2.length()){
		return false;
	}

	const int BUCKETS = 64;
	bool charCount1[BUCKETS] = {0};
	bool charCount2[BUCKETS] = {0};

	for(int i = 0; i < str1.length(); i++){
		charCount1[str1[i] - 'A'] += 1;
		charCount2[str2[i] - 'A'] += 1;
	}

	for(int k = 0; k < BUCKETS; k++){
		//cout << k << " " << charCount1[k] << " " << charCount2[k] << endl;
	    if(charCount1[k] != charCount2[k]){
	        return false;
	    }
	}

	return true;
}

int main(){
	string str1 = "evil";
	string str2 = "live";
	cout << areAnagrams(str1, str2) << endl;
}