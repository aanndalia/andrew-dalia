/*
   Reverse a doubly linked list, input list may also be empty
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
Node* Reverse(Node* head)
{
    // Complete this function
    // Do not write the main method. 
    if(head==NULL){
        return NULL;
    }
    
    Node* before=NULL;
    Node* cur=head;
    Node* after=head->next;
    
    while(after!=NULL){
        cur->next=before;
        cur->prev=after;
        before=cur;
        cur=after;
        after=after->next;
    }
    
    cur->next=before;
    cur->prev=after;
    return cur;
}
