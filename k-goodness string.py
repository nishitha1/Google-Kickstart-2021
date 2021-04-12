# if s[i] != s[n-i+1]
# goodness score += 1
class Solution:
    def __init__(self, givens, n, k):
        self.givens = givens
        self.n = n 
        self.k = k
    
    def compute_goodness(self):
        goodness_score = 0
        if self.n <= 0:
            return 0
        for i in range(n//2):
            if self.givens[i] != self.givens[n-i-1]:
                goodness_score += 1
        if goodness_score == k:
            return 0
        else:
            return abs(k-goodness_score)

t = int(input())
for i in range(1, t + 1):
    n, k = [int(j) for j in input().split()]
    givens = [k for k in input().strip()]
    sol = Solution(givens, n, k)
    print("Case #{}: {}".format(i, sol.compute_goodness()))
