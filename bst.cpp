#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <stack>
#include "bst.h"

using namespace std;

template<class T>
Node<T>::Node(T val) : left(NULL), right(NULL), data(val) {

}

template<class T>
BST<T>::BST() : root(NULL) {

}

template<class T>
BST<T>::BST(T rootVal) : root(new Node<T>(rootVal)) {

}

template<class T>
Node<T>* BST<T>::getRoot(){
	return this->root;
}

template<class T>
void BST<T>::printInorderTraversal(Node<T>* root){
	if(root == NULL){
		return;
	}

	printInorderTraversal(root->left);
	cout << root->data << " ";
	printInorderTraversal(root->right);
}

template<class T>
void BST<T>::printPreorderTraversal(Node<T>* root){
	if(root == NULL){
		return;
	}

	cout << root->data << " ";
	printPreorderTraversal(root->left);
	printPreorderTraversal(root->right);
}

template<class T>
void BST<T>::printPostorderTraversal(Node<T>* root){
	if(root == NULL){
		return;
	}

	printPostorderTraversal(root->left);
	printPostorderTraversal(root->right);
	cout << root->data << " ";
}

template<class T>
void BST<T>::insert(Node<T>* root, T item){
	if(root == NULL){
		root = new Node<T>(item);
		return;
	}

	if(item < root->data){
		if(root->left == NULL){
			root->left = new Node<T>(item);
		}
		else {
			insert(root->left, item);
		}
	}
	else if(item > root->data){
		if(root->right == NULL){
			root->right = new Node<T>(item);
		}
		else {
			insert(root->right, item);
		}
	}
	else {
		cout << "Item is already in BST" << endl;
		return;
	}
}

template<class T>
void BST<T>::buildTree(vector<T> items){
	for(int i=0; i < items.size(); i++){
		this->insert(this->root, items[i]);
	}
}

template<class T>
bool BST<T>::findItem(Node<T>* root, T item){
	if(root == NULL){
		return false;
	}

	if(root->data == item){
		return true;
	}

	if(findItem(root->left, item) || findItem(root->right, item)){
		return true;
	}
	else {
		return false;
	}
}

template<class T>
void BST<T>::printBreadthFirst(Node<T> *root){
	if(root == NULL){
		return;
	}

	cout << "BFS: ";
	queue<Node<T>*> q;
	q.push(root);
	while(!q.empty()){
		Node<T> *poppedNode = q.front();
		cout << poppedNode->data << " ";
		q.pop();
		if(poppedNode->left)
			q.push(poppedNode->left);
		if(poppedNode->right)
			q.push(poppedNode->right);
	}

	cout << endl;
}

template<class T>
void BST<T>::printDepthFirst(Node<T> *root){
	if(root == NULL){
		return;
	}

	cout << "DFS: ";
	stack<Node<T>*> s;
	s.push(root);
	while(!s.empty()){
		Node<T> *poppedNode = s.top();
		cout << poppedNode->data << " ";
		s.pop();
		if(poppedNode->right)
			s.push(poppedNode->right);
		if(poppedNode->left)
			s.push(poppedNode->left);
	}

	cout << endl;
}

template<class T>
void BST<T>::prettyPrint(Node<T>* p, int indent)
{
    if(p != NULL) {
        if(p->left) prettyPrint(p->left, indent+4);
        if(p->right) prettyPrint(p->right, indent+4);
        if (indent) {
            std::cout << std::setw(indent) << ' ';
        }
        cout<< p->data << "\n ";
    }
}

template<class T>
int BST<T>::nodeHeight(Node<T>* root){
	if(root == NULL){
		return 0;
	}

	int leftHeight = nodeHeight(root->left);
	int rightHeight = nodeHeight(root->right);

	if(rightHeight > leftHeight){
		return rightHeight + 1;
	}
	else {
		return leftHeight + 1;
	}
}

template<class T>
Node<T>** BST<T>::traverseTo(Node<T>** startNode, T val){
	if(*startNode == NULL){
		return startNode;
	}

	//cout << "traversing node " << (*startNode)->data << ", looking for val " << val << endl;
	if((*startNode)->data == val){
		return startNode;
	}

	if(val < (*startNode)->data){
		return traverseTo(&((*startNode)->left), val);
	}
	else{
		return traverseTo(&((*startNode)->right), val);
	}
}

template<class T>
bool BST<T>::insertVal(T val){
	/*if(root == NULL){
		root = new Node<T>(val);
		return true;
	}
	*/
	Node<T>** insertPtr = traverseTo(&root, val);
	if(*insertPtr == NULL){
		*insertPtr = new Node<T>(val);
		return true;
	}
	else {
		cout << "Key " << val << " already found in BST" << endl;
		return false;
	}
}

template<class T>
bool BST<T>::findVal(T val){
	/*if(root == NULL){
		return false;
	}
	*/
	Node<T>** findPtr = traverseTo(&root, val);
	if(*findPtr == NULL){
		cout << "Key " << val << " not found in BST" << endl;
		return false;
	}
	else {
		return true;
	}
}

template<class T>
bool BST<T>::removeVal(T val){
	/*if(root == NULL){
		return false;
	}
	*/
	Node<T>** removePtr = traverseTo(&root, val);
	if(*removePtr == NULL){
		cout << "Key " << val << " not found in BST" << endl;
		return false;
	}
	else {
		cout << "Deleting key " << (*removePtr)->data << endl;
		delete *removePtr;
		*removePtr = NULL;
		return true;
	}
}

template<class T>
bool BST<T>::isBalanced(Node<T>* root){
	if(root == NULL){
		return true;
	}

	if(!isBalanced(root->left) || !isBalanced(root->right))
		return false;

	int leftHeight = nodeHeight(root->left);
	int rightHeight = nodeHeight(root->right);

	if((rightHeight - leftHeight > 1) || (rightHeight - leftHeight < -1)){
		return false;
	}
	else{
		return true;
	}
}

template<class T>
void BST<T>::mirrorTree(Node<T> *root){
	if(root == NULL)
		return;

	Node<T>* temp = root->left;
	root->left = root->right;
	root->right = temp;

	mirrorTree(root->left);
	mirrorTree(root->right);
}

template<class T>
T BST<T>::leastCommonAncestor(T val1, T val2){
	if(root == NULL){
		return 0;
	}

	vector<T> path1;
	vector<T> path2;
	bool ret1 = findPath(root, val1, path1);
	bool ret2 = findPath(root, val2, path2);

	/*
	cout << "ret1 " << ret1 << ", ret2 " << ret2 << endl;
	cout << "path1: ";
	for(int i=0; i < path1.size(); i++){
		cout << path1[i] << " ";
	}
	cout << endl;

	cout << "path2: ";
	for(int i=0; i < path2.size(); i++){
		cout << path2[i] << " ";
	}
	cout << endl;*/

	if(ret1 && ret2){
		int i = 0;
		while(i < path1.size() && i < path2.size()){
			if(path1[i] != path2[i]){
				return path1[i-1];
			}
			i++;
		}
		return path1[i-1];
	}

	return 0;
}

template<class T>
bool BST<T>::findPath(Node<T>* startNode, T val, vector<T>& path){
	if(startNode == NULL){
		//path.clear();
		return false;
	}

	path.push_back(startNode->data);

	if(startNode->data == val){
		return true;
	}

	if(findPath(startNode->left, val, path) || findPath(startNode->right, val, path)){
		return true;
	}

	path.pop_back();
	return false;
}