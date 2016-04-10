/*
Regular expression matching
Leetcode OJ #10

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true  
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isMatch(const string& s, const string& r){
	if(!s.length() && !r.length()){
		return true;
	}
	if(!s.length() || !r.length()){
		return false;
	}

	/* create dynamic programming tracking matrix one 
	 character dimension extra in each dierction for
	 each string */
	bool dp[s.length()+1][r.length()+1];

	/* initialize dp matrix to all false */
	for(int i = 0; i < s.length() + 1; i++){
		for(int j = 0; j < r.length() + 1; j++){
			dp[i][j] = false;
		}
	}

	/* initialize r dimension cell to true for previous char */
	dp[0][0] = true;
	for(int j=0; j < r.length()+1; j++){
		if(r[j] == '*' && dp[0][j-1]){
			dp[0][j+1] = true;
		}
	}


	/* fill in dp matrix using previous values. 
	   Matching characters and '.' should be 
	   handled the same way. */
	for(int i = 0; i < s.length(); i++){
		for(int j = 0; j < r.length(); j++){
			if((r[j] == '.') || (r[j] == s[i])){
				dp[i+1][j+1] = dp[i][j];
			}
			else if(r[j] == '*'){
				if(r[j-1] == s[i] || r[j-1] == '.'){
					dp[i+1][j+1] = dp[i+1][j-1] || dp[i+1][j] || dp[i][j+1];
				}
				else{
					dp[i+1][j+1] = dp[i+1][j-1];
				}
			}
		}
	}

	/* print out final matrix (for checking/debugging) */
	for(int i = 0; i < s.length()+1; i++){
		for(int j = 0; j < r.length()+1; j++){
			cout << dp[i][j] << " ";
		}
		cout << "\n";
	}
	cout << "\n";

	return dp[s.length()][r.length()];

}

int main(){
	string s = "aaaaaaaa";
	string r = "a*";
	string result = isMatch(s, r) ? "matched" : "not matched";
	cout << "result: " << result << endl;
}