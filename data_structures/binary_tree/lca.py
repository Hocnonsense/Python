import queue

def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b

def bfs(graph, max_node, root=1):
    """
        从树的根节点运行宽度优先搜索。
        parent: 设置每个节点的直接父节点。
        根节点的父节点设置为0。
        level: 计算每个节点从根节点开始的深度
    """
    level = [-1 for _ in range(max_node + 1)]  # initializing with -1 which means every node is unvisited
    level[root] = 0
    parent = [[0 for _ in range(max_node + 1)] for _ in range(20)] # initializing with 0
    q = queue.Queue(maxsize=max_node)
    q.put(root)
    while q.qsize() != 0:
        u = q.get()
        for v in graph[u]:
            if level[v] == -1:
                level[v] = level[u] + 1
                q.put(v)
                parent[0][v] = u
    return level, parent

def creatSparse(max_node, parent):
    """
        建立稀疏表 which saves each nodes 2^ith parent
    """
    j = 1
    while (1 << j) < max_node:  # 2**i
        for i in range(1, max_node + 1):
            parent[j][i] = parent[j - 1][parent[j - 1][i]]
        j += 1
    return parent

def LCA(u, v, level, parent):
    """
        returns lca of node u,v
    """
    if level[u] < level[v]: # u > v
        u, v = swap(u, v)
    for i in range(18, -1, -1): # u v 宽度相同
        if level[u] - (1 << i) >= level[v]:
            u = parent[i][u]
    if u == v:
        return u
    else:
        # moving both nodes upwards till lca in found
        for i in range(18, -1, -1):
            if parent[i][u] != 0 and parent[i][u] != parent[i][v]:
                u, v = parent[i][u], parent[i][v]
        # returning longest common ancestor of u,v
        return parent[0][u]

def main():
    graph = {
        1: [2, 3, 4],
            2: [5],
            3: [6, 7],
            4: [8],
                5: [9, 10],
                6: [11],
                7: [],
                8: [12, 13],
                    9: [],
                    10: [],
                    11: [],
                    12: [],
                    13: []
    }   # 树
    max_node = len(graph)
    level, parent = bfs(graph, max_node, 1)
    print(level)
    parent = creatSparse(max_node, parent) # 
    print(*parent, sep = '\n')
    print("LCA of node 1 and 3 is: ", LCA(1, 3, level, parent))
    print("LCA of node 5 and 6 is: ", LCA(5, 6, level, parent))
    print("LCA of node 7 and 11 is: ", LCA(7, 11, level, parent))
    print("LCA of node 6 and 7 is: ", LCA(6, 7, level, parent))
    print("LCA of node 4 and 12 is: ", LCA(4, 12, level, parent))
    print("LCA of node 8 and 8 is: ", LCA(8, 8, level, parent))


if __name__ == "__main__":
    main()
