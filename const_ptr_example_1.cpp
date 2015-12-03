#include <iostream>

using namespace std;

void f(const int* p1, int* p2)
{
  int i = *p1;         // Get the (original) value of *p1
  *p2 = 7;             // If p1 == p2, this will also change *p1
  int j = *p1;         // Get the (possibly new) value of *p1

  cout << p1 << " " << p2 << " " << *p1 << " " << *p2 << " " << i << " " << j << endl;

  if (i != j) {
    std::cout << "*p1 changed, but it didn't change via pointer p1!\n";
    //assert(p1 == p2);  // This is the only way *p1 could be different
  }
}

int main()
{
  int x = 5;
  f(&x, &x);           // This is perfectly legal (and even moral!)
  // ...
}