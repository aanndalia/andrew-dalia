#include <iostream>
#include <ctime>
#include <cstdlib>
#include <mutex>
#include <thread>

using namespace std;

mutex m;

class BankAccount
{
private:
	int id;
	double balance;
	
public:
	mutex bankMutex;

	BankAccount(int id, double initialBalance) : id(id), balance(initialBalance) {}
	
	void withdraw(double amount){
		// Locking within withdraw and deposit both will be thread safe (no deadlocks)
		//lock_guard<mutex> guard(bankMutex);
		balance -= amount;
	}

	void deposit(double amount){
		//lock_guard<mutex> guard(bankMutex);
		balance += amount;
	}

	inline double getBalance() const {
		return this->balance;
	}

	inline int getId() const {
		return this->id;
	}
};

void transfer(BankAccount& source, BankAccount& destination, double amount){
	// Locking a global mutex before doing operations will not result in deadlock
	//lock_guard<mutex> guard(m);
	//source.withdraw(amount);
	//destination.deposit(amount);
	
	// Wrapping the lock guard in scope so that it releases control between operations will not result in deadlock
	//{
	//lock_guard<mutex> guardSource(source.bankMutex);
	//source.withdraw(amount);
	//}
	//{
	//lock_guard<mutex> guardDestination(destination.bankMutex);
	//destination.deposit(amount);
	//}

	// Lock guarding without respect to order can result in deadlock since if they are obtained on 2 different threads 
	// in opposite order then there is a conflict
	lock_guard<mutex> guardSource(source.bankMutex);
	source.withdraw(amount);
	lock_guard<mutex> guardDestination(destination.bankMutex);
	destination.deposit(amount);

	/*
	// Ordering based on id and getting mutexes in the same order will resolve deadlock
	if(source.getId() < destination.getId()){
		lock_guard<mutex> guardSource(source.bankMutex);
		source.withdraw(amount);

		lock_guard<mutex> guardDestination(destination.bankMutex);
		destination.deposit(amount);
	}
	else{
		lock_guard<mutex> guardDestination(destination.bankMutex);
		destination.deposit(amount);

		lock_guard<mutex> guardSource(source.bankMutex);
		source.withdraw(amount);
	}
	*/
}

void doNTransfers(BankAccount& source, BankAccount& destination, int N, double amount){
	for(int i = 0; i < N; i++){
		transfer(source, destination, amount);
	}
}

int main()
{
	BankAccount ba1(111, 1000000.00);
	BankAccount ba2(222, 0.00);

	const int numTransfers = 100000;

	thread t1(doNTransfers, ref(ba1), ref(ba2), numTransfers, 3.00);
	thread t2(doNTransfers, ref(ba2), ref(ba1), numTransfers, 1.00);

	t1.join();
	t2.join();

	cout << "Bank account id " << ba1.getId() << " has balance " << ba1.getBalance() << endl;
	cout << "Bank account id " << ba2.getId() << " has balance " << ba2.getBalance() << endl;
}