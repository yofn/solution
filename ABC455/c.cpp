#include<bits/stdc++.h>
using namespace std;
using ll = long long;
int main(){
    int n,k;
    cin >> n >> k;
    map<int,int> mp;
    for(int i=1;i<=n;++i){
        int x;
        cin >> x;
        mp[x]++;
    }
    vector<ll> bs;
    for(auto [x,v]:mp) bs.push_back(1ll*x*v);
    sort(bs.begin(),bs.end());
    if(bs.size()<=k) return 0*puts("0");
    int m = bs.size();
    ll ans = 0;
    for(int i=0;i<m-k;++i) ans += bs[i];
    cout << ans << endl;
    return 0;
}
