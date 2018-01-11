/*
    Insert Node in a doubly sorted linked list 
    After each insertion, the list should be sorted
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
Node* SortedInsert(Node *head,int data)
{
    // Complete this function
   // Do not write the main method. 
    Node* ptr = head;
    Node* newNode = new Node();
    newNode->data=data;
    newNode->next=NULL;
    newNode->prev=NULL;
    
    if(head==NULL){
        return newNode;
    }
        
    if(ptr->data > data){
        newNode->next=ptr;
        ptr->prev=newNode;
        return newNode;
    }
    
    while(ptr->next != NULL){
        if(ptr->data <= data && ptr->next->data >= data){
            Node* newNext = ptr->next;
            ptr->next=newNode;
            newNode->next=newNext;
            newNext->prev=newNode;
            newNode->prev=ptr;
            return head;
        }
        ptr=ptr->next;
    }
    
    ptr->next=newNode;
    newNode->prev=ptr;
    return head;
}
