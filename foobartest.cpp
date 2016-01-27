template<class T>
class Foo{
	T t;
public:
	Foo(T t) : t(t){}
	Foo();
};

class Bar : public Foo<int>{

};

int main(){
	Bar b;
}