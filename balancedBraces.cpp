#include <bits/stdc++.h>

using namespace std;

string isBalanced(string s) {
    // Complete this function
    std::stack<char> braces;
    for(int i=0; i < s.length(); i++){
        if(s[i]=='{' || s[i]=='[' || s[i]=='('){
            braces.push(s[i]);
        }            
        else if(s[i] == '}'){
            if(braces.empty() || braces.top() != '{')
                return "NO";
            else
                braces.pop();
        } else if(s[i]==']'){
            if(braces.empty() || braces.top() != '[')
                return "NO";
            else
                braces.pop();
        } else if(s[i]==')'){
            if(braces.empty() || braces.top() != '(')
                return "NO";
            else
                braces.pop();
        } else {
            continue;
        }
    }
    
    if(!braces.empty())
        return "NO";
    
    return "YES";
}

int main() {
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        string s;
        cin >> s;
        string result = isBalanced(s);
        cout << result << endl;
    }
    return 0;
}
