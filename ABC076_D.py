from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="076"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N=int(input())
  T=list(map(int,input().split()))
  V=list(map(int,input().split()))
  re=[(0,0,0)]
  for i in range(N):
    re.append((V[i],re[-1][2],re[-1][2]+T[i]))
  rest=[(0,0),(re[-1][2],0)]
  re.sort(key=lambda x:x[0])
  for i in range(N):
    v,s,t=re[i+1]
    j=0
    while j<len(rest) and rest[j][0]<=s+0.00001: j+=1
    pp,pv=rest[j-1]
    np,nv=rest[j]
    tmp=[]
    if v>=(pv+nv+np-pp)/2: pass
    elif pp+v-pv>t: pass
    elif np-v+nv<s: pass
    else:
      tmp.append((max(s,pp+v-pv),v))
      tmp.append((min(t,np-v+nv),v))
    idx=j
    for x in tmp:
      rest.insert(idx, x)
      idx+=1
  ans=0
  for i in range(len(rest)-1):
    x,v=rest[i]
    y,w=rest[i+1]
    t=(w-v+y-x)/2
    if i%2==0:
      ans+=(2*v+t)*t/2+(2*w+(y-x-t))*(y-x-t)/2
    else:
      ans+=(y-x)*v
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])