/*
   Find merge point of two linked lists
   Node is defined as
   struct Node
   {
       int data;
       Node* next;
   }
*/
int FindMergeNode(Node *headA, Node *headB)
{
    // Complete this function
    // Do not write the main method. 
    if(headA==NULL || headB==NULL)
        return -1;
    
    for(Node* ptrA=headA; ptrA != NULL; ptrA=ptrA->next){
        for(Node* ptrB=headB; ptrB != NULL; ptrB=ptrB->next){
            if(ptrB==ptrA){
                return ptrB->data;
            }
        }
    }
    
    return -1;
}
