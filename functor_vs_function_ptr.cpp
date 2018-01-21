#include <iostream>

class MultiplierFunctor {
private:
	int multiplier;
public:
	MultiplierFunctor(int mult) : multiplier(mult){}
	int operator () (int multiplyBy){
		return this->multiplier * multiplyBy;
	}
};

int multiplier(int a, int b) {
	return a*b;
}

int divider(int a, int b) {
	return a/b;
}

int doOp(int a, int b, int (*op)(int, int)){
	return (*op)(a, b);
}

int main(){
	MultiplierFunctor multiplierFive(5);
	int res = multiplierFive(6);
	std::cout << res << "\n";
	res = multiplierFive(3);
	std::cout << res << "\n";

	MultiplierFunctor multiplierThree(3);
	res = multiplierThree(6);
	std::cout << res << "\n";
	res = multiplierThree(3);
	std::cout << res << "\n";

	res = doOp(6,3, &multiplier);
	std::cout << res << "\n";
	res = doOp(6,3, &divider);
	std::cout << res << "\n";
}
