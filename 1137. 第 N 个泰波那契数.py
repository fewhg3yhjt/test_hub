class Solution:
    def tribonacci(self, n: int) -> int:
        T=[0 for _ in range(n+1)]
        if n>0:
            T[1]=1
        if n>1:
            T[2]=1
        for i in range(3,n+1):
            T[i]=T[i-3]+T[i-2]+T[i-1]
        return  T[n]
        #test
