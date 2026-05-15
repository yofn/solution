#include<bits/stdc++.h>
using namespace std;

bool f[11][11][26];

int main(){
    int n; cin >> n;
    vector<int> a(n),b(n);
    for(int i=0;i<n;++i) cin >> a[i] >> b[i];
    
    int m; cin >> m;
    vector<string> s(m);
    for(int i=0;i<m;++i) cin >> s[i];

    for(int i=0;i<m;++i){
        int len = s[i].size();
        for(int j=0;j<s[i].size();++j)
            f[len][j+1][s[i][j]-'a'] = true;
    }
    for(auto t:s){
        if(t.size()!=n){
            cout << "No\n";
            continue;
        }
        bool flag = true;
        for(int j=0;j<n;++j)
            flag &= f[a[j]][b[j]][t[j]-'a'];
        cout << (flag?"Yes\n":"No\n");
    }
    return 0;
}
