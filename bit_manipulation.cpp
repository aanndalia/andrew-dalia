#include <iostream>

using namespace std;

int setBit(int n, int bit){
    int nSet = n | (1 << bit);
    return nSet;
}
bool getBit(int n, int bit){
    if((n & (1 << bit)) != 0)
        return true;
    return false;
}
int clearBit(int n, int bit){
    int nCleared = n & ~(1 << bit);
    return nCleared;
}
int toggleBit(int n, int bit){
    if(getBit(n, bit) == true)
        return clearBit(n, bit);
    return setBit(n, bit);
}
int reverseBits(int n) {
    int bits = sizeof(n) * 8;
    int reversed = 0;
    for(int i=0; i < bits; i++){
        int complement = bits - 1 - i;
        if(getBit(n, i)){
            reversed = setBit(reversed, complement);
        }
    }
    return reversed;
}

int main(){
	cout << sizeof(int) << endl;

	int test = 43261596;
	int testReversed = reverseBits(test);
	cout << test << " bit reversed is " << testReversed << endl;
}