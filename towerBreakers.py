def condition(ls):
    cond = True
    if len(ls) > 0:
        for i in ls:
            if i != 1:
                cond = False
            
    return cond

def towerBreakers(n, m):
    # Write your code here
    if m == 1:
        return 1
    else:
        if n % 2 == 1:
            return 1
        else:
            return 2
