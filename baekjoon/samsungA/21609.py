from collections import deque
import heapq

N, M = list(map(int, input().rstrip().split(' ')))

blocks = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find(blocks):
    num = -1
    r_num = -1
    queue = deque([])
    block_l = []
    visit = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if blocks[i][j] > 0 and visit[i][j] == 0:
                normal = []
                rainbow = []
                whole = []
                visit[i][j] = 1
                queue.appendleft([i, j])
                heapq.heappush(normal, (0, i, j))
                heapq.heappush(whole, (0, i, j))
                v = blocks[i][j]
                while queue:
                    x, y = queue.pop()
                    for d in range(4):
                        if 0 <= x+dx[d] < N and 0 <= y+dy[d] < N:
                            if visit[x+dx[d]][y+dy[d]] == 1:
                                continue
                            if blocks[x+dx[d]][y+dy[d]] == 0:
                                visit[x+dx[d]][y+dy[d]] = 1
                                queue.appendleft([x+dx[d], y+dy[d]])
                                heapq.heappush(rainbow, (1, x+dx[d], y+dy[d]))
                                heapq.heappush(whole, (1, x+dx[d], y+dy[d]))
                            elif blocks[x+dx[d]][y+dy[d]] == v:
                                visit[x+dx[d]][y+dy[d]] = 1
                                queue.appendleft([x+dx[d], y+dy[d]])
                                heapq.heappush(whole, (0, x+dx[d], y+dy[d]))
                            elif blocks[x+dx[d]][y+dy[d]] < 0:
                                visit[x+dx[d]][y+dy[d]] = 1

                if len(whole) > num:
                    num = len(whole)
                    r_num = len(rainbow)
                    block_l = whole
                elif len(whole) == num:
                    if r_num < len(rainbow):
                        num = len(whole)
                        r_num = len(rainbow)
                        block_l = whole
                    elif r_num == len(rainbow):
                        _, px, py =  block_l[0]
                        _, x, y = whole[0]
                        if x > px:
                            num = len(whole)
                            r_num = len(rainbow)
                            block_l = whole
                        elif x == px:
                            if y > py:
                                num = len(whole)
                                r_num = len(rainbow)
                                block_l = whole
                while rainbow:
                    _, x, y = heapq.heappop(rainbow)
                    visit[x][y] = 0
    return block_l

def remove(blocks, block_l):
    for _, x, y in block_l:
        blocks[x][y] = -2
    return blocks

def gravity(blocks):
    for j in range(N):
        c = 0
        for i in range(N-1, 0, -1):
            if blocks[i][j] == -2:
                c += 1
            elif blocks[i][j] == -1:
                c = 0
            if blocks[i][j] == -2 and blocks[i-1][j] > -1:
                blocks[i-1+c][j] = blocks[i-1][j]
                blocks[i-1][j] = -2
                c -= 1
    

def rotate(blocks):
    new = []
    for j in range(N):
        tmp = []
        for i in range(N):
            tmp.append(blocks[i][j])
        new.insert(0, tmp)
    return new
        
if __name__ == "__main__":
    answer = 0
    while(1):
        block_l = find(blocks)
        if len(block_l) >= 2:
            answer += len(block_l)**2
            blocks = remove(blocks, block_l)
            gravity(blocks)
            blocks = rotate(blocks)
            gravity(blocks)
        else:
            break
    print(answer)