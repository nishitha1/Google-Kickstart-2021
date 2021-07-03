# Google Kick Start 2021 Round B - Increasing Substring
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a882
# Time: O(N)

##def longestStrictlyIncreasingSubstring(n, s):
##    prev_l = 0
##    for i in range(n):
##        if i == 0:
##            prev_l = 1
##        elif i > 0:
##            if s[i-1] < s[i]:
##                prev_l = prev_l + 1
##            else:
##                prev_l
##        print(prev_l, end = ' ')
##    print()


def longestStrictlyIncreasingSubstring():
    n = int(input())
    start = 'A'
    prev_l  = 0
    for i in input().strip():
        if i > start:
            prev_l += 1
        else:
             prev_l = 1
        start = i
        print(prev_l, end= ' ')
    print()

t = int(input())
for i in range(t):
    #s = [k for k in input().strip()]
    #print("Case #{}:{}".format(i+1, longestStrictlyIncreasingSubstring()))
    print("Case #"+str(i+1),end=": ")
    longestStrictlyIncreasingSubstring()
    
