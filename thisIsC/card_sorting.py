import heapq

N=int(input())
cards=[int(input()) for _ in range(N)]

heapq.heapify(cards)

total=0
while cards:
    if len(cards)<2:
        break
    else:
        num1=heapq.heappop(cards)
        num2=heapq.heappop(cards)
        total+=num1+num2
        heapq.heappush(cards, num1+num2)
print(total)