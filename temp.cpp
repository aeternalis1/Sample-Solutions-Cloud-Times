#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
    int N;
    scanf("%d",&N);
    ll arr[N], dp[N][2];
    for (int i=0;i<N;i++){
        scanf("%lld",&arr[i]);
    }
    dp[0][0] = 0;
    dp[0][1] = arr[0];
    for (int i=1;i<N;i++){
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]);
        dp[i][1] = dp[i-1][0] + arr[i];
    }
    printf("%lld\n",max(dp[N-1][0],dp[N-1][1]));
}