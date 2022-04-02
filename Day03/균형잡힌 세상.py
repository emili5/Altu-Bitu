
# .을 기준으로 입력을 받는다.
# 만약 '('를 만나면 stack에 넣고
#')'을 만나면 stack에서 가장위에거 빼서 짝이 맞으면 뺀다
# 다 검사 후 stack이 비어있으면 yes, 아니면 no

import sys

s = sys.stdin.readline
while True:
    string = s().rstrip()
    stack=[]
    flag = True
    for ch in string:
        if ch=='(' or ch=='[':
            stack.append(ch)
        elif ch==')':
            # stack의 가장 위가 '('이면 빼기
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                flag=False
                break
        elif ch==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                flag=False
                break
        if ch=='.':
            break
if flag:
    print('yes')
else:
    print('no')
