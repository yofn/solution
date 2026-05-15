#include<bits/stdc++.h>
using namespace std;

const int maxn = 2e5+5;
string s[maxn];
int  a[11];
int  b[11];
bool f[11][11][26];

int main(){
    int n; cin >> n;
    for(int i=0;i<n;++i)
		cin >> a[i] >> b[i];
    int m; cin >> m;
    for(int i=1;i<=m;++i)
        cin >> s[i];
    for(int i=1;i<=m;++i){
        int len = s[i].size();
        for(int j=0;j<len;++j)
            f[len][j+1][s[i][j]-'a'] = true;
    }
    for(int i=1;i<=m;++i){
        int len = s[i].size();
        if(len!=n){
            cout << "No\n";
            continue;
        }
        bool flag = true;
        for(int j=0;j<n;++j)
			flag &= f[a[j]][b[j]][s[i][j]-'a'];
        cout << (flag?"Yes\n":"No\n");
    }
    return 0;
}
