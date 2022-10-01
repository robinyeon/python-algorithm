n = int(input())
directions = input().split()

x, y = 1, 1

# dx, dy를 작성할때 단순히 함수 그래프로 속단하지 말고 문제대로 따라가기
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moves = ['L', 'R', 'U', 'D']


for direction in directions:
    for i in range(len(moves)):
        if direction == moves[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # continue로 영역 벗어났을 시 무시
    if nx > n or nx < 1 or ny > n or ny < 1:
        continue
    x, y = nx, ny

print(x, y)

"""
공간 밖을 벗어나는 값들을 무시하게끔 처리하기 위해서
nx, ny라는 변수, 그리고 continue가 필요한 것
"""