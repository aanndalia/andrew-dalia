#include <iostream>
using namespace std;
 
struct Node{
    int data;
    Node* next;
    Node(int val) : data(val), next(NULL){}
};
 
void printList(Node* head){
    for(Node* iter = head; iter != NULL; iter=iter->next){
        cout << iter->data << " ";
    }
    cout << "\n";
}
 
Node* reverseList(Node* head){
    Node* before = NULL;
    Node* current = head;
    Node* after = head->next;
    while(current != NULL){
        current->next = before;
        before = current;
        current = after;
        if(after)
            after = after->next;
    }
    head = before;
    return head;
}
 
Node* reverseListRecursively(Node* head, Node* before = NULL){
    if(head == NULL){
        return before;
    }
   
    Node* after = head->next;
    head->next = before;
    Node* newHead = reverseListRecursively(after, head);
    return newHead;
}
 
int main() {
                // your code goes here
                Node* head = new Node(1);
                head->next = new Node(2);
                head->next->next = new Node(3);
                head->next->next->next = new Node(4);
                head->next->next->next->next = new Node(5);
               
                printList(head);
               
                //Node* newHead = reverseList(head);
                Node* newHead = reverseListRecursively(head);
               
                printList(newHead);
               
                return 0;
}