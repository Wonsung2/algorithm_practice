import sys
# sys.stdin=open("input.txt", 'rt')
T = int(input())
# print('T = ', T)
for t in range(T) :
    n, s, e, k = map(int, input().split())
    # print('n, s, e, k', n, s, e, k)
    a = list(map(int, input().split()))
    a= a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1,a[k-1]))

