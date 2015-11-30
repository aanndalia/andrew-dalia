#include <iostream>
#include <vector>

using namespace std;

template<class T>
struct Node
{
	Node(T data);
	T data;
	Node<T> *left;
	Node<T> *right;
};

template<class T>
class BST
{
private:
	Node<T> *root;
public:
	BST();
	BST(T rootVal);
	Node<T>* getRoot();
	void printInorderTraversal(Node<T>* root);
	void printPreorderTraversal(Node<T>* root);
	void printPostorderTraversal(Node<T>* root);
	void insert(Node<T>* root, T data);
	void buildTree(vector<T> items);
	bool findItem(Node<T>* root, T item);
	void printBreadthFirst(Node<T> *root);
	void printDepthFirst(Node<T> *root);
	void prettyPrint(Node<T>* p, int indent=0);
	int nodeHeight(Node<T>* root);
	bool isBalanced(Node<T>* root);
	void mirrorTree(Node<T> *root);
};