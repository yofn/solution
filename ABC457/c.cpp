#include<bits/stdc++.h>
using namespace std;


int main(){
	int n; cin >> n;
	long long k; cin >> k;
	vector<vector<int>> a(n);
	for(auto &v:a){
		int L; cin >> L;
		v.resize(L);
		for(auto &x:v) cin >> x;
	}
	vector<int> c(n);
	for(auto &x:c) cin >> x;
	
	for(int i=0;i<n;++i){
		int li = a[i].size();
		long long ac = 1LL*c[i]*li;
		if(k>ac) k -= ac;
		else{
			--k;
			cout << a[i][k%li];
			break;
		}
	}
	return 0;
}
