def sumStr(str)->int:
    sumStr = 0
    for n in str:
        sumStr = sumStr +  int(n)
    return sumStr

# Save the input in this variable
# print (sumStr("123"))
ticket = input()
# ticket = "123456"
# Add up the digits for each half
half1 = ticket[:3]
half2 = ticket[-3:]

# print (half1)
# print (half2)
# Thanks to you, this code will work
if sumStr(half1) == sumStr(half2):
    print("Lucky")
else:
    print("Ordinary")


