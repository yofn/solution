#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int maxn = 1003;
char s[maxn][maxn]; //地图
int f[maxn][maxn][4]; //距离标记
int p[maxn][maxn][4]; //p[nx][ny][nd]表示(x,y,d)=>(nx,ny,nd)中的d.
int dx[]={0,1, 0,-1};
int dy[]={1,0,-1, 0};
char dc[]={'R','D','L','U'};
struct node{
    int x,y,d;
    //真正的状态, d表示能以什么方向走出(x,y)
};
int main(){
    int H,W; cin >> H >> W;
    for(int i=1;i<=H;++i) scanf("%s",s[i]+1);
    int sx,sy,gx,gy;
    for(int i=1;i<=H;++i){
        for(int j=1;j<=W;++j){
            if(s[i][j]=='S') sx=i,sy=j,s[i][j]='.';
            if(s[i][j]=='G') gx=i,gy=j,s[i][j]='.';
        }
    }
    //cout << sx << ',' << sy << endl;
    //cout << gx << ',' << gy << endl;
    memset(f,-1,sizeof(f));
    queue<node> q; //广搜得到的状态队列, 当前只有状态, 没有dis
    for(int i=0;i<4;++i){
        q.push({sx,sy,i});
        f[sx][sy][i]=0;
    }
    while(!q.empty()){
        node u = q.front(); q.pop();
        int nx = u.x + dx[u.d];
        int ny = u.y + dy[u.d];
        //cout << u.x << ',' << u.y << ':' << u.d << endl;
        //cout << nx << ',' << ny << endl;
        if(nx<1 || nx>H) continue;
        if(ny<1 || ny>W) continue;
        if(s[nx][ny]=='#') continue;
        for(int i=0;i<4;++i){
            if(s[nx][ny]=='x' && i==u.d) continue;
            if(s[nx][ny]=='o' && i!=u.d) continue;
            if(f[nx][ny][i]!=-1) continue;
            f[nx][ny][i] = f[u.x][u.y][u.d]+1;
            p[nx][ny][i] = u.d;
            q.push({nx,ny,i});
        }
    }
    if(f[gx][gy][0]==-1) return 0*puts("No");
    cout << "Yes\n";
    int x=gx,y=gy,d=0;
    vector<char> path;
    while(x!=sx || y!=sy){
        //cout << x << ',' << y << ':' << d << endl;
        int pd = p[x][y][d]; //pd 到(x,y,d)的方向
        int px = x-dx[pd];
        int py = y-dy[pd];
        path.push_back(dc[pd]);
        x=px,y=py,d=pd;
    }
    reverse(path.begin(),path.end());
    for(int i=0;i<path.size();++i)
        cout << path[i];
    cout << endl;
    return 0;
}
