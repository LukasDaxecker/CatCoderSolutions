length = 19683            
iterations = 7 

def GetCircumferenceSq(length, iterations):
                c = length*4
                num = 4
                index = 0

                while index < iterations:
                                length/=3
                                c+=num*length*2
                                num *= 5
                                index += 1

                return c

print(int(GetCircumferenceSq(length, iterations)))