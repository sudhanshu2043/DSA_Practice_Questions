import heapq
class Solution:
    def DjisktraAlgo(self,n,adj,i,ans):
        pq=[(0,i)]
        ans[i]=0
        while pq:
            dist,node=heapq.heappop(pq)
            for v,d in adj[node]:
                if d+dist<ans[v]:
                    ans[v]=d+dist
                    heapq.heappush(pq,(d+dist,v))
    def findresult(self,n,SPM,disthreshold):
        countcity=float('inf')
        city=-1
        for i in range(n):
            count=0
            for j in range(n):
                if i!=j and SPM[i][j]<=disthreshold:
                    count+=1
            if count<countcity or (count==countcity and i>city):
                countcity=count
                city=i
        return city
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj=[[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        SPM=[[float('inf')]*n for _ in range(n)]
        for i in range(n):
            SPM[i][i]=0
        for i in range(n):
            self.DjisktraAlgo(n,adj,i,SPM[i])
        res=self.findresult(n,SPM,distanceThreshold)
        return res