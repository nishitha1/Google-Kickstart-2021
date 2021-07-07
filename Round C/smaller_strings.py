# Google Kick Start 2021 Round C - Smaller Strings
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ebe5e

# Referred: https://github.com/kamyu104/GoogleKickStart-2021/blob/main/Round%20C/smaller_strings.py

# input: String s
# output: Number of palindrome strings of length N 
# that is lexicographically smaller than s
# count the number of strings T′ of size H 
# (not necessarily palindromes) that are lexicographically 
# smaller than S′
# bc - "aa", "bb" 

MOD = 10 ** 9 + 7
def compute(s, n, k):
    count = 0
    h = (n+1)//2
    for i in range(h):
        count = (count*k + (ord(s[i]) - ord('a')))%MOD
    for i in range(h, n):
        if s[-i-1] != s[i]:
            count = (count+int(s[-i-1] < s[i]))%MOD
            break
    return count
    
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = [k for k in input().strip()]
    print("Case #{}: {}".format(i+1, compute(s, n, k)))
