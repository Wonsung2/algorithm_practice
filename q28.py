import sys
sys.stdin=open("input28.txt", 'r')
n = int(input())
body = []
for i in range(n):
    a, b = map(int, input().split())
    body.append((a,b))

body.sort(key=lambda x : (x[0], x[1]), reverse=True)

largest = 0
cnt = 0
for x, y in body :
    if y > largest :
        largest = y
        cnt += 1

print(cnt)
