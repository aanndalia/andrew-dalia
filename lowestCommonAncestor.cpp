/*
Node is defined as 

typedef struct node
{
   int data;
   node *left;
   node *right;
}node;

*/


node *lca(node *root, int v1,int v2)
{
    if(root == NULL)
        return NULL;
    
    if(root->data == v1 || root->data == v2)
        return root;

    node* leftLca = lca(root->left, v1, v2);
    node* rightLca = lca(root->right, v1, v2);
   
    if(leftLca != NULL && rightLca != NULL)
        return root;
    
    if(leftLca != NULL)
        return leftLca;
    
    if(rightLca != NULL)
        return rightLca;
    
    return NULL;
}

