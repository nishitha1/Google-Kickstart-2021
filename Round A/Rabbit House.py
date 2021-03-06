# Google Kick Start 2021 Round A - Rabbit House
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cb14
# Referred: https://docs.python.org/3/library/heapq.html 
# https://github.com/absansher/KickStart-2021-A/blob/main/3%20(Rabbit%20House)%20.py

# Time: O(R*C*log(R*C))
# Space: O(R*C)

# 2D grid with r rows, c columns
# e.g. abs(h[i][j] - h[i+1][j]) <= 1
# can only increase height

from heapq import *
import itertools

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task] # count: tie breaker for tasks with the same priority
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')


for case in range(1, int(input()) + 1):
    r, c = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(r)]
    modified = [i[:] for i in grid] # copy grid values
    pq = []                         # list of entries arranged in a heap
    entry_finder = {}               # mapping of tasks to entries
    REMOVED = '<removed-task>'      # placeholder for a removed task
    counter = itertools.count()     # unique sequence count
    found = 0
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    
    for i in range(r):
        for j in range(c):
            add_task((i, j), -grid[i][j])
    
    while found < r * c:
        i, j  = pop_task()
        for x, y in dirs:
            if 0 <=i+x<r and 0<=j+y<c and modified[i][j] > modified[i+x][j+y] + 1:
                modified[i+x][j+y] = modified[i][j] - 1
                add_task((i+x, j+y), -modified[i][j] + 1)
        found += 1
        
    s = sum(modified[i][j] - grid[i][j] for i in range(r) for j in range(c))
    print("Case #{}:{}".format(case, s))
