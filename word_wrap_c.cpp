#include <cstring>
#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

char* wordWrap(char* buffer, char* str, int lineWidth) {
	printf("in wordWrap - original string: %s, length: %d\n", str, strlen(str));
	//printf("in wordWrap - length: %d\n", strlen(buffer));
	char* buf = new char[strlen(str) * 2];
	strncpy(buf, str, strlen(buf));
	return buf;
}

string wordWrapCpp(const string& str, int lineWidth){
	string result = "";
	int curWidth = 0;
	int beginBufIdx = 0;
	int lastSpace = -1;
	for(int i=0; i < str.length(); i++){
		if(str[i] == ' '){
			// is space
			lastSpace = i;
		}

		result += str[i];
		curWidth++;

		if(curWidth > lineWidth){
			int leftOverWidth = i - lastSpace;
			if(leftOverWidth > lineWidth){
				cout << "There is a word that exceeds the buffer width. How can this be and god be just?\n";
				return "N/A";
			}
			curWidth = leftOverWidth;
			result[lastSpace] = '\n';
		}
	}
	return result;
}

int main(){
	string str = "This is a block of standard text that should be word wrapped";
	char* cstr = const_cast<char*> (str.c_str());
	printf("original string: %s, length: %d\n", cstr, strlen(cstr));
	char* buffer = new char[strlen(cstr)*2];
	int width = 5;
	char* output = wordWrap(buffer, cstr, width);
	printf("%s\n", output);
	delete[] output;

	string test = "hello";
	test[2] = '\n';
	cout << test << "\n";

	string result = wordWrapCpp(str, width);
	cout << result << "\n";
}