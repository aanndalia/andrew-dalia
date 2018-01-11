/*
  Merge two sorted lists A and B as one linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* MergeLists(Node *headA, Node* headB)
{
  // This is a "method-only" submission. 
  // You only need to complete this method 
    if(headA==NULL && headB==NULL){
        return NULL;
    }
    
    if(headA==NULL){
        return headB;
    }
    
    if(headB==NULL){
        return headA;
    }
    
    Node* ptrA = headA;
    Node* ptrB = headB;
    Node* headMerged = NULL;
    if(headA->data <= headB->data){
        headMerged = headA;
        ptrA=ptrA->next;
    } else {
        headMerged = headB;
        ptrB=ptrB->next;
    }
    
    Node* ptrMerged=headMerged;
    while(ptrA != NULL && ptrB != NULL){
        if(ptrA->data < ptrB->data){
            Node* tmp = ptrA;
            ptrA=ptrA->next;
            ptrMerged->next=tmp;
            ptrMerged=ptrMerged->next;
        } else if(ptrA->data > ptrB->data){
            Node* tmp = ptrB;
            ptrB=ptrB->next;
            ptrMerged->next=tmp;
            ptrMerged=ptrMerged->next;
        } else {
            Node* tmpA = ptrA;
            Node* tmpB = ptrB;
            ptrA=ptrA->next;
            ptrB=ptrB->next;
            ptrMerged->next=tmpA;
            ptrMerged->next->next=tmpB;
            ptrMerged=ptrMerged->next;
        }
    }
    
    while(ptrA != NULL){
        ptrMerged->next = ptrA;
        ptrMerged=ptrMerged->next;
        ptrA=ptrA->next;
    }
    
    while(ptrB != NULL){
        ptrMerged->next = ptrB;
        ptrMerged=ptrMerged->next;
        ptrB=ptrB->next;
    }
    
    return headMerged;
}
