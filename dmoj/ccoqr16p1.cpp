#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
    int N,x,y;
    scanf("%d",&N);
    int pts[N][2];
    vector<int> coords;
    for (int i = 0; i < N; i++){
        scanf("%d %d",&x,&y);
        pts[i][0] = x;
        pts[i][1] = y;
        coords.push_back(x);
        coords.push_back(y);
    }
    sort(coords.begin(),coords.end());
    for (int i = 0; i < N; i++){
        for (int j = 0; j < 2; j++){
            int lo = 0, hi = 2*N, mid;
            while (lo < hi){
                mid = (lo+hi)/2;
                if (coords[mid] > pts[i][j]){
                    hi = mid;
                }else{
                    lo = mid+1;
                }
            }
            pts[i][j] = lo-1;
        }
    }
    
    vector<int> xs[2*N+1], ys[2*N+1];
    for (int i = 0; i < N; i++){
        xs[pts[i][0]].push_back(pts[i][1]);
        ys[pts[i][1]].push_back(pts[i][0]);
    }
    for (int i = 0; i < 2*N+1; i++){
        sort(xs[i].begin(), xs[i].end());
        sort(ys[i].begin(), ys[i].end());
    }
    
    ll ans = 0;
    for (int i = 0; i < N; i++){
        x = pts[i][0];
        y = pts[i][1];
        int lo = 0, hi = xs[x].size()-1, mid;
        while (lo <= hi){
            mid = (lo+hi)/2;
            if (xs[x][mid] > y){
                hi = mid-1;
            }else if (xs[x][mid] < y){
                lo = mid+1;
            }else{
                break;
            }
        }
        ll l = mid, r = xs[x].size() - mid - 1;
        lo = 0;
        hi = ys[y].size()-1;
        while (lo <= hi){
            mid = (lo+hi)/2;
            if (ys[y][mid] > x){
                hi = mid-1;
            }else if (ys[y][mid] < x){
                lo = mid+1;
            }else{
                break;
            }
        }
        ll b = mid, t = ys[y].size() - mid - 1;
        ans += l * r * b * t * 2;
    }
    printf("%lld\n",ans);
    
}
