# Google Kick Start 2021 Round A - L Shaped Plots
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509

# Referred : https://github.com/absansher/KickStart-2021-A/blob/main/2%20(L%20Shaped%20Plots)%20.py
# Time:  O(R * C)
# Space: O(min(R, C))

# Count(x,y)=min(x2,y)+min(y2,x)−2
def count(x, y):
    return max(min(x//2 - 1, y-1) + min(x - 1, y//2-1), 0)
# From Analysis:
# If we can calculate number of consecutive cells that have value 1 in each side of (i,j), 
# we can calculate number of L-shapes of each type with this cell as the common endpoint of the segments using the Count() function above.

# def compute_lshape():
for case in range(1,int(input())+1):
    r, c = map(int, input().split())
    matrix = [list(map(int,input().split())) for i in range(r)]
    up = []
    down = []
    left = []
    right = []
    for _ in range(r):
        # matrix.append(list(map(int, input().split())))
        up.append([0 for i in range(c)])
        down.append([0 for i in range(c)])
        left.append([0 for i in range(c)])
        right.append([0 for i in range(c)])
    
    for j in range(c):
        for i in range(r):
            if i == 0:
                down[i][j] = matrix[i][j]
            else:
                down[i][j] = (down[i-1][j] + 1) * matrix[i][j]
    
    for j in range(c):
        for i in range(r-1, -1, -1):
            if i == r - 1:
                up[i][j] = matrix[i][j]
            else:
                up[i][j] = (up[i+1][j] + 1) * matrix[i][j]
    
    for i in range(r):
        for j in range(c):
            if j == 0:
                right[i][j] = matrix[i][j]
            else:
                right[i][j] = (right[i][j-1] + 1)*matrix[i][j]
    
    for i in range(r):
        for j in range(c-1,-1,-1):
            if j == c - 1:
                left[i][j] = matrix[i][j]
            else:
                left[i][j] = (left[i][j+1] + 1) * matrix[i][j]
    res = 0
    for i in range(r):
        for j in range(c):
            res += count(left[i][j], down[i][j])
            res += count(left[i][j], up[i][j])
            res += count(right[i][j], down[i][j])
            res += count(right[i][j], up[i][j])
    print('Case #',case,': ',res,sep='')

# t = int(input())
# for i in range(t):
#     print("Case #{}:{}".format(i+1, compute_lshape()))
