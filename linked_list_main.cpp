#include <iostream>
//#include "linked_list.h"
#include "linked_list.cpp"

using namespace std;

int main(){
	Node<int> *node1 = new Node<int>(3);
	int node1Data = node1->getData();
	cout << node1Data << endl;

	Node<int> *headNode = new Node<int>(1);
	LinkedList<int> list = LinkedList<int>(headNode);
	list.appendItem(2);
	list.appendItem(4);
	list.printList();
	cout << list.length() << endl;
	list.removeItem(4);
	list.printList();
	cout << "DONE" << endl;
}