'''
while True:
    try:
        mynum=input()
        length=len(mynum)
        hafllen=length//2
        for i in range(hafllen):
            if mynum[i]!=mynum[-1-i]:
                print(False)
                raise ValueError
        print(True)
    except:
        break
'''
print('s'.isalpha())
s= "ab-cd"
mylist=s.split('')
print(mylist)

#错误版本
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n=len(s)
        mylist=['-' for _ in range(n)]
        print(mylist)
        #非字母的位置是不能动的，只能在原来的基础上再往后移动
        
        for i in range(n):
            if s[i].isalpha():
                mylist[-1-i]=s[i]
            else:
                mylist[i]=s[i]
            print(mylist)
        return "".join(mylist)