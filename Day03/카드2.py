# 카드 맨 앞은 제거, 새로운 카드는 맨 뒤에 추가-> 큐!
from collections import deque
deq = deque()
n = int(input())
for i in range(1,n+1):
    deq.append(i)
while len(deq)>1:
    deq.popleft()#가장 왼쪽에 있는 카드 버리기
    deq.append(deq.popleft())
for i in deq:
    print(i)