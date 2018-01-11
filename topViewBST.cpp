/*
struct node
{
    int data;
    node* left;
    node* right;
};

*/

void topView(node * root) {
    if(root==NULL)
        return;
    
    if(root->left==NULL && root->right==NULL){
        cout << root->data << " ";
        return;
    }
    
    node* curRoot=root;
    std::vector<int> nodes;
    while(curRoot->left != NULL){
        nodes.push_back(curRoot->left->data);
        curRoot=curRoot->left;
    }
    
    for(int i=nodes.size()-1; i >= 0; i--){
        std::cout << nodes[i] << " ";
    }
    
    std::cout << root->data << " ";
    
    nodes.clear();
    curRoot=root;
    while(curRoot->right != NULL){
        nodes.push_back(curRoot->right->data);
        curRoot=curRoot->right;
    }
    
    for(int i=0;i<nodes.size();i++){
        std::cout << nodes[i] << " ";
    }
}
