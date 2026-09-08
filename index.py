
def find3(s):
    n=len(s)
    res=""
    for x in range(1,n+1):
        if x % 3 ==0 or "3" in str(x) :
            res+=s[x-1]
    return res
