#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int maxn = 2e5+5;
ll a[maxn];
int n;
ll k;

bool check(ll x){
	ll tot = 0;
	for(int i=1;i<=n;++i){
		if(a[i]>=x) continue;
		tot += (x-a[i]+i-1)/i;
		if(tot>k) return false;
	}
	return true;
}

int main(){ 
	cin >> n >> k;
	for(int i=1;i<=n;++i)
		cin >> a[i];
	
	ll L=1, R=a[1]+k+1;
	while(R-L>1){
		ll mid = L+(R-L)/2;
		if(check(mid)){
			L = mid;
		}else{
			R = mid;
		}
	}
	cout << L << endl;
	return 0;
}
