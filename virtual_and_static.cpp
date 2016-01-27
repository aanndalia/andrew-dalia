#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person{
protected:
    string name;
    int age;
    static int cur_id;

public:    
    Person(){
        cur_id++;
    }

    virtual void getdata() = 0;
    virtual void putdata() = 0;
};

class Professor : public Person {
private:
    int publications;
    //static int cur_id;
public:
    //static int cur_id;
    Professor(){
        //cur_id++;
    }
    void getdata() {
        cin >> name >> age >> publications;
    }
    void putdata() {
        cout << name << " " << age << " " << publications << " " << cur_id << endl;
    }
};

class Student : public Person {
private:
    int marks[6];
    //static int cur_id;
public:
    //static int cur_id;
    Student(){
        //cur_id++;
    }
    void getdata(){
        cin >> name >> age;
        for(int i=0; i < 6; i++){
            cin >> marks[i];
        }
    }
    void putdata(){
        int sumMarks = 0;
        for(int i = 0; i < 6; i++){
            sumMarks += marks[i];
        }
        cout << name << age << sumMarks << cur_id << endl;
    }
};

int Person::cur_id = 1;
//int Professor::cur_id = 1;
//int Student::cur_id = 1;


int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    cout << "n=" << n << endl;
    Person *per[n];
    cout << "before loop" << endl;
    for(int i = 0;i < n;i++){

        cin>>val;
        cout << "val=" << val << endl;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}