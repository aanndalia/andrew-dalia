#include <iostream>
 
using namespace std;

class AddValFunctor 
{
private:
	int val;
public:
	AddValFunctor(int v){
		this->val = v;
	}
	int operator() (int adder){
		return adder + this->val;
	}
};

int main(){
	AddValFunctor add42 = AddValFunctor(42);
	AddValFunctor add7 = AddValFunctor(7);
	cout << add42(5) << endl;
	cout << add7(9) << endl;
}