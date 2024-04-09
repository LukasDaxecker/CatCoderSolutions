n = 6

if n >= 2:
                        add = sum = 1
                        
                        for i in range(n-2):
                                                temp = sum
                                                sum += add
                                                add = temp
else:
                        sum = n

print(sum)