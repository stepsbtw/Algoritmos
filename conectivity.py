from itertools import combinations, permutations

v = ["a", "b", "c", "d"]

combs = list(combinations(v, 2))
perms = list(permutations(v, 2))

g_conn = (v, combs)
g_full = (v, perms)

def gen_graph(nodes, n):
    e = random.sample(n, combs)
    return (nodes, e)


nodes = ["s","a","b","c","d","t"]

edges = [
("s","a"),("s","b"),("b","c"),
("a","d"),("d","t"),("c","t"),
("a","b"),("b","a")
]

g = (nodes, edges)

def adj_list(edges):
    adj = {}
    for u, v in edges:
        if u not in adj:
            adj[u] = []
        adj[u].append(v)
    return adj    

def adj_list(nodes, edges):
    adj = {node: [] for node in nodes}
    for u, v in edges:
        adj[u].append(v)
    return adj
    
def adj_list_undirected(edges):
    adj = {}
    for u, v in edges:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
        adj[v].append(u)
    return adj
    
def adj_list_undirected(nodes, edges):
    adj = {node: [] for node in nodes}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj
    
class G:
    def __init__(self, nodes, edges):
       self.nodes = nodes
       self.edges = edges
       self.adj = adj_list(nodes,edges)

g = G(nodes, edges)
print(g.adj)

# CONEXO:
# existe um caminho entre todo par de nós

# FORTEMENTE CONEXO (direcionados):
# existe todo caminho (u,v) e todo caminho (v,u)

def _dfs(adj, visited, node):
    visited[node] = True
    # pre order operations
    print(node)
    for nbor in adj[node]:
        if not visited[nbor]:
            _dfs(adj, visited, nbor)
    # post order operations
    
def dfs_(adj, visited, node):
    visited[node] = True
    # pre order operations
    for nbor in adj[node]:
        if not visited[nbor]:
            dfs_(adj, visited, nbor)
    print(node)
    # post order operations
    
def _dfs_iter(adj, no_inicial):
    visited = set()
    stack = [no_inicial]
    pre = []
    while stack:
        no = stack.pop()
        if no not in visited:
            visited.add(no)
            # pre
            pre.append(no)
            for nbor in reversed(adj[no]):
                if nbor not in visited:
                    stack.append(nbor)
    return pre
 
def dfs_iter_(adj, no_inicial):
    visited = set()
    stack = [(no_inicial, False)]
    post = []

    while stack:
        no, processed = stack.pop()
        if processed:
            post.append(no)  # pós-ordem
        elif no not in visited:
            visited.add(no)
            stack.append((no, True))  # Marcar para pós-ordem depois
            for nbor in reversed(adj[no]):
                if nbor not in visited:
                    stack.append((nbor, False))
    
    return post
        
def create_visited(nodes):
    visited = {}
    for no in nodes:
        visited[no] = False
    return visited
    
# bsca por profundidade em grafos não direcionados

# TEMPO LINEAR!

visited = create_visited(g.nodes)
_dfs(g.adj, visited, "s")
print("\n")
visited = create_visited(g.nodes)
dfs_(g.adj, visited, "s")

print(_dfs_iter(g.adj, "s"))
print("\n")
print(dfs_iter_(g.adj, "s"))

# quais partes do grafo são alcançáveis apartir de um nó específico?

# DFS + lista alcançaveis
visited = create_visited(g.nodes)

    




