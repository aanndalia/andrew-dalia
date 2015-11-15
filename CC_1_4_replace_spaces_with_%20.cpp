#include <iostream>

using namespace std;

void replaceSpacesWithPercent20(char str[], int trueLength){
	int numSpaces = 0;
	for(int i = 0; i < trueLength; i++){
		if(str[i] == ' '){
			numSpaces++;
		}
	}

	int newStringLength = trueLength + 2 * numSpaces;
	int arrIdx = newStringLength - 1;
	int j = trueLength - 1;
	while(arrIdx >= 0 && j >=0){
		if(str[j] == ' '){
			str[arrIdx--] = '0';
			str[arrIdx--] = '2';
			str[arrIdx--] = '%';
			j--;
		}
		else {
			str[arrIdx--] = str[j--];
		}
	}

}

int main(){
	char str[25] = "Hello I am Andrew.";
	cout << str << endl;
	replaceSpacesWithPercent20(str, 18);
	cout << str << endl;
}