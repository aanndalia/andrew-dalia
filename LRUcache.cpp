#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

struct Node{
   Node* next;
   Node* prev;
   int value;
   int key;
   Node(Node* p, Node* n, int k, int val):prev(p),next(n),key(k),value(val){};
   Node(int k, int val):prev(NULL),next(NULL),key(k),value(val){};
};

class Cache{
protected: 
   map<int,Node*> mp; //map the key to the node in the linked list
   int cp;  //capacity
   Node* tail; // double linked list tail pointer
   Node* head; // double linked list head pointer
   virtual void set(int, int) = 0; //set function
   virtual int get(int) = 0; //get function
};

/* Implement LRUCache here by inheriting from Cache */
class LRUCache : public Cache{
public:
   LRUCache(int capacity) { 
      this->cp = capacity; 
      this->tail = NULL;
      this->head = NULL;
   }

   void set(int key, int value){
      if(mp.size() == 0){
         cout << "Setting first node with key " << key << " and value " << value << endl;
         Node* val = new Node(NULL, NULL, key, value);
         head = val;
         tail = val;
         mp.insert(pair<int, Node*>(key, val));
         return;
      }

      if(mp.find(key) == mp.end()){
         cout << "Setting new node with key " << key << " and value " << value << endl;
         Node* val = new Node(NULL, head, key, value);
         head->prev = val;
         head = val;
         mp.insert(pair<int, Node*>(key, val));
         if(mp.size() > cp){
            cout << "Deleting node with key " << tail->key << " and value " << tail->value << endl;
            Node* toBeTail = tail->prev;
            toBeTail->next = NULL;
            mp.erase(tail->key);
            delete tail;
            tail = toBeTail;
         }
      }
      else{
         cout << "Changing value of key " << key << " from " << mp[key]->value << " to " << value << endl;
         mp[key]->value = value;
      }
   }

   int get(int key){
      if(mp.size() == 0){
         cout << "Cache is empty" << endl; 
         return -1;
      }

      if(mp.find(key) != mp.end()){
         if(head != mp[key]){
            cout << "Cache hit - key " << key << " was found in map" << endl;
            Node* prev = mp[key]->prev;
            Node* next = mp[key]->next;
            prev->next = next;
            if(next != NULL)
               next->prev = prev;
            else
               tail = prev;
            mp[key]->prev = NULL;
            mp[key]->next = head;
            head->prev = mp[key];
            head = mp[key];
         }
         return mp[key]->value;
      }
      else {
         cout << "Cache miss - key " << key << " was not found in map" << endl;
         return -1;
      }
   }

   void printList(){
      if(head == NULL)
         return;

      for(Node* iter = head; iter != NULL; iter = iter->next){
         cout << iter->key << ": " << iter->value << endl;
      }
   }

   Node* getHead(){
      return this->head;
   }

   Node* getTail(){
      return this->tail;
   }
};


int main() {
   int n, capacity, i;
   cout << "Enter capacity: ";
   cin >> capacity;
   cout << "Enter either a get or set command" << endl;
   cout << "get <key>" << endl;
   cout << "set <key> <value>" << endl;
   LRUCache l(capacity);
   while(true) {
      string command;
      cout << "command: ";
      cin >> command;
      if(command == "exit"){
         cout << "Exiting..." << endl;
         return 0;
      }
      else if(command == "get") {
         int key;
         cin >> key;
         cout << l.get(key) << endl;
      } 
      else if(command == "set") {
         int key, value;
         cin >> key >> value;
         l.set(key,value);
      }
      else if(command == "print"){
         l.printList();         
      }
      else{
         cout << "Incorrect command - try again" << endl;
      }
   }
   return 0;
}