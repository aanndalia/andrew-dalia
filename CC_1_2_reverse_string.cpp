#include <iostream>

using namespace std;

void reverseString(char* str){
	int len = 0;
	//int j = 0;
	while(str[len] != '\0'){
		len++;
	}

	for(int i=0; i < len / 2; i++){
		char temp = str[i];
		str[i] = str[len-1-i];
		str[len-1-i] = temp;
	}
}

int main(){
	char str[] = "Latikah";
	reverseString(str);
	cout << str << endl;
}