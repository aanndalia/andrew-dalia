#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

class String
{
public:
	int length;
	char str[6];

	// constructor
	String(int len, char* str) : length(len){ 
		cout << "Constructing String " << len << " " << str << " " << sizeof(this->str) << endl; 
		strncpy(this->str, str, sizeof(this->str));
		cout << "this str " << this->str << endl; 
	}

	// copy constructor
	String(const String& fromStr){
		cout << "Copy constructing String " << endl;
		cout << this->str << endl; 
		cout << fromStr.str << endl;
		this->length = fromStr.length;
		strncpy(this->str, fromStr.str, sizeof(this->str));
	}

	// assignment operator
	String& operator=(const String& fromStr){
		cout << "Assignment operator String " << endl;
		if(this == &fromStr){
			return *this;
		}

		this->length = fromStr.length;
		strncpy(this->str, fromStr.str, sizeof(this->str));
		return *this;
	}
};

int main(){
	//string s = "hello";
	char str[] = "hello";
	String str1(6, str);
	String str2(str1);
	//String str3 = str1;

	cout << str1.length << " " << str1.str << endl;
	cout << str2.length << " " << str2.str << endl;
	//cout << str3.length << " " << str3.str << endl;
}