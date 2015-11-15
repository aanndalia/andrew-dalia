#include <iostream>

using namespace std;

bool isSubString(const string& str, const string& checkSubStr){
	//bool startingLetter[] = new bool[str.length()];
	for(int i=0; i <= (str.length() - checkSubStr.length()); i++){
		if(str[i] == checkSubStr[0]){
			for(int j=1; j < checkSubStr.length(); j++){
				if(checkSubStr[j] != str[i+j]){
					break;
				}
				else if((j == checkSubStr.length() - 1) && checkSubStr[j] == str[i+j]){
					return true;
				}
			}
		}
	}
	return false;
}

bool rotatedWord(const string& word, const string& target){
	if(word.length() != target.length()){
		return false;
	}

	string doubleWord = target + target;
	bool subStr = isSubString(doubleWord, word);
	return subStr;
}

int main(){
	string word = "erbottleswat";
	string target = "waterbottles";
	bool ret = rotatedWord(word, target);
	cout << ret << endl;
}