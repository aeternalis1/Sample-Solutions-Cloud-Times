#include <bits/stdc++.h>
using namespace std;

int main(){
  int N,M;
  scanf("%d",&N);
  map<int,vector<int>> xs;
  map<int,vector<int>> ys;
  set<int> xinds;
  set<int> yinds;
  int x,y;
  for (int i=0;i<N;i++){
    scanf("%d %d",&x,&y);
    xs[x].push_back(y);
    ys[y].push_back(x);
    xinds.insert(x);
    yinds.insert(y);
  }
  for (int i:xinds){
    sort(xs[i].begin(),xs[i].end());
  }
  for (int i:yinds){
    sort(ys[i].begin(),ys[i].end());
  }
  scanf("%d",&M);
  int lastx,lasty;
  scanf("%d %d",&lastx,&lasty);
  long long total = 0;
  for (int i=0;i<M-1;i++){
    scanf("%d %d",&x,&y);
    if (lasty==y){
      if (x > lastx){
        total += upper_bound(ys[y].begin(),ys[y].end(),x)- lower_bound(ys[y].begin(),ys[y].end(),lastx);
      }
      else if (x < lastx){
        total += upper_bound(ys[y].begin(),ys[y].end(),lastx) - lower_bound(ys[y].begin(),ys[y].end(),x);
      }
    }
    else if (lastx == x){
      if (y > lasty){
        total += upper_bound(xs[x].begin(),xs[x].end(),y) - lower_bound(xs[x].begin(),xs[x].end(),lasty);
      }
      else if (y < lasty){
        total += upper_bound(xs[x].begin(),xs[x].end(),lasty) - lower_bound(xs[x].begin(),xs[x].end(),y);
      }
    }
    lastx = x;
    lasty = y;
  }
  printf("%lld",total);
  return 0;
}
