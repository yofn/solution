#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int maxn = 3e5+5;
int fa[maxn];
int sz[maxn];
int find(int x){
    if(fa[x]==x) return x;
    return fa[x]=find(fa[x]);
}
void merge(int x, int y) {
    x = find(x);
    y = find(y);
    if (x == y) return;
    fa[y] = x;
    sz[x] += sz[y];
    sz[y] = 0;
}
int main(){
    int n,q;
    cin >> n >> q;
    for(int i=1;i<=n;++i) fa[i]=i;
    for(int i=1;i<=n;++i) sz[i]=1;
    vector<int> down(n+1);
    while(q--){
        int c,p;
        cin >> c >> p;
        down[c] = p;
    }
    for(int i=1;i<=n;++i){
        if(down[i]) merge(down[i],i);
    }
    for(int i=1;i<=n;++i) cout << sz[i] << " \n"[i==n];
    return 0;
}
