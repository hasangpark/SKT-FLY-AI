#문제의 정의 = 그래프를 DFS,BFS로 탐색한 결과를 출력하는 프로그램을 작성하는 것
#첫째 줄에 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V가 주어짐
#다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어짐
#두 정점 사이에 여러 개의 간선이 있을 수 있고, 입력으로 주어지는 간선은 양방향
#DFS는 재귀로 구현, BFS는 queue로 구현
#입력받은 노드의 개수만큼 이차원 리스트로
#(이차원 리스트의 인덱스각 노드, 해당인덱스의 값들 노드들과 연결 여부) 
#False로 초기화한다음 만약 연결되어 있다면 True로 바꿔주는 형식으로 구현

#BFS에 사용할 queue 임포트하기
from collections import deque
#N,M,V 입력받기
N,M,V = map(int, input().split())
#그래프 이차원리스트로 구현
graph = [[0]  (N + 1) for _ in range(N + 1)]

for _ in range(M)
  m1, m2 = map(int, input().split())
  # 노드 연결 하기
  graph[m1][m2] = graph[m2][m1] = 1

# 너비 우선 탐색
def bfs(start_v)
  discoverd = [start_v]
  # 리스트를 써서 pop(0)하게 되면 시간복잡도가 O(N)이다.
  # 그래서 시간복잡도가 O(1)인 deque를 사용한다.
  queue = deque() 
  queue.append(start_v)
  #queue가 빌때까지 반복
  while queue
    v = queue.popleft()#큐에 있는 맨 왼쪽값 빼낸다
    print(v, end=' ')#해당 값 출력

    for w in range(len(graph[start_v]))
      if graph[v][w] == 1 and (w not in discoverd)
        discoverd.append(w)
        queue.append(w)

# 깊이 우선 탐색
def dfs(start_v, discoverd=[])
  discoverd.append(start_v)# 해당 V값 방문처리
  print(start_v, end=' ')

  for w in range(len(graph[start_v]))
    if graph[start_v][w] == 1 and (w not in discoverd)# 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
      dfs(w, discoverd)# 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)

dfs(V)
print()#개행문
bfs(V)