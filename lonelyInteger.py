def lonelyinteger(a):
    # Write your code here
    st1 = []
    st2 = []
    for i in a:
        if i in st1:
            st2.append(i)
            st1.remove(i)
        elif i in st2:
            continue
        elif (i not in st1) and (i not in st2):
            st1.append(i)
    return st1[0]
