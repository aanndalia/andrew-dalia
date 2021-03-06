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

	bst->insertVal(7);
	bst->printInorderTraversal(bst->getRoot());
	cout << endl;
	cout << "Finding 7: " << bst->findVal(7) << endl;
	cout << "Finding 5: " << bst->findVal(10) << endl;

	bst->removeVal(4);
	cout << "inorder traversal after removing key 4 " << endl;
	bst->printInorderTraversal(bst->getRoot());
	cout << endl;

	bst->removeVal(10);

	int lca1 = 12;
	int lca2 = 8;
	int ret = bst->leastCommonAncestor(lca1, lca2);
	cout << "LCA of " << lca1 << " and " << lca2 << " is " << ret << endl;

	bst->mirrorTree(bst->getRoot());
	cout << "Tree mirrored" << endl;
	bst->printBreadthFirst(bst->getRoot());

}
