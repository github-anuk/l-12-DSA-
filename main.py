class Graf:
    def __init__(self,n):
        self.n=n
        self.adj=[[]*n for i in range(n)]
    
    def create_edges(self,x,y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)
    
    def BFS(self,source):
        visited=[False]*self.n 
        res=[]
        queue = []
        queue.append(source)
        visited[source]=True
        while len(queue)>0:
            s=queue.pop(0)
            res.append(s)
            for node in self.adj[s]:
                if visited[node]== False:
                    queue.append(node)
                    visited[node]=True
        return res 

braf=Graf(4)
braf.create_edges(1,2)
braf.create_edges(2,3)
braf.create_edges(1,4)
print(braf.BFS(1))
