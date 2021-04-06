import copy
moves=list(map(int, input().rstrip().split(' ')))

#case 0: red 1:blue_1 2:blue_2 3:blue_3
red=[i for i in range(0, 42, 2)]
red_idx=[0]*len(red)

blue=[[0], [10, 13, 16, 19, 25, 30, 35, 40], [20, 22, 24, 25, 30, 35, 40], [30, 28, 27, 26, 25, 30, 35, 40]]
blue_idx=[[0]*len(blue[i]) for i in range(4)]
bm={1:3, 2:2, 3:3}
answer=0
def DFS(i, dices, score, finish):
    global answer
    if i>=10:
        if score>answer:
            answer=score
        return 
    if finish==4:
        if score>answer:
            answer=score
        return
    idx=moves[i]
    #새로운 말 추가
    if finish+len(dices)<4:
        if red_idx[idx]==0:
            red_idx[idx]=1
            if idx%5==0 and blue_idx[idx//5][0]==0:
                case=idx//5
                blue_idx[case][0]=1
                dices.append([case, 0])
                DFS(i+1, dices, score+red[idx], finish)
                blue_idx[case][0]=0
            else:
                case=0
                dices.append([case, idx])
                DFS(i+1, dices, score+red[idx], finish)
            dices.pop()
            red_idx[idx]=0 

    #있는 말 이동
    if len(dices)>0:
        for d in range(len(dices)):
            case, dice=dices[d]
            if case==0:
                #도착 말 이후인 경우
                if dice+idx>20:
                    red_idx[dice]=0
                    DFS(i+1, dices[0:d]+dices[d+1:], score, finish+1)
                    red_idx[dice]=1
                else:    
                    if red_idx[dice+idx]==1:
                        continue
                    red_idx[dice]=0
                    red_idx[dice+idx]=1
                    if (dice+idx)%5==0 and dice+idx<20:
                        case=(dice+idx)//5
                        blue_idx[case][0]=1
                        tmp=[case, 0]
                        DFS(i+1, dices[0:d]+[tmp]+dices[d+1:], score+red[dice+idx], finish)
                        blue_idx[case][0]=0
                    else:
                        tmp=[case, dice+idx]
                        if dice+idx==20:
                            blue_idx[1][-1]=1
                            blue_idx[2][-1]=1
                            blue_idx[3][-1]=1
                        DFS(i+1, dices[0:d]+[tmp]+dices[d+1:], score+red[dice+idx], finish)
                    red_idx[dice+idx]=0
                    red_idx[dice]=1
                    if dice+idx==20:
                        blue_idx[1][-1]=0
                        blue_idx[2][-1]=0
                        blue_idx[3][-1]=0
            elif case>0: #BLUE
                if dice+idx>=len(blue_idx[case]):
                    blue_idx[case][dice]=0
                    if dice>bm[case]:
                        if case==1:
                            blue_idx[2][dice-1]=0
                            blue_idx[3][dice]=0
                        elif case==2:
                            blue_idx[1][dice+1]=0
                            blue_idx[3][dice+1]=0
                        elif case==3:
                            blue_idx[2][dice-1]=0
                            blue_idx[1][dice]=0             
                    if dice==0:
                        red_idx[case*5]=0
                    DFS(i+1, dices[0:d]+dices[d+1:], score, finish+1)
                    blue_idx[case][dice]=1
                    if dice==0:
                        red_idx[case*5]=1
                    if dice>bm[case]:
                        if case==1:
                            blue_idx[2][dice-1]=1
                            blue_idx[3][dice]=1
                        elif case==2:
                            blue_idx[1][dice+1]=1
                            blue_idx[3][dice+1]=1
                        elif case==3:
                            blue_idx[2][dice-1]=1
                            blue_idx[1][dice]=1     
                else:
                    if blue_idx[case][dice+idx]==1:
                        continue
                    blue_idx[case][dice]=0
                    if dice==0:
                        red_idx[case*5]=0
                    if dice>bm[case]:
                        if case==1:
                            blue_idx[2][dice-1]=0
                            blue_idx[3][dice]=0
                        elif case==2:
                            blue_idx[1][dice+1]=0
                            blue_idx[3][dice+1]=0
                        elif case==3:
                            blue_idx[2][dice-1]=0
                            blue_idx[1][dice]=0
                    blue_idx[case][dice+idx]=1
                    if dice+idx==len(blue_idx[case])-1:
                        red_idx[-1]=1
                    tmp=[case, dice+idx]
                    if dice+idx>bm[case]:
                        if case==1:
                            blue_idx[2][dice+idx-1]=1
                            blue_idx[3][dice+idx]=1
                        elif case==2:
                            blue_idx[1][dice+idx+1]=1
                            blue_idx[3][dice+idx+1]=1
                        elif case==3:
                            blue_idx[2][dice+idx-1]=1
                            blue_idx[1][dice+idx]=1

                    DFS(i+1, dices[0:d]+[tmp]+dices[d+1:], score+blue[case][dice+idx], finish)
                    blue_idx[case][dice]=1
                    blue_idx[case][dice+idx]=0
                    if dice==0:
                        red_idx[case*5]=1
                    if dice+idx==len(blue_idx[case])-1:
                        red_idx[-1]=0    
                    if dice>bm[case]:
                        if case==1:
                            blue_idx[2][dice-1]=1
                            blue_idx[3][dice]=1
                        elif case==2:
                            blue_idx[1][dice+1]=1
                            blue_idx[3][dice+1]=1
                        elif case==3:
                            blue_idx[2][dice-1]=1
                            blue_idx[1][dice]=1 
                    if dice+idx>bm[case]:
                        if case==1:
                            blue_idx[2][dice+idx-1]=0
                            blue_idx[3][dice+idx]=0
                        elif case==2:
                            blue_idx[1][dice+idx+1]=0
                            blue_idx[3][dice+idx+1]=0
                        elif case==3:
                            blue_idx[2][dice+idx-1]=0
                            blue_idx[1][dice+idx]=0             

DFS(0, [], 0, 0)
print(answer)