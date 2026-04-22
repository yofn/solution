#include<bits/stdc++.h>
using namespace std;
/* 1
(xx)x
x(xx)
*/
string f(string s){
    vector<char> st;
    for(int i=0;i<s.size();++i){
        //能POP的情况
        char c = s[i];
        int n = st.size();
        if(c==')' && n>=3 && st[n-1]=='x' && st[n-2]=='x' && st[n-3]=='('){
            st[n-3]='x';
            st.pop_back();
        }else st.push_back(c);
    }
    return string(st.begin(),st.end());
}
void solve(){
    string s,t;
    cin >> s >> t;
    s = f(s);
    t = f(t);
    //cout << s << endl;
    //cout << t << endl;
    cout << (s==t ? "Yes" : "No") << endl;
}
int main(){
    int t;
    cin >> t;
    while(t--) solve();
    return 0;
}
