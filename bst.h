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
	Node<T>** traverseTo(Node<T>** startNode, T val);
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
	bool insertVal(T val);
	bool findVal(T val);
	bool removeVal(T val);
	T leastCommonAncestor(T val1, T val2);
	bool findPath(Node<T>* startNode, T val, vector<T>& path);
};