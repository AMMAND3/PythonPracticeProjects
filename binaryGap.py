def solution(N):
    # Implement your solution here
    a =N val = ""
    while (a >= 1):
        b = a%2
        val += str(b)
        a = a//2
    val = ''.join(reversed(val))
    ls = 0
    st = ""
    for x in val:
        if x == "1":
            if len(st) > 0 and "0" in st:
                ls = max(ls, st.count("0"))
                st = ""
        elif x == "0":
            st += "0"
    return ls

def binaryGap2(self, n: int) -> int:


    last = None
    ans = 0
    for i in range(32):
        if (n >> i) & 1:
            if last is not None:
                ans = max(ans, i - last)
            last = i
    return ans
