#include <iostream>
#include <vector>
#include "bst.cpp"

using namespace std;

int main(){
	BST<int> *bst = new BST<int>(5);
	//bst->printInorderTravsersal(bst->getRoot());
	cout << endl;
	bst->insert(bst->getRoot(), 2);
	bst->insert(bst->getRoot(), 6);
	bst->insert(bst->getRoot(), 9);
	bst->insert(bst->getRoot(), 3);
	bst->insert(bst->getRoot(), 8);
	bst->insert(bst->getRoot(), 1);
	int vv[5] = { 12,43,4,11,21 };
	vector<int> v(&vv[0], &vv[0]+5);
	bst->buildTree(v);
	bst->printInorderTraversal(bst->getRoot());
	cout << endl;
	bst->printPreorderTraversal(bst->getRoot());
	cout << endl;
	bst->printPostorderTraversal(bst->getRoot());
	cout << endl;
	cout << bst->findItem(bst->getRoot(), 3) << endl;
	cout << bst->findItem(bst->getRoot(), 10) << endl;
	bst->printDepthFirst(bst->getRoot());
	bst->printBreadthFirst(bst->getRoot());
	//bst->prettyPrint(bst->getRoot());
	cout << "Root height: " << bst->nodeHeight(bst->getRoot()) << endl; 
	cout << "Root height: " << bst->nodeHeight(bst->getRoot()->left) << endl;
	cout << "Root height: " << bst->nodeHeight(bst->getRoot()->left->right) << endl;
	cout << "Root height: " << bst->nodeHeight(bst->getRoot()->right) << endl;

	cout << "isBalanced: " << bst->isBalanced(bst->getRoot()) << endl;
}
