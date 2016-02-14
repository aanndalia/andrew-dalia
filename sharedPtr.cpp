#include <iostream>

using namespace std;

template <class T>
class SharedPtr
{
private:
	int *referenceCount;
	T* ptr;
public:
	SharedPtr(T* rawPtr) : ptr(nullptr){
		referenceCount = new int(1);
		ptr = rawPtr;
		cout << "Initializing reference count in constructor to " << *referenceCount << endl;
	}

	SharedPtr(const SharedPtr& other){
		//cout << *referenceCount << endl;
		ptr = other.ptr;
		referenceCount = other.referenceCount;
		(*referenceCount)++;
		cout << "Incrementing reference count in copy constructor to " << *referenceCount << endl;
	}

	~SharedPtr(){
		(*referenceCount)--;
		cout << "Decremented reference count in destructor to " << *referenceCount << endl;
		if(*referenceCount < 1){
			cout << "Deleting resource at " << ptr << endl; 
			delete ptr;
			delete referenceCount;
		}
	}

	SharedPtr& operator= (const SharedPtr& other){
		if(&other == this){
			return *this;
		}

		(*referenceCount)--;
		ptr = other.ptr;
		referenceCount = other.referenceCount;
		(*referenceCount)++;
		cout << "reference count in assignment operator to " << *referenceCount << endl;

		return *this;
	}

	T operator*(){
		return *ptr;
	}

	T* operator->() {
		return ptr;
	}

	inline int getReferenceCount() const {
		return *referenceCount;
	}
};

class A
{
public:
	int x;
	explicit A(int x) : x(x) {}
};

int main()
{
	int* xPtr = new int(8);
	cout << "xPtr address is " << xPtr << endl;
	SharedPtr<int> xSptr(xPtr);
	SharedPtr<int> xSptr2(xSptr);
	SharedPtr<int> xSptr3 = xSptr2;
	xSptr3 = xSptr;
	cout << "Reference count in original is " << xSptr.getReferenceCount() << endl;
	cout << "Reference count in copy is " << xSptr2.getReferenceCount() << endl;
	cout << "Value of xSptr is " << *xSptr << " and xSptr2 is " << *xSptr2 << endl;

	A* aPtr = new A(4);
	cout << "aPtr address is " << aPtr << endl;
	SharedPtr<A> sharedA(aPtr);
	cout << "Reference count of a is " << sharedA.getReferenceCount() << endl;
	cout << "a->x is " << sharedA->x << endl;
}