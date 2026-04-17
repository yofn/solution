#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
//5
//2 5 2 2 1
const int maxn = 22;
int L[maxn];
int n;
int maxpass = 0;
void dfs(ll x,int i,int pass){
    if(i>n){
        //corner case
        maxpass = max(pass,maxpass);
        return;
    }
    dfs(x+L[i],i+1,pass+(x+L[i]>0 ^ x>0));
    dfs(x-L[i],i+1,pass+(x-L[i]>0 ^ x>0));
}
int main(){
    cin >> n;
    for(int i=1;i<=n;++i) cin >> L[i];
    for(int i=1;i<=n;++i) L[i] <<= 1;
    dfs(1,1,0);
    cout << maxpass << endl;
    return 0;
}
