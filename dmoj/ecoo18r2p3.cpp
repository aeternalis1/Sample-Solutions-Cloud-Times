#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
    ll K,M;
    for (int _ = 0; _ < 10; _++){
        scanf("%lld %lld",&K,&M);
        ll lo = 0, hi = 1e12, mid;
        vector<ll> fact, cnt;
        for (int i = 2; K > 1; i++){
            ll tmp = 0;
            while (K % i == 0){
                K /= i;
                tmp++;
            }
            if (tmp){
                fact.push_back(i);
                cnt.push_back(tmp*M);
            }
        }
        while (lo < hi){
            mid = (lo+hi)/2;
            int f = 1;
            for (int i = 0; i < fact.size(); i++){
                ll cur = fact[i], tmp = 0;
                while (cur <= mid){
                    tmp += mid/cur;
                    cur *= fact[i];
                }
                if (tmp < cnt[i]){
                    f = 0;
                    break;
                }
            }
            if (f){
                hi = mid;
            }else{
                lo = mid+1;
            }
        }
        printf("%lld\n",lo);
    }
}