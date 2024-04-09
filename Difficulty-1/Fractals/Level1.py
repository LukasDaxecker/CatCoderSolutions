length = 531441             
iterations = 9 

def GetCircumferecneTri(length, iterations):   # iterations = i(n)
                c = 3*length                # Circumfrence at i(0)
                num = 3                     # number of added tri at i(1)
                index = 0

                while index < iterations:
                                length/=3
                                c+=num*length
                                num*=4
                                index += 1
                return c

print(int(GetCircumferecneTri(length, iterations)))