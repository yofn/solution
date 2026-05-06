#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int mod = 998244353;
int main(){
    string s;
    cin >> s;
    int n = s.size();
    vector<ll> f(3);
    for(int i=0;i<n;++i){
        auto g = f;
        int x = s[i]-'a';
        g[x] += f[0]+f[1]+f[2]-f[x]+1;
        g[x] %= mod;
        swap(f,g);
    }
    int ans = (f[0]+f[1]+f[2])%mod;
    cout << ans << endl;
    return 0;
}
