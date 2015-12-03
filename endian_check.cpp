#include <iostream>

using namespace std;

bool isLittleEndian(){
	// create unsigned int with value 1
	unsigned int i = 1;

	// cast address of int to char pointer which means only the first byte (lowest address) 
	// of i will be pointed to by c since an integer is 4 bytes and a char is 1 byte
	char* c = (char*) &i;

	// If *c is not 0, then it is little endian since the the lowest address byte is where the "1" is stored
	// If *c is 0, then it is big endian since the "1" must be stored at the byte with the highest address
	if(*c){
		return true;
	}
	else{
		return false;
	}
}

int main()
{
	cout << "is little endian: " << isLittleEndian() << endl;
}