#include <iostream>
#include <string>

using namespace std;

const char* itoa(int number){
    string str = "";
    bool isNegative = false;
    
    if(number == 0){
        return "0";
    }
    
    if(number < 0){
        isNegative = true;
        number = -number;
    }
    
    int newNumber = number;
    while(newNumber > 0){
        int digit = newNumber % 10;
        newNumber /= 10;
        char newChar =  '0' + digit;
        str = newChar + str;
    }
    
    if(isNegative){
        str = "-" + str;
	}
	
	return str.c_str();
}
 
 