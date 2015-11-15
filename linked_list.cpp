#include <iostream>
#include "linked_list.h"

using namespace std;

template<class T>
Node<T>::Node(T data){
	this->data = data;
	this->next = NULL;
}

template<class T>
Node<T> *Node<T>::nextNode(){
	return this->next;
}

template<class T>
void Node<T>::setNextNode(Node<T>* nextNode){
	this->next = nextNode;
}

template<class T>
T Node<T>::getData(){
	return this->data;
}

template<class T>
void Node<T>::setData(T data){
	this->data = data;
}

template<class T>
LinkedList<T>::LinkedList(Node<T>* head){
	this->head = head;
}

template<class T>
LinkedList<T>::LinkedList(T data){
	this->head = new Node<T>(data);
}

template<class T>
void LinkedList<T>::printList(){
	for(Node<T>* curr = head; curr != NULL; curr = curr->nextNode()){
		cout << curr->getData() << " ";
	}
	cout << endl;
}

template<class T>
void LinkedList<T>::appendItem(T data){
	Node<T> *newNode = new Node<T>(data);
	Node<T> *curr = head;
	while(curr->nextNode() != NULL){
		curr = curr->nextNode();
	}
	curr->setNextNode(newNode);
}

template<class T>
void LinkedList<T>::removeItem(T item){	
	while(head->getData() == item){
		Node<T>* headToDelete = head;
		head = head->nextNode();
		delete headToDelete;
	}
	
	Node<T> *curr = head;
	while(curr != NULL && curr->nextNode() != NULL){
		if(curr->nextNode()->getData() == item){
			Node<T>* nodeToDelete = curr->nextNode();
			curr->setNextNode(curr->nextNode()->nextNode());
			delete nodeToDelete;
		}
		curr = curr->nextNode();
	}
}

template<class T>
int LinkedList<T>::length(){
	int len = 0;
	for(Node<T>* curr = head; curr != NULL; curr = curr->nextNode()){
		len++;
	}
	return len;
}

template<class T>
bool LinkedList<T>::findItemAt(int pos, T& item){
	int index = 0;
	if(pos < 1){
		return false;
	}

	for(Node<T>* curr = head; curr != NULL; curr = curr->nextNode()){
		if(index == pos){
			item = curr->getData();
			return true;
		}
		index++;
	}
	return false;
}

template<class T>
void LinkedList<T>::removeItemAt(int pos){

}

template<class T>
void LinkedList<T>::addItemAt(int pos, T item){

}
