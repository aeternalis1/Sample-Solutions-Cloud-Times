#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
    int N,M,q;
    scanf("%d",&N);
    int arr[N];
    arr[0] = 0;
    for (int i = 1; i <= N; i++){
        scanf("%d",&arr[i]);
        arr[i] += arr[i-1];
    }
    scanf("%d",&M);
    for (int i = 0; i < M; i++){
        scanf("%d",&q);
        int lo = 0, hi = N, mid;
        while (lo < hi){
            mid = (lo+hi)/2;
            if (arr[mid] < q){
                lo = mid+1;
            }else{
                hi = mid;
            }
        }
        printf("%d\n",lo);
    }
}
