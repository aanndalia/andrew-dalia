#include <iostream>

int pow(int b, int e){
	if(b==0)
		return 0;
	if(e==0)
		return 1;
	if(b==1)
		return 1;
	if(e==1)
		return b;

	int halfPow = pow(b, e/2);

	if(e % 2 == 0)
		return halfPow*halfPow;
	else
		return halfPow*halfPow*b;
}

int atoi(const std::string& str){
	if(str=="")
		return 0;

	bool isNegative=(str[0]=='-');
	int length=str.length();
	int res=0;
	int begin=isNegative ? 1 : 0;
	int e=0;
	for(int i=length-1; i >= begin; --i){
		int digit=str[i]-'0';
		if(digit > 9 || digit < 0)
			return 0;

		res += digit*pow(10, e);
		e++;
	}

	//std::cout << length << "\n";
	res = isNegative ? -res : res;
	return res;
}

int main(){
	int res=atoi("1");
	std::cout << res << "\n";
	res=atoi("-1");
	std::cout << res << "\n";
	res=atoi("0");
	std::cout << res << "\n";
	res=atoi("13");
	std::cout << res << "\n";
	res=atoi("-13");
	std::cout << res << "\n";
	res=atoi("101");
	std::cout << res << "\n";
	res=atoi("97");
	std::cout << res << "\n";
}
