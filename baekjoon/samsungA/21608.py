from collections import defaultdict

N = int(input())

likes = []
students = []

s2like = defaultdict(list)
for _ in range(N**2):
    tmp = list(map(int, input().rstrip().split(' ')))
    students.append(tmp[0])
    likes.append(tmp[1:])
    s2like[tmp[0]].extend(tmp[1:])

seat = [[0]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N**2):
    coord = []
    l = -1
    for x in range(N):
        for y in range(N):
            if seat[x][y] != 0:
                continue
            c = 0
            for d in range(4):
                nx = x+dx[d]
                ny = y+dy[d]
                if 0 <= nx < N and 0<= ny < N:
                    if seat[nx][ny] in likes[i]:
                        c += 1
            if c > l:
                l = c
                coord = [[x, y]]
            elif c == l:
                coord.append([x, y])
    
    if len(coord) == 1:
        seat[coord[0][0]][coord[0][1]] = students[i]
    elif len(coord) > 1:
        blank = -1
        idx = []
        for c in coord:
            x = c[0]
            y = c[1]
            tmp = 0
            for d in range(4):
                nx = x+dx[d]
                ny = y+dy[d]
                if 0 <= nx < N and 0<= ny < N:
                    if seat[nx][ny] == 0:
                        tmp += 1
            if tmp > blank:
                blank = tmp
                idx = [[x, y]]
            elif tmp == blank:
                idx.append([x, y])
        idx.sort()
        seat[idx[0][0]][idx[0][1]] = students[i]
    else:
        n = False
        for x in range(N):
            for y in range(N):
                if seat[x][y] == 0:
                    seat[x][y] = students[i]
                    n = True
                    break
            if n == True:
                break

answer = 0
        
for x in range(N):
    for y in range(N):
        count = 0
        for d in range(4):
            if 0 <= x+dx[d] < N and 0<= y+dy[d] < N:
                if seat[x+dx[d]][y+dy[d]] in s2like[seat[x][y]]:
                    count += 1
        if count > 0:
            answer += 10**(count-1)  

print(answer)