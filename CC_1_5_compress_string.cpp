#include <iostream>
#include <sstream>

using namespace std;

template <typename T>
string numberToString ( T num ) {
	ostringstream ss;
	ss << num;
	return ss.str();
}

string compressedString(const string& str){
	if(str.length() < 2){
		return str;
	}

	string compressedStr = "";
	char prevChar = str[0];
	int currentCharCount = 1;
	for(int i = 1; i < str.length(); i++){
        if(str[i] == prevChar){
        	currentCharCount++;
        }
        else{
        	compressedStr += prevChar;
        	string numCount = numberToString(currentCharCount);
        	compressedStr += numCount;
        	prevChar = str[i];
        	currentCharCount = 1;
        	if(compressedStr.length() > str.length()){
        		return str;
        	}
        }
        //cout << compressedStr << endl;
	}

	compressedStr += prevChar;
	compressedStr += numberToString(currentCharCount);
	if(compressedStr.length() > str.length()){
		return str;
	}

	return compressedStr;
}

int main(){
	//string str = "aabcccccaaa";
	string str = "abccde";
	string compressedStr = compressedString(str);
	cout << str << " -> " << compressedStr << endl;
}