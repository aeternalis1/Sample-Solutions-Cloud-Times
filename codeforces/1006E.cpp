#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MAXN = 200001;

int par[MAXN];
vector<int> edges[MAXN];
vector<int> order;
int ind[MAXN], size[MAXN];

void dfs(int cur){
    ind[cur] = order.size();
    order.push_back(cur);
    size[cur] = 1;
    for (int i: edges[cur]){
        dfs(i);
        size[cur] += size[i];
    }
}


int main(){
    int N, Q, a, k;
    scanf("%d %d",&N, &Q);
    for (int i = 1; i < N; i++){
        scanf("%d", &par[i]);
        par[i]--;
        edges[par[i]].push_back(i);
    }
    for (int i = 0; i < N; i++){
        sort(edges[i].begin(), edges[i].end());
    }
    dfs(0);
    for (int i = 0; i < Q; i++){
        scanf("%d %d",&a,&k);
        a--;
        if (k > size[a]){
            printf("-1\n");
            continue;
        }
        printf("%d\n", order[ind[a] + k - 1] + 1);
    }
}