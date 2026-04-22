#include<bits/stdc++.h>
using namespace std;
const int maxn = 3e5+5;
vector<int> adj[maxn]; //Graph
bool vis[maxn]; //vis[u]表示u有没有被访问过.
//一般图(NOT TREE)上的深搜
void dfs(int u){
    if(vis[u]) return;
    vis[u] = true;
    for(auto v:adj[u]) dfs(v);
}
int main(){
    int n,m;
    cin >> n >> m;
    //建一个有向图
    for(int i=1;i<=m;++i){
        int u,v;
        cin >> u >> v;
        adj[u].push_back(v);
    }
    //深搜
    dfs(1);
    int ans = 0;
    for(int i=1;i<=n;++i) if(vis[i]) ++ans;
    cout << ans << endl;
    return 0;
}
