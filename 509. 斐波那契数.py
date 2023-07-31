class Solution:
    def fib(self, n: int) -> int:
        F=[0 for _ in range(n+1)]
        if n>0:
            F[1]=1
        for i in range(2,n+1):
            F[i]=F[i-1]+F[i-2]
        return F[n]