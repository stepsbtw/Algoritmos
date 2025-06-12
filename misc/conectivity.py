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
#print(g.adj)

# CONEXO:
# existe um caminho entre todo par de nós

# FORTEMENTE CONEXO (direcionados):
# existe todo caminho (u,v) e todo caminho (v,u)

def dfs(adj, visited, node, pre=[],post=[]):
    visited.add(node)
    pre.append(node)
    
    for nbor in adj[node]:
        if nbor not in visited:
            dfs(adj, visited, nbor, pre, post)
    post.append(node)
    return pre, post
    
def dfs_iter(adj, no_inicial):
    visited = set()
    stack = [(no_inicial, False)]
    pre = []
    post = []
    pre_n = {}
    post_n = {}
    i=-1
    j=-1

    while stack:
        no, explored = stack.pop()
        if explored:
            j+=1
            post.append(no)
            post_n[no] = j
        elif no not in visited:
            i+=1
            visited.add(no)
            pre.append(no)
            pre_n[no] = i
            stack.append((no, True))  # pós-visita (pós-ordem)
            for nbor in reversed(adj[no]):
                if nbor not in visited:   
                    stack.append((nbor, False))  # pré-visita
    return pre, post, pre_n, post_n
    
# bsca por profundidade em grafos não direcionados

# TEMPO LINEAR!

pre, post, pre_n, post_n = dfs_iter(g.adj, "s")
print(pre)
print(post)
print(pre_n)
print(post_n)

# quais partes do grafo são alcançáveis apartir de um nó específico?

# DFS + lista alcançaveis 
        




