#include <iostream>
 
using namespace std;
 
struct Node
{
    Node(int val) : data(val), next(NULL) {}
    int data;
    Node* next;
};
 
bool hasCycle2(Node* head)
{
   // Complete this function
   // Do not write the main method
    if(head == NULL){
        return false;
    }
   
    Node* ptr1 = head;
   
    if(head->next == NULL){
        return false;
    }
   
    Node* ptr2 = head->next->next;
   
    while(ptr1 != NULL && ptr2 != NULL && ptr1 != ptr2){
        ptr1 = ptr1->next;
        if(ptr2->next == NULL){
            return false;
        }
        else{
            ptr2 = ptr2->next->next;
        }
    }
   
    if(ptr1 == ptr2){
        return true;
    }
   
    return false;
}
 
Node* findCollisionPoint(Node* head)
{
   // Complete this function
   // Do not write the main method
    if(head == NULL){
        return NULL;
    }
   
    Node* ptr1 = head;
   
    if(head->next == NULL){
        return NULL;
    }
   
    Node* ptr2 = head->next->next;
   
    while(ptr1 != NULL && ptr2 != NULL && ptr1 != ptr2){
        ptr1 = ptr1->next;
        if(ptr2->next == NULL){
            return NULL;
        }
        else{
            ptr2 = ptr2->next->next;
        }
    }
   
    if(ptr1 == ptr2){
        return ptr1;
    }
   
    return NULL;
}
 
int getLoopSize(Node* loopNode)
{
    if(loopNode == NULL){
        cout << "loopNode is NULL" << endl;
        return 0;
    }
 
    Node* ptr = loopNode->next;
    int count = 1;
    while(ptr != NULL && ptr != loopNode){
        cout << "traversing in getLoopSize: " << ptr->data << endl;
        ptr = ptr->next;
        count++;
    }
 
    if(ptr == NULL){
        cout << "Found null ptr" << endl;
        return 0;
    }
    else{
        return count;
    }
}
 
bool hasCycle(Node* head){
    Node* collisionPoint = findCollisionPoint(head);
    if(collisionPoint == NULL){
        return false;
    }
    return true;
}
 
void removeCycle(Node* head){
 
    if(head == NULL){
        return;
    }
 
    Node* collisionPoint = findCollisionPoint(head);
    if(collisionPoint == NULL){
        return;
    }
 
    int loopSize = getLoopSize(collisionPoint);
    cout << "Loop size is " << loopSize << endl;
   
    Node* ptr1 = head;
    Node* ptr2 = head;
    for(int i = 0; i < loopSize; i++){
        ptr2 = ptr2->next;
    }
 
    while(ptr1 != NULL && ptr2 != NULL && ptr1 != ptr2){
        //cout << "ptr1 and ptr2 addresses: " << ptr1 << " " << ptr2 << endl;
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;
    }
 
    if(ptr1 == ptr2){
        int count = 0;
        while(count < loopSize - 1){
            ptr1 = ptr1->next;
            count++;
        }
       
        ptr1->next = NULL;
    }
}
 
int main()
{
    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);
    head->next->next->next->next = new Node(5);
    head->next->next->next->next->next = new Node(6);
    head->next->next->next->next->next->next = new Node(7);
    head->next->next->next->next->next->next->next = head->next->next; // loop back to Node with val 3
 
    cout << "has a cycle? " << hasCycle(head) << endl;
    cout << "getLoopSize: " << getLoopSize(findCollisionPoint(head)) << endl;
    cout << "removing cycle" << endl;
    removeCycle(head);
    cout << "has a cycle? " << hasCycle(head) << endl;
   
    Node* ptr = head;
    while(ptr != NULL){
        cout << ptr->data << " ";
        ptr = ptr->next;
    }
    cout << "\n";
}