'''
def solution(board):
    row=len(board)
    col=len(board[0])
    k=min(row, col)
    s=0
    for i in board:
        s+=sum(i)
    if s==0:
        return 0
    elif 0<s<4:
        return 1
    m_k=0
    while (k>m_k):
        if k*k>s:
            k-=1
            continue
        i, j=0, 0
        while(i<row):
            if i+k>row:
                break
            while(j<col):
                if board[i][j]!=1:
                    j+=1
                    continue
                if j+k>col:
                    break
                answer=0
                for x in range(i, i+k):
                    if board[x][j:j+k]==[1]*k:
                        answer+=1*k
                    else:
                        m_k=answer//k
                        break
                if answer==k*k:
                    return answer
                else:
                    j+=1
            j=0
            i+=1
        k-=1
    return m_k*m_k
'''
def solution(board):
    s=[]
    for i in range(len(board)):
        r_s=sum(board[i])
        for j in range(len(board)):
            
#solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])
solution([[0,0,1,1],[1,1,1,1]])