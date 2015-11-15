#include <iostream>

using namespace std;

template<class T>
class Node
{
private:
	T data;
	Node<T> *next;
public:
	Node(T data);
	Node<T> *nextNode();
	void setNextNode(Node<T> *nextNode);
	T getData();
	void setData(T data);
};

template<class T>
class LinkedList
{
private:
	Node<T> *head;
public:
	LinkedList(Node<T>* head);
	LinkedList(T data);
	void printList();
	void appendItem(T data);
	void removeItem(T item);
	int length();
	bool findItemAt(int pos, T& item);
	bool removeItemAt(int pos);
	bool addItemAt(int pos, T item);
};