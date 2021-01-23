#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
    int N,M,a,b,S,T;
    scanf("%d %d",&N,&M);
    vector<int> edges[N+1];
    for (int i = 0; i < M; i++){
        scanf("%d %d",&a,&b);
        edges[a].push_back(b);
        edges[b].push_back(a);
    }
    scanf("%d %d",&S,&T);
    queue<int> q;
    q.push(S);
    int dist[N+1];
    memset(dist,-1,sizeof dist);
    dist[S] = 0;
    while (!q.empty()){
        int cur = q.front();
        q.pop();
        for (int i:edges[cur]){
            if (dist[i] == -1){
                dist[i] = dist[cur] + 1;
                q.push(i);
            }
        }
    }
    printf("%d", M - dist[T]);
}