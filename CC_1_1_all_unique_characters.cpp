#include <iostream>

using namespace std;

bool allCharactersUnique(const string& str){
	bool charSet[64] = {false};
	for(int i=0; i < str.length(); i++){
		if(charSet[str[i] - 'A'] == true){
			return false;
		}
		else {
			charSet[str[i] - 'A'] = true;
		}
	}
	return true;
}

int main(){
	string testStr = "avadacadavera";
	//testStr = "abc";
	//testStr = "AZ";
	//testStr = "ANDREA";
	cout << testStr << ": " << allCharactersUnique(testStr) << endl;
}