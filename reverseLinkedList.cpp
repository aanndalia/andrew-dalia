/*
  Reverse a linked list and return pointer to the head
  The input list will have at least one element  
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Reverse(Node *head)
{
  // Complete this method
    if(head==NULL)
        return NULL;
    
    Node* before=NULL;
    Node* cur=head;
    Node* after=head->next;
    
    while(after!=NULL){
        cur->next=before;
        before=cur;
        cur=after;
        after=after->next;
    }
    
    cur->next=before;
    head=cur;
    return head;
}
