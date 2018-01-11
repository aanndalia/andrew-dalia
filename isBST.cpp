/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.  

The Node struct is defined as follows:
   struct Node {
      int data;
      Node* left;
      Node* right;
   }
*/
    bool checkOrder(std::vector<int>& v){
        if(v.size() < 2)
            return true;
        
        for(int i=1; i<v.size(); i++){
            if(v[i] <= v[i-1])
                return false;
        }
        
        return true;
    }    

    void inOrderTraversal(Node* root, std::vector<int>& v){
        if(root==NULL)
            return;
        
        inOrderTraversal(root->left, v);
        v.push_back(root->data);
        inOrderTraversal(root->right, v);
    }

    bool checkBST(Node* root) {
       if(root==NULL)
          return true;
       
       std::vector<int> v;
       inOrderTraversal(root, v);
       return checkOrder(v);        
    }
