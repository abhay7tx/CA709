def dfs(city,count,cost):
    if count==n:
        return cost+graph[city][0]

    ans=999999

    for i in range(n):
        if vis[i]==False:
            vis[i]=True
            ans=min(ans,dfs(i,count+1,cost+graph[city][i]))
            vis[i]=False

    return ans

n=4

graph=[
[0,1,2,3],
[2,0,5,2],
[8,1,0,5],
[1,2,5,7]
]

vis=[False]*n
vis[0]=True

print("Minimum Cost =",dfs(0,1,0))