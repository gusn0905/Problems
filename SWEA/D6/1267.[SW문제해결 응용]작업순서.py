# D6 1267. [S/W 문제해결 응용] 작업순서
def find_start(lst, ver):
    # lst: branch, ver: vertex
    st = []
    for r in range(1, ver+1):
        cnt = 0
        for j in range(len(lst)):
            if lst[j][1] == r:
                cnt += 1
        if cnt == 0:
            st.append(r)
    return st


def dfs(starting, graphs, vert, bran):
    # starting: start,graphs: graph, vert: vertex, bran: branch
    path = []
    visited = [0 for _ in range(vert+1)]
    for v in range(len(bran)):
        visited[bran[v][1]] += 1
    stack = []
    for s in range(len(starting)):
        visited[starting[s]] = 1
        stack.append(starting[s])
    while len(stack) > 0:
        v = stack.pop(-1)
        visited[v] -= 1
        if visited[v] == 0:
            path.append(v)
            for w in range(1, vert + 1):
                if graphs[v][w] == 1:
                    stack.append(w)
    return path


T = 10
for tc in range(1, T+1):
    vertex, edge = map(int, input().split())
    t = list(map(int, input().split()))
    branch = []
    graph = [[0] * (vertex+1) for _ in range(vertex+1)]
    for i in range(0, edge*2, 2):
        temp = t[i:i+2]
        branch.append(temp)
        graph[temp[0]][temp[1]] = 1
    #print(branch)
    start = find_start(branch, vertex)
    result = dfs(start, graph, vertex, branch)
    print("#{0}".format(tc), end=' ')
    for p in result:
        print(p, end=' ')
    print()