def valcheck(g0, g1, g2, valg):
    s = 0
    g1[1] = valg
    # row and col
    if 2 * g1[1] == g1[2] + g1[0]:
        s += 1
    if 2 * g1[1] == g2[1] + g0[1]:
        s += 1
    # diag   
    if 2 * g1[1] == g2[2] + g0[0]:
        s += 1
    if 2 * g1[1] == g2[0] + g0[2]:
        s += 1
    return s
        
def solve(g0, g1, g2):
    num_seq = 0
    # row
    if 2*g0[1] == g0[2] + g0[0]:
        num_seq += 1
    if 2*g2[1] == g2[2] + g2[0]:
        num_seq += 1
    # col
    if 2*g1[0] == g2[0] + g0[0]:
        num_seq += 1
    if 2 * g1[2] == g2[2] + g0[2]:
        num_seq += 1
    # diag
    ecv, erv, edpv, ednv = 0, 0, 0, 0
    ec = g0[1] + g2[1]
    if ec % 2 == 0:
        ec = ec//2
        ecv = valcheck(g0, g1, g2, ec)
    er = g1[0] + g1[2]
    if er % 2 == 0:
        er = er // 2
        erv = valcheck(g0, g1, g2, er)
    edp = g0[0] + g2[2]
    if edp % 2 == 0:
        edp = edp // 2
        edpv = valcheck(g0, g1, g2, edp)
    edn = g0[2] + g2[0]
    if edn % 2 == 0:
        edn = edn // 2
        ednv = valcheck(g0, g1, g2, edn)
    final_v = max(ecv, erv, edpv, ednv)
    num_seq += final_v
   
    return num_seq        

t = int(input())
for i in range(t):
    g0, g1, g2 = [0]*3, [0]*3, [0]*3
    g0 = list(map(int, input().split()))
    g1[0], g1[2] = map(int, input().split())
    g2 = list(map(int, input().split()))
    print("Case #{}: {}".format(i+1, solve(g0, g1, g2)))
