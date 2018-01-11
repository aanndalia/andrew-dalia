/*
  Remove all duplicate elements from a sorted linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* RemoveDuplicates(Node *head)
{
  // This is a "method-only" submission. 
  // You only need to complete this method. 
    if(head==NULL)
        return NULL;
    
    Node* ptr = head;
    Node* nextPtr = head->next;
    while(nextPtr!=NULL){
        while(nextPtr!=NULL && (nextPtr->data == ptr->data)){
            Node* nodeToDelete = nextPtr;
            nextPtr=nextPtr->next;
            delete nodeToDelete;
        }
        
        ptr->next=nextPtr;
        ptr=ptr->next;
        
        if(nextPtr!=NULL)
            nextPtr=nextPtr->next;
    }
    
    return head;
}
