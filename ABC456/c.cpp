#include<bits/stdc++.h>
using namespace std;
int main(){
    string s;
    cin >> s;
    int n = s.size();
    vector<int> f(n+1,1);
    for(int i=1;i<n;++i){
        if(s[i]!=s[i-1]) f[i+1] += f[i];
    }
    long long ans = accumulate(f.begin(),f.end(),-1LL);
    cout << ans%998244353 << endl;
    return 0;
}
