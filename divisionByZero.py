numerator = 12000
denominator = 0

try:
    numerator/denominator
except:
    raise Exception("This division is impossible")


try:
    int(numerator/denominator) #the code that raises the error
except ValueError:
    raise ValueError("This division is impossible") from None
print (numerator/denominator)


