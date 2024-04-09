import sympy
from sys import setrecursionlimit

setrecursionlimit(10000)

number = 46216567629137
count = 0

def DeleteIndex(index, num):
                numNew = ""
                for i in range(len(num)):
                                if i != index:
                                                numNew += num[i]
                return numNew

def GetCount(num):
                global count
                i = 0
                
                while i < len(str(num)):
                                                                         
                                if sympy.isprime(int(num)) == False: #  i >= len(str(num)) or                                    
                                                return
                                
                                if int(num) % 10 != 0 and int(num) < 10 and sympy.isprime(int(num)):
                                                count += 1
                                                return
                                                
                                GetCount(DeleteIndex(i, str(num)))
                                i += 1
                                
GetCount(number)
print(count)