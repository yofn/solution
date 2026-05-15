#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int mod = 998244353;

int main() {
    string s, t; cin >> s >> t;
    int n = s.size();
    int m = t.size();
    ll tot = 1LL * n * (n+1) / 2;
    vector<int> f(m+1);
    for(int i=0; i<n; ++i){
        auto g = f;
        f[0] = i+1;
        for(int j=1; j<=m; ++j){
            if(s[i]!=t[j-1]) continue;
            g[j] = f[j-1];
        }
        tot -= g[m];
        swap(f,g);
    }
    cout << tot << endl;
}
