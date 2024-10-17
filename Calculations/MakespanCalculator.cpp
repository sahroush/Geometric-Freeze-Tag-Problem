#pragma GCC optimize("O2")
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int , int> pii;

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

const int maxn = 50;
const ll mod = 1e9+7;

#define pb push_back
#define endl '\n'
#define dokme(x) cout << x , exit(0)
#define ms(x , y) memset(x , y , sizeof x)
ll pw(ll a, ll b, ll md = mod){ll res = 1;while(b){if(b&1){res=(a*res)%md;}a=(a*a)%md;b>>=1;}return(res);}

struct point{
    ld x, y;
};

int n;
point origin;
vector < point > p;
ld ans = 1e9;
int d[maxn];
int par[maxn];
int cnt = 0; 
int sz[maxn];

int dsu[maxn];

int getpar(int v){
    return ((dsu[v] != -1) ? getpar(dsu[v]) : v);
}

stack < pii > stk;

void merge(int u, int v){
    u = getpar(u), v = getpar(v);
    if(sz[u] > sz[v])
        swap(u, v);
    dsu[u] = v;
    stk.push({u, v});
    sz[v] += sz[u];
}

void cut(){
    auto [u, v] = stk.top();
    stk.pop();
    dsu[u] = -1;
    sz[v] -= sz[u];
}

ld dist(int i, int j){
    ld d = sqrt(abs(p[i].x - p[j].x)*abs(p[i].x - p[j].x) + abs(p[i].y - p[j].y)*abs(p[i].y - p[j].y));
    return d;
}

ld solve(int v = 0, ld h = 0){
    ld res = h;
    for(int i = 1 ; i < n ; i ++)if(par[i] == v)
        res = max(res, solve(i, h + dist(v, i)));
    return res;
}

ld ldrng(ld s = 0){
    ld x = rng() / 100000.0;
    x = (x - ll(x)) * (1-s);
    if(rng()%2)return -x;
    return x;
}

void make_points(){
    p.clear();
    p.pb(origin);
    p.pb({0.954, 0.298});
    p.pb({-0.108, 0.994});
    p.pb({-0.995, 0.097});
    p.pb({-0.768, -0.639});
    p.pb({0.488, -0.872});
    n = p.size();
    ms(dsu, -1);
    for(int i = 0 ; i < n ; i ++)
        sz[i] = 1;
}

void generate_all_trees(int v = 1){
    if(v == n){
        if(d[0] != 1)return;
        ans = min(ans, solve());
        return;
    }
    for(int i = 0 ; i < n ; i ++){
        par[v] = i;
        d[i] ++;
        if(d[i] <= 2 and getpar(i) != getpar(v)){
            merge(v, i);
            generate_all_trees(v+1);
            cut();
        }
        d[i] --;
    }
}

int32_t main(){
	cin.tie(0)->sync_with_stdio(0);
    ld mx = 0;
    ans = 1e9; 
    make_points();
    generate_all_trees();
    mx = max(mx, ans);
    cout << mx << endl;
	return(0);
}
