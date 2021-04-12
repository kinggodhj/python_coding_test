def solution(board):
    row=len(board)
    col=len(board[0])
    m=0
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j]==0:
                continue
            board[i][j]=min(board[i][j-1], board[i-1][j], board[i-1][j-1])+1
            if board[i][j]>m:
                m=board[i][j]
    if m==0:
        for i in range(row):
            for j in range(col):
                if board[i][j]>m:
                    m=board[i][j]
    return (m*m)
#solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])
#solution([[0,0,1,1],[1,1,1,1]])